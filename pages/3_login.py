#This module provides the login and registration functionality for the Streamlit application

from pages import st, os, sqlite3, re


def create_connection(db_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'database', db_name)
    return sqlite3.connect(db_path)

def create_table():
    conn=create_connection('../admin.db')
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS admins(
                   username TEXT PRIMARY KEY,
            password TEXT NOT NULL)''')
    conn.commit()
    conn.close()



def authenticate(username, password):
    conn = create_connection('admin.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM admins WHERE username = ? AND password = ?''', (username, password))
    result = cursor.fetchone()
    conn.close()
    return result

def register(username, password):
    conn = create_connection('admin.db')
    cursor = conn.cursor()

    
    cursor.execute("SELECT * FROM admins WHERE username=?", (username,))
    if cursor.fetchone() is not None:
        conn.close()
        return False, "Username already exists. Please choose a different username."

    
    cursor.execute('''
        INSERT INTO admins (username, password) VALUES (?, ?)
    ''', (username, password))
    conn.commit()
    conn.close()
    return True, "Account created successfully!"

def validate_password(password):
    """ Validate password with specific criteria. """
    if len(password) < 6:
        return False, "Password must be at least 6 characters long."
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character."
    return True, ""    


create_table()
st.title("Login Page")

    
if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
if 'page' not in st.session_state:
        st.session_state['page'] = 'Login'

tabs = st.tabs(["Login", "Sign Up"])
with tabs[0]:
        st.subheader("Login Section")
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')

        if st.button("Login"):
            if authenticate(username, password):
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.session_state["page"] = "Admin"
                st.switch_page(st.Page("pages/4_admin.py"))
            else:
                st.error("Incorrect Username/Password")

with tabs[1]:
        st.subheader("Create New Account")
        
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type='password')
        st.write("Password must contain 6 characters with one UpperCase character and a special Character")
        code = st.text_input("Enter Code")
        
        if st.button("Sign Up"):
            if new_username and new_password and code:
                if code == "8090":
                    valid, message = validate_password(new_password)
                    if valid:
                        success, message = register(new_username, new_password)
                        if success:
                            st.success(message)
                            st.info("Go to Login Menu to login")
                        else:
                            st.warning(message)
                    else:
                        st.warning(message)
                else:
                    st.warning("Please enter the correct code to sign up.")
            else:
                st.warning("Please enter username, password, and code.")
    
   

if st.session_state["page"] == "Admin" and st.session_state['logged_in']:
        st.success(f"Welcome, {st.session_state['username']}!")
elif not st.session_state['logged_in'] and st.session_state["page"] != "Home":
        st.warning("Please log in to continue.")


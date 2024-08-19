# This file provides the implementation for the admin page of the diabetes prediction application,
# including functions to fetch user data, display it in a table, and allow data download. 


from pages import st, pd, sqlite3
from pages.utils.data import fetch_user_data


def create_connection():
    conn = sqlite3.connect('diab_predictor.db')
    return conn



if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
if 'username' not in st.session_state:
        st.session_state['username'] = ''

if st.session_state['logged_in']:
        st.success(f"Welcome, {st.session_state['username']}!")
        st.title("Admin Page")
        data = fetch_user_data()
        df = pd.DataFrame(data, columns=['ID', 'Name', 'Contact Number','Gender', 'Pregnancies', 'Glucose',  'Blood Pressure',  'Skin Thickness','Insulin', 'BMI','Age', 'Feedback'])

        st.dataframe(df)

        if st.button("Download Data"):
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='user_data.csv',
                mime='text/csv',
            )
       
else:
        st.switch_page("pages/3_login.py")
  
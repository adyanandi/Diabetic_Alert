import streamlit as st


pg = st.navigation([st.Page("pages/1_home.py",title="Home",icon="💊"),
                    st.Page("pages/2_result.py", title="Result",icon="⛑️"),
                    st.Page("pages/3_login.py",title="Admin Login",icon="🖥️"),
                    st.Page("pages/4_admin.py",title="Admin Section",icon="👨‍💼")])
pg.run()
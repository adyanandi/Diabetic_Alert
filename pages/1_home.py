# This file defines the home page of the diabetes prediction web app.
# It handles user input for prediction, validation of data, and navigation between pages.

# This file is the main entry point for the Diabetes Prediction web application.
# It sets up the page configuration, initializes necessary components, and controls the navigation between pages.

from pages import st
from pages import PREDICT
from pages.utils.data import create_db

create_db()  
st.session_state['logged_in'] = False
st.title('Diabetic Alert : Your Diabetes Insight Tool')

st.markdown("""Welcome to our Diabetes Prediction Web App! Easily assess your risk of developing diabetes by entering your health data, such as age, BMI, and glucose levels. 
                    Our advanced algorithm delivers instant and personalized predictions . 
                    Prioritize your health and take control of your diabetes risk today!""")

st.session_state["feedback_submitted"] = False

st.subheader("Predict Diabetes")   
st.info("You don't need to fill out all fields. Enter only the information you have.")
st.header("Enter Personal Info ")
name = st.text_input("Your Name")
contact_number = st.text_input("Contact Number")
gender=st.selectbox("Gender",["Female","Male","Other"])

contact_number_valid = False

if contact_number:
    contact_number = contact_number.strip()  


    if (len(contact_number) == 10 and contact_number.isdigit() and 
       contact_number[0] in ['6', '7', '8', '9']):
       contact_number_valid = True

    elif (contact_number.startswith('+') and 
       len(contact_number) == 13 and 
       contact_number[1:].isdigit()):
       contact_number_valid = True

    elif (contact_number.startswith('+91 ') and 
       len(contact_number) == 14 and 
       contact_number[4:].isdigit() and 
       contact_number[4] in ['6', '7', '8', '9']):
       contact_number_valid = True
    else:
       st.error("Please enter a valid contact number")
else:
    st.error("Contact number is required")

st.header("Enter values")
feature_values = []
user_inputs = {}
available_features = {
'Pregnancies': 'Pregnancies',
'Glucose': 'Glucose (mg/dL)',
'BloodPressure': 'Blood Pressure (mm Hg)',
'SkinThickness': 'Skin Thickness (mm)',
'Insulin': 'Insulin (µU/mL)',
'BMI': 'BMI (kg/m²)',
'Age': 'Age (years)'
}


for feature, label in available_features.items():
    if feature in ['BMI']:
        value = st.number_input(label, value=None, format="%.2f")
    else:
        value = st.number_input(label, value=None, step=1)

    if value is not None:
        user_inputs[feature] = value
        feature_values.append(value)

entered_features = list(user_inputs.keys())

if st.button("Predict Diabetes"):

    error = False
    if 'Pregnancies' in user_inputs and not (0 <= user_inputs['Pregnancies'] <= 20):
        st.error("Pregnancies must be between 0 and 20.")
        error = True
    if 'Glucose' in user_inputs and not (0 <= user_inputs['Glucose'] <= 200):
        st.error("Glucose must be between 0 and 200.")
        error = True
    if 'BloodPressure' in user_inputs and not (0 <= user_inputs['BloodPressure'] < 123):
        st.error("Blood Pressure must be between 0 and 122.")
        error = True
    if 'SkinThickness' in user_inputs and not (0 <= user_inputs['SkinThickness'] < 100):
        st.error("Skin Thickness must be between 0 and 99.")
        error = True
    if 'Insulin' in user_inputs and not (0 <= user_inputs['Insulin'] < 847):
        st.error("Insulin must be between 0 and 846.")
        error = True
    if 'BMI' in user_inputs and not (0.0 <= user_inputs['BMI'] <= 68):
        st.error("BMI must be between 0 and 68.")
        error = True
    if 'Age' in user_inputs and not (0 < user_inputs['Age'] <= 100):
        st.error("Age must be between 1 and 100.")
        error = True
    if not name:
        st.error("Name is required.")
        error = True
    if not contact_number_valid:
        st.error("Valid Contact Number is required.")
        error = True
    if gender in ["Male", "Other"] and 'Pregnancies' in user_inputs :
            if user_inputs['Pregnancies'] != 0:
                st.error("Pregnancies value is not applicable for selected gender.")
                error = True  
    if not error:
        result=True
        
        st.session_state["user_inputs"] = user_inputs
        st.session_state["feature_values"] = feature_values
        st.session_state["entered_features"] = entered_features
        st.session_state["user_name"] = name  
        st.session_state["user_contact"] = contact_number 
        st.session_state["user_gender"] = gender 
        st.session_state["page"] = "Result"

        st.switch_page(st.Page("pages/2_result.py"))
        
        
      


                    
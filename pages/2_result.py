# This file implements the result page for the diabetes prediction application 
# It handles navigation between different pages, displays prediction results, and collects user feedback.

from pages import st
from pages.utils.models import load_model, predict_diabetes, load_accuracies
from pages.utils.data import store_user_data




user_inputs = st.session_state.get("user_inputs")
feature_values = st.session_state.get("feature_values")
entered_features = st.session_state.get("entered_features")
user_name = st.session_state.get("user_name")
if user_name:
    st.title(f"Prediction Results for {user_name}!!")
accuracies = load_accuracies('acc.json')
if entered_features:
    model = load_model(entered_features)
    if model and feature_values:
        prediction = predict_diabetes(model, feature_values)
        if(prediction[0]>=0.5):
            prediction[0]=1
        else:
            prediction[0]=0    
        if prediction[0] == 1:
            st.error("Attention Needed : Potential Risk of Diabetes")
            st.markdown("""

            **Recommendation:** 

            Based on the input data, there is an indication that you might be at risk for diabetes. It is  advised to consult with a healthcare professional as soon as possible. 
            """)
        elif prediction[0]==0:
            st.success("No Immediate Risk of Diabetes")
            
            st.markdown("""
            

            Your results indicate that you are not at risk for diabetes at this time. Nevertheless, maintaining a healthy lifestyle with a balanced diet and regular physical activity is beneficial for your overall health. 
            """) 

        features_key = str(entered_features)
        if features_key in accuracies:
            accuracy = accuracies[features_key]['accuracy']
            st.info(f"Accuracy: {accuracy * 100:.2f}%")
        else:
            st.warning("Accuracy information for the selected combination is not available.")

        if "feedback_submitted" not in st.session_state:
            st.session_state["feedback_submitted"] = False

        st.header("Was the prediction correct?")
        feedback = st.radio("Please select one:", ["", "Yes", "No","Don't Know"], index=0)

        if feedback and feedback not in ["", "Don't Know"] and not st.session_state["feedback_submitted"]:
            name = st.session_state.get("user_name")
            contact_number = st.session_state.get("user_contact")
            gender = st.session_state.get("user_gender")
            pregnancies = user_inputs.get('Pregnancies', None)
            glucose = user_inputs.get('Glucose', None)
            insulin = user_inputs.get('Insulin', None)
            blood_pressure = user_inputs.get('BloodPressure', None)
            age = user_inputs.get('Age', None)
            skin_thickness = user_inputs.get('SkinThickness', None)
            bmi = user_inputs.get('BMI', None)

            store_user_data(name, contact_number,gender, pregnancies, glucose, blood_pressure,skin_thickness ,insulin, bmi,age, feedback)
            
            st.session_state["feedback_submitted"] = True 
            st.success("Thankyou for feedback")
        else:
                if not feedback :
                    st.write("Please provide feedback to proceed.")
                elif st.session_state["feedback_submitted"]:
                    st.write("Feedback already submitted.")

    else:
            st.write("Failed to load model")     
            
else:
    st.switch_page("pages/1_home.py")




## Diabetes Predictor Using Machine Learning


The Diabetic Alert: Your Diabetes Insight Tool project is a web application designed to predict the likelihood of diabetes in users based on their health metrics. Built using Streamlit and machine learning, the tool leverages 11 different models, to deliver accurate predictions. The application is tailored for individuals seeking to monitor their health and assess their diabetes risk conveniently.

With a secure login system, the tool allows users to input health data such as glucose levels, BMI, and other relevant factors. The application then analyzes this data and provides a prediction of diabetes risk, which is stored in a database for future reference. The project is user-friendly, making it accessible to both healthcare professionals and individuals concerned about their health.


## Demo

For users:

![Diabetic Alert Demo](https://i.imgur.com/RsjoGGu.gif)

For admins:

![Diabetic Alert Demo](https://i.imgur.com/irGca9q.gif) 

## Features

- **Secure Login**: Admins can log in to access and manage user data.
- **Health Metric Capture**: Regular users can input health data such as glucose levels, blood pressure, and BMI.
- **Prediction Accuracy**: The application provides accurate predictions based on the input data.
- **Data Management**: Admins can view, manage, and analyze the submitted health data through the admin dashboard.
- **User-Friendly Interface**: An intuitive and accessible interface for both admins and regular users.
- **Database Storage**: All user inputs and predictions are securely stored in a database.
## Tech Stack

**Client:** Streamlit

**Server:** Python, SQLite

**Machine Learning:** Scikit-learn, TensorFlow, Keras

**Database:** SQLite


## Installation

To set up the project, follow these steps:

1. **Clone the Repository:**
   ```bash
    git clone https://github.com/adyanandi/Diabetic_Alert.git
   cd Diabetic_Alert
2. **Ensure pipenv is Installed:**
    ```bash
    pipenv install
3. **Install Dependencies from requirements.txt:**
     ```bash
     pipenv install -r requirements.txt
4. **Activate the Virtual Environment**
     ```bash
     pipenv shell
5. **Run the Application**
     ```bash
     streamlit run app.py
.     


     






      
    
## Run Locally
To use the Diabetic Alert application,after installation follow these steps:

1. **Run the Application:**
   After setting up the project and activating the virtual environment, start the application with:
   ```bash
   streamlit run run.py
2. **Login as an Admin**

• Navigate to the admin login page.

• Enter your admin username and password to access the admin dashboard.

• **Note:** Regular users do not need to log in; they will interact with the application directly.

3. **Input Health Metrics (For Regular Users):**
• Regular users can access the main application interface without logging in.

• Enter the following health data:

Glucose Level: 120 mg/dL

Blood Pressure: 80/120 mmHg

BMI: 25 , and other information

4. **Make Predictions:**

• Regular users can click the Predict button after entering their health data.

• The application will display the prediction results based on the input data.

5. **Interpret Results:**

• Review the results displayed on the results page. The application provides insights and recommendations based on the prediction.

6. **Admin Data Management:**

• After regular users submit their data, it is stored in the database.

• Admins can log in to view and manage this data through the admin dashboard.

• Admins can access detailed records of all user inputs and perform data management tasks as needed.

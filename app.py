import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

@st.cache_resource
def train_model():
    df = pd.read_csv('https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv')
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df = df.dropna()
    df = df.reset_index(drop=True)
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    df = df.drop('customerID', axis=1)
    cat_cols = df.select_dtypes(include='object').columns.tolist()
    df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
    df = df.fillna(0)
    X = df.drop('Churn', axis=1)
    y = df['Churn']
    X = X.fillna(0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model, X_train.columns.tolist()

model, columns = train_model()

st.title("📊 Customer Churn Predictor")
st.write("Fill in the customer details below:")

tenure = st.slider("How many months has the customer been with us?", 0, 72, 12)
monthly_charges = st.number_input("Monthly bill amount ($)", 0.0, 200.0, 65.0)
total_charges = monthly_charges * tenure
contract = st.selectbox("Contract type?", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet service?", ["DSL", "Fiber optic", "No"])
tech_support = st.selectbox("Has tech support?", ["Yes", "No", "No internet service"])
online_security = st.selectbox("Has online security?", ["Yes", "No", "No internet service"])
gender = st.selectbox("Gender?", ["Male", "Female"])
senior = st.selectbox("Is senior citizen?", ["No", "Yes"])
partner = st.selectbox("Has a partner?", ["Yes", "No"])
dependents = st.selectbox("Has dependents?", ["Yes", "No"])
paperless = st.selectbox("Paperless billing?", ["Yes", "No"])

if st.button(" Predict Now"):
    input_dict = {col: 0 for col in columns}
    input_dict['tenure'] = tenure
    input_dict['MonthlyCharges'] = monthly_charges
    input_dict['TotalCharges'] = total_charges
    input_dict['SeniorCitizen'] = 1 if senior == "Yes" else 0
    if gender == "Male": input_dict['gender_Male'] = 1
    if partner == "Yes": input_dict['Partner_Yes'] = 1
    if dependents == "Yes": input_dict['Dependents_Yes'] = 1
    if paperless == "Yes": input_dict['PaperlessBilling_Yes'] = 1
    if contract == "One year": input_dict['Contract_One year'] = 1
    elif contract == "Two year": input_dict['Contract_Two year'] = 1
    if internet == "Fiber optic": input_dict['InternetService_Fiber optic'] = 1
    elif internet == "No": input_dict['InternetService_No'] = 1
    if tech_support == "No internet service": input_dict['TechSupport_No internet service'] = 1
    elif tech_support == "Yes": input_dict['TechSupport_Yes'] = 1
    if online_security == "No internet service": input_dict['OnlineSecurity_No internet service'] = 1
    elif online_security == "Yes": input_dict['OnlineSecurity_Yes'] = 1

    input_df = pd.DataFrame([input_dict])
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.divider()
    if prediction == 1:
        st.error(f"This customer will likely LEAVE — {probability*100:.1f}% chance of churning")
    else:
        st.success(f" This customer will likely STAY — only {probability*100:.1f}% chance of churning")
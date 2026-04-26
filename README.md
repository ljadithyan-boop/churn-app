# 📊 Customer Churn Predictor

> A machine learning web app that predicts whether a telecom customer will leave or stay — built with Python and Streamlit.

🔗 **Live App:** [Click here to try it](#) ← replace this with your Streamlit link after deploying

---

## 📌 Project Overview

Customer churn is one of the biggest problems in the telecom industry. Losing a customer costs much more than keeping one. This app helps businesses identify **which customers are likely to leave** before they actually do — so they can take action early.

---

## 🤔 What does this app do?

You enter details about a customer such as:
- How long they've been a customer
- Their monthly bill amount
- Their contract type
- Whether they have tech support or online security

The app instantly predicts whether that customer is likely to **STAY ✅** or **LEAVE ⚠️** — along with the exact probability percentage.

---

## 🧠 How it works

1. Loads real telecom data — IBM Telco Dataset with 7,043 customers and 21 features
2. Cleans and preprocesses the data automatically
3. Encodes categorical variables using One Hot Encoding
4. Trains a Logistic Regression model
5. Takes your inputs and makes a live prediction with probability score

---

## 📈 Model Performance

| Model | Accuracy |
|-------|----------|
| Logistic Regression | 81.76% |
| Decision Tree | 80.62% |

### Key Insights from the Data
- ~26% of customers in the dataset churned
- Month-to-month contract customers churn the most
- Customers with Fiber optic internet churn more than DSL customers
- Longer tenure customers are much less likely to churn

---

## 🛠️ Built With

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Streamlit | Web app framework |
| Scikit-learn | Machine learning model |
| Pandas | Data manipulation |
| NumPy | Numerical operations |

---

## 🚀 Run it locally

```bash

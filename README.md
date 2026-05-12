🏦 Loan Approval Prediction System

This project is a Machine Learning application that helps banks and financial institutions predict whether a loan applicant is eligible for a loan or not. It uses historical data to make accurate predictions.

📄 Project Description

The goal of this project is to automate the loan eligibility process. By using a trained Random Forest (or your specific model) algorithm, the system analyzes applicant details like income, credit score, and education to provide an instant "Approved" or "Rejected" status.

🛠️ Main Features
Interactive UI: Built with Streamlit for a smooth user experience.

Instant Prediction: Get results in real-time after entering data.

Data Driven: Uses advanced data preprocessing and machine learning.

💻 Technologies Used
Python (Core Language)

Pandas & NumPy (Data Manipulation)

Scikit-Learn (Machine Learning Model)

Streamlit (Web Interface)

Pickle (To save and load the trained model)

📊 Dataset Information
The model is trained on a dataset containing the following information:

Gender & Marital Status

Education & Employment

Applicant Income

Loan Amount & Term

Credit History (Key factor for prediction)

🚀 How to Run the Project
To run this project on your local machine, follow these steps:

Clone the repository:

Bash
git clone https://github.com/hamidngri5-gif/loan_approval_project.git
Install requirements:

Bash
pip install -r requirements.txt
Run the Streamlit app:

Bash
streamlit run loan_approval.py

import streamlit as st
import pandas as pd
import pickle

# load model
model = pickle.load(open("model.pkl", "rb"))
st.markdown("""
    <div style="
        background-color:#ff4b4b;
        padding:20px;
        border-radius:12px;
        text-align:center;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);">
        <h1 style="color:white;">🏦 Loan Approval Prediction App</h1>
    </div>
""", unsafe_allow_html=True)
#st.title("🏦 Loan Approval Prediction App")

# 🔹 USER INPUTS
id_laon = st.number_input("Loan ID")
no_of_dependents = st.number_input("Number of Dependents", min_value=0, max_value=10)

education = st.selectbox("Education", ["Graduate", "Not Graduate"])

self_employed = st.selectbox("Self Employed", ["Yes", "No"])

income_annum = st.number_input("Annual Income")

loan_amount = st.number_input("Loan Amount")

loan_term = st.number_input("Loan Term")

cibil_score = st.number_input("CIBIL Score")

residential_assets_value = st.number_input("Residential Assets Value")

commercial_assets_value = st.number_input("Commercial Assets Value")

luxury_assets_value = st.number_input("Luxury Assets Value")

bank_asset_value = st.number_input("Bank Asset Value")


# 🔹 PREDICTION BUTTON
st.markdown("""
<style>
div.stButton > button {
    background-color: green;
    color: white;
    border: 2px solid white;
    padding: 10px 25px;
    border-radius: 10px;
    font-size: 16px;
    font-weight: bold;
}
div.stButton > button:hover {
    background-color: darkgreen;
    border: 2px solid white;
}
</style>
""", unsafe_allow_html=True)



if st.button("Predict"):

    input_df = pd.DataFrame([{
        "loan_id":id_laon,
        "no_of_dependents": no_of_dependents,
        "education": education,
        "self_employed": self_employed,
        "income_annum": income_annum,
        "loan_amount": loan_amount,
        "loan_term": loan_term,
        "cibil_score": cibil_score,
        "residential_assets_value": residential_assets_value,
        "commercial_assets_value": commercial_assets_value,
        "luxury_assets_value": luxury_assets_value,
        "bank_asset_value": bank_asset_value
    }])

    prediction = model.predict(input_df)

    # 🔹 OUTPUT

    if prediction[0] == 0:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")
import streamlit as st
import numpy as np
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #0e1117;
}

.block-container {
    padding-top: 2rem;
}

h1 {
    text-align: center;
    color: #4CAF50;
}

.stButton>button {
    width: 100%;
    height: 55px;
    border-radius: 10px;
    font-size: 18px;
    font-weight: bold;
    background-color: #4CAF50;
    color: white;
}

.stButton>button:hover {
    background-color: #45a049;
}

div[data-testid="stMetric"]{
    background:#1e1e1e;
    padding:15px;
    border-radius:10px;
    border:1px solid #333;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "Model", "loan_prediction_model.pkl")

model = joblib.load(MODEL_PATH)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🏦 Loan Approval Prediction")

st.sidebar.markdown("---")

st.sidebar.subheader("Project")

st.sidebar.write("Machine Learning Based Loan Approval Prediction")

st.sidebar.subheader("Algorithm")

st.sidebar.success("Random Forest Classifier")

st.sidebar.subheader("Dataset")

st.sidebar.write("4269 Loan Applications")

st.sidebar.subheader("Technologies")

st.sidebar.write("""
- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
""")

st.sidebar.subheader("Developer")

st.sidebar.info("NIKUNJ")

st.sidebar.markdown("---")

st.sidebar.caption("AIML Summer Internship 2026")

# ---------------- TITLE ----------------
st.title("🏦 Loan Approval Prediction Dashboard")

st.markdown(
"""
<center>

Predict whether a customer will receive a loan approval based on
their financial details using Machine Learning.

</center>
""",
unsafe_allow_html=True
)

st.divider()

# ---------------- METRICS ----------------

c1, c2, c3 = st.columns(3)

c1.metric("Model", "Random Forest")
c2.metric("Dataset", "4269 Records")
c3.metric("Features", "11")

st.divider()

# ---------------- INPUTS ----------------

left, right = st.columns(2)

with left:

    dependents = st.number_input(
        "Number of Dependents",
        min_value=0,
        max_value=10,
        value=0
    )

    education = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"]
    )

    self_employed = st.selectbox(
        "Self Employed",
        ["No", "Yes"]
    )

    income = st.number_input(
        "Annual Income",
        min_value=0,
        value=5000000,
        step=100000
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0,
        value=10000000,
        step=100000
    )

with right:

    loan_term = st.number_input(
        "Loan Term (Years)",
        min_value=1,
        value=10
    )

    cibil = st.slider(
        "CIBIL Score",
        300,
        900,
        700
    )

    residential = st.number_input(
        "Residential Assets",
        min_value=0,
        value=1000000,
        step=100000
    )

    commercial = st.number_input(
        "Commercial Assets",
        min_value=0,
        value=1000000,
        step=100000
    )

    luxury = st.number_input(
        "Luxury Assets",
        min_value=0,
        value=1000000,
        step=100000
    )

    bank = st.number_input(
        "Bank Assets",
        min_value=0,
        value=1000000,
        step=100000
    )

# ---------------- ENCODING ----------------

education = 1 if education == "Graduate" else 0

self_employed = 1 if self_employed == "Yes" else 0

st.divider()

# ---------------- PREDICTION ----------------

if st.button("🔍 Predict Loan Status"):

    input_data = np.array([[
        dependents,
        education,
        self_employed,
        income,
        loan_amount,
        loan_term,
        cibil,
        residential,
        commercial,
        luxury,
        bank
    ]])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    confidence = np.max(probability) * 100

    st.subheader("Prediction Result")

    if prediction == 1 or prediction == "Approved":

        st.success("✅ Loan Approved")

        st.progress(int(confidence))

        st.write(f"### Confidence : {confidence:.2f}%")

        st.balloons()

    else:

        st.error("❌ Loan Rejected")

        st.progress(int(confidence))

        st.write(f"### Confidence : {confidence:.2f}%")

st.divider()

st.markdown(
"""
<center>

Developed using ❤️ Python | Scikit-Learn | Streamlit

</center>
""",
unsafe_allow_html=True
)

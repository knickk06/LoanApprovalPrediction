# 🏦 Loan Approval Prediction System

A Machine Learning web application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on an applicant's financial and personal details.

Developed as part of the **AIML Summer Internship 2026** conducted by **IIHMF, MNNIT Allahabad, Prayagraj**.

---

## 📌 Project Overview

Financial institutions process thousands of loan applications every day. Manual evaluation is often time-consuming and may lead to inconsistent decisions.

This project uses Machine Learning to automate the loan approval prediction process by analyzing applicant information such as income, CIBIL score, loan amount, assets, education, and employment status.

The final model has been deployed using **Streamlit**, allowing users to interact with the prediction system through a simple web interface.

---

## 🎯 Objectives

- Predict loan approval status using Machine Learning.
- Perform complete data preprocessing and exploratory data analysis (EDA).
- Compare multiple classification algorithms.
- Select the best-performing model.
- Deploy the model using Streamlit.

---

## 📂 Dataset

**Source:** Kaggle Loan Approval Dataset

### Dataset Information

- Total Records: **4269**
- Features: **11**
- Target Variable: **Loan Status**

### Features Used

- Number of Dependents
- Education
- Self Employed
- Annual Income
- Loan Amount
- Loan Term
- CIBIL Score
- Residential Assets Value
- Commercial Assets Value
- Luxury Assets Value
- Bank Asset Value

Target:

- Approved
- Rejected

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Git & GitHub

---

## 📊 Machine Learning Workflow

1. Problem Understanding
2. Data Collection
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Feature Engineering
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Model Deployment

---

## 🤖 Machine Learning Models

The following classification models were implemented:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

Random Forest was selected as the final model due to its superior performance.

---

## 📈 Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score

---

## 🚀 Streamlit Application

### Live Demo

**https://loan-approval-prediction-mgikbpfxsp8uvgzcrus5yf.streamlit.app/**

### Features

- User-friendly interface
- Instant loan prediction
- Real-time input
- Fast response
- Web-based deployment

---

## 📁 Project Structure

```
LoanApprovalPrediction/
│
├── Dataset/
│
├── Notebook/
│   └── Loan_Approval_Prediction.ipynb
│
├── Model/
│   └── loan_prediction_model.pkl
│
├── Streamlit_App/
│   └── app.py
│
├── Documentation/
│
├── README.md
│
├── requirements.txt
│
└── .gitignore
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/knickk06/LoanApprovalPrediction.git
```

Move into the project folder

```bash
cd LoanApprovalPrediction
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
cd Streamlit_App
streamlit run app.py
```

---

## 📷 Application Screenshots

Add screenshots here.

Example:

- Home Page
- Loan Approved Prediction
- Loan Rejected Prediction

---

## 📚 Future Improvements

- Explainable AI using SHAP
- Hyperparameter tuning
- Cloud deployment (AWS/Azure)
- REST API integration
- Database connectivity
- Deep Learning implementation

---

## 🎓 Internship Details

**Program**

Artificial Intelligence & Machine Learning Summer Internship 2026

**Organization**

Indian Institute of Information Management & Human Factors (IIHMF)

Motilal Nehru National Institute of Technology (MNNIT), Allahabad

---

## 👨‍💻 Author

**Your Name**

GitHub:
https://github.com/knickk06

---

## 📄 License

This project was developed for educational purposes as part of the AIML Summer Internship Program.

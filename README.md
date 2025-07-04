# Loan Eligibility Predictor 

This project is a Machine Learning-based web app that predicts whether a user is eligible for a loan based on their details such as income, education, property area, and more. Built using `scikit-learn`, `Gradio`, and deployed on Hugging Face Spaces.



https://github.com/user-attachments/assets/819a8eaf-7fa7-4d23-9873-c20515ff80db



https://github.com/user-attachments/assets/5e8757a7-897d-4e9a-a389-2523fcac18a3



---

## Demo

https://huggingface.co/spaces/Prap017/loan_eligibility_predictor
---

## Features

-  Predict loan eligibility based on applicant details
-  Built with RandomForestClassifier (scikit-learn)
-  Trained on real-world loan dataset
-  Web interface using Gradio
-  Free deployment via Hugging Face

---

## Project Structure

loan-eligibility-predictor/
├── src/
│ ├── app.py # Gradio interface code
│ ├── loan_model.pkl # Trained ML model
├── requirements.txt # Dependencies
├── README.md # Project documentation



---

## Dataset

- Source: Public loan dataset (e.g., Kaggle – Loan Prediction Dataset)
- Format: CSV with fields like:
  - Gender, Married, Education, Self_Employed
  - ApplicantIncome, LoanAmount, Property_Area
  - Loan_Status (target)

---

## ML Model Overview

- Algorithm: `RandomForestClassifier`  
- Preprocessing: Label Encoding on categorical features  
- Target: `Loan_Status` (0 = Not Eligible, 1 = Eligible)

```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

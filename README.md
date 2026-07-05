# 🏦 Smart Lender – AI-Based Loan Approval Prediction

Smart Lender is a Machine Learning-based web application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on the applicant's financial and personal information.

The project was developed as part of the **SmartBridge IBM SkillsBuild Internship** using Python, Flask, and XGBoost.

---

## 📌 Project Overview

Financial institutions process thousands of loan applications every day. Manual verification is time-consuming and may lead to inconsistent decisions.

Smart Lender automates this process by using a trained **XGBoost Machine Learning model** to predict loan approval status instantly through an easy-to-use web interface.

---

## 🚀 Features

- 🏠 Interactive Home Page
- 📝 Loan Application Form
- 🤖 Machine Learning Prediction
- ⚡ XGBoost Classification Model
- 🌐 Flask Web Application
- 📱 Responsive User Interface
- ✅ Instant Loan Approval/Rejection Result

---

## 🛠️ Technology Stack

### Programming Language
- Python

### Machine Learning
- XGBoost
- Scikit-learn
- Pandas
- NumPy

### Web Development
- Flask
- HTML5
- CSS3

### Development Tools
- Google Colab
- Visual Studio Code
- Git
- GitHub

---

## 📂 Project Structure

```
Smart Lender
│
├── dataset
│   └── loan_prediction.csv
│
├── Flask
│   ├── templates
│   │   ├── home.html
│   │   ├── index.html
│   │   └── result.html
│   │
│   ├── static
│   ├── app.py
│   ├── model.pkl
│   ├── scaler.pkl
│   └── bank.png
│
├── IBM
│
├── Training
│   └── Loan Prediction.ipynb
│
└── README.md
```

---

## 📊 Machine Learning Workflow

1. Dataset Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Data Preprocessing
5. Feature Encoding
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Flask Integration
10. Loan Prediction

---

## 🤖 Machine Learning Models Used

- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- XGBoost ✅ (Selected Model)

Among all models, **XGBoost** achieved the best performance and was selected for deployment.

---

## 💻 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Smart-Lender.git
```

Move to project folder

```bash
cd Smart-Lender/Flask
```

Install dependencies

```bash
pip install flask pandas numpy scikit-learn xgboost
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📸 Application Screenshots

### Home Page

- Smart Lender Landing Page
  <img width="1134" height="645" alt="image" src="https://github.com/user-attachments/assets/d1679658-5883-4945-9269-095d4a58f89a" />


### Loan Prediction Form

- User enters applicant information.
  <img width="1132" height="640" alt="image" src="https://github.com/user-attachments/assets/09509254-f79d-4e7f-9486-66e4b78ef152" />


### Prediction Result

- Loan Approved
  <img width="1150" height="636" alt="image" src="https://github.com/user-attachments/assets/4e31b71e-6416-48d7-89ec-d249f3f58d07" />

- Loan Rejected
<img width="1134" height="637" alt="image" src="https://github.com/user-attachments/assets/0bc25ba3-5183-4e82-b816-6e7d8fd2fa1d" />

---

## 📈 Future Enhancements

- IBM Cloud Deployment
- User Authentication
- Database Integration
- Explainable AI
- Mobile Application
- REST API Integration

---

## 🎯 Project Outcome

The Smart Lender application successfully predicts loan approval status using machine learning, reducing manual effort and enabling faster, data-driven loan decisions.

---

## 👨‍💻 Developed By

**Sahith Kotaru**

B.Tech – Data Science

Kallam Haranadhareddy Institute of Technology

---

## 📄 License

This project is developed for academic and learning purposes as part of the SmartBridge IBM SkillsBuild Internship.

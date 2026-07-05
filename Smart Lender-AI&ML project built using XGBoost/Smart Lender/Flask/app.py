from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/application")
def application():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        # ------------------------
        # Categorical Encoding
        # ------------------------

        gender = 1 if request.form["Gender"] == "Male" else 0
        married = 1 if request.form["Married"] == "Yes" else 0

        dependents = request.form["Dependents"]
        dependents = 3 if dependents == "3+" else int(dependents)

        education = 0 if request.form["Education"] == "Graduate" else 1
        self_employed = 1 if request.form["Self_Employed"] == "Yes" else 0

        property_area = {
            "Rural": 0,
            "Semiurban": 1,
            "Urban": 2
        }[request.form["Property_Area"]]

        # ------------------------
        # Numerical Inputs
        # ------------------------

        applicant_income = float(request.form["ApplicantIncome"])
        coapplicant_income = float(request.form["CoapplicantIncome"])
        loan_amount = float(request.form["LoanAmount"])
        loan_term = float(request.form["Loan_Amount_Term"])
        credit_history = float(request.form["Credit_History"])

        # Scale numerical values
        scaled = scaler.transform([[
            applicant_income,
            coapplicant_income,
            loan_amount,
            loan_term
        ]])

        applicant_income = scaled[0][0]
        coapplicant_income = scaled[0][1]
        loan_amount = scaled[0][2]
        loan_term = scaled[0][3]

        features = np.array([[
            gender,
            married,
            dependents,
            education,
            self_employed,
            applicant_income,
            coapplicant_income,
            loan_amount,
            loan_term,
            credit_history,
            property_area
        ]])

        prediction = model.predict(features)

        if prediction[0] == 1:
            message = "Congrats! Your Loan is Approved"
            icon = "✅"
            color = "#16a34a"
        else:
            message = "Sorry! Your Loan is Rejected"
            icon = "❌"
            color = "#dc2626"

        return render_template(
            "result.html",
            message=message,
            icon=icon,
            color=color
        )

    except Exception as e:
        return f"<h2>Error:</h2><p>{e}</p>"


if __name__ == "__main__":
    app.run(debug=True)
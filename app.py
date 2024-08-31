from flask import Flask, render_template, request, url_for
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

model = joblib.load(open("Bankloan.jb", "rb"))

df = pd.read_csv("Clean df")
 
@app.route('/')
def home():
    return render_template("home.html")

@app.route("/details")
def details():
    return render_template("details.html")

@app.route("/output")
def output():
    return render_template("output.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        Age = request.form.get("Age")
        Experience = request.form.get("Experience")
        Income = request.form.get("Income")
        Family = request.form.get("Family")
        CCAvg = request.form.get("CCAvg")
        Education = request.form.get("Education")
        Mortgage = request.form.get("Mortgage")
        Personal_Loan = request.form.get("Personal.Loan")
        Securities_Account = request.form.get("Securities.Account")
        CD_Account = request.form.get("CD.Account")
        Online = request.form.get("Online")

        ## convert it into appropriate datatype
        Age = int(Age)
        Experience = int(Experience)
        Income = int(Income)
        Family = int(Family)
        CCAvg = float(CCAvg)
        Education = int(Education)
        Mortgage = float(Mortgage)
        Personal_Loan = int(Personal_Loan)
        Securities_Account = int(Securities_Account)
        CD_Account = int(CD_Account)
        Online = int(Online)

        user_data = [[Age, Experience, Income, Family, CCAvg, Education, Mortgage, Personal_Loan, Securities_Account, CD_Account, Online]]
                
        pred = model.predict(user_data)[0]
        prediction = str(round(pred,2))

        return render_template("output.html", prediction_text=f"Loan eligibility prediction is :- {prediction}")

if __name__ =="__main__":
    app.run(debug=True)
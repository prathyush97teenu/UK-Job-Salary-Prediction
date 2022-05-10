from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("salary_rf.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        Title=request.form['Title']
        if(Title=='Business_Development_Manager'):
            Business_Development_Manager = 1
            Management_Accountant = 0
            Project_Manager = 0
            Sales_Executive = 0
            Finance_Manager = 0
            Account_Manager = 0 
            Mechanical_Design_Engineer = 0
            Credit_Controller = 0
            Financial_Controller = 0
            Recruitment_Consultant = 0

        elif(Title=='Management_Accountant'):
            Business_Development_Manager = 0
            Management_Accountant = 1
            Project_Manager = 0
            Sales_Executive = 0
            Finance_Manager = 0
            Account_Manager = 0 
            Mechanical_Design_Engineer = 0
            Credit_Controller = 0
            Financial_Controller = 0
            Recruitment_Consultant = 0

        elif(Title=='Project_Manager'):
            Business_Development_Manager = 0
            Management_Accountant = 0
            Project_Manager = 1
            Sales_Executive = 0
            Finance_Manager = 0
            Account_Manager = 0 
            Mechanical_Design_Engineer = 0
            Credit_Controller = 0
            Financial_Controller = 0
            Recruitment_Consultant = 0

        elif(Title=='Sales_Executive'):
            Business_Development_Manager = 0
            Management_Accountant = 0
            Project_Manager = 0
            Sales_Executive = 1
            Finance_Manager = 0
            Account_Manager = 0 
            Mechanical_Design_Engineer = 0
            Credit_Controller = 0
            Financial_Controller = 0
            Recruitment_Consultant = 0
            
        elif(Title=='Finance_Manager'):
            Business_Development_Manager = 0
            Management_Accountant = 0
            Project_Manager = 0
            Sales_Executive = 0
            Finance_Manager = 1
            Account_Manager = 0 
            Mechanical_Design_Engineer = 0
            Credit_Controller = 0
            Financial_Controller = 0
            Recruitment_Consultant = 0
            
        elif(Title=='Account_Manager'):
            Business_Development_Manager = 0
            Management_Accountant = 0
            Project_Manager = 0
            Sales_Executive = 0
            Finance_Manager = 0
            Account_Manager = 1 
            Mechanical_Design_Engineer = 0
            Credit_Controller = 0
            Financial_Controller = 0
            Recruitment_Consultant = 0

        elif(Title=='Mechanical_Design_Engineer'):
            Business_Development_Manager = 0
            Management_Accountant = 0
            Project_Manager = 0
            Sales_Executive = 0
            Finance_Manager = 0
            Account_Manager = 0 
            Mechanical_Design_Engineer = 1
            Credit_Controller = 0
            Financial_Controller = 0
            Recruitment_Consultant = 0

        elif(Title=='Credit_Controller'):
            Business_Development_Manager = 0
            Management_Accountant = 0
            Project_Manager = 0
            Sales_Executive = 0
            Finance_Manager = 0
            Account_Manager = 0 
            Mechanical_Design_Engineer = 0
            Credit_Controller = 1
            Financial_Controller = 0
            Recruitment_Consultant = 0


        elif(Title=='Financial_Controller'):
            Business_Development_Manager = 0
            Management_Accountant = 0
            Project_Manager = 0
            Sales_Executive = 0
            Finance_Manager = 0
            Account_Manager = 0 
            Mechanical_Design_Engineer = 0
            Credit_Controller = 0
            Financial_Controller = 1
            Recruitment_Consultant = 0 
            
        elif(Title=='Recruitment_Consultant'):
            Business_Development_Manager = 0
            Management_Accountant = 0
            Project_Manager = 0
            Sales_Executive = 0
            Finance_Manager = 0
            Account_Manager = 0 
            Mechanical_Design_Engineer = 0
            Credit_Controller = 0
            Financial_Controller = 0
            Recruitment_Consultant = 1
        
        else:
            Business_Development_Manager = 0
            Management_Accountant = 0
            Project_Manager = 0
            Sales_Executive = 0
            Finance_Manager = 0
            Account_Manager = 0 
            Mechanical_Design_Engineer = 0
            Credit_Controller = 0
            Financial_Controller = 0
            Recruitment_Consultant = 0

        Location = request.form["Location"]
        if(Location=='UK'):
            UK = 1
            London = 0
            South_East_London = 0
            The_City = 0
            Central_London = 0
            Leeds = 0
            West_Midlands = 0
            Manchester = 0
            Surrey = 0
            Birmingham = 0

        elif(Location=='London'):
            UK = 0
            London = 1
            South_East_London = 0
            The_City = 0
            Central_London = 0
            Leeds = 0
            West_Midlands = 0
            Manchester = 0
            Surrey = 0
            Birmingham = 0

        elif(Location=='South_East_London'):
            UK = 0
            London = 0
            South_East_London = 1
            The_City = 0
            Central_London = 0
            Leeds = 0
            West_Midlands = 0
            Manchester = 0
            Surrey = 0
            Birmingham = 0

        elif(Location=='The_City'):
            UK = 0
            London = 0
            South_East_London = 0
            The_City = 1
            Central_London = 0
            Leeds = 0
            West_Midlands = 0
            Manchester = 0
            Surrey = 0
            Birmingham = 0


        elif(Location=='Central_London'):
            UK = 0
            London = 0
            South_East_London = 0
            The_City = 0
            Central_London = 1
            Leeds = 0
            West_Midlands = 0
            Manchester = 0
            Surrey = 0
            Birmingham = 0
            
        elif(Location=='Leeds'):
            UK = 0
            London = 0
            South_East_London = 0
            The_City = 0
            Central_London = 0
            Leeds = 1
            West_Midlands = 0
            Manchester = 0
            Surrey = 0
            Birmingham = 0
        
        elif(Location=='West_Midlands'):
            UK = 0
            London = 0
            South_East_London = 0
            The_City = 0
            Central_London = 0
            Leeds = 0
            West_Midlands = 1
            Manchester = 0
            Surrey = 0
            Birmingham = 0
        
        elif(Location=='Manchester'):
            UK = 0
            London = 0
            South_East_London = 0
            The_City = 0
            Central_London = 0
            Leeds = 0
            West_Midlands = 0
            Manchester = 1
            Surrey = 0
            Birmingham = 0
        
        elif(Location=='Surrey'):
            UK = 0
            London = 0
            South_East_London = 0
            The_City = 0
            Central_London = 0
            Leeds = 0
            West_Midlands = 0
            Manchester = 0
            Surrey = 1
            Birmingham = 0
        
        elif(Location=='Birmingham'):
            UK = 0
            London = 0
            South_East_London = 0
            The_City = 0
            Central_London = 0
            Leeds = 0
            West_Midlands = 0
            Manchester = 0
            Surrey = 0
            Birmingham = 1

        else:
            UK = 0
            London = 0
            South_East_London = 0
            The_City = 0
            Central_London = 0
            Leeds = 0
            West_Midlands = 0
            Manchester = 0
            Surrey = 0
            Birmingham = 0

        Company = request.form["Company"]
        if(Company=='UKStaffsearch'):
            UKStaffsearch = 1
            CVbrowser = 0
            London4Jobs = 0
            Hays = 0
            JAM_Recruitment_Ltd = 0
            Office_Angels = 0
            Jobsite_Jobs = 0
            ARRAY = 0
            JOBG8 = 0
            Randstad = 0
        
        elif(Company=='CVbrowser'):
            UKStaffsearch = 0
            CVbrowser = 1
            London4Jobs = 0
            Hays = 0
            JAM_Recruitment_Ltd = 0
            Office_Angels = 0
            Jobsite_Jobs = 0
            ARRAY = 0
            JOBG8 = 0
            Randstad = 0
        
        elif(Company=='London4Jobs'):
            UKStaffsearch = 0
            CVbrowser = 0
            London4Jobs = 1
            Hays = 0
            JAM_Recruitment_Ltd = 0
            Office_Angels = 0
            Jobsite_Jobs = 0
            ARRAY = 0
            JOBG8 = 0
            Randstad = 0

        elif(Company=='Hays'):
            UKStaffsearch = 0
            CVbrowser = 0
            London4Jobs = 0
            Hays = 1
            JAM_Recruitment_Ltd = 0
            Office_Angels = 0
            Jobsite_Jobs = 0
            ARRAY = 0
            JOBG8 = 0
            Randstad = 0
            
        elif(Company=='JAM_Recruitment_Ltd'):
            UKStaffsearch = 0
            CVbrowser = 0
            London4Jobs = 0
            Hays = 0
            JAM_Recruitment_Ltd = 1
            Office_Angels = 0
            Jobsite_Jobs = 0
            ARRAY = 0
            JOBG8 = 0
            Randstad = 0
        
        elif(Company=='Office_Angels'):
            UKStaffsearch = 0
            CVbrowser = 0
            London4Jobs = 0
            Hays = 0
            JAM_Recruitment_Ltd = 0
            Office_Angels = 1
            Jobsite_Jobs = 0
            ARRAY = 0
            JOBG8 = 0
            Randstad = 0
        
        elif(Company=='Jobsite_Jobs'):
            UKStaffsearch = 0
            CVbrowser = 0
            London4Jobs = 0
            Hays = 0
            JAM_Recruitment_Ltd = 0
            Office_Angels = 0
            Jobsite_Jobs = 1
            ARRAY = 0
            JOBG8 = 0
            Randstad = 0
            
        elif(Company=='ARRAY'):
            UKStaffsearch = 0
            CVbrowser = 0
            London4Jobs = 0
            Hays = 0
            JAM_Recruitment_Ltd = 0
            Office_Angels = 0
            Jobsite_Jobs = 0
            ARRAY = 1
            JOBG8 = 0
            Randstad = 0
        
        elif(Company=='JOBG8'):
            UKStaffsearch = 0
            CVbrowser = 0
            London4Jobs = 0
            Hays = 0
            JAM_Recruitment_Ltd = 0
            Office_Angels = 0
            Jobsite_Jobs = 0
            ARRAY = 0
            JOBG8 = 1
            Randstad = 0
        
        elif(Company=='Randstad'):
            UKStaffsearch = 0
            CVbrowser = 0
            London4Jobs = 0
            Hays = 0
            JAM_Recruitment_Ltd = 0
            Office_Angels = 0
            Jobsite_Jobs = 0
            ARRAY = 0
            JOBG8 = 0
            Randstad = 1

        else:
            UKStaffsearch = 0
            CVbrowser = 0
            London4Jobs = 0
            Hays = 0
            JAM_Recruitment_Ltd = 0
            Office_Angels = 0
            Jobsite_Jobs = 0
            ARRAY = 0
            JOBG8 = 0
            Randstad = 0
        
        Category = request.form["Category"]
        if(Category=='IT_Jobs'):
            IT_Jobs = 1
            Engineering_Jobs = 0
            Accounting_Finance_Jobs = 0
            Sales_Jobs = 0
            Other_General_Jobs = 0
            Teaching_Jobs = 0
            Healthcare_Nursing_Jobs = 0
            Trade_Construction_Jobs = 0
            Retail_Jobs = 0
            PR_Advertising_Marketing_Jobs = 0

        elif(Category=='Engineering_Jobs'):
            IT_Jobs = 0
            Engineering_Jobs = 1
            Accounting_Finance_Jobs = 0
            Sales_Jobs = 0
            Other_General_Jobs = 0
            Teaching_Jobs = 0
            Healthcare_Nursing_Jobs = 0
            Trade_Construction_Jobs = 0
            Retail_Jobs = 0
            PR_Advertising_Marketing_Jobs = 0
        
        elif(Category=='Accounting_Finance_Jobs'):
            IT_Jobs = 0
            Engineering_Jobs = 0
            Accounting_Finance_Jobs = 1
            Sales_Jobs = 0
            Other_General_Jobs = 0
            Teaching_Jobs = 0
            Healthcare_Nursing_Jobs = 0
            Trade_Construction_Jobs = 0
            Retail_Jobs = 0
            PR_Advertising_Marketing_Jobs = 0
        
        elif(Category=='Sales_Jobs'):
            IT_Jobs = 0
            Engineering_Jobs = 0
            Accounting_Finance_Jobs = 0
            Sales_Jobs = 1
            Other_General_Jobs = 0
            Teaching_Jobs = 0
            Healthcare_Nursing_Jobs = 0
            Trade_Construction_Jobs = 0
            Retail_Jobs = 0
            PR_Advertising_Marketing_Jobs = 0
        
        elif(Category=='Other_General_Jobs'):
            IT_Jobs = 0
            Engineering_Jobs = 0
            Accounting_Finance_Jobs = 0
            Sales_Jobs = 0
            Other_General_Jobs = 1
            Teaching_Jobs = 0
            Healthcare_Nursing_Jobs = 0
            Trade_Construction_Jobs = 0
            Retail_Jobs = 0
            PR_Advertising_Marketing_Jobs = 0
        
        elif(Category=='Teaching_Jobs'):
            IT_Jobs = 0
            Engineering_Jobs = 0
            Accounting_Finance_Jobs = 0
            Sales_Jobs = 0
            Other_General_Jobs = 0
            Teaching_Jobs = 1
            Healthcare_Nursing_Jobs = 0
            Trade_Construction_Jobs = 0
            Retail_Jobs = 0
            PR_Advertising_Marketing_Jobs = 0
        
        elif(Category=='Healthcare_Nursing_Jobs'):
            IT_Jobs = 0
            Engineering_Jobs = 0
            Accounting_Finance_Jobs = 0
            Sales_Jobs = 0
            Other_General_Jobs = 0
            Teaching_Jobs = 0
            Healthcare_Nursing_Jobs = 1
            Trade_Construction_Jobs = 0
            Retail_Jobs = 0
            PR_Advertising_Marketing_Jobs = 0
        
        elif(Category=='Trade_Construction_Jobs'):
            IT_Jobs = 0
            Engineering_Jobs = 0
            Accounting_Finance_Jobs = 0
            Sales_Jobs = 0
            Other_General_Jobs = 0
            Teaching_Jobs = 0
            Healthcare_Nursing_Jobs = 0
            Trade_Construction_Jobs = 1
            Retail_Jobs = 0
            PR_Advertising_Marketing_Jobs = 0
        
        elif(Category=='Retail_Jobs'):
            IT_Jobs = 0
            Engineering_Jobs = 0
            Accounting_Finance_Jobs = 0
            Sales_Jobs = 0
            Other_General_Jobs = 0
            Teaching_Jobs = 0
            Healthcare_Nursing_Jobs = 0
            Trade_Construction_Jobs = 0
            Retail_Jobs = 1
            PR_Advertising_Marketing_Jobs = 0
        
        
        elif(Category=='PR_Advertising_Marketing_Jobs'):
            IT_Jobs = 0
            Engineering_Jobs = 0
            Accounting_Finance_Jobs = 0
            Sales_Jobs = 0
            Other_General_Jobs = 0
            Teaching_Jobs = 0
            Healthcare_Nursing_Jobs = 0
            Trade_Construction_Jobs = 0
            Retail_Jobs = 0
            PR_Advertising_Marketing_Jobs = 1
	
        ContractType = request.form["ContractType"]
        if(ContractType=='full_time'):
            full_time = 1
            part_time = 0
        
        else:
            full_time = 0
            part_time = 1
                
        ContractTime = request.form["ContractTime"]
        if(ContractTime=='permanent'):
            permanent = 1
            contract = 0
        else:
            permanent = 0
            contract = 1
        
        prediction=model.predict([[Business_Development_Manager, Management_Accountant,
        Project_Manager, Sales_Executive, Finance_Manager,
        Account_Manager, Mechanical_Design_Engineer, Credit_Controller,
        Financial_Controller, Recruitment_Consultant, UK, London,
        South_East_London, The_City, Central_London, Leeds,
        West_Midlands, Manchester, Surrey, Birmingham, UKStaffsearch,
        CVbrowser, London4Jobs, Hays, JAM_Recruitment_Ltd,
        Office_Angels, Jobsite_Jobs, ARRAY, JOBG8, Randstad,
        IT_Jobs, Engineering_Jobs, Accounting_Finance_Jobs, Sales_Jobs,
        Other_General_Jobs, Teaching_Jobs, Healthcare_Nursing_Jobs,
        Trade_Construction_Jobs, Retail_Jobs,
        PR_Advertising_Marketing_Jobs,full_time,permanent]])
        
        #prediction=model.predict([[1, 0, 0, 0, 0,
        #0, 0, 0, 0, 0, 0, 0, 0,
        #0, 0, 0, 1, 0, 0, 0, 0, 0, 
        #0, 0, 0, 0, 0, 0, 1, 0, 	
        #0, 0, 0, 0, 0, 0, 0, 	
        #1, 0, 0]])
        
        output=round(prediction[0],2)
        
        return render_template('home.html',prediction_text="Estimated Salary is €{}".format(output))
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)

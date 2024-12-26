from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Define min and max values for each feature
feature_limits = {
    "Age": {"min": 18, "max": 170},
    "Tenure": {"min": 1, "max": 80},
    "MonthlyCharges": {"min": 0, "max": 500},
    "TotalCharges": {"min": 0, "max": 9984.36},
    "ServiceUsage1": {"min": 0, "max": 300},
    "ServiceUsage2": {"min": 0, "max": 300},
    "ServiceUsage3": {"min": 0, "max": 300},
}

def check_feature_limits(feature_name, value):
    limits = feature_limits.get(feature_name)
    if limits:
          if value <= limits["min"] or value >= limits["max"]:
              return f"{feature_name} value {value} is out of bounds. Should be between {limits['min']} and {limits['max']}."
    return None

@app.route('/', methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        gender = request.form["Gender"]
        gender_mapped = 1 if gender == "Male" else 0  
        
        # DATA COLLECTION
        age = int(request.form["Age"])
        tenure = int(request.form["Tenure"])
        monthlyCharges = float(request.form["MonthlyCharges"])
        totalCharges = float(request.form["TotalCharges"])
        ServiceUsage1 = float(request.form["ServiceUsage1"])
        ServiceUsage2 = float(request.form["ServiceUsage2"])
        ServiceUsage3 = float(request.form["ServiceUsage3"])
        
        checks = [
            check_feature_limits("Age", age),
            check_feature_limits("Tenure", tenure),
            check_feature_limits("MonthlyCharges", monthlyCharges),
            check_feature_limits("TotalCharges", totalCharges),
            check_feature_limits("ServiceUsage1", ServiceUsage1),
            check_feature_limits("ServiceUsage2", ServiceUsage2),
            check_feature_limits("ServiceUsage3", ServiceUsage3),
        ]
        
        # CHECKS
        
        for check in checks:
            if check:
                return render_template('churn.html', data=f"Error: {check}")
        if not all(request.form.get(field) for field in ['Gender', 'Age', 'Tenure', 'MonthlyCharges', 'TotalCharges', 'ServiceUsage1', 'ServiceUsage2', 'ServiceUsage3', 'Payment']):
            return render_template('churn.html', data="Error: All fields are required.")
        number_of_months = totalCharges / monthlyCharges
        total_service_usage = ServiceUsage1 + ServiceUsage2 + ServiceUsage3
        avg_service_usage = (ServiceUsage1 + ServiceUsage2 + ServiceUsage3) / 3
        try:
            age = int(request.form["Age"])
            tenure = int(request.form["Tenure"])
            monthlyCharges = float(request.form["MonthlyCharges"])
            totalCharges = float(request.form["TotalCharges"])
        except ValueError:
            return render_template('churn.html', data="Error: Please enter valid numerical values.")
          
        # ENCODING
        payment_method = request.form["Payment"]
        payment_cash = 1 if payment_method == "Cash" else 0
        payment_credit_card = 1 if payment_method == "Credit Card" else 0
        payment_paypal = 1 if payment_method == "PayPal" else 0
        
        features = [
            gender_mapped,
            age,
            tenure,
            number_of_months,
            total_service_usage,
            avg_service_usage,
            payment_cash,
            payment_credit_card,
            payment_paypal
        ]
        
        try:
            model = joblib.load('./models/model.pkl')
            scaler = joblib.load('./models/scaler.pkl')
        except Exception as e:
            return render_template('churn.html', data=f"Error loading model or scaler: {str(e)}")



        scaled_features = scaler.transform([features])
        prob = model.predict_proba(scaled_features)[0][1]
        print(f"Prediction: {prob}")
        prob = prob*100
        
        return render_template('churn.html', data=prob)
    else:
        return render_template('churn.html', data="100")


if __name__ == '__main__':
    app.run(debug=True)

# Assignment Title: Predict Customer Churn and Build Insights for Retention

## Scenario:
You are tasked with analyzing customer data for a subscription-based service provider to identify patterns, predict churn, and propose retention strategies. Additionally, build a recommendation engine to enhance customer engagement.


## Steps to Run the Flask API Locally

1. **Clone the Repository**:
   - Clone the project repository to your local machine:
     ```bash
     git clone https://github.com/Kevinjoythomas/craftmyplate-final-assignment
     ```
   - Navigate to the project directory:
     ```bash
     cd craftmyplate-final-assignment
     ```

2. **Python Environment**:
   - Python 3.8.19

3. **Required Libraries**:
   - Install the required dependencies listed in `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

4. **Model File**:
   - Ensure the trained model file (`model.pkl`) and scaler (`scaler.pkl`) is available in the specified folder (`./models/`).

5. **Install Dependencies**:
   - Install the required Python libraries:
     ```bash
     pip install -r requirements.txt
     ```

6. **Run the Flask App**:
   - Start the Flask development server:
     ```bash
     python app.py
     ```
   - The server will run locally at `http://127.0.0.1:5000/`.

7. **Test the API**:
   - Open a web browser or Postman to test the API.
   - **Using a Browser**:
     - Go to `http://127.0.0.1:5000/` to access the user interface.
     - Fill in the required form fields and submit.
   - **Using Postman**:
     - Send a POST request to `http://127.0.0.1:5000/` with the following sample JSON payload for example:
       ```json
       {
         "Gender": "Male",
         "Age": 30,
         "Tenure": 12,
         "MonthlyCharges": 50.0,
         "TotalCharges": 600.0,
         "ServiceUsage1": 10.0,
         "ServiceUsage2": 15.0,
         "ServiceUsage3": 20.0,
         "Payment": "Credit Card"
       }
       ```
     - Verify the response JSON for predictions.


## Example Response
- On successful form submission, the predicted churn probability will be displayed as a percentage.
- ![Success](https://github.com/Kevinjoythomas/craftmyplate-final-assignment/blob/main/static/css/Screenshot%202024-12-26%20182227.png)


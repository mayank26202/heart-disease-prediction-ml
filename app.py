from flask import Flask, request, render_template, redirect, url_for, send_file
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')



app = Flask(__name__)

# Load the models
with open('models.pkl', 'rb') as f:
    models = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        
        # Initialize feature variables
        features = ['age', 'gender', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        data = []
        
        # Convert to numeric values and validate
        try:
            for feature in features:
                value = request.form[feature]
                if feature in ['age', 'gender', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'slope', 'ca', 'thal']:
                    value = int(value)
                elif feature == 'oldpeak':
                    value = float(value)
                data.append(value)
            
            # Convert list to numpy array
            data = np.array([data])
            
        except ValueError as e:
            return f"Error: {e}. Ensure all inputs are valid numeric values."

        # Predict using each model
        predictions = {}
        model_names = ["Random Forest", "Logistic Regression", "Decision Tree", "SVC", "KNN"]
        try:
            for i, model in enumerate(models):
                model_name = model_names[i]
                pred_proba = model.predict_proba(data)[0][1]  # Probability of positive class
                predictions[model_name] = pred_proba
        except Exception as e:
            return f"Error during prediction: {e}"

        # Calculate average prediction
        average_prediction = np.mean(list(predictions.values())) * 100

        return render_template('result.html', name=name, email=email, age=data[0][0], gender=data[0][1],
                               cp=data[0][2], trestbps=data[0][3], chol=data[0][4], fbs=data[0][5],
                               restecg=data[0][6], thalach=data[0][7], exang=data[0][8], oldpeak=data[0][9],
                               slope=data[0][10], ca=data[0][11], thal=data[0][12],
                               average_prediction=average_prediction, predictions=predictions)
    


if __name__ == '__main__':
    app.run(debug=True)

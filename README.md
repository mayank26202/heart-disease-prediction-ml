
# Heart Disease Prediction App

## Description

This Flask-based web application predicts the likelihood of heart disease based on user input. It uses multiple machine learning models to provide predictions and evaluates each model’s performance. The app includes a user-friendly interface for input and displays the prediction results along with model-specific details.

## Screenshots

### Index Page

<img src="screenshots/index1.jpg" alt="Index Page 1" width="600" height="450">
<img src="screenshots/index2.jpg" alt="Index Page 2" width="600" height="450">



### Result Page

<img src="screenshots/result1.jpg" alt="result Page 1" width="600" height="450">
<img src="screenshots/result2.jpg" alt="result Page 2" width="600" height="450">

## Models Used

The application utilizes the following machine learning models:

1. **Random Forest**: An ensemble learning method that combines multiple decision trees to improve prediction accuracy and control overfitting.
2. **Logistic Regression**: A statistical model that estimates the probability of a binary outcome based on one or more predictor variables.
3. **Decision Tree**: A model that uses a tree-like graph of decisions and their possible consequences, including chance event outcomes.
4. **SVC (Support Vector Classifier)**: A classification method that finds the hyperplane that best divides a dataset into classes.
5. **K-Nearest Neighbors (KNN)**: A classification algorithm that assigns the class of the majority of its nearest neighbors.

## Instructions

### Setting Up the Environment

1. **Create a Virtual Environment**

   Use `conda` to create a virtual environment. Replace `myenv` with your desired environment name.

   ```bash
   conda create --name myenv python=3.8

2. **Activate Virtual Environment**

    ```bash
    conda activate --name myenv

3. **Install requirements.txt**

    Ensure you are in the project directory and install the required packages using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt

4. **Start the Application**

    Run the Flask application with:

    ```bash
    python app.py

## The application will be available at 'http://127.0.0.1:5000/'

## File Structure

    ```bash
    /project-directory
    /static
        /img
            background.jpg
        styles.css
    /templates
        index.html
        result.html
    app.py
    models.pkl
    requirements.txt
    README.md
    /screenshots
        index.png
        result.png


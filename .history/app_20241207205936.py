from flask import Flask, request, render_template
import joblib

# Step 1: Load the trained model and vectorizer
model = joblib.load('spam_classifier_model.pkl')  # Load the trained Naive Bayes model
vectorizer = joblib.load('vectorizer.pkl')  # Load the vectorizer for text preprocessing

# Step 2: Initialize the Flask app
app = Flask(__name__)

# Step 3: Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML form for user input

# Step 4: Define the route to handle form submissions and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form['email_text']  # Get the text input from the form
    if not email_text.strip():  # Handle empty input
        return render_template('index.html', result="Please enter some text.")
    
    # Step 5: Vectorize the input and make a prediction
    email_vectorized = vectorizer.transform([email_text])  # Transform input using the vectorizer
    prediction = model.predict(email_vectorized)[0]  # Predict using the trained model
    result = "Spam" if prediction == 1 else "Ham"  # Convert numerical output to readable result
    
    return render_template('index.html', result=result)  # Render the result on the same page

# Step 6: Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

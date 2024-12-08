from flask import Flask, request, render_template
import joblib

# Load the trained model and vectorizer
model = joblib.load('spam_classifier_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', result=None, input_text="")

@app.route('/predict', methods=['POST'])
def predict():
    sms_text = request.form['email_text']  # Get the input text
    if not sms_text.strip():  # Handle empty input
        return render_template('index.html', result="Please enter some text.", input_text="")
    
    # Vectorize and predict
    sms_vectorized = vectorizer.transform([sms_text])
    prediction = model.predict(sms_vectorized)[0]
    
    # Generate result and advice
    if prediction == 1:  # Spam
        result = "Spam"
        advice = "Be cautious with this message. Avoid clicking on links or sharing personal information."
    else:  # Ham
        result = "Ham"
        advice = "This message looks safe. You can proceed as usual."
    
    return render_template('index.html', result=result, advice=advice, input_text=sms_text)

if __name__ == '__main__':
    app.run(debug=True)

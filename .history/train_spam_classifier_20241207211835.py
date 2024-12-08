import pandas as pd  # Importing pandas for data manipulation and analysis
from sklearn.feature_extraction.text import CountVectorizer  # For converting text to numerical feature vectors
from sklearn.model_selection import train_test_split  # For splitting data into training and testing sets
from sklearn.naive_bayes import MultinomialNB  # Importing the Naive Bayes classifier
import joblib  # For saving and loading the trained model and vectorizer

# Step 1: Load and Process Dataset
file_path = 'SMSSpamCollection'  # Path to the dataset file
# Read the dataset file. It's a tab-separated file with two columns: label and message
data = pd.read_csv(file_path, sep='\t', header=None, names=['label', 'message'])

# Map the labels to binary values for easier processing by the model
# 'ham' (legitimate message) becomes 0, 'spam' (unwanted message) becomes 1
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Step 2: Split into Training and Testing Sets
# Separate the dataset into features (X: the message) and target labels (y: spam/ham)
X = data['message']  # Input feature: the SMS message text
y = data['label']  # Output label: 0 (ham) or 1 (spam)

# Split the data into training and testing sets
# 80% for training, 20% for testing, and use random_state=42 for reproducibility
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Vectorize Text Data
# Convert raw text messages into numerical feature vectors using CountVectorizer
vectorizer = CountVectorizer()  # Creates an object to transform text into a bag-of-words representation
X_train_vec = vectorizer.fit_transform(X_train)  # Learn vocabulary and transform training messages into vectors
X_test_vec = vectorizer.transform(X_test)  # Transform testing messages using the learned vocabulary

# Step 4: Train the Model
# Initialize the Multinomial Naive Bayes model, a common choice for text classification
model = MultinomialNB()
# Train the model using the training vectors and their corresponding labels
model.fit(X_train_vec, y_train)

# Step 5: Save Model and Vectorizer
# Save the trained model to a file for future use
joblib.dump(model, 'spam_classifier_model.pkl')
# Save the vectorizer to transform new messages into numerical vectors for prediction
joblib.dump(vectorizer, 'vectorizer.pkl')

# Print a confirmation message to indicate the script has completed successfully
print("Model trained and saved successfully!")

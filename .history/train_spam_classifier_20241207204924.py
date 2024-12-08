import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import joblib

# Step 1: Load and Process Dataset
file_path = 'SMSSpamCollection'  # Update with your file path
data = pd.read_csv(file_path, sep='\t', header=None, names=['label', 'message'])

# Map labels to binary values: 'ham' -> 0, 'spam' -> 1
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Step 2: Split into Training and Testing Sets
X = data['message']
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Vectorize Text Data
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Step 4: Train the Model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Step 5: Save Model and Vectorizer
joblib.dump(model, 'spam_classifier_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Model trained and saved successfully!")

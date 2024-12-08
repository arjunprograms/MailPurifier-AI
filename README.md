# MailPurifier-AI

MailPurifier-AI is a machine learning-powered application designed to classify SMS messages as **Spam** or **Ham** (not spam). The project features a trained Naive Bayes classifier deployed in a user-friendly web application built with Flask. This tool is intended to showcase how machine learning can effectively filter unwanted messages and provide actionable advice.

---

## Features

- **Spam Detection**: Identifies and flags spam messages using a trained classifier.
- **User-Friendly Interface**: A clean and intuitive web interface for users to paste and classify messages.
- **Real-Time Feedback**: Provides advice based on classification results (Spam or Ham).
- **Edge Case Handling**: Handles ambiguous messages with robust classification.

---

## Demo

### **Live Demo**
Coming soon...

### **Screenshots**
| Spam Message Example | Ham Message Example |
|-----------------------|---------------------|
| ![Spam Screenshot](images/spam_example.png) | ![Ham Screenshot](images/ham_example.png) |

---

## How It Works

1. **Dataset**: The model was trained on the SMS Spam Collection dataset, which contains 5,574 labeled messages.
2. **Model**: A Naive Bayes classifier was chosen for its simplicity and effectiveness in text classification tasks.
3. **Web Application**: Flask was used to build the web app, allowing users to interact with the classifier easily.

---

## Installation

### **Prerequisites**
- Python 3.7 or later
- pip (Python package manager)

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/arjunprograms/MailPurifier-AI.git
   cd MailPurifier-AI

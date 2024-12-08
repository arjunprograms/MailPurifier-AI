# TextPurifier-AI

TextPurifier-AI is an AI-powered text classification application that identifies SMS messages as either **Spam** or **Ham** (not spam). It uses a trained Naive Bayes machine learning model to classify messages in real-time, providing actionable advice based on the classification. The project includes a user-friendly web interface built with Flask, allowing easy interaction with the classifier.

---

## Features

- **Spam Detection**: Accurately identifies and flags spam messages.
- **Real-Time Feedback**: Displays the result (Spam or Ham) along with actionable advice.
- **User-Friendly Interface**: Simple and intuitive web interface for seamless interaction.
- **Clear Functionality**: Keeps input messages visible after classification with the option to clear them.
- **Edge Case Handling**: Handles ambiguous messages effectively.

---

### **Spam Example**
![Spam Example](images/Spam.png)

### **Ham Example**
![Ham Example](images/Ham.png)

---

## How It Works

1. **Dataset**: The model was trained using the [SMS Spam Collection Dataset](https://www.dt.fee.unicamp.br/~tiago/smsspamcollection/), containing 5,574 labeled messages.
2. **Model**: A Naive Bayes classifier was selected for its proven efficiency in text classification tasks.
3. **Interface**: Built with Flask, the app provides a simple interface where users can paste messages, classify them, and view results along with recommendations.

---

## Installation

### **Prerequisites**
- Python 3.7 or later
- pip (Python package manager)

### **Steps**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/arjunprograms/TextPurifier-AI.git
   cd TextPurifier-AI

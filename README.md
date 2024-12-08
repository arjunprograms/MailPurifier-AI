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
(https://github.com/user-attachments/assets/6b17f9c5-5bc4-461c-aeb7-947b5cb6e145)


### **Ham Example**
(https://github.com/user-attachments/assets/c39ff258-1438-4109-bd61-7d6479fd1c44)



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

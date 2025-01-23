# Cred-Arth: AI-Powered Financial Risk Prediction & Investment Planning



## 📌 Overview
**Cred-Arth** is an AI-powered financial analysis platform built using **Flask** and **OpenAI's GPT-4 API**. It allows users to input their transaction details and financial data to receive risk predictions and a strategic investment plan for the future.

The platform leverages machine learning and AI-driven insights to help users make informed financial decisions, mitigate risks, and optimize their investment portfolio.

## ✨ Features
- 📊 **Financial Risk Prediction:** Analyze transaction details and assess financial risks.
- 📈 **Investment Planning:** AI-generated recommendations on how to invest wisely.
- 🔄 **Interactive UI:** User-friendly interface for seamless data input and report generation.
- 📦 **Secure Data Handling:** Ensures user data privacy and confidentiality.
- 🛠 **Built with Flask:** Lightweight and scalable backend.
- 🤖 **Powered by GPT-4 API:** Generates personalized financial insights.

## 🏗️ Project Structure
```
Cred-Arth/
│── static/         # CSS, JS, and images for the frontend
│── templates/      # HTML templates for the Flask app
│── model.py        # Machine learning & AI processing logic
│── app.py          # Main Flask application file
│── requirements.txt # List of dependencies
│── README.md       # Project documentation
```

## 🚀 Installation & Setup
### Prerequisites
Ensure you have **Python 3.8+** installed.

### Step 1: Clone the Repository
```bash
git clone https://github.com/piyush182004/RISK-PREDICTION.git
cd 
```

### Step 2: Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up OpenAI API Key
Create a `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### Step 5: Run the Flask App
```bash
python app.py
```
The app will be available at **http://127.0.0.1:5000/**.

## 🛠 Usage Guide
1. Navigate to the home page.
2. Enter your transaction details.
3. Click "Analyze" to generate a risk report.
4. View AI-generated investment recommendations.

## 📌 API Integration
Cred-Arth utilizes the **OpenAI GPT-4 API** for financial analysis.
Example API Call:
```python
import openai
openai.api_key = "your_api_key"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a financial advisor......."},
        {"role": "user", "content": "Analyze my transaction details and suggest investments........."}
    ]
)
print(response["choices"][0]["message"]["content"])
```

## 📌 Deployment
To deploy **Cred-Arth**, you can use platforms like:
- **Heroku**
- **AWS EC2**
- **Google Cloud App Engine**
- **Railway.app**

Example Deployment on Heroku:
```bash
git init
git add .
git commit -m "Initial commit"
heroku create cred-arth
heroku config:set OPENAI_API_KEY=your_openai_api_key_here
git push heroku master
heroku open
```
![image](https://github.com/user-attachments/assets/0b5e8a07-5c89-4d28-a1dd-c0b5034eaaeb)
![image](https://github.com/user-attachments/assets/d0701579-c770-40a9-821c-0b49624cf315)


## 🎯 Future Improvements
- 🌐 Add **user authentication** for personalized insights.
- 📉 Implement **graphical data visualization** for better analytics.
- 💰 Integrate **real-time stock market data** for smarter investment strategies.
- 📲 Develop a **mobile-friendly** version for better accessibility.

## 🤝 Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Commit changes: `git commit -m 'Added new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request.

💡 *Empower your financial journey with AI-driven insights!* 🚀


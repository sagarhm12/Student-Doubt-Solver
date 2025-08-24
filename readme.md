# Portia Student Doubt Solver

A fully automated agent to answer student questions using AI (Gemini/GPT) and send replies via email—all from a Google Form submission!  
Perfect for universities, schools, or tutoring centers looking to scale student Q&A with responsible, step-wise explanations.

## ✨ Features

- Students submit questions through a simple Google Form
- Questions go to a Google Sheet (auto-linked to the Form)
- The agent reads new questions, answers them with Google Gemini (or GPT, if configured), then emails the response back to the student
- Uses Portia AI for reliable, plain-language, stepwise answers
- Marks responses as “Answered” in your Sheet to avoid duplicates

---

## 🗂️ Folder Structure

├── main.py # Main agent script
├── .env # Contains API keys
├── credentials.json # Google Service Account credentials
├── recipients.csv # (Optional) Example batch email list
└── README.md # This file


---

## 🚀 Setup Instructions

### 1. Prepare Your Google Form & Sheet

- Create a Google Form for student questions.  
  Example fields: **Email**, **Name**, **Question**
- In Form settings, link responses to a new Google Sheet (e.g., "Student Doubt Questions").

### 2. Connect to Google APIs

- Create a Google Cloud project.
- Enable **Google Sheets API** and **Google Drive API**.
- Create a Service Account, generate a JSON key, and download it as `credentials.json`.
    - [Guide with screenshots here.](#)
- Share your Sheet with the Service Account’s email as “Editor”.

### 3. Get Required API Keys

- [Sign up for Gemini API (Google AI Studio)](https://makersuite.google.com/app/apikey) and place in `.env` as `GOOGLE_API_KEY`
- Get a [Portia API Key](https://app.portialabs.ai/) and place in `.env` as `PORTIA_API_KEY`


### 4. Install All Dependencies


### 5. Configure Your Google Sheet Columns

Minimum columns:  
- **Email**
- **Name**
- **Question**
- **Answered** (mark as “Yes” after answering)

### 6. Run the Agent

(or `poetry run python main.py` if using poetry)

---

## 🛠️ How It Works

The script:
- Polls your Google Sheet for unanswered questions
- Generates a simple, stepwise answer with Gemini or GPT (using the "Doubt Solver" prompt template)
- Sends an email to the student with the answer
- Marks the row as "Answered" to prevent repeat responses

---

## 👩‍💻 Customizing

- Change the AI prompt template, output style, or add custom logging to fit your school/tutor brand!
- Add more complex workflow (attachments, follow-ups, Slack/Teams messaging...)

---

## ❓ Troubleshooting

- **API/permission errors:** Did you enable both Sheets and Drive APIs? Did you share the sheet with the Service Account?
- **“Answered” not updating:** Is your Sheet column title exactly **Answered**?
- **Email issues:** Portia may ask you to authenticate the first time you send mail—watch terminal for prompts.

---

## ⭐ Credits

Built using:
- [Portia AI](https://portialabs.ai/)
- [Google Gemini](https://ai.google.dev/)
- [gspread](https://gspread.readthedocs.io/)

---

## 📄 License

MIT License (or your choice)

---

**Happy learning!**

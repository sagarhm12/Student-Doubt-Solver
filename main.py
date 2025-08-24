import os
from dotenv import load_dotenv
from portia import Config, Portia, DefaultToolRegistry, LLMProvider
import gspread

# 1. Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PORTIA_API_KEY = os.getenv("PORTIA_API_KEY")

# 2. Set up config for Portia using Gemini
config = Config.from_default(
    llm_provider=LLMProvider.GOOGLE,
    default_model="google/gemini-2.0-flash",
    google_api_key=GOOGLE_API_KEY,
    portia_api_key=PORTIA_API_KEY
)

portia = Portia(
    config=config,
    tools=DefaultToolRegistry(config),
)

# 3. Setup Google Sheets access (requires shared service account on sheet)
gc = gspread.service_account(filename="credentials.json")
worksheet = gc.open("Student Doubt Questions").sheet1

# 4. Fetch (new) questions
rows = worksheet.get_all_records()
for idx, entry in enumerate(rows, start=2):  # Skip header, start at row 2
    if entry.get("Answered", "").strip().lower() in ("yes", "y", "answered"):
        continue  # Already answered

    student_email = entry["Email"]
    student_name = entry.get("Name", "Student")
    student_question = entry["Question"]

    # Compose the answer prompt for Gemini
    tutor_prompt = f"""
You are “Student Doubt Solver,” a helpful tutor.
Audience: school/college students (varying levels).
Goal: answer the student’s question clearly, step-by-step, using simple language first, then optional deeper detail.
Constraints:
• Prefer plain language; avoid jargon unless explained.
• If you don’t know, say so and suggest how to find out.
Output format:
Direct Answer (2–3 sentences)

The question is: {student_question}
"""

    # Portia generates the answer
    try:
        plan_run = portia.run(tutor_prompt)
        answer = plan_run.outputs

        # Compose the outgoing email
        subject = f"Answer to your doubt: {student_question[:30]}..."
        mail_task = (
            f"Send an email to {student_email} with this subject: '{subject}' "
            f"and this body:\n\nDear {student_name},\n\n{answer}\n\nBest wishes,\nPortia AI Tutor"
        )
        print(f"Sending answer to {student_email}: {answer}")
        mail_result = portia.run(mail_task)  # May prompt for login/auth the first time

        # Mark as answered in the sheet (add/write cell or relevant column)
        worksheet.update_cell(idx, worksheet.find("Answered").col, "Yes")
    except Exception as e:
        print("Error answering/sending mail:", e)

print("All done.")
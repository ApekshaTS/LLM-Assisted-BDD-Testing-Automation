# LLM-Assisted-BDD-Testing-Automation

*Project Structure*
llm-bdd-testing/
│
├── app/
│   ├── app.py                     # Flask web application
│   └── templates/
│       ├── login.html             # Styled login page
│       └── dashboard.html         # Styled dashboard page
│
├── pipeline/
│   ├── generate_scenarios.py      # Uses Llama AI to generate Gherkin scenarios
│   ├── validate_scenarios.py      # Validates Gherkin steps
│   ├── select_happy_path.py       # Extracts and stores the "happy path" scenario
│   ├── approve_and_run.py         # Manual approval + test execution pipeline
│   ├── approval_log.txt           # Stores approval timestamps (auto-created)
│
├── tests/
│   └── features/
│       ├── login.feature          # Full Gherkin scenarios (generated)
│       ├── happy_path.feature     # Selected scenario for automation
│       └── steps/
│           └── login_steps.py     # Playwright + Behave step definitions
│
├── venv/                          # Virtual environment
└── README.md                      # (This file)

*How the Project Works*

1️⃣ User enters plain-English requirement
Example:
"User should be able to login with email and password."

2️⃣ Llama AI generates BDD Gherkin scenarios
One positive (happy path)
One negative (error flow)

3️⃣ Generated Gherkin is validated
Validator checks:
✔ known actions
✔ correct Gherkin syntax
✔ supported step types

4️⃣ Happy path scenario is extracted
Saved into:
tests/features/happy_path.feature

5️⃣ User approves execution
Approval is logged in:
pipeline/approval_log.txt


*Setup Instructions*
✅ 1. Clone the project
git clone <your-repo-url>
cd llm-bdd-testing

✅ 2. Create a virtual environment
python -m venv venv

Activate it:
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

✅ 3. Install dependencies
pip install flask behave playwright google-genai

Install Playwright browsers:
playwright install

✅ 4. Start the sample web application
python app/app.py

App runs at:
http://localhost:5000/login

Keep this terminal open.

*LLM Integration (Using Llama AI)*
This project uses Phi 3 Instruct through the ollama framework.

✅ 5. Install Ollama
Download from:
https://ollama.com/download

Then run:
ollama run phi3

If it prints a response, your model is ready.

✅ 6. Generate Gherkin scenarios
In another terminal:
python pipeline/generate_scenarios.py

Program will ask:
Enter requirement:
Type your requirement (e.g., login feature).

Output saved to:
tests/features/login.feature

*Scenario Validation*
✅ 7. Validate Gherkin
python pipeline/validate_scenarios.py

Example output:
=== Scenario Validation Report ===
Scenario 1 validated successfully
Scenario 2 validated successfully

*Select Happy Path*
✅ 8. Extract the happy path scenario
python pipeline/select_happy_path.py

Creates:
tests/features/happy_path.feature

*Manual Approval*
✅ 9. Approve execution
python pipeline/approve_and_run.py

You will see:
Do you want to run the automated test? (y/n):
Type:
y

Your approval gets saved to:
pipeline/approval_log.txt

*Run Automated BDD Test*
What happens now?
Playwright launches the browser
Opens login page
Enters credentials
Clicks login
Confirms dashboard

You should see:
1 feature passed, 0 failed
1 scenario passed

🎉 Test Successful!

6️⃣ Automated test runs using Behave + Playwright
Browser opens → form filled → login tested → dashboard verified.

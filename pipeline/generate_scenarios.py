import subprocess
import json

def generate_with_ollama(prompt):
    """Call Ollama locally to generate text."""
    process = subprocess.Popen(
        ["ollama", "run", "phi3"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    out, err = process.communicate(prompt)
    return out

requirement = input("Enter requirement: ")

prompt = f"""
You are an expert QA engineer.
Your task is to convert the following requirement into **clean BDD Gherkin scenarios only**.

STRICT RULES:
- Output MUST start with: Feature: <something>
- Then include the scenarios:
    At least ONE positive (happy path) scenario
    At least ONE negative scenario
- Use ONLY Gherkin format:
    Given
    When
    Then
    And
- Do NOT add paragraphs, descriptions, stories, or explanations.
- Do NOT add long prose.
- Do NOT start with “As a user…” or user stories.
- Do NOT add extra commentary.
- ONLY output Gherkin.

Here is an example of valid Gherkin output:
Feature: Login functionality

Scenario: Successful login with valid credentials
  Given the user is on the login page
  When the user enters a valid email
  And the user enters a valid password
  And the user clicks the login button
  Then the user should be redirected to the dashboard

Scenario: Invalid login attempt
  Given the user is on the login page
  When the user enters an invalid password
  And the user clicks the login button
  Then an error message should be displayed

Generate each scenario based on this format only. 

Requirement:
{requirement}

Now output ONLY valid Gherkin:
"""

response = generate_with_ollama(prompt)

print("\nGenerated Gherkin Scenarios:\n")
print(response)

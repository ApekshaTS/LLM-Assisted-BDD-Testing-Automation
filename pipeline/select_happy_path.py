import re
import os
import sys

SOURCE_FILE = "tests/features/login.feature"
HAPPY_PATH_FILE = "tests/features/happy_path.feature"

def is_positive_scenario(text):
    """Simple rule: positive scenarios usually contain words like 'successful', 'valid', 'redirected', 'dashboard'."""
    keywords = ["successful", "valid", "redirected", "dashboard"]
    text_lower = text.lower()
    return any(k in text_lower for k in keywords)

def main():
    if not os.path.exists(SOURCE_FILE):
        print(f"ERROR: Feature file not found: {SOURCE_FILE}")
        sys.exit(1)

    with open(SOURCE_FILE, "r") as f:
        content = f.read()

    # Split into individual scenarios
    scenarios = re.split(r"\n\s*Scenario:", content)
    
    happy_scenario = None

    for sc in scenarios[1:]:
        scenario_text = "Scenario:" + sc  # add back the removed keyword
        if is_positive_scenario(scenario_text):
            happy_scenario = scenario_text
            break

    if not happy_scenario:
        print("No clear positive/happy path found. Please adjust your scenarios.")
        sys.exit(1)

    # Write the happy path file
    with open(HAPPY_PATH_FILE, "w") as f:
        f.write("Feature: Happy Path Scenario\n\n")
        f.write(happy_scenario)

    print("\nHappy path scenario selected successfully!")
    print(f"Saved to: {HAPPY_PATH_FILE}\n")

if __name__ == "__main__":
    main()

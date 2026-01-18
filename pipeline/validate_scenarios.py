import re
import sys
import os

# Allowed BDD actions for your project
ALLOWED_ACTIONS = [
    "user", "login", "log in", "click", "choose", "select",
    "enter", "input", "provide", "submit", "fail", "type",
    "redirect", "dashboard", "enters", "clicks", "sees", "is on",
    "error", "message", "session", "authenticate", "unauthenticate",
    "invalid", "valid", "password", "email",
    "page", "navigate", "load", "see", "display", "view", 
    "status", "access", "permission", "account", "profile", "settings"
]

FEATURE_FILE = "tests/features/login.feature"

def validate_step(step):
    """Check if a step contains any allowed action keyword."""
    step_lower = step.lower()
    return any(action in step_lower for action in ALLOWED_ACTIONS)

def validate_scenario(scenario):
    """Validate each step of the scenario."""
    errors = []
    steps = scenario.split("\n")
    
    for step in steps:
        step = step.strip()
        if step.startswith(("Given", "When", "Then", "And")):
            if not validate_step(step):
                errors.append(f"Invalid step (unknown action): {step}")
    return errors

def main():
    if not os.path.exists(FEATURE_FILE):
        print(f"ERROR: Feature file not found: {FEATURE_FILE}")
        sys.exit(1)

    with open(FEATURE_FILE, "r") as f:
        content = f.read()

    # Split into individual scenarios
    scenarios = re.split(r"\n\s*Scenario:", content)
    
    print("\n=== Scenario Validation Report ===\n")
    
    all_errors = []

    for index, sc in enumerate(scenarios[1:], start=1):
        scenario_text = "Scenario:" + sc
        print(f"Validating Scenario {index}...")

        errors = validate_scenario(scenario_text)

        if errors:
            print("Errors found:")
            for e in errors:
                print("   -", e)
            all_errors.extend(errors)
        else:
            print("Scenario is valid.")
        
        print()

    if not all_errors:
        print("All scenarios are valid!\n")
    else:
        print("Validation completed with errors.\n")

if __name__ == "__main__":
    main()

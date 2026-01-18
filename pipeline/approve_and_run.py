import os
import sys
import subprocess

HAPPY_PATH_FILE = "tests/features/happy_path.feature"

def main():
    # Check if the happy path file exists
    if not os.path.exists(HAPPY_PATH_FILE):
        print(f"ERROR: Happy path file not found: {HAPPY_PATH_FILE}")
        print("Run select_happy_path.py first.")
        sys.exit(1)

    print("\n=== Happy Path Scenario Ready ===\n")
    
    # Show contents to user
    with open(HAPPY_PATH_FILE, "r") as f:
        print(f.read())

    # Manual approval
    choice = input("\nDo you want to run the automated test? (y/n): ").strip().lower()
    
    if choice != "y":
        print("Execution cancelled.")
        sys.exit(0)

    from datetime import datetime
    with open("pipeline/approval_log.txt", "a") as f:
        f.write(f"[APPROVED] {datetime.now()} - happy_path.feature executed\n")

    print("\nRunning automated BDD test...\n")

    # Run Behave test for only the happy path file
    try:
        subprocess.run([sys.executable, "-m", "behave", HAPPY_PATH_FILE], check=True)
    except Exception as e:
        print("ERROR running Behave:", e)
        sys.exit(1)

    print("\nTest execution completed!\n")

if __name__ == "__main__":
    main()

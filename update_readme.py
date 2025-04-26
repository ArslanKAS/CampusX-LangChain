import datetime

# Path to your README.md file
README_PATH = "README.md"  # adjust if needed

# Character or text to add daily
CHARACTER_TO_ADD = "\u2728"  # (✨) or any small symbol you want

# Read the current README.md
with open(README_PATH, "a", encoding="utf-8") as file:
    # Add today's date and a character (optional)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    file.write(f"\n{CHARACTER_TO_ADD} {today}")

print("README.md updated!")
from datetime import datetime

# Get the current date
today = datetime.now().strftime("%Y-%m-%d")

# Get user input
entry = input("Write your diary entry:\n")

# Create or open the diary file
filename = f"diary_{today}.txt"

# with open(filename, "a") as file:
#     file.write(f"{datetime.now().strftime('%H:%M:%S')} - {entry}\n")

print(f"Diary entry saved to {filename}")
with open(filename, "a") as file:
    file.write(f"\n--- {datetime.now().strftime('%H:%M:%S')} ---\n")
    file.write(entry + "\n")
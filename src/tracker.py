import csv
import os
from datetime import datetime

DATA_FILE = "data/sessions.csv"

def init_file():
    if not os.path.exists("data"):
        os.mkdir("data")
    if not os.path.isfile(DATA_FILE):
        with open(DATA_FILE, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Subject", "Hours", "Notes"])

def add_session():
    subject = input("Subject: ")
    hours = input("Hours studied: ")
    notes = input("Notes (optional): ")
    date = datetime.now().strftime("%Y-%m-%d")
    
    with open(DATA_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, subject, hours, notes])
    
    print("✅ Session added!\n")

def view_sessions():
    if not os.path.exists(DATA_FILE):
        print("No sessions found.\n")
        return
    
    print("\n--- Study Sessions ---")
    with open(DATA_FILE, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))
    print()

def export_sessions():
    print("Sessions already saved to:", DATA_FILE)

def main():
    init_file()
    while True:
        print("📚 StudyTracker Menu")
        print("1. Add Session")
        print("2. View Sessions")
        print("3. Export to CSV")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_session()
        elif choice == '2':
            view_sessions()
        elif choice == '3':
            export_sessions()
        elif choice == '4':
            print("Bye! Keep studying smart. 💡")
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()

import csv
import os
from datetime import datetime, timedelta
from collections import defaultdict
import matplotlib.pyplot as plt

DATA_FILE = "data/sessions.csv"

def init_file():
    if not os.path.exists("data"):
        os.mkdir("data")
    if not os.path.isfile(DATA_FILE):
        with open(DATA_FILE, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Subject", "Hours", "Notes"])

def add_session():
    from colorama import Fore
    subject = input("Subject: ")
    try:
        hours = float(input("Hours studied: "))
    except ValueError:
        print(Fore.RED + "⚠️ Invalid number. Please try again.\n")
        return
    notes = input("Notes (optional): ")
    date = datetime.now().strftime("%Y-%m-%d")
    
    with open(DATA_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, subject, hours, notes])
    
    print(Fore.GREEN + "✅ Session added!\n")

def view_sessions():
    from colorama import Fore
    if not os.path.exists(DATA_FILE):
        print(Fore.RED + "⚠️ No sessions found.\n")
        return
    
    print("\n📖 " + Fore.CYAN + "Your Study Sessions:")
    with open(DATA_FILE, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))
    print()

def export_sessions():
    from colorama import Fore
    print(Fore.GREEN + "💾 Sessions saved to: " + DATA_FILE + "\n")

def get_study_hours_this_week():
    total = 0.0
    week_start = datetime.now() - timedelta(days=datetime.now().weekday())
    
    with open(DATA_FILE, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                date = datetime.strptime(row["Date"], "%Y-%m-%d")
                if date >= week_start:
                    total += float(row["Hours"])
            except:
                continue
    return total

def goal_tracker():
    from colorama import Fore
    try:
        goal = float(input("Enter your weekly study goal in hours: "))
    except ValueError:
        print(Fore.RED + "⚠️ Invalid number. Try again.\n")
        return
    studied = get_study_hours_this_week()
    
    print(f"\n📈 You studied {studied:.2f} hours this week.")
    if studied >= goal:
        print(Fore.GREEN + "🎉 Congrats! You reached your goal!\n")
    else:
        print(Fore.YELLOW + f"⏳ {goal - studied:.2f} more hours to go.\n")

def show_subject_pie_chart():
    from colorama import Fore
    subjects = defaultdict(float)
    
    with open(DATA_FILE, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                subjects[row["Subject"]] += float(row["Hours"])
            except:
                continue
    
    if not subjects:
        print(Fore.RED + "⚠️ No data to display.\n")
        return
    
    labels = subjects.keys()
    sizes = subjects.values()

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("📊 Study Time by Subject")
    plt.axis("equal")
    plt.show()

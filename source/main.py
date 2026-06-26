##calls functions from other files
import sys
from tracker import *

print("=" * 55)
print('''                                                
           ┌────────────────────────────────────────┐
           │ 💰 EXPENSE TRACKER APPLICATION    💰   │
           └────────────────────────────────────────┘
      ''') 
print("=" * 55)
print()

print("Welcome to Expense Tracker!".upper())
print("-" * 55)

def login_expence():
    while True:
      print("\n📋         MAIN MENU")
      print("=" * 55)

      print("\n1. Start")
      print("2. Exit")

      print("-" * 55)

      user_input = input("👉 Enter your choice: ")
      if user_input == "":
          print("❌ Input can't be empty!\n")
          continue

      if user_input == '1':
          print("\n✅ Launching Expense Tracker...\n")
          user_opiton()
          break

      if user_input == '2':
        print("\n👋 Exiting... Goodbye! Have a great day.\n")
        sys.exit()

      else:
        print("❌ Invalid entry! Please try again.\n")
        continue

if __name__ == "__main__":
    login_expence()
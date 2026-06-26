##loads data from data.json file, 
from pathlib import Path
import json
import random
from datetime import datetime
import time

##defining json file path
my_file = Path("E:\dev_file\Project_file\Expense Tracker\data\data.json") #easy way

base_path = Path(__file__).resolve().parent ##it shows our current file 
file_path = base_path.parent /"data"/ "data.json" ##it contains inside the data like data.json file
Folder_path = file_path.parent ##it only contails folder data 

def user_opiton():
   while True:
      
      print("\n" + "=" * 60)
      print("                MAIN MENU")
      print("=" * 60)

      print('''
            💸 1. Add Expense
            📖 2. View Expenses
            🔍 3. Search by Category
            💰 4. Show Total Spent
            📅 5. Monthly Summary
            🗑️ 6. Delete Expense
            💾 7. Save & Exit''')

      
      print("-" * 60)

      user_input = input("👉 Enter your option: ")
      if user_input == '1':
          add_expense()
      elif user_input == '2':
          view_expenses()
      elif user_input == '3':
          search_by_category()
      elif user_input == '4':
          total_spend()
      elif user_input == '5':
          monthly_summary()
      elif user_input == '6':
          delete_expense()
      elif user_input == '7':
          print("\n💾 Saving... Goodbye!\n")
          break
      else:
        print(f"❌ '{user_input}' invalid entry!, try again")


def add_expense():
    
    print("\n" + "=" * 60)
    print("              ADD NEW EXPENSE")
    print("=" * 60)

    print("You need to add your expenses here.\n")

    print('''
             🍔  1. Food
             ✈️  2. Travel
             🧾 3. Bills
             🛍️  4. Shopping
             🎮 5. Entertainment
             📦 6. Other''')

    
    print("-" * 60)

    category = {
         1: "food",
         2: "travel",
         3: "bills",
         4: "shopping",
         5: "entertainment",
         6: "other",
    }

    user_input = input("👉 Enter your category as shown (or your own): ")
    if user_input.isalpha():
       print(f"✅ Your category is: {user_input}")

    if user_input.isdigit():
        try:
          Category_input = int(user_input)
          user_input = category.get(Category_input, "invalid input")
        except ValueError:
            print("❌ Invalid entry!")
        print(f"\n✅ Your category is: {user_input}")

    take_user = input("📝 What did you spend money on?: ")
    print(f"\n📌 Under the category '{user_input}', you spent money on '{take_user}'.")

    while True:
        user_amount = input("💲 How much amount did you spend?: $")
        if user_amount.isdigit():
            take_amount = int(user_amount)
            break
        elif user_amount.isalpha():
            print(f"❌ Enter a number! Not '{user_amount}'")
            continue

    while True:
      
      print("\n" + "-" * 60)
      print("📅 Date Format: 25/6/2026")
      print("-" * 60)

      user_date = input("📆 On what DATE did you spend your money?: ")
      try:
        pased_date = datetime.strptime(user_date, "%d/%M/%Y")
        break
      except ValueError:
        print("❌ Invalid format, try again.")
        continue

    ##getting month name from date formate
    date_part = user_date.split('/')
    month_num = date_part[1]
    months = {1: "jan", 2: "feb", 3: "mar", 4: "april", 5: "may", 6: "jun", 7: "july", 8: "agu", 9: "sep", 10: "oct", 11: "nov", 12: "dec"}
    int_date = int(month_num)
    month_name = months.get(int_date, "invalid number")

    ##formating data and saving
    coustomer_id = random.randint(1,200)
    with open(file_path, "r") as f:
        try:
            user = json.load(f)
        except json.JSONDecodeError:
            user = []

    expences = {
        "id": coustomer_id,
        "category": user_input,
        "amount": take_amount,
        "description": take_user,
        "take_date": user_date,
        "month": month_name
    }

    user.append(expences)

    with open(file_path, "w") as f:
       json.dump(user, f, indent=4)

       
       print("\n" + "=" * 60)
       print("✅ Expense Saved Successfully!")
       print("=" * 60)

def view_expenses():
    
    print("\n" + "=" * 60)
    print("📖               YOUR EXPENSES")
    print("=" * 60)

    expencenes = load_data()

    for data in expencenes:
        
        print("-" * 60)
        print(f'''
📅 Date        : {data['take_date']}
📂 Category    : {data['category']}
💰 Amount      : ${data['amount']}
📝 Description : {data['description']}
        ''')
    
    print("=" * 60)


def search_by_category():
    with open(file_path, "r") as f:
        category = json.load(f)

    see_string = set()

    print("\n" + "=" * 60)
    print("🔍          SEARCH BY CATEGORY")
    print("=" * 60)

    print("📂 Your Categories:")
    j = 1
    for data in category:
        current_string = data['category']

        if current_string in see_string:
            continue

        see_string.add(current_string)
        print(f"   {j}. {data['category']}")

        j += 1

    while True:
      
      print("\n" + "-" * 60)

      print("Select a category you only wanted to view!")
      user_input = input("👉 Enter Which Category You Want To See (Or 'n' To Exit): ".title())

      if user_input.isdigit():
        print("❌ Enter category name, not number!")
        continue

      if user_input == 'n':
        break

      category_item = None
      for data in category:
          if user_input == data['category']:
              category_item = data

              
              print("-" * 60)

              print(f'''
📅 Date        : {category_item['take_date']}
📂 Category    : {category_item['category']}
💰 Amount      : ${category_item['amount']}
📝 Description : {category_item['description']}
              ''')


def total_spend():
    
    print("\n" + "=" * 60)
    print("💰            TOTAL SPENDING REPORT")
    print("=" * 60)

    data = load_data()

    monthly_total = {}
    for data in data:
        month = data['month']
        money = data['amount']

        if month not in monthly_total:
            monthly_total[month] = 0

        monthly_total[month] += money

    
    print("\n📊 Monthly Report")
    print("-" * 60)

    for month, money in monthly_total.items():
        print(f"📅 {month.title():<12} 💵 ${money}")

    grand_total = sum(monthly_total.values())

    
    print("-" * 60)
    print(f"💸 Grand Total Spent : ${grand_total}")

def monthly_summary():
    
    print("\n" + "=" * 60)
    print("📅            MONTHLY SUMMARY")
    print("=" * 60)

    month_data = load_data()
    summary_dict = {}

    for data in month_data:
        month = data['month']

        if month not in summary_dict:
            summary_dict[month] = []

        detail = {
            "date": data['take_date'],
            "category": data['category'],
            "description": data['description'],
            "money": data['amount']
        }

        summary_dict[month].append(detail)

    for month, detail in summary_dict.items():
        
        print("\n" + "-" * 60)
        print(f"📆 {month.upper()}")
        print("-" * 60)

        for things in detail:
            print(f'''
📅 Date        : {things['date']}
📂 Category    : {things['category']}
📝 Description : {things['description']}
💰 Money       : ${things['money']}
''')


def delete_expense():
    
    print("\n" + "=" * 60)
    print("🗑️             DELETE EXPENSE")
    print("=" * 60)

    data = load_data()

    while True:
       data_collect = {}

       for item in data:
           month = item['month']

           if month not in data_collect:
               data_collect[month] = []

           detail = {
               "id": item['id'],
               "date": item['take_date'],
               "category": item['category'],
               "description": item['description'],
               "money": item['amount'],
               "date": item['take_date']
           }

           data_collect[month].append(detail)

       for month, detail in data_collect.items():
         
         print("\n" + "-" * 60)
         print(f"📆 {month.upper()}")
         print("-" * 60)

         for things in detail:
            print(f'''
🆔 ID          : {things['id']}
📂 Category    : {things['category']}
💰 Amount      : ${things['money']}
📝 Description : {things['description']}
📅 Date        : {things['date']}
''')

       
       print("=" * 60)
       print("📌 Your current expenses are listed above.")
       print("=" * 60)

       user_input = input("🗑️ Enter ID which expense you want to remove (or 'n' for exit): ")

       if user_input == 'n':
        return

       if user_input.isdigit():
         taken_input = int(user_input)

         found = False
         for delete in data:
             if taken_input == delete['id']:
                 found = True
                 data.remove(delete)

         if found == True:
             
             print("\n✅ Expense found. Removing it...")

             with open(file_path, "w") as f:
                  json.dump(data, f, indent=4)

             userinput = input("👉 Press 'y' for more removing or 'n' for exit: ")

             if user_input == 'n':
                return
             if user_input == 'y':
                continue

         if found == False:
             
             print("❌ ID not found.")
             continue

       else:
        
        print("❌ Invalid entry, try again!")
        time.sleep(0.9)    

def load_data():
    with open(file_path, "r")as f:
        data = json.load(f)
        return data




from database1 import add_entry, get_entries
user_input = None
menu = """Please select the following options:

1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """

entries = [
    {"content":"Today I started learning python", "date":"01-01-2020"},
    {"content":"I created my first SQLite database", "date":"02-02-2020"},
    {"content":"I finished writing my programming dairy application", "date":"03-03-2020"},
    {"content":"Today I'm going to continue learning programming", "date":"04-04-2020"}
]

def prompt_new_entry():
        entry_content = input("What have you learned today?")
        entry_date = input("Enter the date:")
        add_entry(entry_content, entry_date)
 
def view_entries(entries):
    for entry in entries:
        print(f"{entry['date']}\n {entry['content']} \n\n")
      

while(user_input != "3"):
    user_input = input(menu)
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    elif user_input == "3":
        break
 
    else:
        print("Invalid option, Please try again!")



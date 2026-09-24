inventory = 0
invalid_entries = 0

while True:
    user_input = input("Enter stock: ")

    if user_input.isdigit() and (int(user_input) >= 0):
        inventory += int(user_input)
        if inventory > 500:
            print("Error! Total inventory exceeds 500 units!")
            break
    elif user_input.lower() == "quit":
        print(f"Total Units Processed: {inventory}\nNumber of Failed/Rejected Entries: {invalid_entries}")
        break
    else:
        invalid_entries += 1
        print("Error. Invalid input.")
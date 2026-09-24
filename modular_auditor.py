def get_valid_input():
    user_input = input("Enter :")

    if user_input.isdigit() and (int(user_input) >= 0):
        return int(user_input)
    elif user_input.lower() == "quit":
        return user_input.lower()
    else:
        user_input = "Input Error"
        print("Invalid Value")
        return user_input

def process_delivery(current_total, new_value): 
    current_total =+ new_value
    return(current_total)

def calculate_tax(amount):
    return(10/100 * amount)

def generate_report(total_units, failed_attempts):
    print(f"Total Units Processed: {total_units}\nNumber of Failed/Rejected Entries: {failed_attempts}")


inventory = 0 
invalid_entries = 0

while True:
    user_input = get_valid_input()

    if user_input == "Input Error":
        invalid_entries += 1
        continue
    elif user_input == "quit":
        generate_report(inventory, invalid_entries)
        print(f"Tax: {calculate_tax(inventory)}")
        break
    else:
        inventory += user_input
        if inventory > 500:
                print("Error! Total inventory exceeds 500 units!")
                break

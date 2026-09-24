def get_valid_input():
    user_input = input("Enter :")

    if user_input.isdigit() and (int(user_input) >= 0):
        return int(user_input)
    else:
        print("Invalid Value")

def process_delivery(current_total, new_value): 
    current_total =+ new_value
    return(current_total)

def calculate_tax(amount):
    return(10/100 * amount)

def generate_report(total_units, failed_attempts):
    print(f"Total Units Processed: {total_units}\nNumber of Failed/Rejected Entries: {failed_attempts}")
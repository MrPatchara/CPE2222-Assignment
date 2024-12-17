import random

security_guards = ["A", "B", "C", "D", "E"]

morning_rate = 200
afternoon_rate = 150

schedule = {
    "Monday": ["", ""],
    "Tuesday": ["", ""],
    "Wednesday": ["", ""],
    "Thursday": ["", ""],
    "Friday": ["", ""]}

def generate_schedule():
    for day in schedule:
        morning_guard = random.choice(security_guards)
        afternoon_guard = random.choice(security_guards)
        
        while morning_guard == afternoon_guard:
            afternoon_guard = random.choice(security_guards)
        
        schedule[day][0] = morning_guard
        schedule[day][1] = afternoon_guard

def calculate_income():
    income = {guard: 0 for guard in security_guards}
    for day in schedule:
        morning_guard, afternoon_guard = schedule[day]
        income[morning_guard] += morning_rate
        income[afternoon_guard] += afternoon_rate
    return income

def print_schedule():
    print("-"*50)
    print(f"{'':<15} | {'8:00 - 12:00':<12}  | {'13:00 - 17:00':<12} |")
    print("-"*50)
    
    for day in schedule:
        morning_guard, afternoon_guard = schedule[day]
        print(f"{day:<15} | {morning_guard:^12}  |  {afternoon_guard:^12} |")
        print("-"*50)
    print("-"*30)
    print("Income Summary")
    print("-"*30)
    for guard, amount in income.items():
        print(f'{guard} earns {amount} Bath for this week\n')


generate_schedule()
income = calculate_income()

print_schedule()

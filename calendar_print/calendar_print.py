
print ('how many day are in this month?')
days_in_month = int(input())

if days_in_month not in [28,29,30,31]:
    print('Invalid input for number of days in month.')
    exit()

print('what day of the week did this month start on? ' \
'Enter 1 for Monday, 2 for Tuesday, 3 for Wednesday, 4 for Thursday, 5 for Friday, 6 for Saturday, 7 for Sunday,')
first_day_of_month = int(input())


print ('S   M   T   W   T   F   S')

print("    " * (first_day_of_month ), end="")

day = 1

def calendar():
    print ("1   2   3   4   5   6  7 ")
    print ("8   9   10  11  12  13  14")
    print("15  16  17  18  19  20  21")
    print('22  23  24   25  26  27  28')

while day <= days_in_month:
    print(f"{day:<4}", end="")  # print day with spacing
    if first_day_of_month == 6:   # reached Saturday—new line
        print()
        first_day_of_month = 0
    else:
        first_day_of_month += 1
    day += 1

print() 

de


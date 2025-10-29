# Counting Sundays

# I'm not proud of this ... it did give me the right answer though

def solve():
    date = [0, 1, 1901]
    day_count = 1
    sundays = 0

    while date[2] < 2001:
        day_count += 1
        date[0] += 1

        if(day_count % 7 == 0 and date[0] == 1):
            sundays += 1
        
        if date[0] >= 28:
            if date[1] == 2:
                if  date[0] == 28 and is_leap_year(date[2]):
                    continue
                else:
                    date[0] = 0
                    date[1] += 1
                continue

            if date[0] < 31 and is_long_month(date[1]):
                continue

            if date[0] >= 30:
                if date[1] == 12:
                    date[0], date[1] = 0, 1
                    date[2] += 1
                else:
                    date[0] = 0
                    date[1] += 1

    day_count += 1
    if(day_count % 7 == 0):
        sundays += 1

    return [date, get_weekday(day_count % 7), day_count, f'Sundays: {sundays}']

def is_long_month(month):
    return month not in (9, 4, 6, 11)
        
def is_leap_year(year):
    if year % 4 != 0:
        return False
    
    if year % 100 == 0 and year % 400 != 0:
        return False

    return True 

def get_weekday(day):
    match day:
        case 0: return 'Sunday'
        case 1: return 'Monday'
        case 2: return 'Tuesday'
        case 3: return 'Wednesday'
        case 4: return 'Thursday'
        case 5: return 'Friday'
        case 6: return 'Saturday'

actual = solve()
print (actual)
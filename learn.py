from datetime import date
d = date(2025, 7, 29)
name = input("Your name: ")
year = int(input("Your year of biryhday: "))
month = int(input("Your Month of birhtday: "))
day = int(input("Your day of birthday: "))
birt = date(year, month, day)
age_d = (d - birt).days
age_y = d.year - birt.year - ((d.month, d.day) < (birt.month, birt.day))
age_m = d.month - birt.month - ((d.day) < (birt.day))
born = date(year + 18, month, day)

if d.day < birt.day:
    age_m -= 1
if age_m < 0:
    age_y -= 1
    age_m += 12
com = date(birt.year + 18, birt.month, birt.day)
com_in_y = com.year - d.year
com_in_m = com.month - d.month
com_in_d = com.day - d.day
if com.day < d.day:
    com_in_y -= 1
if com_in_m < 0:
    com_in_y -= 1
    com_in_m += 12
if com_in_d < 0:
    com_in_m -= 1
if d < born:
    print(f'''
            {name} you are not 18 years old yet.
            You are were born: {age_d} days ago
            Or {age_y} years and {age_m} month ago
            You'll be 18 in: {com_in_y} years {com_in_m} month
          ''')
else:
    print(f'''
            {name} you are adult!
            And your coming of age was: {age_d} days ago
            Or {age_y} years and {age_m} month ago
        ''')
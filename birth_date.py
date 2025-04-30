from datetime import date
def get_days_in_month(month,year):
    
    if month==2:
        if year%4==0 and(year%100 != 0 or year%400==0):
            return 29
        else:
            return 28
    elif month in [4,6,9,11]:
        return 30
    else:
        return 31
def calculate_age(birth_date,current_date):
    years = current_date.year-birth_date.year
    
    months = current_date.month- birth_date.month
    
    days = current_date.day - birth_date.day
    
    
    if days <0:
        months -=1
        days +=get_days_in_month(birth_date.month,birth_date.year)
    if months <0:
        years -=1
        months +=12
    return years,months,days

birth_day = int(input("Enter a day: "))
birth_month = int(input("Enter a month: "))
birth_year = int(input("Enter a  year: "))

current_date = date.today()
birth_date = date(birth_year,birth_month,birth_day)

if birth_date <= current_date:
    age_years,age_months,age_days = calculate_age(birth_date,current_date)
    print(f"your age is {age_years} years ,{age_months} months and {age_days} days.")
else:
    print("please enter the vaild date")
    
    
    
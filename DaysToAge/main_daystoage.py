days = int(input('How many days have you lived till to day: '))
years = int(days // 365)
days %= 365
months = int(days // 30.4)
days %= 30.4
weeks = int(days // 7)
days = int(days % 7)
print('You are', years, 'year(s) and', months, 'month(s) and', weeks, 'week(s) and', days, 'day(s) old.')

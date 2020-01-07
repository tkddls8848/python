a=2
b=1
answer = ''
mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
tot_mon = sum(mon[0:a - 1])
total = tot_mon + b
result = total % 7
print(day[result])


from datetime import date

today = date.today()
d4 = today.strftime("%m")
d5 = today.strftime("%d")
d6 = today.strftime("%y")
res1 = d4+d5+d6
a = int(res1)
print(a)
hours = int(raw_input("How many hours:"))
rate = int(raw_input("At what rate:"))

pay = 0

if hours > 40:
    pay = rate * (0.5 * (hours-40) + hours)

else:
    pay = rate * hours

print pay

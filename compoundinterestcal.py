# Python compund interest calculator

principle = 0 
rate = 0 
time = 0 

while principle <= 0 :
    principle = float (input("Enter the principle amount: "))
    if principle <= 0 :
        print("Please enter a positive number for the principle amount.")

print(principle)

while rate <= 0 :
    rate = float (input("Enter the rate amount: "))
    if rate <= 0 :
        print("Please enter a positive number for the rate amount.")

print(rate)

while time <= 0 :
    time = float (input("Enter the time amount: "))
    if time <= 0 :
        print("Please enter a positive number for the time amount.")

print(time)

total = principle * pow((1 + rate/100),time)
print(f"The total amount after {time} years is: {total}")

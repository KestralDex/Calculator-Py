height = float(input('Enter your height in meters: '))
weight = float(input('Enter your weight in kilograms: '))
bmi = round(weight / (height ** 2),2)
print(f'Your BMI is: {bmi}')

if (bmi < 18.5):
    print('You are underweight')
elif (bmi >= 18.5 and bmi < 25):
    print('You are normal weight')
elif (bmi >= 25 and bmi < 30):
    print('You are overweight')
elif (bmi >= 30 and bmi < 35):
    print('You are obese')
else:
    print('You are clinically obese')
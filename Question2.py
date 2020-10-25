# Question:

# Write a program to convert temperature in Celsius to Fahrenheit & vice versa.

# Code:

temp=float(input('Enter temprature: '))
unit=str(input('Celsius(C) or Farenheit(F): '))
if unit.lower()=='c':
    temp_f=(temp*9/5)+32
    print(f'Temprature in farenheit is: {temp_f}')
else:
    temp_c=(temp-32)*5/9
    print(f'Temprature in celsius is: {temp_c}')
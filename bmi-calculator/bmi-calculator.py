height, weight = 0, 0

try:
  height = float(input('Height (centimeters): '))
except:
  raise TypeError('Error. Invalid height.')

try:
  weight = float(input('Weight (kilograms): '))
except:
  raise TypeError('Error. Invalid weight.')

bmi = round(weight / height / height * 10000, 1)

if bmi < 18.5:
  range = 'underweight'
elif bmi >= 18.5 and bmi <= 24.9:
  range = 'healthy weight'
elif bmi >= 25 and bmi <= 29.9:
  range = 'overweight'
else:
  range = 'obese'

print('Your BMI is {}, which puts you in the {} range.'.format(bmi, range))

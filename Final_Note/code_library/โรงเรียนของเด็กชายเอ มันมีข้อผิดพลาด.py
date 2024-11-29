myInput =int(input())
grade = 0

if myInput < 0:
  grade = 'Error : Value must be greater than or equal to 0.'

elif myInput > 100:
  grade = 'Error : Value must be less than or equal to 100.'

elif myInput >= 90:
  grade = 'A'

elif myInput >= 80:
  grade = 'B'

elif myInput >= 70:
  grade = 'C'

elif myInput >= 60:
  grade = 'D'

elif myInput >= 0:
  grade = 'F'

print(grade)

five_multiples = []
grades_count = int(input().strip())
grades = []

for j in range(grades_count):
  grades_item = int(input().strip())
  grades.append(grades_item)

for i in range(1,100):
  i *= 5
  five_multiples.append(i)
   
def gradingStudents(grades):
  rounded_grades = []
  for grade_item in grades:
    five_multiple_greater_than_grade = None
    for x in range(len(five_multiples)):
      if grade_item > five_multiples[x]:
        five_multiple_greater_than_grade = five_multiples[x+1]
    if grade_item >= 38 and (five_multiple_greater_than_grade - grade_item < 3):
      rounded_grade = five_multiple_greater_than_grade
    else:
      rounded_grade = grade_item
    rounded_grades.append(rounded_grade)
  return rounded_grades

result = gradingStudents(grades)
for grade in result:
  print(grade)
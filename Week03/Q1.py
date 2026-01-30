grades = [85, 92, 78, 95, 80]
#adding a new grade to the array
grades.append(90)
#sorting the array from smallest to largest
grades.sort()
print(f"Sorted grades: {grades}")
#displaying the highest grade
print(f"Highest grades: {grades[-1]}")
#displaying the lowest grade
print(f"Lowest grades: {grades[0]}")
#displaying the number of grades
print(f"Total number of grades: {len(grades)}")

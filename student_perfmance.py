import numpy as np


students = np.array([
    'mike',
    'mbappe',
    'olise',
'dembele',
    'kone'
])

marks = np.array([
    [98,12,23,45,90],
    [97,92,93,95,99],
    [96,62,53,85,70],
    [95,52,73,65,30],
    [94,82,13,25,10]
])
#display
print("students:",students)

print("marks:",marks)
#shape

print("student's shape",students.shape)

print("marks' shape",marks.shape)

#student totals
totals = np.sum(marks,axis=1)
print("student_totals = ",totals)

#student average

average = np.mean(marks,axis=1)
print("student_averages",average)

#final print-format

for i in range(len(students)):
    output = f"  {students[i]} -> Total: {totals[i]}, Average: {average[i]:.2f}"
    print(output)


#best student
Best = np.argmax(totals)
print(f" Best student is {students[Best]} with totals marks of {totals[Best]} and average marks of {average[Best]:.2f}")

#worst student

worst = np.argmin(totals)
print(f" Worst student is {students[worst]} with totals marks of {totals[worst]} and average marks of {average[worst]:.2f}")
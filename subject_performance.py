import numpy as np

subjects = np.array(['maths','english','kiswahili','science','socialstudies'])

marks = np.array([
    [98,12,23,45,90],
    [97,92,93,95,99],
    [96,62,53,85,70],
    [95,52,73,65,30],
    [94,82,13,25,10]
])

average_marks = np.mean(marks,axis=0)

print("Average marks for each subject:")

for i in range(len(subjects)):
    print(f"{subjects[i]}: {average_marks[i]:.2f}")


# highest scored subject

highest_subject_index = np.argmax(average_marks)

print(f"The highest scored subject is: {subjects[highest_subject_index]} with {average_marks[highest_subject_index]}")


# lowest scored subject


highest_subject_index = np.argmin(average_marks)

print(f"The highest scored subject is: {subjects[highest_subject_index]} with {average_marks[highest_subject_index]}")

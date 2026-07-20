import pandas as pd

# Student data
table = {
    "Name": ["Mike", "Mbappe", "Dembele", "Olise", "Kone"],
    "Age": [20, 21, 22, 19, 20],
    "Marks": [90, 78, 96, 57, 45]
}

# Create DataFrame
df = pd.DataFrame(table)

# Display the table
print("Student Records")
print(df)

# Average marks
average_marks = df["Marks"].mean()
print("\nAverage Marks:", average_marks)

# Student with highest marks
top_student = df.loc[df["Marks"].idxmax()]
print("\nTop Student:")
print(top_student)

# Students who passed (Marks >= 50)
passed_students = df[df["Marks"] >= 50]
print("\nPassed Students:")
print(passed_students)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

subjects = ["Math","Physics","Computer Science"]
math_scores = np.random.randint(0,101,20)
physics_scores = np.random.randint(0,101,20)
cs_scores = np.random.randint(0,101,20)

study_hours = np.linspace(1,10,20)

score_matrix = np.array([math_scores,physics_scores,cs_scores]).transpose()
#print(score_matrix)

#other way:
# score_matrixx = np.column_stack((math_scores,physics_scores,cs_scores))
# print(score_matrixx)


# for column in range(0,3):
#     print(f"Mean of {subjects[column]}: {score_matrix[:,column].mean()}")
#easier way:
mean_subjects = score_matrix.mean(axis=0)
# print(f"Mean of subjects: {mean_subjects}")

# for row in range(0,20):
#     print(f"Mean of student {row + 1}: {score_matrix[row,:].mean()}")
#easier way:
mean_students = score_matrix.mean(axis=1)
# print(f"Mean of students: {mean_students}")

#axis = 0 = columns and axis = 1 = rows

cs_column = score_matrix[:,2]

# cs_count = 0
# for x in cs_column:
#     if x >= 50:
#         cs_count += 1
#
# print(f"CS >= 50: {cs_count}")
#easier way:
# cs_count = np.sum(cs_column >=50)
# print(f"CS >= 50: {cs_count}")

student_ids = np.arange(1,21)
df = pd.DataFrame({
    "ID": student_ids,
    "Math": score_matrix[:,0],
    "Physics": score_matrix[:,1],
    "Computer Science": score_matrix[:,2],
    "Study Hours": study_hours
})

# print(df)
# print(df.head(5))
# print(df.tail(3))
# print(df.shape)

df["Average Score"] = mean_students
print(df)
print("")
# print(df[df["Average Score"] >= 70])
# print(len(df[df["Average Score"] >= 70]))
#
# print(df[(df['Math'] > 80) & (df['Physics'] > 80)])
# print(df.loc[df['Average Score'].idxmax()])
#idxmax -> znajduje indeks wiersza z najwyższą wartościa z podanej kolumny
#loc[] -> pobiera cały wiersz o tym indeksie

# print(df.sort_values(by="Average Score", ascending = False).head())
# print("")
# print(df.sort_values(by= "Study Hours"))
# print("")
# print(df[["ID","Math","Average Score"]])
#
plt.figure()
plt.scatter(df["Study Hours"], df["Average Score"])
plt.title("Study Hours vs Average Score")
plt.xlabel("Study Hours")
plt.ylabel("Average Score")
plt.show()

plt.figure()
plt.bar(subjects,mean_subjects,color = 'pink')
plt.title("Average Score by Subject")
plt.ylabel("Average Score")
plt.show()

#bar() porównuje kategorie, a hist() pokazuje rozkład wartości liczbowych

plt.figure()
plt.hist(df['Math'],bins = 5, color = 'g',rwidth = 0.9)
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")
plt.show()

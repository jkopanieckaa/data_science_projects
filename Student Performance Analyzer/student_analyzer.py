import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression #macine learning

np.random.seed(42)
study_hours = np.round(np.linspace(1,10,20),2)
noise = np.random.normal(0,8,20)

#we take that student who spent 0h on studying will get 25 and that each hour adds 6points to a score
#we add noise because we take into cosideration that hour of studying is not the same for each student ex. one might have been tired or has previous knowledge or luck
scores = 25 + 6 * study_hours + noise
scores = np.round(np.clip(scores,0,100),2)

df = pd.DataFrame({
    "Study Hours": study_hours,
    "Score": scores
})

print(df.head())

#double [[]] because scikit-learn expects x to be 2D
x = df[["Study Hours"]] #feature - input data on which model predicts the outcome
y = df["Score"] #target - data that model pis supposed to predict

model = LinearRegression()
model.fit(x,y) # teaching a model
# finds the best-fitting straight line that describes the relationship between x and y
# before we used noise,25 and 6 to calculate scores, now the model finds its own values based on the data

print(model.coef_) # how many points is added with each hour of studying
print(model.intercept_) # score predicted for 0h of studying

new_student = pd.DataFrame({
    "Study Hours": [5,8,9,2,3,5]
})

prediction = model.predict(new_student)
print(prediction)


plt.figure()
plt.scatter(df["Study Hours"],df["Score"],label = "Actual Scores",color = "deeppink")
plt.plot(x, model.predict(x),color = "blue",label = "Predicted Scores")
plt.xlabel("Study Hours"); plt.ylabel("Score"); plt.title("Study Hours vs Exam Score"); plt.legend()
plt.show()
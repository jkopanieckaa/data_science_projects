import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression #machine learning
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score


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

#train/test split
# 80 - 20
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)
#random state works similar to np.random.seed
# print(x_train.shape) # 16 students and 1 feature

model = LinearRegression()
model.fit(x_train,y_train) # teaching a model
# finds the best-fitting straight line that describes the relationship between x and y
# before we used noise,25 and 6 to calculate scores, now the model finds its own values based on the data

print(f"How many points does one hour of studying adds to predicted score: {model.coef_}")
print(f"Score predicted for 0h of studying: {model.intercept_}")

# new_student = pd.DataFrame({
#     "Study Hours": [5,8,9,2,3,5]
# })
# prediction = model.predict(new_student)
# print(prediction)

prediction = model.predict(x_test)
print(f"Actual Scores:\n {y_test.values}")
print(f"Predicted Scores:\n {prediction}")

errors = np.abs(y_test - prediction)
print(f"Errors:\n {errors.values}")

# mae = errors.mean()
# print(f"Mean Absolute Error:\n {mae}")

#how many points the model is wrong by, on average
mae_sklearn = mean_absolute_error(y_test,prediction)
print(f"Mean Absolute Error:\n {mae_sklearn}")

#how much of the variation in scores the model can explain
r2 = r2_score(y_test,prediction)
print(f"R2 Score:\n {r2}")
# R2 = 1: the model perfectly fits the evaluated data
# R2 = 0.5: the model explains 50% of the variation in scores
# R2 = 0: the model is no better than predicting the mean score
# R2 < 0: the model performs worse than predicting the mean score


plt.figure()
plt.scatter(x_train["Study Hours"], y_train, label = "Training data", color = "deeppink")
plt.scatter(x_test["Study Hours"], y_test, label = "Test data", color = "green")
plt.plot(x, model.predict(x),color = "blue",label = "Regressio Line")
plt.xlabel("Study Hours"); plt.ylabel("Score"); plt.title("Study Hours vs Exam Score"); plt.legend()
plt.show()


# The relationship between study hours and exam scores is linear and positive. According to the model, each additional hour of studying increases the predicted exam score by approximately 3.52 points
# The Mean Absolute Error (MAE) is 7.89, which means that the model's predictions are off by 7.89 points on average
# The R² score is 0.835, meaning that the model explains approximately 83.5% of the variation in exam scores in the test dataset
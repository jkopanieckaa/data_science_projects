import pandas as pd
import numpy as np

np.random.seed(42)
study_hours = np.linspace(1,10,20)
study_hours = np.round(study_hours, 2)
noise = np.random.normal(0,8,20)

#we take that student who spent 0h on studying will get 25 and that each hour adds 6points to a score
#we add noise because we take into cosideration that hour of studying is not the same for each student ex. one might have been tired or has previous knowledge or luck
scores = 25 + 6 * study_hours + noise
scores = np.clip(scores,0,100)
scores = np.round(scores,2)

df = pd.DataFrame({
    "Study Hours": study_hours,
    "Score": scores
})

print(df.head())
print(df.shape)

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# -----------------------------
# STUDENT MARKS DATASET
# -----------------------------

data = {
    "Study_Hours": [2,3,4,5,6,7,8,9,10,11,
                    2,4,6,8,10,3,5,7,9,12],

    "Attendance": [60,65,70,72,75,80,82,85,88,90,
                   62,70,78,84,92,68,74,81,87,95],

    "Previous_Exam_Marks": [40,45,50,55,60,65,68,72,75,80,
                            42,52,62,70,78,48,58,66,73,85],

    "Assignment_Marks": [45,50,55,60,65,70,72,75,80,85,
                         48,55,65,72,82,52,62,70,78,90],

    "Internal_Marks": [40,45,48,52,55,60,62,65,68,72,
                       42,50,58,65,70,46,55,63,68,75],

    "Practice_Test_Score": [35,42,48,52,58,62,65,70,74,78,
                            38,50,60,68,76,45,55,64,72,82],

    "Sleep_Hours": [6,6,7,7,7,8,8,8,8,9,
                    6,7,7,8,9,6,7,8,8,9],

    "Final_Marks": [42,48,54,59,64,70,73,78,82,87,
                    44,55,65,73,82,50,60,69,77,91]
}


df = pd.DataFrame(data)


# -----------------------------
# FEATURES AND TARGET
# -----------------------------

X = df.drop("Final_Marks", axis=1)
y = df["Final_Marks"]


# -----------------------------
# TRAIN TEST SPLIT
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)


# -----------------------------
# LINEAR REGRESSION
# -----------------------------

model = LinearRegression()

model.fit(X_train, y_train)


# -----------------------------
# TEST PREDICTION
# -----------------------------

y_pred = model.predict(X_test)


# -----------------------------
# MODEL EVALUATION
# -----------------------------

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)


print("\n================================")
print("   STUDENT MARKS PREDICTION")
print("================================")


# -----------------------------
# USER INPUT
# -----------------------------

study_hours = float(input("Enter Study Hours: "))

attendance = float(input("Enter Attendance (%): "))

previous_marks = float(
    input("Enter Previous Exam Marks: ")
)

assignment_marks = float(
    input("Enter Assignment Marks: ")
)

internal_marks = float(
    input("Enter Internal Marks: ")
)

practice_test = float(
    input("Enter Practice Test Score: ")
)

sleep_hours = float(
    input("Enter Sleep Hours: ")
)


# -----------------------------
# NEW STUDENT DATA
# -----------------------------

new_student = pd.DataFrame([{
    "Study_Hours": study_hours,
    "Attendance": attendance,
    "Previous_Exam_Marks": previous_marks,
    "Assignment_Marks": assignment_marks,
    "Internal_Marks": internal_marks,
    "Practice_Test_Score": practice_test,
    "Sleep_Hours": sleep_hours
}])


# -----------------------------
# PREDICTION
# -----------------------------

prediction = model.predict(new_student)


# -----------------------------
# OUTPUT
# -----------------------------

print("\n================================")
print("        PREDICTION RESULT")
print("================================")

print("Study Hours:", study_hours)
print("Attendance:", attendance, "%")
print("Previous Exam Marks:", previous_marks)
print("Assignment Marks:", assignment_marks)
print("Internal Marks:", internal_marks)
print("Practice Test Score:", practice_test)
print("Sleep Hours:", sleep_hours)

print("\nPredicted Final Marks:",
      round(prediction[0], 2))


# -----------------------------
# MODEL PERFORMANCE
# -----------------------------

print("\n================================")
print("       MODEL EVALUATION")
print("================================")

print("MAE  :", round(mae, 2))
print("MSE  :", round(mse, 2))
print("RMSE :", round(rmse, 2))
print("R2 Score :", round(r2, 2))

print("\nProgram completed successfully!")

import pickle

with open("student_marks_model.pkl","wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")    
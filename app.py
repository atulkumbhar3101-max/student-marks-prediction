import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("student_marks_model.pkl", "rb") as file:
    model = pickle.load(file)


# Page title
st.title("🎓 Student Marks Prediction")

st.write("Enter student details to predict final exam marks.")


# Input fields
study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=8.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=85.0
)

previous_marks = st.number_input(
    "Previous Exam Marks",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

assignment_marks = st.number_input(
    "Assignment Marks",
    min_value=0.0,
    max_value=100.0,
    value=80.0
)

internal_marks = st.number_input(
    "Internal Marks",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

practice_test = st.number_input(
    "Practice Test Score",
    min_value=0.0,
    max_value=100.0,
    value=78.0
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=8.0
)


# Prediction button
if st.button("Predict Final Marks"):

    new_student = pd.DataFrame([{
        "Study_Hours": study_hours,
        "Attendance": attendance,
        "Previous_Exam_Marks": previous_marks,
        "Assignment_Marks": assignment_marks,
        "Internal_Marks": internal_marks,
        "Practice_Test_Score": practice_test,
        "Sleep_Hours": sleep_hours
    }])

    prediction = model.predict(new_student)

    st.success(
        f"Predicted Final Marks: {prediction[0]:.2f}"
    )


    # Input Summary
    st.subheader("📋 Input Summary")

    st.write("Study Hours:", study_hours)
    st.write("Attendance:", attendance, "%")
    st.write("Previous Exam Marks:", previous_marks)
    st.write("Assignment Marks:", assignment_marks)
    st.write("Internal Marks:", internal_marks)
    st.write("Practice Test Score:", practice_test)
    st.write("Sleep Hours:", sleep_hours)
import streamlit as st

# ------------------------------
# App Title
# ------------------------------
st.title("GPA & CGPA Calculator")
st.write("Enter marks for each semester and calculate your GPA & overall CGPA")

# ------------------------------
# Function: Convert marks to grade points
# ------------------------------
def get_grade_point(marks):
    if marks >= 85:
        return 4.0
    elif marks >= 80:
        return 3.66
    elif marks >= 75:
        return 3.33
    elif marks >= 70:
        return 3.0
    elif marks >= 65:
        return 2.66
    elif marks >= 60:
        return 2.33
    elif marks >= 55:
        return 2.0
    elif marks >= 50:
        return 1.7
    else:
        return 0.0

# ------------------------------
# Input: Number of Semesters
# ------------------------------
num_semesters = st.number_input("How many semesters do you want to calculate?", min_value=1, step=1)

semester_data = []  # List to store GPA and Credit Hours of each semester

# ------------------------------
# Loop through each semester
# ------------------------------
for s in range(int(num_semesters)):
    st.markdown(f"### Semester {s + 1}")

    num_subjects = st.number_input(
        f"Number of subjects in Semester {s + 1}:",
        min_value=1, step=1, key=f"subs_{s}"
    )

    total_points = 0
    total_credits = 0

    for i in range(int(num_subjects)):
        marks = st.number_input(
            f"Marks for Subject {i + 1} (Semester {s + 1}):",
            min_value=0.0, max_value=100.0, key=f"m{s}_{i}"
        )

        credit_hour = st.number_input(
            f"Credit Hours for Subject {i + 1} (Semester {s + 1}):",
            min_value=1.0, max_value=5.0, value=3.0, step=1.0, key=f"c{s}_{i}"
        )

        grade_point = get_grade_point(marks)
        total_points += grade_point * credit_hour
        total_credits += credit_hour

    # GPA Calculation for this semester
    if total_credits > 0:
        gpa = total_points / total_credits
    else:
        gpa = 0.0

    st.success(f"GPA for Semester {s + 1} = **{gpa:.2f}**")
    semester_data.append((gpa, total_credits))

# ------------------------------
# Calculate CGPA for All Semesters
# ------------------------------
if st.button("Calculate Overall CGPA"):
    if semester_data:  # Check that GPA data exists
        total_quality_points = sum(gpa * ch for gpa, ch in semester_data)
        total_credit_hours = sum(ch for _, ch in semester_data)

        if total_credit_hours > 0:
            cgpa = total_quality_points / total_credit_hours
            st.markdown("---")
            st.success(f"Your Overall CGPA after {int(num_semesters)} semesters is: **{cgpa:.2f}**")
        else:
            st.warning("Please enter valid credit hours and marks to calculate CGPA.")
    else:
        st.warning("Please enter at least one semester of data before calculating CGPA.")

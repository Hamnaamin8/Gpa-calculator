import streamlit as st
import pandas as pd

# ------------------------------------------------------------
# 🎓 GPA & CGPA CALCULATOR
# ------------------------------------------------------------

st.set_page_config(page_title="GPA & CGPA Calculator", page_icon="🎓", layout="centered")

# ---- HEADER ----
st.title("🎓 GPA & CGPA Calculator")
st.markdown("Compute **semester GPA** and overall **CGPA** ")

# ------------------------------------------------------------
# GRADING SCALE
# ------------------------------------------------------------
GRADE_SCALE = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D": 1.0,
    "F": 0.0
}

st.subheader("📘 GPA Calculator")

# ---- GPA INPUT SECTION ----
num_subjects = st.number_input("📚 How many subjects did you take this semester?", min_value=1, step=1)

semester_data = []
for i in range(int(num_subjects)):
    st.markdown(f"**Subject {i+1} Details**")
    subject = st.text_input(f"Subject {i+1} Name:", key=f"subject_{i}")
    grade = st.selectbox(f"Grade for {subject or f'Subject {i+1}'}:", list(GRADE_SCALE.keys()), key=f"grade_{i}")
    credit = st.number_input(f"Credit Hours for {subject or f'Subject {i+1}'}:", min_value=1.0, step=0.5, key=f"credit_{i}")

    semester_data.append({
        "Subject": subject,
        "Grade": grade,
        "Credit Hours": credit
    })

# ---- GPA CALCULATION ----
if st.button(" Calculate GPA"):
    df = pd.DataFrame(semester_data)
    df["Grade Point"] = df["Grade"].map(GRADE_SCALE)
    df["Weighted Points"] = df["Grade Point"] * df["Credit Hours"]

    total_credits = df["Credit Hours"].sum()
    total_weighted_points = df["Weighted Points"].sum()
    gpa = total_weighted_points / total_credits if total_credits > 0 else 0.0

    st.success(f"Semester GPA: **{gpa:.2f}**")

    st.subheader("📊 Subject-wise Summary")
    st.dataframe(df, use_container_width=True)

    st.markdown(f"**Total Credit Hours:** {total_credits}")
    st.markdown(f"**Total Grade Points:** {total_weighted_points:.2f}")
    st.markdown(f"**Formula:** GPA = Total Grade Points ÷ Total Credit Hours")

# ------------------------------------------------------------
# CGPA SECTION
# ------------------------------------------------------------
st.markdown("---")
st.subheader("CGPA Calculator")

st.write("Enter your previous academic details to calculate your updated CGPA.")

previous_cgpa = st.number_input("Previous CGPA:", min_value=0.0, max_value=4.0, step=0.01)
previous_credits = st.number_input("Total Credit Hours Completed Before This Semester:", min_value=0.0, step=0.5)
new_credits = st.number_input("Credit Hours Taken This Semester:", min_value=0.0, step=0.5)
current_gpa = st.number_input("This Semester's GPA:", min_value=0.0, max_value=4.0, step=0.01)

if st.button("Calculate CGPA"):
    if previous_credits + new_credits > 0:
        updated_cgpa = ((previous_cgpa * previous_credits) + (current_gpa * new_credits)) / (previous_credits + new_credits)
        st.success(f"Updated CGPA: **{updated_cgpa:.2f}**")
        st.markdown(f"**Formula:** ((Old CGPA × Old Credits) + (New GPA × New Credits)) ÷ Total Credits")
    else:
        st.error("Please make sure total credits are greater than 0 before calculating.")

# ------------------------------------------------------------

st.markdown("---")
st.markdown("<p style='text-align:center; font-weight:bold; font-size:16px;'>📘 This calculator is made by <b>Hamna (FA23-BST-028)</b></p>", unsafe_allow_html=True)

import streamlit as st
import pandas as pd

# ------------------------------------------------------------
# 🎓 GPA & CGPA CALCULATOR
# ------------------------------------------------------------

st.set_page_config(page_title="GPA & CGPA Calculator", page_icon="🎓", layout="centered")

# ---- HEADER ----
st.title("🎓 GPA & CGPA Calculator")
st.markdown("Compute **semester GPA** and overall **CGPA** for multiple semesters easily!")

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

# ------------------------------------------------------------
# GPA CALCULATOR
# ------------------------------------------------------------
st.subheader("📘 Semester GPA Calculator")

num_subjects = st.number_input("📚 How many subjects did you take this semester?", min_value=1, step=1)

semester_data = []
for i in range(int(num_subjects)):
    st.markdown(f"**Subject {i+1} Details**")
    subject = st.text_input(f"Subject {i+1} Name:", key=f"subject_{i}")
    grade = st.selectbox(f"Grade for {subject or f'Subject {i+1}'}:", list(GRADE_SCALE.keys()), key=f"grade_{i}")
    credit = st.number_input(f"Credit Hours for {subject or f'Subject {i+1}'}:", min_value=1.0, step=0.5, key=f"credit_{i}")
    semester_data.append({"Subject": subject, "Grade": grade, "Credit Hours": credit})

if st.button("Calculate GPA"):
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
# MULTI-SEMESTER CGPA CALCULATOR
# ------------------------------------------------------------
st.markdown("---")
st.subheader("🎯 Multi-Semester CGPA Calculator")

st.write("Enter GPA and Credit Hours for **any number of semesters** to calculate your overall CGPA.")

num_semesters = st.number_input("How many semesters do you want to include?", min_value=1, step=1)

semesters = []
for i in range(int(num_semesters)):
    st.markdown(f"**Semester {i+1}**")
    gpa = st.number_input(f"GPA for Semester {i+1}:", min_value=0.0, max_value=4.0, step=0.01, key=f"gpa_{i}")
    credits = st.number_input(f"Credit Hours for Semester {i+1}:", min_value=0.0, step=0.5, key=f"credits_{i}")
    semesters.append({"Semester": i + 1, "GPA": gpa, "Credit Hours": credits})

if st.button("Calculate Overall CGPA"):
    df_cgpa = pd.DataFrame(semesters)
    total_credits = df_cgpa["Credit Hours"].sum()
    total_weighted = (df_cgpa["GPA"] * df_cgpa["Credit Hours"]).sum()

    if total_credits > 0:
        overall_cgpa = total_weighted / total_credits
        st.success(f"🎓 Overall CGPA after {int(num_semesters)} semesters: **{overall_cgpa:.2f}**")
        st.dataframe(df_cgpa, use_container_width=True)
        st.markdown(f"**Total Credits:** {total_credits}")
        st.markdown(f"**Formula:** (Σ(GPA × Credits)) ÷ Σ(Credits)")
    else:
        st.error("Please enter valid credit hours before calculating CGPA.")

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; font-weight:bold; font-size:16px;'>📘 This calculator is made by <b>Hamna (FA23-BST-028)</b></p>",
    unsafe_allow_html=True
)

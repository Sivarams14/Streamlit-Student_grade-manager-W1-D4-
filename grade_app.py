
# grade_app.py
# Week 1 - Day 4: Streamlit Student Grade Manager

import streamlit as st


# Page configuration
st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="centered"
)


# Store students in session state instead of a normal list
if "students" not in st.session_state:
    st.session_state.students = []


def get_grade(mark):
    """
    Return the grade based on the student's mark.
    """

    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def add_student():
    """
    Display a Streamlit form to add a student.
    Validate the input before storing the student.
    """

    st.subheader("Add Student")

    with st.form("add_student_form"):

        name = st.text_input("Enter student name").strip()

        mark = st.number_input(
            "Enter student mark (0-100)",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

        submitted = st.form_submit_button("Add Student")

        if submitted:

            if name == "":
                st.error("Name cannot be empty. Please try again.")

            else:
                grade = get_grade(mark)

                student = {
                    "name": name,
                    "mark": mark,
                    "grade": grade
                }

                st.session_state.students.append(student)

                st.success(
                    f"{name} added successfully with grade {grade}."
                )


def show_results():
    """
    Display all students in a Streamlit table.
    Also display average, highest and lowest marks.
    """

    st.subheader("Student Results")

    students = st.session_state.students

    if len(students) == 0:
        st.info("No students have been added yet.")
        return

    # Display students in a table
    st.table(students)

    # Get all marks
    marks = [student["mark"] for student in students]

    # Calculate statistics
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    st.subheader("Class Performance")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Average", f"{average:.1f}")

    with col2:
        st.metric("Highest", highest)

    with col3:
        st.metric("Lowest", lowest)


def main():
    """
    Main page of the Streamlit Student Grade Manager.
    """

    st.title("🎓 STUDENT GRADE MANAGER")

    st.write(
        "Add student marks, calculate grades, "
        "and view class performance."
    )

    st.divider()

    add_student()

    st.divider()

    show_results()


# Start the application
if __name__ == "__main__":
    main()

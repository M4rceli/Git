import streamlit as st

def main():
    st.title("Strona tytułowa")

    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://images.pexels.com/photos/3225517/pexels-photo-3225517.jpeg');
            background-size: cover;
        }
        header {
            background: red !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Professor"):
            display_professor()
    with col2:
        if st.button("Room"):
            display_room()
    with col3:
        if st.button("Student"):
            display_students()

def display_professor():
    # Kod do wyświetlenia tabeli dla zakładki Professor
    pass

def display_room():
    # Kod do wyświetlenia tabeli dla zakładki Room
    pass

def display_students():
    # Kod do wyświetlenia tabeli dla zakładki Students
    pass

if __name__ == "__main__":
    main()

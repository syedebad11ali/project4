import streamlit as st
import os

st.title("Personal Library App")

# Set your directory path here
DIRECTORY = r"C:\Users\HASEEB\Desktop\project4"

# Define the Library class
class Library:
    def __init__(self, book, author, progress):
        self.book = book
        self.author = author
        self.progress = progress

    def __str__(self):
        return f"Book: {self.book}\nAuthor: {self.author}\nProgress: {self.progress}\n"

# Get user choice
user_choice = st.selectbox("Choose an action:", ["Add a book", "Remove a book", "Search for a book", "View all books", "Exit"])

# Common file input
file_name = st.text_input("Enter your file name (without extension):")
file_path = os.path.join(DIRECTORY, f"{file_name}.txt")

if not os.path.exists(DIRECTORY):
    os.makedirs(DIRECTORY)

if user_choice == "Add a book":
    book = st.text_input("Book Name:").capitalize()
    author = st.text_input("Author Name:").capitalize()
    progress = st.text_input("Progress:").capitalize()
    if st.button("Add Book"):
        new_book = Library(book, author, progress)
        with open(file_path, "a") as file:
            file.write(str(new_book))
        st.success(f"Book '{book}' added to your library.")

elif user_choice == "Remove a book":
    book_to_remove = st.text_input("Book Name to Remove:").capitalize()
    if st.button("Remove Book"):
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                lines = file.readlines()
            updated_lines = [line for line in lines if not line.startswith(f"Book: {book_to_remove}")]
            with open(file_path, "w") as file:
                file.writelines(updated_lines)
            st.success(f"Book '{book_to_remove}' removed.")
        else:
            st.warning("File does not exist.")

elif user_choice == "Search for a book":
    book_to_search = st.text_input("Book Name to Search:").capitalize()
    if st.button("Search"):
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                lines = file.readlines()
            found = False
            for line in lines:
                if book_to_search in line:
                    st.success(f"Found: {line.strip()}")
                    found = True
                    break
            if not found:
                st.info(f"'{book_to_search}' not found in the library.")
        else:
            st.warning("File does not exist.")

elif user_choice == "View all books":
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            books = file.readlines()
        if books:
            st.text("\n".join([line.strip() for line in books]))
        else:
            st.info("The file is empty.")
    else:
        st.warning("File does not exist.")

elif user_choice == "Exit":
    st.info("Goodbye! Have a nice day.")

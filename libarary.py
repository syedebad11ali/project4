#Please look at lines and locate the directory variable before starting the code ok
import os

class library:
    def __init__(self,book,author,progress):
        """This take the book,author and progress as input"""
        self.book=book
        self.author=author
        self.progress=progress
    def __str__(self):

        return f"Book: {self.book}\n, Author: {self.author}\n, Progress: {self.progress}\n"
        

# class shelf(library):
#     def __init__(self):

directory=r"C:\Users\HASEEB\Desktop\project4" #if using my code change the directory or remov ethe directory parts in the code
while True:
    try:
        user_choice=int(input("Choice from the following choices:"
        " 1 for adding a book:\n "
        " 2 for removing a book:\n "
        " 3 to search for a book:\n "
        " 4 for all of the books:\n"
        " 5 for exiting:\n"))
        if user_choice not in [1,2,3,4,5]:
            raise ValueError("Invalid choice please select from the fiven options")
        break
    except ValueError as e:
        print(f"Error:{e} try again ")
    

if user_choice == 1:
    user_input=input("Do You Want Add A Book (yes) or (no): ").lower()


    if user_input == "yes" or user_input=="y":

        file=input("Enter your file name : ")
        book_name=input("Enter Your Book Name: ").capitalize()
        author_name=input("Enter The Name Of The Author: ").capitalize()
        progress_staus=input("Enter Your Progress:").capitalize()
        
        user=library(book_name,author_name,progress_staus)

        file_path=os.path.join(directory,f"{file}.txt")

        if not os.path.exists(directory):
            os.makedirs(directory)

        if  os.path.exists(file_path):        
            with open(file_path,"a") as file:
                file.write(str(user))
                
        print("Book Detail Saved")
    elif user_input == "no" or user_input=="n":
        print("Goodbye have a nice day")
    else:
        print(f"Chose from the above choice your input is invalid {user_input}")

elif user_choice == 2:
    # for removing
    user_input=input("Do You Want Remove A Book (yes) or (no): ").lower()

    if user_input == "yes" or user_input=="y":

        file=input("Enter your file name : ")
        remove_book_name=input("Enter Book Name You Want To Remove: ").strip().capitalize()
        file_path=os.path.join(directory,f"{file}.txt")

        if os.path.exists(file_path):
            with open (file_path,"r") as file:
                lines=file.readlines()
                
            update_line = []
            for line in lines:
                if not line.startswith(f"Book: {remove_book_name}"):
                    update_line.append(line)
            with open(file_path,"w") as file:
                file.writelines(update_line)
                

            print(f"Your {remove_book_name} has been Removed from {file}.txt")
        else:
            print("File does not exist")
    elif user_input == "no" or user_input=="n":
        print("Goodbye have a nice day")
    else:
        print(f"Chose from the above choice your input is invalid {user_input}")
if user_choice == 3:
    file=input("Enter your file name : ")
    search_book_name=input("Enter Book Name You Want To Search: ").strip().capitalize()
    file_path=os.path.join(directory,f"{file}.txt")

    if os.path.exists(file_path):
        with open (file_path,"r") as file:
            book=file.readlines()
            
            found=False
            for line in book:
                if search_book_name in line:
                    print(f"Found: {line.strip()}")
                    found=True
                    break
            if not found:
                print(f"Book: {search_book_name} not found in {file}.txt")
    else:
        print(f"The file {file}.txt does not exist")
if user_choice == 4:
    file=input("Enter your file name : ")

    file_path=os.path.join(directory,f"{file}.txt")

    if os.path.exists(file_path):
        with open (file_path,"r") as file:
            books=file.readlines()
            if books:
                print("\n All Book In File:")
                for line in books:
                    print(line.strip())
            else:
                print(f"The file {file}.txt is empty")
    else:
        print(f"The file {file_path} does not exist")

if user_choice == 5:
    print ("Have a nice day")
    
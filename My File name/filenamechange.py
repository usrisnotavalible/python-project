import os

path = input("Enter path:")
# format_ = print(f"Entered the format {input()}")
file_name = input("Enter File name")
new_file_name = input("Enter new file name")


def folder(path, file_name, new_file_name):
    if os.path.exists(path) == True:
        print("Path Exist")
    else:
        print("Soory! path does not exist")

    if os.path.isfile(file_name) == True:
        os.rename(file_name, new_file_name)
        capital_name = new_file_name.capitalize()
        print("Name Successfully changed")
    else:
        print("File name does not exist")


folder(path, file_name, new_file_name)
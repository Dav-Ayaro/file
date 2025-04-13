# Lab11.py

# function to create a file
def create_file():
    with open("users.txt", "w") as file:
        pass

#function to add a user
def add_user(username):
    with open("users.txt", "a") as file:
        file.write(username + "\n")

# #function to upadate a user
def update_user(old_username, new_username):
    with open("users.txt", "r") as file:
        users = file.readlines()
    with open("users.txt", "w") as file:
        for user in users:
            if user.strip() == old_username:
                file.write(new_username + "\n")
            else:
                file.write(user)

# #function to remove a user
def remove_user(username):
    with open("users.txt", "r") as file:
        users = file.readlines()
    with open("users.txt", "w") as file:
        for user in users:
                file.write(user)


# Down here is the test code to see if the functions works properly
create_file()
add_user("dave")
add_user("john")
update_user("dave", "dave_updated")
remove_user("john")

print("users.txt file Created and updated!!!")



## you can see a file by
#ls to see the file
#cat users.txt to see the content of the file OR
#nano users.txt to edit the file and t see the content inside it

"""import sqlite4
sqlc=sqlite4.connect('pwdmgr.db')
cursor=sqlc.cursor()
command="CREATE TABLE pwd(
        
)"
"""
master_password=input("Please Enter Your Password:")
def view():
    with open("passwords.txt","r") as f:
        for lines in f.readlines():
            data=lines.rstrip()#rstrip removes return carraiges
            user,pswd=data.split(":")
            print(f"UserName:{user}\tPassword:{pswd}")
def add():
    username=input("Enter your UserName:")
    password=input("Enter your password:")

    with open("passwords.txt","a" )as f:#using with closes file automatically
        f.write(username + ":" + password+"\n")
def remove():
    rmvid=input("Enter the Username you want to remove:")
    if rmvid==user:
        for lines in f.readlines():
            data = lines.rstrip()  # rstrip removes return carraiges
            user, pswd = data.split(":")
            
if master_password!="Kibbu":
    print("Invalid Password:")
    exit()
else:
    while True:
        mode=input("Do you Want to View or Add Password or Quit the Program (View,Add,Quit)").lower()
        if mode=="quit":
            break
        if mode=="view":
            view()
        elif mode=="add":
            add()
        else:
            print("invalid Choice")
            continue   
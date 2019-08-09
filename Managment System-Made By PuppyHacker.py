class Users:
    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
    def get_name(self):
        return self.name
    def get_pay(self):
        return self.pay
    def get_all(self):
        return "name: {} pay: {}\n".format(self.name, self.pay)

dict_of_users={}
def add_user():
    while True:
        print("Welcome To The User WIzard!")
        name = input("Please Enter Your Full Name\n->")
        pay = input("Please Enter The Pay\n->")
        print("Thank You!")
        print("Wait While We Makeing The User")
        dict_of_users[name]=Users(name,pay)
        print("Done!\n")
        con=input("Add another user?(y/n)")
        if con == "y":
            add_user()
        if con == "n":
            break
        break



def start():
    sec = dict(name="secretary", pwd="123123")
    manager = dict(name="manager", pwd="manager")
    print("Made By Tamir Forte\n\n")
    print("Welcome!\nFor Manager:\nUsername:manager Password:manager")
    print("For secretary:\nUsername:secretary Password:123123")
    print("To exit press N and N again")
    username= input("\nEnter Your UserName\n->")
    pwd=input("Enter Your Password\n->")
    if username == sec['name'] and pwd == sec['pwd']:
        print("welcome secretary!")
        secr()
    elif username == manager['name'] and pwd == manager['pwd']:
        print("welcome manager!")
        managerf()
    if username == "N" and pwd == "N":
        goodbye()
    else:
        print("Worng username Or password\nTry again")
        start()
def print_all():
    for user in dict_of_users.keys():
        place = dict_of_users[user]
        print(Users.get_all(place))
def print_user():
    name = input("enter the name you want to see\n->")
    place = dict_of_users[name]
    print(Users.get_all(place))
def delete_user():
    name=input("Enter The Name You Want To Delete\n->")
    del dict_of_users[name]
    print("done!")
def text_file():
    file = open(r"C:\Users\TamirForte\Desktop\user_text.txt","w")
    for user in dict_of_users.keys():
        place = dict_of_users[user]
        file.write(Users.get_all(place))
    file.close()
    print("Done!\nFile saved on your Desktop!")
def avarege():
    x=0
    y=0
    for user in dict_of_users.keys():
        place = dict_of_users[user]
        x += int(Users.get_pay(place))
        y += 1
    ave = x / y
    print("the salary avarege is",ave)
def cr_del():
    c = input("To Create a user press 1\nTo delete a user press 2\n->")
    if c == "1":
        add_user()
    if c == "2":
        delete_user()
def secr():
    print("Welcome!\nHere are your options")
    c = input("1- Create or delete users\n2- Print all the users to a text file\n3- To log off\n-> ")
    if c == "1":
        cr_del()
        secr()
    if c == "2":
        text_file()
        secr()
    if c == "3":
        start()
def managerf():
    print("Welcome Manager!\nHere are your options")
    c = input("1- Create or delete users\n2- watch a specific user\n3- show a avarege pay\n4- show all workers\n5- log off\n->")
    if c == "1":
        cr_del()
        managerf()
    if c == "2":
        print_user()
        managerf()
    if c == "3":
        avarege()
        managerf()
    if c == "4":
        print_all()
        managerf()
    if c == "5":
        start()
def goodbye():
    print("Thank You For Trying The App\nMade by Tamir Forte")
    x=input()
start()

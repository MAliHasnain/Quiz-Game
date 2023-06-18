#Bismillah

def login(name,password):

    """This function take input for login and check from the stored file whether the id has registered or not!"""

    success = False
    file = open("CS21068_1.txt","r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if(a==name and b==password):
            success=True
            break
    file.close()
    if(success):
        print("Login Successfull!!!")
    else:
        print("wrong username or password")
        begin()
        access(option)

'''--------------------------------------------------------------------------------------------------------'''

def register(name,password):

    """This function take input for registrations and then store registration in the file! """

    file=open("CS21068_1.txt","a")
    file.write("\n"+name+","+password)
    file.close()

'''----------------------------------------------------------------------------------------------------------'''

def login1():

    """This function take login input after user registered itself! """

    print("login Kindly")
    name = input("Enter Your Name: ")
    password = input("Enter Your Password: ")
    login(name, password)

'''----------------------------------------------------------------------------------------------------------'''

def access(option):

    """This function take choice from the user, whether to login or to register!"""

    if(option=="login"):
         name=input("Enter Your Name: ")
         password =input("Enter Your Password: ")
         login(name,password)
    else:
         print("Enter Your Name And Password To Register")
         name = input("Enter Your Name: ")
         password = input("Enter Your Password: ")
         register(name,password)
         print("Register Successfully!!!")
         login1()

'''----------------------------------------------------------------------------------------------------------'''

def begin():

    """This function restarts the login & register choice if user input incorrectly  """

    global option
    option = input("login or register (login,reg):")
    option=option.lower()
    if(option!="login" and option!="reg"):
        begin()

'''-----------------------------------------------------------------------------------------------------------'''

def changes():

    """This function provide choices to admin whether to view or add question and further choices for different subject """

    choice1 = input("Do you want to View Questions or Add Questions?(View,Add)  ")
    choice1 = choice1.lower()
    if choice1 == "view":
        choice2 = input("Which subject do you want to view(pst,IQ)? ")
        choice2 = choice2.lower()
        if choice2 == "pst":
            file = open("CS21068_2.txt", "r")
            print(file.read())
            file.close()
            print('THANK YOU!!!')
        elif choice2 == "iq":
            file = open("CS21068_3.txt", "r")
            print(file.read())
            file.close()
            print('THANK YOU!!!')
        else:
            changes()
    elif choice1 == "add":
        choice3 = input("Which subject do you want to add(pst,IQ)? ")
        choice3 = choice3.lower()
        if choice3 =="pst":
            file=open("CS21068_2.txt","a+")
            file1=open("CS21068_4.txt","a+")
            num=int(input("How many questins do you want to add?  "))
            for i in range(num):
                quest=input("Enter your Question here along with 3 options : ")
                file.write("*"+quest+"\n")
                answ=input("Enter your answer option here as (A/B/C) : ")
                file1.write(answ+"\n")
                file.close()
                file1.close()
                print('THANK YOU!!!')
        elif choice3 =="iq":
            file=open("CS21068_3.txt","a+")
            file1 = open("CS21068_5.txt", "a+")
            num = int(input("How many questins do you want to add?  "))
            for i in range(num):
                quest1 = input("Enter your Question here along with 3 options : ")
                file.write("*"+quest1+"\n")
                answ1 = input("Enter your answer option here as (A/B/C) : ")
                file1.write(answ1+"\n")
                file.close()
                file1.close()
                print('THANK YOU!!!')
        else:
            print("WRONG CHOICE!!! ")
            changes()
    else:
        print("WRONG CHOICE!!! ")
        changes()

'''----------------------------------------------------------------------------------------------------------'''

def start():

    """This function take input from user whether he is student or admin of quiz game and starts the game!!! """

    print("Quiz Game")
    opt=input("Student or Admin (std,admin):")
    opt=opt.lower()
    if (opt=="std"):
        begin()
        access(option)
        choice = input("Which subject do you want select?(PST,IQ)?  ")
        choice = choice.lower()
        print("Give your answer in the form of (A/B/C) or (a,b,c) ")
        if choice == "pst":
            with open("CS21068_2.txt", "r") as quesfile, open("CS21068_4.txt", "r") as ansfile:
                questions = [question.strip() for question in quesfile.readlines()]
                answers = [answer.strip() for answer in ansfile.readlines()]
                score = 0

                for question, answer in zip(questions, answers):
                    user_ans = input(question + "?\n")
                    if user_ans.lower() == answer.lower():
                        print("Correct!")
                        score += 1
                        print("score:", score)
                    else:
                        print("Incorrect!")
                        score = score
                        print("score:", score)

                print("Your final score is : ", score)
                if score>5:
                    print("Well done! ")
                else:
                    print("Better luck next time! ")
        elif choice == "iq":
            with open("CS21068_3.txt", "r") as quesfile, open("CS21068_5.txt", "r") as ansfile:
                questions = [question.strip() for question in quesfile.readlines()]
                answers = [answer.strip() for answer in ansfile.readlines()]
                score = 0

                for question, answer in zip(questions, answers):
                    user_ans = input(question + "?\n")
                    user_ans = user_ans.lower()
                    if user_ans == answer.lower():
                        print("Correct!")
                        score += 1
                        print("score:", score)
                    else:
                        print("Incorrect!")
                        score = score
                        print("score:", score)
                print("Your final score is ", score)
                if score>5:
                    print("Well done! ")
                else:
                    print("Better luck next time! ")
        else:
            print("WRONG CHOICE!")
        print("THANKYOU!")
    elif (opt=="admin"):
        admin="cisd"
        password1=input("Enter password:")
        if password1==admin:
            print("NOW YO ARE IN ADMIN MODE!")
            changes()
        else:
            print("wrong password!")
            start()
    else:
        start()
start()

'''----------------------------------------------------------------------------------------------------------'''

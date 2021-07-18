#This is a Faulty Calculator 
#Smruti Ranjan Nayak 
#Date : 7/11/2021 
#1st Project
#wrong value : 45*3 = 555 , 56+9 = 77, 56/6=4 

import os
def sl():
    print(" CALCULATOR ")
    print("")
    os.system("cls")
    value1 = int(input("First Value  : "))
    value2 = int(input("Second Value : "))

    print("""
        
        [1] + 
        [2] -
        [3] *
        [4] /
        
        """)
    choose_value = int(input("Choose Option : "))

    if choose_value == 1 :
        if hex(value1) == '0x38' and hex(value2) == '0x9':
            os.system("cls")
            print("+" *50)
            print(f"""
                
                {value1} + {value2} = {int(0x4d)}
                
                """)
            print("+"*50)
        else:
            os.system("cls")
            print("+" *50)
            sum1 = value1 + value2
            print(f"""
                
                {value1} + {value2} = {sum1}
                
                """)
            print("+"*50)
    elif choose_value == 2:
        os.system("cls")
        print("-" *50)
        sum1 = value1 - value2
        print(f"""
                
            {value1} - {value2} = {sum1}
                
            """)
        print("-"*50)
    elif choose_value == 3:
        if hex(value1) == '0x2d' and hex(value2) == '0x3':
            os.system("cls")
            print("*" *50)
            print(f"""
                
                {value1} * {value2} = {int(0x22b)}
                
                """)
            print("*"*50)
        else:
            os.system("cls")
            print("*" *50)
            sum1 = value1 * value2
            print(f"""
                
                {value1} * {value2} = {sum1}
                
                """)
            print("*"*50)
    elif choose_value == 4:
        if hex(value1) == '0x38' and hex(value2) == '0x6' :
            os.system("cls")
            print("/" *50)
            print(f"""
                
                {value1} / {value2} = {int(0x4)}
                
                """)
            print("/"*50)
        else:
            os.system("cls")
            print("/" *50)
            sum1 = value1 / value2
            print(f"""
                
                {value1} / {value2} = {sum1}
                
                """)
            print("/"*50)


sl()
while True:
    print("")
    yes_no = str(input("Use Again ( Y or N ) : ")).upper()
    if yes_no == "Y":
        sl()
    else:
        os.system("cls")
        print(" ")
        print(" Thank You For Using Faulty Calculator ")
        print(" ")
        print(exit)
        print("")
        exit()

    
from string import digits
import sys 
import re
import math

#intering info
while True :
    try :
            name = input("Please enter your username: ").strip() 
            if not name :
                print ("We don't allow free spaces. ")        
                continue
            else:
                while True :
                    try :
                        password = input("Please enter a valid password: ")
                        repassword = input("Confirm your password: ")
                        if not password : 
                                    print ("We don't allow free spaces. ")
                                    continue
                        else :    
                                if len(password) >= 8 :     
                                    if password == repassword :
                                        print("Password set successfully. ")
                                        continue
          
                                    else :
                                        print("Passwords do not match. Please try again. ")
                                        continue
                                else :
                                    print ("Password must be more than 8 digits. ")
                                    continue
                    except ValueError :
                        print ("Try again")
                    break
    except ValueError :
         print("error") 
    break

while True:
    try:
        for _ in range (5): 
          correctname =input("Enter your username: ")
          correctpassword =input("Enter your password: ")

          if repassword != correctpassword or correctname != name :
                print("Incorrect password or username. ")
          else :
                print ("Hallo,", name)
                break 
        break    
    except ValueError() :
          print ("An error accured. ")       

#grating
while True :
    try: 
        for _ in range(1000) :
            while True :
                    try: 
                        gender = str(input("Enter gender: \n"))
        
                        if gender == "male"  :
                            print ("Hallo, Sir")
                            break

                        elif gender == "female":
                            print ("Hallo, Ma'am")
                            break

                        else:
                            print("Please choose gender (male) or (female). ")    
                             
                    except ValueError:
                        print ("Enter gender: " ) 
                    pass   
                    
#intring name
            name = input("Enter the name: \n").strip().title()
            print (f"Hallo, {name}")

#intering age
            while True :
                    try:           
                        age = int(input("Enter the age: \n" ))
                        (age) = input
                    except ValueError:
                        print ("It is not an age. ")
                    else:
                        break

#intering grade
            while True :
                try:
                            for _ in range (9):   
                                while True :
                                    try :
                                            score = float(input("Enter the score: \n"))
                                            break
        
                                    except ValueError :
                                        print ("Enter the real score. ") 
                 
                                if score >= 90:
                                    print ("Grade: A")
                                elif score >= 80:
                                    print ("Grade: B")
                                elif score >= 70:
                                    print ("Grade: C")
                                elif score >= 60:
                                    print ("Grade: D")
                                else:
                                    print ("Grade: F")             
                            break  
                except Exception as e :
                    print("Try again. ")  
            print("Thank You. ")
    except ValueError :
        print ("Try again. ")
    break                      

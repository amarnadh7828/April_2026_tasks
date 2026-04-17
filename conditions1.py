# Syntax:
# if condition:
#      statement 1
#      statement 2
#      statement n

# age = 14
# if age>=18:
#     print(f"eligible  to vote")
#     print(f"welcome to pythonlife")
#     num_1 = input("enter :")
#     print(num_1)


# print("sample statements")



# user_name = input("enter the username: ")
# password = input("entre the password: ")
# if user_name == "swathi" and password == "swathi@123":
#     print(f"login success")
#     print(f"welcome {user_name}")
# else:
#     print(f"invalid login credentials.....")




# Syntax:
# if condition-1:  
#      statement 1 
# elif condition-2:
#      stetement 2 
# elif condition-3:
#      stetement 3 
#      ...         
# else:            
#      statement

#granding system

# marks = int(input("enter the marks: "))
# if marks>=90 and marks<=100:
#     print(f"you got A grade obtained marks {marks}")
# elif marks>=80 and marks<=89:
#     print(f"you got B grade obtained marks {marks}")
# elif marks>=70:
#     print(f"you got C grade obtaiend marks {marks}")
# elif marks>=60:
#     print(f"you got D grade obtained marks {marks}")
# elif marks>=35:
#     print(f"pass you obtained marks {marks}")
# elif marks>=0 and marks<=34:
#     print(f"failed.... you marks {marks}")
# else:
#     print("enter valid marks")


# marks = int(input("enter the marks: "))
# if marks>100 or marks<0:
#     print(f"invalid inputs , marks should be between 0 to 100")
# elif marks>=90:
#     print(f"you got A grade obtained marks {marks}")
# elif marks>=80:
#     print(f"you got B grade obtained marks {marks}")
# elif marks>=70:
#     print(f"you got C grade obtained marks {marks}")
# elif marks>=35:
#     print(f"pass you obtained marks {marks}")
# else:
#     print("fail ")



# Syntax:
# if condition1:
#     # code block for condition1
#     if condition2:
#         # code block for condition2
#     else:
#         # code block for condition2 being false
# else:
#     # code block for condition1 being false



# user_name = input("enter the username: ")
# password = input("entre the password: ")
# if user_name == "swathi" and password == "swathi@123":
#     print(f"login success")
#     print(f"welcome {user_name}")
# else:
#     print(f"invalid login credentials.....")




# user_name = input("enter the username: ")
# password = input("entre the password: ")
# otp = int(input("entre the otp: "))
# if user_name == "akhil":
#     if password == "akhil@123":
#         if otp == 1234:
#             print(f"login success..")
#             print(f"welcome {user_name}")
#         else:
#             print(f"invalid otp")
#     else:
#         print(f"invalid password..")
# else:
#     print(f"invalid username.. ")



# Syntax:
# result = value_if_true if condition else value_if_false


# num_1 = int(input("enter the number: "))
# if num_1%2==0:
#     print(f"even number")
# else:
#     print(f"not even")

# num_1 = int(input("enter the number: "))
# result = "even" if num_1%2==0 else "not even"
# print(result)

# num_1 = int(input("enter the number: "))
# print("even") if num_1%2==0 else print("not even")



# Vowel Checker:
# Write a Python program that takes a character as input and checks whether it is a vowel or not. Use the if-else statement.

# char = input("enter the char: ")
# if char == "a" or char == "e" or char == "i":
#     print(f"vowel")


# char = input("enter the char: ")
# if char == "a":
#     print("vowel")
# elif char == "e":
#     print("vowel")


# char = input("enter the char: ")
# vowels = "aeiouAEIOU"
# if char in vowels:
#     print("Vowel")
# else:
#     print("not vowel")


# num_1 = int(input("enter the number"))
# if num_1 >0:
#     print(f"positive")
# elif num_1<0:
#     print("negative")
# else:
#     print("zero")

weight = float(input('enter your weight in kg: '))
height = float(input('enter your height in meters: '))
a =weight / (height ** 2)
print(f'your bmi is: {a}')
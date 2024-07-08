# number_entered= False
# while number_entered == False:
#     try:
#         age = int(input('Age: '))
#         print(age)
#         number_entered = True
#         break
#     except ValueError:
#         print("Oopsie poopsie! Invalid input! Please use a number!")
# print("Code complete")
# # exception error handling. Useful for input errors
# # also allows you toanticipate error types and use different code if triggered
# # I created a loop to ensure you must enter an integer value to continue. Neat!


try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be zero you actual baby.")
except ValueError:        
    print("Oopsie poopsie! Invalid input! Please use a number!")
# You can utilitze multiple exception types within one try block.

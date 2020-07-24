ch = input("enter a single character: ")
if ch >='A' and ch <='Z':
    print("you have entered a upper case character ")
elif ch >='a' and ch <= 'z':
    print("you have entered a lower case character ")
elif ch >='0' and ch <= '9':
    print("you have entered a numerical digit ")
else:
    print("you have entered special character ")

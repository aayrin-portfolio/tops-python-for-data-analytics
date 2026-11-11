"""
1.Write a python script that checks if a user's entered age is 18 or above and
prints "eligible for IPL ticket booking" if true, otherwise prints "not eligible". 
"""
age = int(input("Enter your age:"))

if age>=18:
    print("Eligible for IPL ticket booking")
else:
    print("Not eligible")   

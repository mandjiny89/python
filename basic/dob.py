dob = input("Enter your data of birth in specific format DD-MM-YYYY: ")
month = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec')
index = int(dob[3:5]) -1
bd_month = month[index]
print(bd_month)
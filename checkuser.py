import re
username=input('Please Enter the username: ')
password=input('Please Enter the password: ')
#check username
if len(username)>=6:
    if(bool(re.match('((?=.*[a-z])(?=.*[A-Z]).{6,30})', username))==True):
        print('Username belongs to category 1.')
    elif(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,30})', username))==True):
        print('Username belongs to category 2.')
    elif(bool(re.match('((?=.*\d).{6,30})', username))==True):
        print('Username belongs to category 2.')
else:
    print('Invalid username')
#check password
if len(password)>=6:
    if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{6,30})',password))==True):
        print("The password is strong")
    else:
        print("The password is weak")
else:
    print("Invalid password.")

'''
password=input('Please Enter the password: ')
if len(password)>=6:
    if(bool(re.match('(?=.*[A-Z])', password))==True):
        if(bool(re.match('(?=.*[a-z])', password))==True):
            if(bool(re.match('(?=.*[0-9])', password))==True):
                if(bool(re.match('(?=.*[!@#$%^&*])', password))==True):
                    print("The password is strong")
                else:
                    print('Password is weak.')
            else:
                print('Password is weak.')
        else:
            print('Password is weak.')
    else:
        print('Password is weak.')
    
else:
    print('Invalid password')
'''
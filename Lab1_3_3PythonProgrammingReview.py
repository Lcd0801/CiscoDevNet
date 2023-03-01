# personal-info.py 

 

firstName = input("What is your first name? ") 

lastName = input("What is your last name? ") 

location = input("What is your location? ") 

age = input("What is your age? ") 

print("Hi " + firstName, lastName + "! Your location is " + location + " and you are " + age + " years old.") 

# if-acl.py 

 

aclNum = int(input("What is the IPv4 ACL number? ")) 

if aclNum >= 1 and aclNum <= 99: 

    print("This is a standard IPv4 ACL.") 

elif aclNum >=100 and aclNum <= 199: 

    print("This is an extended IPv4 ACL.") 

else: 

    print("This is not a standard or extended IPv4 ACL.") 

# while-loop.py 

while True: 

    x=input("Enter a number to count to: ") 

    if x == 'q' or x == 'quit': 

        break 

    x=int(x) 

    y=1 

    while True: 

        print(y) 

        y=y+1 

        if y>x: 

            break 

# file-access.py 

 

devices=[] 

file=open("devices.txt","r") 

for item in file: 

    item=item.strip() 

    devices.append(item) 

file.close() 

print(devices) 

# file-access-input.py 

 

file = open("devices.txt", "a") 

while True: 

    newItem = input("Enter device name: ") 

    if newItem == "exit": 

        print("All done!") 

        break 

    file.write(newItem + "\n") 

file.close() 
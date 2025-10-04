#This is the email slicing exercise 
email = input ("Enter your email: ")
index = email.index("@")
domain =email [index +1:] 
username = email [:index]

print (f'Your username is: {username}, and your domain is {domain}.')
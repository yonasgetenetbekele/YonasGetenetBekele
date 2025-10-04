#This is the email slicing exercise 
email = input ("Enter your email: ")

domain =email [email.index("@") +1:] 
username = email [:email.index("@")]

print (f'Your username is: {username}, and your domain is {domain}.')
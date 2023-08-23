import re

# mail="harishberam1704@gmail.com"
# mail2="harish.beram123@yahoo.in"
# mail3="harish.beram@terralogic.com"

pattern=r"[a-zA-Z0-9]+(|\.[a-zA-Z0-9]+)(|\d+|[a-zA-Z]+)\@[a-z]+\.(com|in)"
mail=input("Enter Mail: ")
user_choice=input("Enter Your  Answer Yes | No ")
out=re.search(pattern,mail)
if user_choice == "Yes"  or user_choice =="Y" or user_choice =="yes":
    if out:
        vaild_email=out.group()
        fw=open("emaildata.txt","a")
        fw.write(vaild_email + '\n')

else:
    fr=open("emaildata.txt","r")
    print(fr.read())
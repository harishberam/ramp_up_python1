# #Write a Python program for the following requirements.
# #Read a String statement from the command line
# #Findout total number of characters present in the statement.
# Find out total number of duplicate Characters in the statement
# Find out total number of words present in the statement
# Find out total number of duplicate words in the statement
# Reverse the characters present in the statement.
# Form a new statement from the reversed words.
# Remove the duplicate characters from the latest statement.
# Print final latest String statement.

#################################################

str1=input("Enter the String: ")
print(str1)

###################################################
count=0
for i in str1:
    count=count+1
print("Number of characters:",count)

####################################################
# str2=set()
# count=0
# dup_cha = {}
# for i in str1:
#     if i in str2:
#         count=count+1
#     else:
#         str2.add(i)
# print("The duplicate character is :",count)

d={}
str2=set(str1)
for i in str2:
    if str1.count(i)>1:
        d[i]=str1.count(i)
print(d)

#######################################################

word_list=str1.split()
word_count=len(word_list)
print("The total  number of the words: ",word_count)

###################################################
words =str1.split()
duplicta_words = {}

for word in set(words):
    if words.count(word) > 1:
        if word not in d:
            d[word] = words.count(word)

print("dupicate_words",duplicta_words)


#########################################

reversed_string=""
reverse_char=reversed_string+str1[::-1]
print(reverse_char)

#########################################

data=str1
data=data.split()
reversed_words=""
for i in data:
    i=i[::-1]
    reversed_words +=i+" "
print(reversed_words)


#################################################

new_statement=reversed_words
print("new_statemnt_from_reversed_words :",reversed_words)

###################################################
#remove characters from new-statement

unique_char=set(new_statement)

remove_dup_chars=""
for char in unique_char:
    if new_statement.count(char)>1:
        remove_dup_chars=new_statement.replace(char,"")
        new_statement=remove_dup_chars
print("after remove duplicates_chars new statement:",new_statement)

#######################################################

final_statements=new_statement
print("final_statements:",new_statement)



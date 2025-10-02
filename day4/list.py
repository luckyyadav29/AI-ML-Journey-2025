number=[1,'2',3,4,5] #defining a list
print(type(number)) #checking the type of variable
print(number[0]) #indexing
print("hello" + number[1]) #adding string with string
new_num=[[9,8,7],[6,5,4],[3,2,1]]#list inside a list
print(new_num[2][0]) #positive indexing
print(new_num[-3][-1]) #negative indexing
#list slicing
print(number[1:4]) #slicing from index 1 to 3
print(new_num[1:][1:]) 

print(len(new_num)) #length of list , since length of list is reduced which shows list are mutable

new_num[0][-1]=10 #changing value of list
print(new_num)

#concatenation of list and replication
print(number + ['6','7']) #concatenation
print(number * 3) #replication

del number[0] #deleting an element from list
print(number) #printing the list after deleting an element

#in and not in operator
print(2 not in number) #checking if 2 is not in the list
print('2' in number) #checking if '2' is  in the list

n1,n2,n3,n4=number #unpacking the list(multiple assignment)
print(n1,n2,n3,n4) #printing unpacked values

#remove() function
number.remove('2') #removing '2' from the list
print(number) #printing the list after removing an element

# sort() function
string=['A','C','B','E','D'] #defining a list of strings
string.sort() #sorting the list in ascending order
print(string) #printing the sorted list
string.sort(reverse=True) #sorting the list in descending order
print(string) #printing the sorted list
new_num = [[9,8,7],[6,5,4],[3,2,1]]
new_num.sort()
print(new_num) #sorting the list of lists based on first element of each sublist
new_num.sort(key=sum)
print(new_num) #sorting the list of lists based on sum of each sublist

print('Four score and seven ' + \
 'years ago...') #line continuation using backslash


import random
print(random.choice(number)) #choosing a random element from the list
print(random.randint(0,len(number)-1)) #choosing a random index from the list

number.append('6')#adding an element at the end of the list
print(number) #printing the list after adding an element

spam=number
print(spam) #printing the spam list
spam[-1]='Q' # it is the reference of number list, not  a new list
print(number) #printing the number list after changing an element in spam list

print(type(("hello",))) # tuple with one value, mark the comma
print(type("hello")) # string
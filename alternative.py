# part1: Making each alternate character into an upper case character and each other alternate character
# a lower case character.
string=input('Enter string: ')

for i in range(len(string)):
    
    if i%2==0:
        print(string[i].upper())
        
    else:
        print(string[i].lower())


#part2: Making each alternative word lower and upper case.
string=input('Enter string: ')
string1=string.split()

for i in range(len(string1)):
    
    if i%2!=0:
        print(string1[i].upper())
        
    else:
        print(string1[i].lower())
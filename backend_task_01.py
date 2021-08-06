n=int(input()) #Enter the number of words
l=list()
l1=list()
for i in range(n):
    a=input()  #Enter the word
    if a in l:
        pass
    
    else:
        l1.append(a)  #Adding the distinct word to the list
    l.append(a)

print(len(l1))    #First line of the output

for i in range(len(l1)):
    print(l.count(l1[i]),end=" ")
   

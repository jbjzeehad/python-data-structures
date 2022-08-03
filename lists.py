# @ Jbj Zeehad

names=["James","Tom","Amy"]  #lists
print(names[1])   #out: Tom

m= [
[1,2,3],
[4,5,6]
]
print(m[1][2])  #out: 06

words=["spam","eggs","sausage","spam"]      #list operations
print("spam" in words)      #True
print("egg" in words)       #False
print("tomato" in words)    #False

x=[2,4,6,8]  #loops
for n in x:
    print(n) #out : 2,4,6,8

y=[2,4,6]   #list functions
y.append(8)
y.remove(4)
y.insert(0,8)
print(y)            #o:[8,2,6,8]
print(y.count(8))   #o: 2

z=[2,4,6,8]         
z.reverse()
print(z)        #o:[8,6,4,2]
z.sort()
print(z)        #o:[2,4,6,8]
print(min(z))   #o:2
print(max(z))   #o:8

#part 02
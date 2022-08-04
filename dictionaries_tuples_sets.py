# @ Jbj Zeehad


ages={
    "Dave" : 24,
    "Mary" : 42,
    "John" : 58
}                       #dictionaries > key : value

print(ages["Dave"])     
print(ages["Mary"])
                    
nums={
    1:"one",
    2:"two",
    3:"three"
}                       #dictionary function
print(1 in nums)
print("three" in nums)      #False
print(4 not in nums)        #True


pairs={
    1:"apple",
    "orange" : [2,3,4],
    True : False,
    12 : "True"
}                   #get() function

print(pairs.get("orange"))          #o: [2,3,4]
print(pairs.get(7,42))              #o: 42
print(pairs.get(12345,"not found")) #o: not found

#Tuples
words=("spam","eggs","sausages")
print(words[0])                 #o: spam

dict={
    ("David",42) : "red",
    ("Bob",24) : "green"
}
print(dict[("Bob",24)])    #o: green

numbers=(1,2,3)     #tuple unpacking
a,b,c=numbers
print(a)        #o : 1
print(b)        #o : 2
print(c)        #o : 3

w,x,*y,z=[1,2,3,4,5,6,7,8,9]
print(w)        #o : 1
print(x)        #o : 2
print(y)        #o : [3,4,5,6,7,8]
print(z)        #o : 9

#sets
num_sets={1,2,3,4,5}
print(3 in num_sets)    #o : True

#part 03
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

nums_set ={1,2,1,3,1,4,5,6}
print(nums_set)
nums_set.add(-7)        #o : {1,2,3,4,5,6}
nums_set.remove(3)      #o : {1,2,4,5,6,-7}
print(nums_set)         #duplicate elements auto. get removed from set

first={1,2,3,4,5,6}
second={4,5,6,7,8,9}
print(first | second)       #o :{1,2,3,4,5,6,7,8,9}
print(first & second)       #o :{4,5,6}
print(first - second)       #o :{1,2,3}
print(second - first)       #o :{8,9,7}
print(first ^ second)       #o :{1,2,3,7,8,9}


#part 03
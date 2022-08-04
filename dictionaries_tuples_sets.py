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




#part 03
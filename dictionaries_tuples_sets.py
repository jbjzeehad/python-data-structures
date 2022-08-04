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

'''
Problem :
You are analyzing sales data from a ticket office.
The ticket for an adult is $20, while the ticket for a child under 18 is $5.
The data you are given is in a dictionary format, where the keys are the sold ticket numbers, and the values are the customer ages.
For example, "123-08": 24 means that the ticket was bought a 24 year old.
Your goal is to calculate how much more money the office would make if it would change the ticket discount age to the given input.
So, your program needs to take an integer as input and output the percentage of revenue growth, if the discount was given to people under that age.

For example, if the office made $15000 with the original discount age, and would make $15024 with 14 as the discount age, then the growth would be ((15024-15000)/15000)*100 = 16%

So, for the input 14, your program should output 16. The output should be an integer (use int() to convert the result).
'''

data = {
    "100-90": 25, "42-01": 48, 
    "55-09": 12, "128-64": 71, 
    "002-22": 18, "321-54": 19, 
    "097-32": 33, "065-135": 64, 
    "99-043": 80, "111-99": 11, 
    "123-019": 5, "109-890": 72, 
    "132-123": 27, "32-908": 27, 
    "008-09": 25, "055-967": 35, 
    "897-99": 44, "890-98": 56, "344-32": 65, 
    "43-955": 59, "001-233": 9, "089-111": 15, 
    "090-090": 17, "56-777": 23, "44-909": 27, 
    "13-111": 21, "87-432": 15, "87-433": 14, 
    "87-434": 23, "87-435": 11, "87-436": 12, 
    "87-437": 16, "94-121": 15, "94-122": 35, 
    "80-089": 10, "87-456": 8, "87-430": 40
}
cstmr_age = int(input())
old_incm=0
new_incm=0
for var in data.values():
    if var<18:
        old_incm+=5
    else:
        old_incm+=20
    if var<cstmr_age:
        new_incm+=5
    else:
        new_incm+=20
if cstmr_age<18:
    growth=((new_incm - old_incm)/old_incm)*100
    print(int(growth))
else:
    print(0)



#part 03
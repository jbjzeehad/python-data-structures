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

cubes=[i**3 for i in range(5)]          #list comprehensions
print(cubes)                #o:[0,1,8,27,64]

evens=[i**2 for i in range(10) if i**2 % 2 ==0]
print(evens)                #o:[0, 4, 16, 36, 64]


'''Problem : Given a sentence as input, calculate and output the average word length of that sentence.To calculate the average word length, you need to divide the sum of all word lengths by the number of words in the sentence'''

text = input()
word_list=text.split()
word_cnt=len(word_list)

letter_cnt=0
for w in word_list:
    letter_cnt=letter_cnt+len(w)

average=letter_cnt/word_cnt
print(average)         

#part 02
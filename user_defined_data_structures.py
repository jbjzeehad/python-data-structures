# @ Jbj Zeehad

#stack

'''Stack in Python. Stack is a user defined 
data structure. In simple english, stack 
is a pile of things arranged one on the top of other.
You like travelling ?
well, yeah who doesn't. 
We pack clothes in a bag every time we have to travel.
How do we pack? 
We put clothes in a bag one by one, on top of the other.
And How do we take it out?
We take out the cloth that was placed at last, first
because that's on the top... then the second last one.
then the third last one.. and so on. 

That's why, Stack is called First In, Last Out or 
we can say Last In, First Out. That describes the order.
'''

'''Similarly we can create a stack in python. 
Let's create one. How do we create an object?
OOPs!!! Name a class, create its blueprint. 
define its properties and behaviour and you are done 
man.'''

class Stack: #class has been defined. It's simple. Just Name it.
            #Now we need an init function, which is basically 
            #a blueprint of a class. cool!'''
    def _init_ (self):
        self.items = [] 

        '''Done. Our stack will store items in a list.
        Well, we always pack our clothes in an empty bag, right?
        so, our list is empty in the beginning and 
        will be populated with items when the time comes to travel.
        Lol! No, That's when we will populate our 
        empty bag with clothes. '''


        '''well, before we start packing, we need to check if our bag is empty.
        how do we do it? we unzip it, look into it.
        ask our mind, hey is it empty? Mind compares it
        with picture of an empty bag and if both looks same, 
        it returns yes boss. It's true that the bag is empty. 
        We, then, grab that bag.


        so, same here. check our list is empty or stacked. 
        create a function that checks if list is empty, let's call this 
        function is_empty. This function compares our list with an empty list
        and if both are equal, it says True, otherwise returns False. '''
    
    def is_empty(self):
        return self.items == []


        '''So, now that we know our empty bag is empty. Let's stack it, right?
        well, we push our clothes inside bag and pop it out one by one.
        First clothes in, we know we can take it out only at last because 
        that goes further down as we push more clothes in the bag.

        But hey we are programming, we want to push 
        some data into our list. 

        We need to define a function that will let us 
        push data in our list just like we push clothes in our bag.So, we Name 
        this function, push. It takes data as argument and 
        push it at first position in our list. Why only at first position?
        Well, remember that bag thing, we always push our clothes
        at the same position. At the top. Right? Every cloth we push in, 
        takes the top position and other clothes get pushed below.
        Same here, we push our items at the first position and 
        every other item gets pushed to (their position + 1 ).
        Now, we can push our items at the last position as well using
        append method. But if we push our items at the last position,
        we will have to take them out using the same route, 
        then we can use pop() instead of pop(0). Details in push method 
        explanation. '''
    
    def push (self,data):
        self.items.insert(0, data)

        '''isn't it simple? we are done in two simple lines. 

        Now, we don't just push our clothes in. We pop them out too when 
        needed. And in what order? Last in, (at the top), first out. 
        Similarly, here we will define function pop, this function won't 
        take any argument, because we simply take clothes out from bag, 
        we need additional clothes (arguments) only when we want to push in.
        While taking out, we simply take clothes out from bag itself. 
        Here, we have our list, (self) and we can take items out obviously 
        using the same route. We pushed data at the first position, 
        we will take them out from the first position. 

        remember, we do the same with our travel bag. We don't cut open 
        our bag on other side to take out clothes in same order. same, here.
        we will pop out items from first position. Let's do it. while pushing in,
        we don't get anything. but while taking out, 
        we get one cloth that we take out each time we repeat this 
        exercise. We get one cloth in return. 
        That's why, our push function didn't return anything 
        but our pop function will return us the popped item 
        every time. Woah! It's easy.
        '''
    
    def pop(self):
        return self.items.pop(0)

        ''' is it complex? man, if you understand the basic concept, 
        it's just two lines of code each time. Funny. 

        while packing,we push clothes in, we then take them out. 
        when finally done, we want to check if we kept all our clothes
        in our bag? Well, we can't do that in real life.
        we will have to take all of them out and then put in the bag again.
        it's difficult. But, here, we can print the entire list to check
        what data it contains after all these exercise. 
        so, how do we do it? You just said that. we print them. 

        we define the print_stack method, that takes the list(self)
        and print all of its items. Boom!! Done. You have mastered Stack. 
        Congratulations!! Celebration!! '''


    def print_stack(self):
        print(self.items)

        '''Just 2 lines each F***ing time. '''


travelBag = Stack()
travelBag.push('shirts')
travelBag.push('Pants') 
travelBag.push('gun')
travelBag.push('everything')
travelBag.print_stack()

travelBag.pop()
travelBag.print_stack()


#part 04
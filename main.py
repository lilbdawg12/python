#VARIABLES
#----------#
#STRINGS
#first_name = "Blaize"
#last_name = "ramsay"
#full_name = first_name +""+ last_name
#print("hello "+first_name)
#print(type(name))

#INT DATATYPE
#age = 20
#age = age+1
#print("your age is: "+str (age))
#print (type(age))

#FLOAT DATATYPE
#height = 250.5
#print ("your height is :"+str(height)+"cm")
#print(type(height))

#BOOLEAN DATATYPE
#human = False
#print ("Are you a human: " +str (human))
#print(type(human))
#------------------
#multiple assignment = allows us to assign multiple variables at the same time in one line of code
#---------------------
#name = "Blaize"
#age = 21
#attractive = True

#name, age, attractive = "Blaize", 21, True

#print (name)
#print (age)
#print (attractive)

#Blaize=21
#Justin=23
#Anim=19
#Joe=23

#Blaize = Justin = Anim = Joe = 30

#print(Blaize)
#print(Justin)
#print(Anim)
#print(Joe)

#--------------
#String Methods
#---------------
#name = 'Blaize Ramsay'

#print(len(name))
#print(name.find('R'))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count('R'))
#print(name.replace("B","R"))
#print(name*100)

#---------------------
#type casting = convert data type of a value to another data type
#-----------------
#x = 1 #int
#y = 2.0 #float
#z = "3" #string

#x= str('x is ' +str (x))
#y = str ('y is ' + str (y))
#z = int (z)

#print('x is ' +str (x))
#print(y)
#print(z*260)
#-----------------
#user input
#-------------------
#name = input('What is your name?:')
#age = int(input ('how old are you?:'))
#height = float(input('how tall are you?:'))

#print ('hello '+name)
#print ('you are'+str(age)+ 'years old')
#print('you are '+ str(height)+'cm tall')

#------------------------------------
#import math
#--------------------------------------

#pi = 3.14
#x = 1
#y = 2
#z = 3

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(pi))
#print(max(x,y,z))
#print(min(x,y,z))
#------------------
#string Slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]
#-----------------------
#name = 'Blaize Ramsay'

#first_name = name[0:6] #or [:4]
#last_name = name [7:]
#funky_name = name [0:15:4] #or [::4]
#reversed_name = name[::-1]

#print(reversed_name)
#print(last_name)

#website1 = 'http://google.com'
#website2 = 'http://wikipedia.com'
#slice = slice(7,-4)

#print(website1[slice])
#print(website2[slice])

#if statement = a block of code that will execute if it's condition is true

#age = int(input('How old are you?: '))

#if age == 100:
    #print('your old af')
#elif age >= 18:
    #print('you are an adult!')
#elif age < 0:
    #print("you havn't been born yet!")
#else:
    #print('You are a child!')
#-----------------
#Logical operators (and,or,not) = used to check if two or more conditional statements is true
#---------------------------------------------------
#temp = int(input("what is the temperatur outside?: "))

#if temp >= 0 and temp <= 30:  #if not(temp >= 0 and temp <= 30:) all this does is put it in reverse
    #print('the temperature is good today!')
    #print('go outside!')
#elif temp < 0 or temp >30:
    #print('the temperature is bad today!')
    #print('stay inside')

#------------------
#While Loop = a statement that will execute it's block of code, 
#             as long as it's condition remains true

#while 1==1:     #loop
    #print('help im stuck in a loop')

#name = ""
#while len(name) == 0:
#    name = input ("Enter your name: ")

#print("hello "+ name)
                        #EXAMPLES of loop
#username = ''
#while len(username) == 0:
     #username = input ("Enter your username: ")
   

#print('Welcome, '+ username)
#import time
#------------------------------------
#for loop =     a statement that will execute it's block of code
#               a limited amount of times
#
#               While loop = ulimited
#               For loop = limited
#----------------------------

#for i in range(10):
    #print(i+1)

#for i in range (20,40+1,2):
    #print(i+1)
    
#for i in 'Blaize Ramsay':
    #print(i)
    
#for seconds in range(10,0,-1):
    #print (seconds)
    #time.sleep(1)
#print ('Happy New Year')
#----------------
#nested loops = The "inner loop" will finish all of it's iterations before
#               finishing one iteration of the "outter loop"
#---------------------------------------------------------------
#rows = int(input("How many rows?: "))
#columns = int(input("How many columns?: "))
#symbol = input('emter a symbol to use')

#for i in range(rows):
#    for j in range(columns):
#        print(symbol, end ='')
#    print()

#a list is a named collection of items

#   The items in a list can be anythin - number, text, 
#              variables, objects, and even other list
#   a list whos items are other lists is called a multidimensial list

#create a list of integers
int_list = [-3,7,4,0,-2,342]

#create a list of strings
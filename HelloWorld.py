#print hello world in python 
print "hello world"
print ("hello world")
print 'hello world'


# '''--------do anything---------'''
print ('''hello 
   world
     i am interesting

 ''')

print ('''hello 
world
i am interesting

''')

# let user tell when to say hello world
user = input("Enter decision : ")
if user == 'yes' or user == "Yes":
   print("Hello world")
else:
   print(f"You said : {user}")

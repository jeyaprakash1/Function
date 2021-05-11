# Types of arguments

# positional arguments

def add(n1,n2):
    return n1+n2
add(10,20)

# Keyword arguments

def add(name,msg):
    print('Hi',name,msg)
add(name='venkat',msg='welcome')
add(msg='welcome',name='sakthi')

# Default arguments

def greeting(name='admin'):
    print('welcome',name)
greeting('samar')
#output: welcome samar

def greeting(name='admin'):
    print('welcome',name)
greeting()
#output : welcome admin

#variable length arguments

def calc(*n):
    total=0
    for x in n:
        total=total+x
    print(total)
calc(90)
calc(90,80,70,60) # speify using comma separation while declare more value
calc()

# Keyword variable length arguments

def calc(**n):
    for sub,mark in n.items():
        print(sub,'scored',mark)
calc(tamil=90)
calc(tamil=90,english=70,maths=60)



















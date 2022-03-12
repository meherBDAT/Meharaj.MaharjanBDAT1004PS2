#!/usr/bin/env python
# coding: utf-8

# In[1]:


Question 1 Answer:

The Value of a will be 6 at the end.

At first the value of a is 0. But after execution of each b(). it calls the functions c(a) and adds the number to each time 
with the gloval variable 'a'.

1) a = 0 + 2 = 2
2) a = 2 + 2 = 4
3) a = 4 + 2 = 6
4) a = 6



# In[18]:


# Question2 answer

def fileLength(file_name):
    try:
        file = open(file_name)
        contents = file.read()
        file.close()
        print(len(contents))

    except FileNotFoundError:
        print("File " +  file_name +"not found.")
    except:
        print('Other error.')

fileLength('midterm.py')

fileLength('idterm.py')
       


# In[12]:


# Question 3 answer

class Marsupial:
    def __init__(self):
        self.pouch=[]

    def put_in_pouch(self, item):
        self.pouch.append(item)
        
    def pouch_contents(self):
        return self.pouch

class Kangaroo(Marsupial):

    def __init__(self, x,y):
        Marsupial.__init__(self)
        self.x=x
        self.y=y  

    def jump(self, dx, dy):
        self.x+=dx
        self.x+=dy

    def __str__(self):
        return "I am a Kangaroo located at coordinates ("+ str(self.x)+","+ str(self.y)+")"

    

k = Kangaroo(0,0)
print(k)

k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
print(k.pouch_contents())

k.jump(1,0)
k.jump(1,0)
k.jump(1,0)
print(k)


# In[19]:


#Question 4 answer
x=0
def collatz(x):
    if x == 1:
        print(x)
    elif x % 2 == 0:
        print(x)
        x = x/2
        collatz(x)
    else:
        print(x)
        x = 3*x + 1
        collatz(x)
collatz(1)
collatz(10)


# In[21]:


# Question 5 answer
def binary(x):
    if x == 0:
        return '0'
    else:
        binaryOutput = ''
        while x > 0:
            binaryOutput = str((x % 2)) + binaryOutput
            x //= 2
        return binaryOutput

print(binary(0))
print(binary(1))
print(binary(3))
print(binary(9))


# In[9]:


# Question 6 answer
from html.parser import HTMLParser
class HeadingParser(HTMLParser):
    h1 = False
    def handle_starttag(self, tag, attrs):
        if tag == 'h1':
            self.h1 = True
             
    def handle_data(self, data):
        if self.h1:
            print(data, end='')

infile = open('w3c.html')
content = infile.read()
infile.close()
hp = HeadingParser()
hp.feed(content)


# In[5]:


# Question 7 answer
def webdir(url, integer,indent):
    

webdir('http://reed.cs.depaul.edu/lperkovic/csc242/test1.html', 2, 0)
    


# In[ ]:


#Question 8 answer
 
Let us say that the name of the database table is 'weatherdata'
 Here is the SQL Queries on the table
a)All the temperature data:
    select temperature from whether;

b)All the cities, but without repetition:
    select distinct city from weatherdata;

c) All the records for India:
    select * from weatherdata where countrt =='India';

d)All the Fall records:
    select * from weatherdata where season == 'Fall';

e)The city, country, and season for which the average rainfall is between 200
and 400 millimeters.:
    select city, countrt, season from weatherdata where rainfall between 200 and 400;

f) The city and country for which the average Fall temperature is above 20
degrees, in increasing temperature order.:
    select city, countrt from weatherdata where season == 'Fall' and temperature > 20 order by temperature ASC;

g) The total annual rainfall for Cairo.:
    select sum(rainfall) AS annual_rainfall from weatherdata where city == 'Cairo';

h) The total rainfall for each season.:
    select season, sum(rainfall) AS annual_rainfall from weatherdata group by season;


# In[12]:


#Question 9 answer
words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

# a) answer
print([x.upper() for x in words])

# b) answer
print([x.lower() for x in words])

# c) answer
print([len(x) for x in words])

# d) answer
print([[x.upper(), x.lower(), len(x)] for x in words])

# e) answer
print([x for x in words if len(x)>=4])


# In[ ]:





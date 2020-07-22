#!/usr/bin/env python
# coding: utf-8

# Day 2
# basic python syntax
# python varibales and assignment statement
# python operators
# 1.)Basic syntax:
# Back slash:

# In[1]:


print("hello python")


# end of line error while scanning string literal
# 

# In[2]:


print("hello       python")


# 2.)Triple Quotes:
# ascii text art SMS
# print(""" art """)
# 
# without print statement
# making doc string - without print

# In[3]:


print('''……..@*@*
….@*……..@* …………………………@*
..@*……………@* ………………@*……..@*
.@*……………….@*……….@*……………..@*
@*…………………..@*…@*………………….@*
@*………………………*……………………..@*
.@*…………………………………………….@*
..@*………………………………………..@*
….@*…………………………………..@*
……..@*…………………………..@*
………..@*……………………@*
…………….@*…………..@*
……………….@*……@*
………………….*..@*
……………………@
……………………*
……………………@
……………………*
''')


# In[4]:


'''this program is written by mohit'''


# In[5]:


print('''this program is written by mohit''')


# 3 uses of """ - printing text art, making doc string, making SQL statements
# 
# a = """ this program is written by mohit """- this can run in SQL

# 3.)string inside the quotes

# In[6]:


print('hello world')


# In[7]:


print('python's world')


# In[8]:


print("python's world")


# 4.) escape sequence of string
# backslash + t for spaces

# In[9]:


print("hello\tpython")


# backslash + n for line separator

# In[10]:


print("hello\npython")


# use apostrohes with backslash

# In[11]:


print("python\'s world")


# 5.) Formatted Output

# In[12]:


name="mohit"
marks="90"
age="20"
print("the name of person is ", name, "marks is", marks, "ages is", age)


# In[13]:


name="mohit"
marks=90.867
age=20
print("the name of person is ", name, "marks is", marks, "ages is", age)


# using multiple statements

# In[14]:


print("the name of person is %s marks is %f age is %d"%(name,marks,age))


# %s is string
# %f is float
# %d is integer
# 

# In[15]:


print("the name of person is %10s marks is %10f age is %d"%(name,marks,age))


# 2 decimal places

# In[16]:


print("the name of person is %10s marks is %10.2f age is %d"%(name,marks,age))


# In[17]:


print("the name of person is %10s marks is %10.1f age is %d"%(name,marks,age))


# In[18]:


pring(f"the name of person is {name} the marks is {marks} age is {age}")
same output


# greater than 3.4 version needed for above

# python variables
# varible means linking of the data to a name
# according to the data type, the interpreter reserves the memory space
# varible refers to the memory location that contains the data
# memory or ram, define a varible a=10
# every byte has a address
# symbolic address is variable
# integer, float = object
# = is assignment operator, sets linking from a to 10
# holds data and points
# a10 is variable 10a is not a variable
# rules to define a variable
# a kw cannout be used as a variable "if", "def" and "for" are the reserved kws. they cannot be used as variables
# a variable can contain letters (upper case or lower case), numbers, underscore
# python is case sensitive, hence variables are also case sensitive
# a variable cannot start with a number
# a variable is assigned to data by using the assignment operator

# use meaningful names

# In[20]:


print("cisco_temp=40")


# python assignment statement
# <variable name>=<data>example
# x = y = z = 10

# In[21]:


x = 20
id(x)


# In[22]:


y=20
id(y)


# same number! why? because pointing to same memory object

# del x is delete
# deletion deletes path from x to 20
# not from y to 20
# hence y value still holds
# 
# it is like cutting the bindings
# 

# del y
# both are erased now
# 20 is still floating

# types of python operators
# arithmetic operators
# comparison operators
# assignment operators
# bitwise operators
# logical operators
# membership operators
# identity operators
# 
# arithmetic operators
** exponent - performs exponential (power) calculation on operators
* multiplication
/ division
% modulus > remainder
+ addition
- subtraction
// floor division: floor division means that after performing the division it returns the lower integer value as the result > get lowest integer value
integer/integer = float value
integer/integer = integer value (in python 2)
# In[24]:


10/3


# In[25]:


10//3


# hence lower value

# In[26]:


10**3


# In[27]:


10*3


# In[28]:


10%5


# In[29]:


10+5


# In[30]:


10-5

comparison operators
== the operator returns true if the right=side operand and left-side operamd are equal
< the less than operator returns true if right-side operand is less than left-side operand
> the greater than operator returns true if right side operand is greater than the left-side operand
<= the less than or equal to operator returns true if the right-side operand is less than or equal to the left-side operand
>= the greater than or equal to operator returns true if the right-side operand is greater than or equal to the left-side operand
!= the not equal to operator returns true if right-side operand is not equal to the left-side operand

true is 1, false is 0

use python shell to check syntax errors
# In[31]:


a = 10
b= 10
c = 20
a == c


# In[32]:


a<c


# In[33]:


b>c


# In[34]:


a<=b


# In[35]:


a>=c


# In[36]:


a!=b

assignment operators
= a=b, b is assigned to a
+= a+=b is equal to a=a+b, a=a+b also works as a syntax
-+ a-=b is equal to a=a-b
*= a*=b is equal to a=a*b
/= a/=b is equal to a=a/b
**= a**=b is equal to a=a**b

command prompt - type python here

notepad++ is best

any editor is fine

must recognize python syntax
# In[41]:


a=10
b=10
c=20
a+b

bitwise operators
works on bits= 1,0
refer truth tables in binary numbers
| = bitwise OR operation
& = bitwise AND operation
~ = Binary one's Complement
^ = bitwise XOR operation
<< = binary left shift operator, the left-hand operand bit is shifted to the left by the number on the right
>> = binary right shift operator, the right=hand operand bit is shifted to the right by the number on the rightlogical operators
And = if both the sides right and left are true then the AND operator returns true
Or = if any side it true then the OR operator returns true
Not = the not operator inverts the outcome of the condition. if a condition in the not operator returns true, then the not operator makes it false, vice versa.

revise true false logic sums

T or T = T
T or F = T
F or T = T
F or F = F

T and F = F
F and T = F
F and F = F
T and T = T
# In[44]:


10>9


# In[45]:


20>m


# In[49]:


10<9


# In[47]:


20>m


# In[50]:


10>9 and 20>m


# In[51]:


10<9 and 20>m


# because the system went back and reverse calculated
membership operators
in - if the specified operand is found in the sequence, then the "in" operator returns true, otherwise it returns false
not in - if the specified operand is not found in the sequence, then the not in operator returns true, otherwise it returns false

identity operators
is - if 2 variables refer to the same memory location then the is operator returns true, otherwise it returns false
is not - if 2 variables refer to the same memory location, then the "is not" operator returns false, otherwise it returns true

-5 to 256 is same memory range
# operator precedence lowest to highest:
# assignment expression :=
# lambda expression lambda
# conditional expression if-else
# boolean OR or
# boolean AND and
# boolean NOT not x
# comparisons, including membership tests and identity tests in,not in,is,is not,<,<=,>,>=,!=,==
# bitwise OR |
# bitwise XOR ^
# bitwise AND &
# shifts <<,>>
# addition and subtraction +,-
# multiplication, matrix multiplication, division, floor division, remainder *,@,/,//,%
# positive,negative,bitwise NOT +x,-x,~x
# exponentiation *
# await expression await x
# subscription, slicing, call, attribute reference x[index],x[index:index],x(arguments...),x.attribute
# binding or parenthesized expression, list display, dictionary display, set display     (expressions...),[expressions...],{key:value...},{expressions...}

# In[52]:


10+10/29*4


# python 2 gives different answer
# python 3 gives decimal answer
# 

# In[53]:


10>8>9


# In[54]:


10>8 and 10>9


# In[56]:


a =240
b = 1
a|b


# In[57]:


bin(240)


# In[58]:


a & b


# In[59]:


str = "Python is a programing language"
"a" in str #checks if a is present in the string


# In[60]:


"z" in str #checks if a is present in the string


# In[61]:


"z" not in str


# In[62]:


k=10
f=10

k==f #value is same


# In[63]:


k is f #and they are also pointing to same memory location


# In[64]:


id(k)


# In[65]:


id(f) #prven both points to same memory location


# In[66]:


x=1.5
y=1.5

x==y


# In[67]:


a = 257
b = 257
a==b


# In[68]:


a is b


# In[ ]:





# %%
s1 = 'Lorem ipsum dolor sit amet'
s2 = "Lorem ipsum dolor sit amet"
# %%
s3 = """Lorem ipsum dolor sit amet, 
consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. 

Ut enim ad minim veniam,
quis nostrud exercitation"""
# %%
def foo():
    """Function foo()
Prints "Hello Python"

created: 09.04.2021
modified: 09.04.2021
author: me
"""
    print('Hello Python')
# %%
foo()
# %%
print(foo.__doc__)
print(sorted.__doc__)
# %%
x = 12

print(f'value of {x} ** 2 is {x ** 2}')
# %%
print('x' * 10)


# %%
s2[4]
# %%
s2[0:5]
# %%
s2[0:20:2]
# %%
s2[::2]
# %%
s2[::-1]
# %%

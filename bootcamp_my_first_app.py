import streamlit as st

st.header('10 Cool Beginner Python Tricks That Will Make Your Life Easier')
st.caption('Simple but effective tips for every python lovers')
st.text("""The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities.

In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.""")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([
    "1. Walrus operator",
    "2. Splitting a string",
    "3. Reversing a string",
    "4. Merging two dictionaries",
    "5. The zip() function",
    "6. Assigning multiple list values to a variable",
    "7. Remove duplicate list items",
    "8. Lambda function",
    "9. Swapping variable value",
    "10. Use a password in your code",
    ])

with tab1:
    st.markdown("""The `Walrus` or `:=` operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.""")
    st.markdown("""**Example**
    If we want to check and print the length of a list:
    """)
    st.code("""Mylist = [1,2,3]
if(l := len(mylist) > 2)
print(l)""")
    st.markdown("""**Output**  
    ```3```
    """)

with tab2:
    st.markdown("""If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!""")
    st.markdown("""**Example**""")
    st.code("""string = “hello world”
string.split()
    """)
    st.markdown("""**Output**  
    ```['hello', 'world']```
    """)

with tab3:
    st.markdown("""If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.""")
    st.markdown("""**Example**""")
    st.code("""str="hello world!"
a=str[::-1]
print(a)
    """)
    st.markdown("""**Output**  
    ```!dlrow olleh```
    """)

with tab4:
    st.markdown("""This amazing trick will help you merge two dictionaries with just 1 line of code. We just need to use `**` in front of the name of the two dictionaries like below two merge them into a single dictionary:""")
    st.markdown("""**Example**""")
    st.code("""d1 = {“a”: 10, “b”:20}
d2 = {“c”: 30, “d”:40}
d3 = {**d1, **d2}
print(d3)
    """)
    st.markdown("""**Output**  
    ```{'a': 10, 'b': 20, 'c': 30, 'd': 40}```
    """)

with tab5:
    st.markdown("""The `zip()` function in python can make your life a lot easier when working with lists and dictionaries. It is used to combine several lists of the same length.""")
    st.markdown("""**Example**""")
    st.code("""
    colour = ['red', 'yellow', 'green']
    fruits = ['apple', 'banana', 'mango']
    for colour, fruits in zip(colour, fruits):
        print(colour, fruits)
    """)
    st.markdown("""**Output**  
    ```red apple
yellow banana
green mango```
    """)
    st.markdown("""The `zip()` function can also be used for combining two lists into a dictionary. This method can be really helpful while grouping data from the list.
    """)
    st.markdown("""**Example**""")
    st.code("""students = ['Rajesh', 'kumar', 'Kriti']
marks = [87, 90, 88]
dictionary = dict(zip(students, marks))
print(dictionary)
    """)
    st.markdown("""**Output**  
    ```{'Rajesh': 87, 'kumar': 90, 'Kriti': 88}```
    """)

with tab6:
    st.markdown("""If you want to assign some specific values of a list to a variable and all the remaining values to another variable in a list format, you can use the following technique:""")
    st.markdown("""**Example**""")
    st.code("""mylist = [1,2,3,4,5]
a, *b = mylistprint
print("a =", a")
print(”b =", b)
    """)
    st.markdown("""**Output**  
    ```a = 1
b = [2, 3, 4, 5]```
    """)
with tab7:
    st.markdown("""Do you have duplicate items in your list which you want to remove? You can do that with only one line of code using the set() function.""")
    st.markdown("""**Example**""")
    st.code("""mylist = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8, 9]
newlist = set(mylist)
print(newlist)
    """)
    st.markdown("""**Output**  
    ```{1, 2, 3, 4, 5, 6, 7, 8, 9}```
    """)
with tab8:
    st.markdown("""If you need a function that is not very complicated, it can be done easily in one line using **lambda**. They are also called anonymous functions and are used heavily in data science and web development.""")
    st.markdown("""**Example**  
Let’s say you want to write a function to multiply two numbers. Instead of writing a conventional function, you can do that in one line using:
    """)
    st.code("""mul = lambda a, b: a * b
mul(5, 6)
    """)
    st.markdown("""**Output**  
    ```30```
    """)

with tab9:
    st.markdown("""Do you have duplicate items in your list which you want to remove? You can do that with only one line of code using the set() function.""")
    st.markdown("""**Example**""")
    st.code("""a = 100
b = 200
a, b = b, a
print('a = ', a)
print('b = ', b)
    """)
    st.markdown("""**Output**  
    ```a = 200
b = 100```
    """)

with tab10:
    st.markdown("""This python trick is amazing for securing your code with a password. We will use the `getpass()` function from the library `getpass` which encodes your input. This will prevent anyone from running the code without a password. Isn’t that cool!""")
    st.markdown("""**Example**""")
    st.code("""from getpass import getpass
password = getpass(“password: “)
if password == “abcd”:
    print(“welcome strnger!”)
else:
    print(“wrong password”)
    """)
    st.markdown("""**Output**  
    ```password: **** [abcd]
Welcome stranger!
Password: **** [zxcv]
Wrong password```
    """)



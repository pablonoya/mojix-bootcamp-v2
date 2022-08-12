import streamlit as st

st.header('10 Cool Beginner Python Tricks That Will Make Your Life Easier')
st.caption('Simple but effective tips for every python lovers')
st.text("""The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities.

In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.""")

tab1, tab2, tab3 = st.tabs(["1 Walrus operator", "2. Splitting a string", "3. Reversing a string"])

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
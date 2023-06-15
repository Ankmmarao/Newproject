import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import streamlit as st
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
st.title("The New Project Analysis")
from PIL import Image

logo=Image.open(r"C:\Users\India\OneDrive\Pictures\durgamma.png")
st.write(logo)
st.title("PYTHON PROGRAM")
st.sidebar.title("Most Import Books")
names=["1.Python","2.Features of Python","3.Conditional Statements","4.Basic Loops","5.Basic Programs"]
for nam in names:
    st.sidebar.write(nam)
if st.checkbox("1.Click here to ,What is Python"):
    st.write("Python is a general purpose, dynamic, high-level, and interpreted programming language. It supports Object Oriented programming approach to develop applications. It is simple and easy to learn and provides lots of high-level data structures.Python is easy to learn yet powerful and versatile scripting language, which makes it attractive for Application Development.Python's syntax and dynamic typing with its interpreted nature make it an ideal language for scripting and rapid application development.Python supports multiple programming pattern, including object-oriented, imperative, and functional or procedural programming styles.Python is not intended to work in a particular area, such as web programming. That is why it is known as multipurpose programming language because it can be used with web, enterprise, 3D CAD, etc.We don't need to use data types to declare variable because it is dynamically typed so we can write a=10 to assign an integer value in an integer variable.Python makes the development and debugging fast because there is no compilation step included in Python development, and edit-test-debug cycle is very fast.")
if st.checkbox("2.Click Here TO,Features of the Python"):
    st.write("1. Easy to Learn and Use\n2. Expressive Language\n3. Interpreted Language\n4. Cross-platform Language\n5. Free and Open Source\n6. Object-Oriented Language\n7. Extensible\n8. Large Standard Library\n9. GUI Programming Support\n10. Integrated\n11. Embeddable\n12. Dynamic Memory Allocation")
if st.checkbox("3.Click to know the Basic Conditional Statements in Python"):
    st.title("Type-1 IF")
    st.write("The if statement is used to test a specific condition. If the condition is true, a block of code (if-block) will be executed.")
    a = st.number_input("Enter an integer one:", value=0, step=1, format="%d")
    b = st.number_input("Enter an integer Two:", value=0, step=1, format="%d")
    st.write("Example is Biggest of Two")
    st.title("Type-2 IF-Else")
    st.write("The if statement is used to test a specific condition. If the condition is true, a block of code (if-block) will be executed.Otherwise Else Block Will be Executed.")

    a = st.number_input("Enter an integer one1:", value=0, step=1, format="%d")
    b = st.number_input("Enter an integer Two2:", value=0, step=1, format="%d")
    st.write("Example is Biggest of Two")


    if a>b:
        st.write("The A value is Big than B",a)
    else:
        st.write("The B value is Big than A",b)
    st.title("Type-3 Nested-If")
    st.write("In Python, you can use nested if statements to create more complex conditional structures. A nested if statement is an if statement that is nested within another if statement. This allows you to check multiple conditions and execute different blocks of code based on the outcomes. Here's an example:.")

    a = st.number_input("Type an integer one:", value=0, step=1, format="%d")
    b = st.number_input("Type an integer Two:", value=0, step=1, format="%d")
    c = st.number_input("Type an integer Three:", value=0, step=1, format="%d")
    st.write("Example is Biggest of Three")
    if a>b:
        if a>c:
            st.write("The value of A is Big Among Three",a)
        else:
            st.write("The value of C is Big Among Three",c)
    if b>a:
        if b>c:
            st.write("The value of  B is Big Among Three",b)
        else:
            st.write("The value of C is Big Among Three",c)
    st.title("Type-4 if-else-if ladder")
    st.write("The if-else-if ladder, also known as the if-elif-else ladder, is a series of conditional statements that are used to test multiple conditions in a specific order. It allows you to check different conditions sequentially and execute the corresponding block of code associated with the first true condition encountered")
    c = st.number_input("Enters an integer value:", value=0, step=1, format="%d")
    if c<0:
        st.write("The Number is Negative ")
    elif c==0:
        st.write("The Number is Zero") 
    else:
        st.write("The Number is Positive")   
if st.checkbox("4.Click to Know the Basic Loops in the Python"):
    st.title("1.For Loop")
    st.write("for loop: A for loop is used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object. It executes a block of code for each item in the sequence. Here's an example:")
    a = st.number_input("Enter an integers the one:", value=0, step=1, format="%d")
    for i in range(a):
        st.write("The Range for your Number is:",i)
    st.title("2.While Loop")
    st.write("while loop: A while loop repeatedly executes a block of code as long as a given condition is true. It continues iterating until the condition becomes false. ")
    a=st.number_input("Enter  value of the Range you want :",value=0, step=1, format="%d")
    while a>0:
        st.write("The Range is:",a)
        a=a+1
    st.title("3.Loop Controled Statements")
    st.write("Loop control statements: Python provides loop control statements to modify the behavior of loops. Some commonly used control statements include break, continue, and pass. break terminates the loop prematurely, continue skips the rest of the current iteration and moves to the next one, and pass is used as a placeholder when no action is needed in the loop body.")
    st.write("1.Example of Break CONTROL STATEMENT")
    a = st.number_input("Type an integer Range:", value=0, step=1, format="%d")
    for i in range(a):
        st.write("The Range is:",i)
        if i==5:
            break
    st.write("Here the ,whater Number you Enter The Range will be Break for 5 beacusse we are using Break statement")
    st.write("2.Example of Continue CONTROL STATEMENT")
    a = st.number_input("Type an integer Range you want:", value=0, step=1, format="%d")
    for i in range(a):
        st.write("The Range is:",i)
        if i==5:
            continue
        

    st.write("Here the ,whater Number you Enter The Range will be skip iteration for 5 beacusse we are using continue statement ")
    

if st.checkbox("5.Click Here the to perform the Calcultion Operations"):
    a=st.number_input("Enter the value of the a number:")
    b=st.number_input("Enter the value of the b number:")
    c=st.number_input("Enter the One operation in 1.Addition,2.Subtraction,3.Multiplication,4.DEvision:")
    if c==1:
        st.write("The Addition of ",(a+b))
    elif c==2:
        st.write("The Subtraction of ",(a-b))
    elif c==3:
        st.write("The Multiplication of ",(a*b))
    elif c==4:
        st.write("The Devision ",(a/b))
    else:
        st.write("Please nter the proper option")
if st.checkbox("6.Click to Check the Even or Odd Number"):
    g=st.number_input("Enter the value of the One Positive number:")
    if (g%2)==0:
        st.write("The Given Number is Even",g)
    else:
        st.write("The Given Number is Odd",g)
if st.checkbox("7.Click to check the Amstrong Number"):
    num = st.number_input("Enter the value of the one positive number:")
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        st.write((num,"is an Armstrong number"))
    else:
        st.write((num,"is not an Armstrong number"))
if st.checkbox("8.Click to know the palindrome Number"):
    num = st.number_input("Enter the One Positive number:")
    temp = num
    rev = 0
    while(num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    if(temp == rev):
        st.write("This value is a palindrome number!",rev)
    else:
        st.write("This value is not a palindrome number!",rev) 
if st.checkbox("9.Clich Here to Upload CSV file and perform the SOme Quariers on the CSV file"):
    fiel=st.file_uploader("Choose the CSV file:",type=['csv'])
    if fiel is not None:
        df=pd.read_csv(fiel)
        c=pd.DataFrame(df)
    if st.checkbox("1.Click to know the first first 5 rows of the csv file"):
        st.write(df.head())
    if st.checkbox("2.Click to know the indexes of the dataset"):
        st.write(df.index)
    if st.checkbox("3.Click to know the shape of the Dataset"):
        st.write(df.shape)
    if st.checkbox("4.Click to know the Unique data for that perticular column"):
        selected_user = st.selectbox("Select User Column", options=df.columns)
        unique_users = df[selected_user].unique()
        st.write("The Unique Data for your column:",unique_users)
    if st.checkbox("5.Click to impliment Graphical Represantation on different Coluns"):
        selected_user1 = st.selectbox("Select User 1 Column", options=df.columns)
        selected_user2 = st.selectbox("Select User 2 Column", options=df.columns)
        selected_column1 = st.selectbox("Select Column 1", options=df.columns)
        selected_column2 = st.selectbox("Select Column 2", options=df.columns)
        user1_data = df[df[selected_user1] == selected_user1][[selected_user1, selected_column1]]
        user2_data = df[df[selected_user2] == selected_user2][[selected_user2, selected_column2]]
        plt.plot(user1_data[selected_column1], label=selected_user1)
        plt.plot(user2_data[selected_column2], label=selected_user2)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.legend()
        st.pyplot(plt)
    if st.checkbox("6.Click to GET Different Coulmns on the DataSet,would you like to"):
        selected_features = st.multiselect("Select Columns", options=df.columns)
        selected_data = df[selected_features]
        st.dataframe(selected_data)
    if st.checkbox("7.Click Here to Enter the Multiple Features based on your interest and Check it Available or not"):
        def main():
            st.title("Dataset Filtering Example")
            feature1 = st.text_input("Enter Feature 1:")
            feature2 = st.number_input("Enter Feature 2:")
            feature3 = st.selectbox("Choose Feature 3:", df['Feature 3'].unique())

    
            filtered_data = filter_dataset(feature1, feature2, feature3)

    
            st.write("Filtered Data:")
            st.write(filtered_data)
        def filter_dataset(feature1, feature2, feature3):
            filtered_data = df[(df['Feature 1'] == feature1) & (df['Feature 2'] == feature2) & (df['Feature 3'] == feature3)]
            return filtered_data
        if __name__ == '__main__':
            main()
if st.checkbox("10.Click to Check the Prime number or Not"):
    num =st.number_input("Enter an integer:", value=0, step=1, format="%d")
    flag = False
    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        if flag:
            st.write(num, "is not a prime number")
        else:
            st.write(num, "is a prime number")
if st.checkbox("11.Click to Get REquired Table"):
    number = st.number_input("Enter an the integer:", value=0, step=1, format="%d")
    st.write ("The Multiplication Table of: ", number)
    for count in range(1, 11):
        st.write(number, 'x', count, '=', number * count)   
if st.checkbox("12.Click to Know the Different types of functions "):
    st.title("Type-1 Function without Arugument and Return Type")
    st.write("In this type of function in Python, While defining, declaring, or calling them, We won’t pass any arguments to them. This type of function won’t return any value when we call them.")
    def Adding():
        a = st.number_input("Enter an integer one val:", value=0, step=1, format="%d")
        b = st.number_input("Enter an integer Two val:", value=0, step=1, format="%d")
        Sum = a + b
        st.write("After Calling :", Sum)
    Adding()
    st.title("Type-2 Function with no argument and with a Return value")
    st.write("In this type of function in Python, We won’t pass any arguments to it while defining, declaring, or calling it. When we call this type of function, it returns some value.")
    def Multiplication():
        c = st.number_input("Enter an  one number:", value=0, step=1, format="%d")
        d = st.number_input("Enter an  second number:", value=0, step=1, format="%d")
        Multi = c * d
        return Multi
    st.write("After Calling the Multiplication : ", Multiplication())
    st.title("Type-3 Function with argument and No Return value")
    st.write("This program for the type of function in Python allows the user to enter 2 integer values, and then, We are going to pass those values to the user-defined method to Multiply them.")
    def Multiplications(e,f):
        Multi = e * f
        st.write("After Calling the Function:", Multi)
    ab = st.number_input("Enter an  one positive number:", value=0, step=1, format="%d")
    cd = st.number_input("Enter an  second positive number:", value=0, step=1, format="%d")
    Multiplications(ab,cd) 
    st.title("Type-4 Function with argument and Return value")
    st.write("This type of function in the Python program allows the user to enter 2 integer values. Then, we pass those values to the user-defined method to add those values and return the value using the return keyword.")
    def Addition(g,h):
        Sum = g+h
        return Sum
    fg= st.number_input("Enter an positive value-1:", value=0, step=1, format="%d")
    gf = st.number_input("Enter an positive value-2:", value=0, step=1, format="%d")
    st.write("After Calling :", Addition(fg,gf))
if st.checkbox("13.Click to know the Different types of Function Arguments"):
    st.title("Type-1 Default Arguments")
    st.write("A default argument is a kind of parameter that takes as input a default value if no value is supplied for the argument when the function is called. Default arguments are demonstrated in the following instance.")
    def function( n1, n2 = 20 ):
        st.write("number 1 is: ", n1)    
        st.write("number 2 is: ", n2)
    fg1= st.number_input("Enter an a value-1:", value=0, step=1, format="%d")
    function(fg1)
    st.write("Here the one Fealut Arugument")
    st.sidebar.title("Explanation:")
    st.write("The number of Arguments in the Formal Argumets is Two But WHILE calling Function through Actual  parameters is one .So the Defalut Arguments is One")
    fg3= st.number_input("Enter an  value-1:", value=0, step=1, format="%d")
    fg4= st.number_input("Enter an  value-2:", value=0, step=1, format="%d")
    function(fg3,fg4)
    st.write("Here the NO Default Aruments") 

    st.write("The number of Arguments in the Formal Parameters is Two But WHILE calling Function through Actual  parameters is Two .So the Defalut Arguments is Zero")
    st.title("Type-2 Keyword Arguments")
    st.write("A function called's arguments are linked to keyword arguments. When invoking a function with keyword arguments, the user may tell whose parameter value it is by looking at the parameter label.We can remove certain arguments or arrange them in a different order since the Python interpreter will connect the provided keywords to link the values with its parameters. Another way to use keywords to invoke the function() method is as follows:")
    def function( n1, n2 ):
        print("number 1 is: ", n1)    
        print("number 2 is: ", n2)
    st.write( "Without using keyword" )
    function( 50, 30)
    st.write( "With using keyword" )  
    a1= st.number_input("Enter an  value-1 keyword:", value=0, step=1, format="%d")
    a2= st.number_input("Enter an  value-2 keyword:", value=0, step=1, format="%d") 
    function( a1,a2)
    st.title("Type-3 Required Arguments")
    st.write("The arguments given to a function while calling in a pre-defined positional sequence are required arguments. The count of required arguments in the method call must be equal to the count of arguments provided while defining the function.We must send two arguments to the function function() in the correct order, or it will return a syntax error, as seen below.") 
    def function( n1, n2 ):
        st.write("number 1 is: ", n1)    
        st.write("number 2 is: ", n2)    
    st.write( "Passing out of order arguments" )  
    a1= st.number_input("Enter an  value-1 as argumet1:", value=0, step=1, format="%d")
    a2= st.number_input("Enter an  value-2 as argument2:", value=0, step=1, format="%d")   
    function( a1,a2 )       
    st.write( "Passing only one argument" )
    try:
        a3=st.number_input("Enter an  value-2 as argument1:", value=0, step=1, format="%d") 
        function( a3 )
    except:
        st.write( "Function needs two positional arguments" )  
    st.title("Type-4 Variable-Length Arguments")
    st.write("We can use special characters in Python functions to pass as many arguments as we want in a function. There are two types of characters that we can use for this purpose:*args -These are Non-Keyword Arguments**kwargs -These are Keyword Arguments.")
    def function( *args_list ):
        ans = []    
        for l in args_list:
            ans.append( l.upper() )    
            return ans    
   
    object = function('Python', 'Functions', 'tutorial')    
    st.write( object )    
    def function( **kargs_list ):
        ans = []    
        for key, value in kargs_list.items():
            ans.append([key, value])    
            return ans
    object = function(First = "Python", Second = "Functions", Third = "Tutorial")    
    st.write(object)  
    st.title("Type-5 The Anonymous Functions\Lambda Functions")
    st.write("These types of Python functions are anonymous since we do not declare them, as we declare usual functions, using the def keyword. We can use the lambda keyword to define the short, single output, anonymous functions.Lambda expressions can accept an unlimited number of arguments; however, they only return one value as the result of the function. They can't have numerous expressions or instructions in them. Since lambda needs an expression, an anonymous function cannot be directly called to print.")
    lambda_ = lambda argument1, argument2: argument1 + argument2;
    a1= st.number_input("Enter an  value-1 as argumets1:", value=0, step=1, format="%d")
    a2= st.number_input("Enter an  value-2 as arguments2:", value=0, step=1, format="%d") 
    st.write( "Value of the function is : ", lambda_( a1,a2) )
if st.checkbox("15.Click Here to Practice Python After  you Learn"):
    def run_code(code):
        process = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output,error = process.communicate()
        return output, error


    def highlight_code(code):
        return highlight(code, PythonLexer(), HtmlFormatter())


    st.title("Python Interpreter with Streamlit")

    code = st.text_area("Enter Python code", height=250)
    if st.button("Run"):
        output,error = run_code(code)
        if output:
            st.markdown("## Output:")
            st.code(output.decode())
        if error:
            st.markdown("## Error:")
            st.code(error.decode(), language='text')
    if code:
        st.markdown("## Code:")
        st.code(highlight_code(code), language='python')
if st.checkbox("16.Click Here to Complete the Some Python Related Tasks"):
    coding_tasks = [
    {
        "task_description": "Task 1: Write a Python function to calculate the square of a number.",
        "task_solution": """def calculate_square(num):
                                return num ** 2""",
    },
    {
        "task_description": "Task 2: Write a Python program to print the Fibonacci series.",
        "task_solution": """def fibonacci_series(n):
                                if n <= 0:
                                    return []
                                elif n == 1:
                                    return [0]
                                elif n == 2:
                                    return [0, 1]
                                else:
                                    fib = [0, 1]
                                    while len(fib) < n:
                                        fib.append(fib[-1] + fib[-2])
                                    return fib"""
    },
    {
        "task_description": "Task 3: Write a Python class to represent a rectangle.",
        "task_solution": """class Rectangle:
                                def __init__(self, length, width):
                                    self.length = length
                                    self.width = width
                                    
                                def calculate_area(self):
                                    return self.length * self.width
                                    
                                def calculate_perimeter(self):
                                    return 2 * (self.length + self.width)"""
    }
]


    task_index = st.session_state.get('task_index', 0)
    if task_index >= len(coding_tasks):
        st.title("Coding Tasks")
        st.write("Congratulations! You have completed all the tasks.")
    else:
        current_task=coding_tasks[task_index]
        st.title("Coding Tasks")
        st.markdown(current_task['task_description'])
        user_code = st.text_area("Write your code here", height=200)
    if st.button("Submit Code"):
        st.write("Code submitted!")
        st.markdown("Solution:")
        st.code(current_task['task_solution'], language="python")
        task_index += 1
        st.session_state['task_index'] = task_index

    
        
      


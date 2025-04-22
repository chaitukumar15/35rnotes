

# 1 st class function -> function as first class citizen
# 1. function as argument to another function   
# 2. function as return value from another function
# 3. function as variable
# 4. function as data structure element

# copy 
# closure 


# hi i am starting fun 
# hi i am original
# hi i am ending fun





# def decorator(func):
#     def wrapper():
#         print("hi i am starting fun")
#         func()
#         print("hi i am ending fun")
#     return wrapper
# @decorator
# def fun():
#     print("hi i am original")

# # fun=decorator(fun)
# fun()

# a
# c 
# b









# def g(normal):
    
#     def u():
#         print("a")
#         normal()
#         print("b")

#     return u


# def normal():
#     print("c")

# v=g(normal)

# v()



# if True:
#     print("hi")




# def dec(g):
#     def wrapper():
#         print("Chaitanya")
#         print(g())
#         print("Kumar")
#     return wrapper

# def g():
#     return "hi"

# g = dec(g)
# g()







# def f(p):
#     def wrapper():
#         print("cit - chennai")
#         p()
#         print("cit-eee")
#     return wrapper
   

# def namer():
#     print("chaitanya")

# namer=f(namer)

# namer()


# which which is decorated -> 1 st def cheyali
# def namer():
#     print("chaitanya")

#  i need to change the fun -> decorator function
    # 1. need to send our original function to decorator function (using args)
    # args are received in decorator function as parameters
# def decorator(func):
#     def wrapper(n):
#        if n%2==0:
#            print(func(n))
#        else:
#            print("not even")
        
#     return wrapper

# # @decorator
# def square(n):
#     return n**2
# # square=decorator(square)

# square(6)




# def dec_name(param):
#     def wrapper():
#         pass
#     return wrapper



# fun definition -> function name-> function object 

# fun calling / invocation ->calling a function 


# closure -> function inside a function -> inner function -> outer function -> return value of outer function -> inner function object -> closure object -> closure variable -> free variable -> non local variable
# A closure is a function object that has access to variables in its lexical scope even when the function is called outside that scope



def two():
    print("hi i am outer")

def one():    
    print("hi i am inner")

def three():
    print("hi i am inner 2")

# Decorator factory that accepts three functions
def decorator(one, two, three):
    # Actual decorator that receives the function to be wrapped (four)
    def actual_decorator(func):
        def wrapper():
            print("hi i am starting fun")
            one()
            two()
            three()
            func()  # Call the decorated function
            print("hi i am ending fun")
        return wrapper
    return actual_decorator

@decorator(one, two, three)
def four():
    print("hi i am inner 3")

four()

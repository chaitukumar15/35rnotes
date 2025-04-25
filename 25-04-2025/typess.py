

# class breed:
#     def __init__(self,bark):
#         self.bark=bark
    
#     def barking(self):
#         return "hi dog is brking"

# class dog(breed):
#     def __init__(self,bark,model):
#         super().__init__(bark)
#         self.model=model
     
#     def typee(self):
#         return "hi this is dog breeds"


# class cats(breed):
#     def __init__(self,bark,m):
#         super().__init__(bark)
#         self.m=m
     
#     def y(self):
#         return "hi this is cat breeds"



# cat=cats("meow","russian cat")

# print(cat.bark)


# dog=dog("dog barking","lab")


# single 

# class a:
#     def __init__(self,b,c):
#         self.b=b
#         self.c=c
#     def hello(self):
#         return "hi this is b and c"
    

# class b(a):
#     def __init__(self, b, c,d):
#         super().__init__(b, c)
#         self.d=d
#     def helochild(self):
#         return "i hv d"
    

# class c(b):
#     def __init__(self,b,c,d,i):
#         self.i=i;
#         super().__init__(b,c,d)
# # v=b(10,20,30)
#     def h3(self):
#         return "hi this is child 3"
    

# v=c(10,20,30,40)

# print(v.h3())

# print(v.i)

# print(v.hello())

# print(v.b)



# class breed:
#     def __init__(self,bark):
#         self.bark=bark
    
#     def barking(self):
#         return "hi dog is brking"
    
#     def u(self):
#         return "hi am common method in parent1"
    

# class hello:
#     def __init__(self,a,b):
#         self.a=a;
#         self.b=b
#     def g(self):
#         return "hi this is hello"
#     def u(self):
#         return "hi am common method in parent2"
    


# class childd(hello,breed):
#     def __init__(self, bark,a,b,o):
#         breed.__init__(self,bark)
#         hello.__init__(self,a,b)
#         self.o=o

#     def hello123(self):
#         return "this is child method"
    
#     def u(self):
#         return "hi am common method in child mthod"
    

# h=childd("meow",10,20,200)

# print(h.hello123())

# print(h.g())

# print(h.barking())

# print(h.u())



class person:
    def __init__(self,age,name):
        self.name=name
        self.age=age
    

class stuent(person):
    def __init__(self, age, name,student_id,grade):
        super().__init__(age, name)
        self.student_id=student_id
        self.grade=grade
        
    def get_details(self):
        return "hi detaild of student"
    
class teacher(person):
    def __init__(self, age, name,emp_id,sub):
        super().__init__(age, name)
        self.emp_id=emp_id
        self.sub=sub
        
    def get_details(self):
        return "hi detaild of teacher"
    

teacher1=teacher(27,"chaitanya",1,"maths")

studentt=stuent(22,"ramesh",3,"h")


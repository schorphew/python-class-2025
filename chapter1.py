# # a = 5 #integer
# # b = 5.0 #float 
# # c = "Tawan Raizer" #string
# # d = True #Boolean True | False
# # e = 6+5 #complex

# # print(a)
# # print(b)
# # print(c)
# # print(d)
# # print(e)

# # a = 55
# # b = 6.5
# # print(a)
# # print(b)

# # z=a+b #float
# # print(z)


# # #Descriptive name or meaning full name
# # tax = 0.7
# # firstname = "Tawan"
# # email = 'tawan.h@itd.kmutnb.ac.th'
# # age = 18

# # #Multi words variable name
# # # Snake Case
# # Student_First_name = "Tawan"
# # student_last_name = 'Raizer'
# # student_Age = 18
# # Student_Email = "s68xxxxx@email.kmutnb.ac.th"

# # print("Student name :" + Student_First_name)
# # print(f"Student last name : {student_last_name}")

# #datatype
# a = 1 #int
# b = 1.1 #folat
# c = "1" #string

# print(a+a) #2
# print(a+b) #2.2
# print(c+c) #11
# print(a+b) #2.1
# #print(a+c) #error

# print(type(a))
# print(type(b))
# print(type(c))

# #convert type
# a = float(a) #float
# b = int(b)
# c = int(c)
# print(a+c)

#Scope Variable - Global and Local Variable
X = " Awesome" #String

def my_function():
    X = "Fantastic."
    print("Python is" + X)

my_function()
print("Python is" + X)
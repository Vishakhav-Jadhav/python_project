#dictionary
#how to create dictionary
# my_dict={'name':'vish','age':23,}
# print(my_dict)

# ##dict constructor

# person=dict(name="vish",age=12,grade="a")
# print(person)


# #using list of tuple
# per=dict([('name','vish'),('age', 23)])
# print(per)


#dict methods 

# .keys:return  all keys 
# .value(): rerurn all values
# .items(): all key value pair
# .get(): return all values for keys


# student={
#     1:"class x",
#     'name':'vish',
#     'age':23

# }
# print(student.keys())
# print(student.values())
# print(student.items())

# #print(student.get('name))
# ##add operator
# student['email']='vishh@gmail.com'
# print(student)

# #remove
# del student["email"]
# print(student)

# #pop method

# student.pop('age')
# print(student)


# student={
#     1:"class x",
#     'name':'vish',
#     'age':23

# }
# #using for loop

# for keys in student:
#     print(keys)


#     for values in student:
#         print( student[values])

# for keys,values in student.items():
#     print(keys,values)

#nested dictionary

# student={

#     'stu1':
#     {
#         'name':'vish',
#         'age':23,
#         'marks':78
#     },
#     'stu2':{
#        'name':'vish',
#         'age':23,
#         'marks':78
#     }
#     }
# print(student['stu1'])
# print(student['stu1'] ['name'])

# list in python is collection of iteam or element  that are ordered ,mutable ,or allow duplicate values
#most veratile element in python which means we can store multiple values /iteams in one single variable
# l1=["kd",12,3.4,"vuhj"]
# print(l1)
# print(type(l1))
# print(l1[3])
# print(l1[-2])
# #slicing  allow u  to  access range of element
# #list_name[start:stop:step]
# print(l1[1:4]) #one to 3 slicinng 
# print(l1[0:3]) #starting of 2 element
# print(l1[-2:]) #last element 
# print(l1[::2]) #alteranative element 
# print(l1[::-1])# reverse list use -1 step 
#modifying list

#append methos
# l2=["banana","apple","cherry"]
# l2.append("mango")
# print(l2)
#remove method
# l2.remove("apple")
# print(l2)

 #methos 
#  append():add element ate the end of list
# extend(): add multiple element at the end of the add two list one another second
# insert(): insert the elemt at the specific position
# remove():remove the element 
# pop(): remove and return element of specified index
# clear(): remove all element from list
# count(): count  no. of element in list
# sort():sort list ascending and decending order
# reverse():reverse the list   using -1 step
# copy(): return a shallow copy of the list

#extend method
# my_list=["banana",34,3.5,"apple","cherry"]
# print(len(my_list))
# one_more=["appy","mango"]
# my_list.extend(one_more)
# print(my_list)

# insert method
# my_list=["banana",34,3.5,"apple","cherry"]
# my_list.insert(0,"vish")
# print(my_list)

# #remove method
# my_list.remove("vish")
# print(my_list)


#clear method 
# my_list=["baana","apple","cherry"]
# my_list.clear()
# print(my_list)

#finding index
# my_list=["baana","apple","apple","apple"]
# l1=my_list.index("apple")
# print(l1)

#count method
# my_list=["baana","apple","apple","apple"]
# cnt=my_list.count("baana")
# print(cnt)

# reverse method
# my_list=["baana","apple","apple","apple"]
# my_list.reverse()
# print(my_list)

#sorting 

# l5=[12,0.5,67,8,3,2,4]
# l5.sort()
# print(l5)

# #decsending order use reverse keyword=True
# l5.sort(reverse=True)
# print(l5)


#pop
#num=[10,20,60]
# poped=num.pop(0)
# print(poped)
# print(num)

# num=[10,20,60]
# poped=num.pop()
# print(poped)
# print(num)

# #copy method
# my_list=["baana","apple","apple","apple"]
# copy_list=my_list.copy()
# print(copy_list)

#join list
a=[1,2,3,4]
b=["banana","jdfojf"]
concanate=a+b
print(concanate)

for x in b:
    b.append(x)
print(b)  


a.extend(b)
print(a)

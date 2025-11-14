#set 
# unordered
# mutable
# immutable

#creating set operation 
#adding element

# num={1,2,3,4}
# num.add(8)
# print(num)

#removing ement

# fruit={'apple','mango','cherry'}
# fruit.remove('cherry')
# print(fruit)

#methods
#union =combine element from 2 sets
# set1={1,2,3,4,5}
# set2={3,4,5}
# union_set = set1.union(set2)
# print(union_set)

#intersecion:common element
# set1={1,2,3,4,5}
# set2={3,4,5}
# inter_set = set1.intersection(set2)
# print(inter_set)


#difference :element present in 1 set not in 2

# set1={1,2,3,4,5}
# set2={3,4,5}
# diff_set = set1.difference(set2)
# print(diff_set)

#ymmetric_difference
# set1={1,2,3,4,5}
# set2={3,4,5}
# sdiff_set = set1.symmetric_difference(set2)
# print(sdiff_set)


#set iteration

# num={1,2,3,5,6}
# for i in num:
#     print(i)

#set comprehension

sqr={x**3 for x in range(1,6)}
print(sqr)
# st="akki"
# print(st[0])
# print(st[-1])

# a=[0,1,2,3,4,10]
# print(a[0])
# print(a[-1])
# print(len(a))

# print(a[:])

#-------------problem 1----------------
# fruit_list=[]

# for i in range(0,7):
#     user_fruit_list=input("enter fruit name\n")
#     fruit_list.append(user_fruit_list)
# print(fruit_list)



#-------------problem 2-----------------
# marks_of_stu=[]

# for i in range(0,6):
#     marks_each_stu=int(input("enter marks of each student\n"))
#     # marks_each_stu=int(marks_each_stu)
#     marks_of_stu.append(marks_each_stu)
# print(marks_of_stu)
# marks_of_stu.sort()
# print(marks_of_stu)



#-------------problem 3------------------
# tpl=(1,2,3,4,5,6)
# print(tpl[1])
# tpl[1]=1



#--------------problem 4------------------
# lst=[1,5,3,4]
# lst_sum=0
# # lst_sum=lst[1]+lst[0]+lst[2]+lst[3]
# for i in range(0,len(lst)):
#     print(i)
#     lst_sum =lst_sum+lst[i]
# print(lst_sum)



#--------------problem 5------------------
a=(7,0,8,0,0,9)

#-------method 1---------
cut=0
for i in range(0,len(a)):
    if a[i]==0:
        # print(i)
        # print(a[i])
        cut=cut+1
print(cut)

#--------method 2-------
cut=a.count(0)
print(a.count(0))
print(cut)

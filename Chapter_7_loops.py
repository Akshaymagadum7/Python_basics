#-------------------------------p1----------------------------------------------------------
# table_no=int(input("enter a number:- "))

# for i in range(1, 11):
#     val=table_no*i
#     # print(table_no, "*", i, "=", val)
#     print(f"{table_no} X {i} = {val}")  #-----------called f string


# ---------------------------------p2----------------------------------------------
# l1=["harry", "sachin", "soham", "Rahul"]

# for l in l1:
#     if l.startswith("s"):
#         print("Hello", l)
#     # or
#     if l[0]=="s":
#         print("hello", l)


# ----------------------------------p3-------------------------------------------------
table_no=int(input("enter a number:- "))

i=1
while i<=10:
    print(table_no, "X", i, "=", table_no*i)
    i+= 1

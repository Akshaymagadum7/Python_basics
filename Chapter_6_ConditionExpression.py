# input_age=float(input("enter your age:- "))

# if(input_age>=18):
#     print("you can get driver liance")
# else:
#     print("not elgible for liance")



#-------------------problem 1--------------------
# num_list=[]

# for i in range(0,4):
#     user_num=int(input("enter a number:- "))
#     num_list.append(user_num)

# k=num_list[0]
# for j in num_list:
#     # print(j)
#     if k<j:
#         k=j
# print(k)



#--------------------problem 2--------------------
# english=int(input("enter your marks in english:- "))
# maths=int(input("enter yur marks in maths:- "))
# science=int(input("enter your marks in science:- "))

# if english>=33:
#     if maths>=33:
#         if science>=33:
#             total_percent=(((english+maths+science)*100)/300)
#             if total_percent>=40:
#                 print("student passed with - ", total_percent, "%")
#                 # print("student passed with - ", str(total_percent) + "%")
#             else:
#                 print("overall student failed - ", total_percent, "%")
#                 # print("overall student failed - ", str(total_percent) + "%")
#         else:
#             print("student is failed in science")
#     else:
#         print("student failed in maths")
# else:
#     print("student is failed in english")

#_____________________________ better way_________________________

# if english<33 or maths<33 or science<33:
#     print("failed")
# elif (english+maths+science)/3 >=40:
#     print("passed")
# else:
#     print("failed overall")



#-----------------------------problem 3----------------------------
# text=input("enter the comments:-\n")

# if("make a lot of money" in text or "buy now" in text or "subscribe now" in text or "click this" in text):
#     print("its a spam mail")
# else:
#     print("not a spam")



#----------------------------problem 4-----------------------------
# username=input("enter username with less then 10 charecters:-\n")

# if (len(username)>10):
#     print("not allowed- ", len(username))
# else:
#     print(username)


#---------------------------problem 5---------------------------------
# name_list=["akki", "kumar", "monoj", "suresh"]

# ur_name=input("enter ur name:-\n")
# if(ur_name in name_list):
#     print("present")
# else:
#     print("absent")


#__________________________not using "in"_______________________
# dummy=False
# for i in range(0, len(name_list)):
#     if(name_list[i]==ur_name):
#         print("present")
#         dummy=True

# if not dummy:
#     print("not present")


#---------------------------problem 6---------------------------------

# std_mark=int(input("enter your total marks:- "))

# if std_mark >=90 and std_mark<=100:
#     print("EX")
# elif std_mark >=80 and std_mark<90:
#     print("A")
# elif std_mark >=70 and std_mark<80:
#     print("B")
# elif std_mark <70:
#     print("C")       





# ----------Problem 1---------------
# a=input("enter ypur name :-\n ")
# b="Hi"
# c="Good afternoon"

# print(b,a,c)



#----------Problem 2----------------
# letter= '''Dear <|NAME|>,
# you are selected!!
# Date:- <|DATE|>'''

# name=input("enter your name\n")
# date=input("enter date\n")

# letter=letter.replace("<|NAME|>" , name)
# letter=letter.replace("<|DATE|>", date)

# print("\n",letter)



#----------Problem 3 & 4----------------
# letter= '''Dear  <|NAME|>,
# you are selected!!
# Date:- <|DATE|>'''

# print(letter.find("  "))

# letter =letter.replace("  ", "-")
# print(letter)



#-----------problem 5---------------------
massage="Dear Akshay,keep going!!"

massage=massage.replace(",", ",\n\n")
print(massage)
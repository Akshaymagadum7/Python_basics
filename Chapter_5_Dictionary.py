

a={
    "akki":"bhai",
    "marks":100,
    "list":[1,2,3],
    'another':{'a':"-a","b":"-b"},
    1:2,
    #"list":"natak" #------------------------as duplicate keys are not allowed it will replace the value of prvious list as "natak"
    "List":"amazon" #------------------------its case sensitive so this "List" will be considered as new key.

}

print(a)
print(type(a))
print(a["akki"])
print(a["marks"])
print(a["list"])
print(type(a["another"]))
print(type(a["marks"]))
print(type(a["list"]))
print(type(a["akki"]))
print(a['another']['a'])
print(a[1])

a['list']=[4,5]
print(a['list'])

print(a.items())
a.update({'frnd':'kiran'})
print(a)


#---------------problem 1-------------
# hin_dict={
#     'thobda':'face',
#     'hath':'hand',
#     'jahaj':'boat'
# }

# print("options are- ", list(hin_dict.keys()))
# a= input("enter the hindi word- \n")
# #print("meaning of your hindi word is :- ",hin_dict[a]) #--------may lead to keyerror if word entered is not present
# print("meaning of your hindi word is- ", hin_dict.get(a))



#-------------problem 5-----------------
# new_dict={}

# for i in range(0, 4):
#     frnd_name=input("enter your name:-\n")
#     frnd_frouit=input("enter your fav frouit:- ")
#     new_dict.update({frnd_name:frnd_frouit})

# print(new_dict)



#-------------problem 6-----------------
new_set={1,2,3,4,"akki", [1,2,3]}
print(new_set) #----------------------------------error unhashable type 'list'
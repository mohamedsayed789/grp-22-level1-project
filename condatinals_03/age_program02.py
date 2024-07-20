#program to check for person age
#inputs

person_age = input("please enter a no : ")
#convert from string to int ( casting)
person_age = int(person_age)

#processing
#outputs
if person_age > 16:
    print("you are a man")

# elif preson_age >= 11 and person_age <= 16

elif person_age >= 11:
    print("yuo are a boy")

else:
    print("you are a child")



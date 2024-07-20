# show strings functions
print('---- Create and print string ----')
emp_name = 'Yahia Momtaz'
print(emp_name)
print(type(emp_name))

print('-------- upper(), lower() functions -------------')
uper_emp_name = emp_name.upper()
lower_emp_name = emp_name.lower()
print(emp_name)
print(uper_emp_name)
print(lower_emp_name)

print('------ isupper(), islower(), isalpha() functions --- True , False --')
print(uper_emp_name.isupper())
print(lower_emp_name.islower())
print(emp_name.isupper())
print(emp_name.isalpha())
emp_code = '1001' # string
print(emp_code.isdigit())
emp_code = '1001abc' #string
print(emp_code.isalnum())
emp_sign = '+- !@'
print(not emp_sign.isalnum())

print('-------------- endsWith() function -----------------')
file_path = 'c:/mydocuments/egypt.jpg'
file_path = file_path.lower()
if file_path.endswith('pdf'):
    print('it is a book')
elif file_path.endswith('jpg'):
    print('it is a image')
elif file_path.endswith('mp4'):
    print('it is a video')
else:
    print('unknow type')

print('-------------- startswith() function ---------')
emp_mobile = '01521456870'
if emp_mobile.startswith('010'):
    print('it is vodafone number')
elif emp_mobile.startswith('011'):
    print('it is etisalat number')
elif emp_mobile.startswith('012'):
    print('it is orange number')
else:
    print('unknow network')

print('------ in membership --------------')
emp_cv = 'iam a programmer, iam interset jave, python, c++ '
if 'python' or 'jave' in emp_cv:
    print('this is the wanted employee')
else:
    print('this is not the wanted employee')

print('-------------- count function -----------')
emp_cv = 'iam a programmer, iam interset jave, python, c++ '
print(emp_cv.count('python'))

print('---------- index(),  replace() functions |  slicing---------------')
emp_email = 'aly.momtaz.mohamed@gmail.com'
user_name = emp_email[0: emp_email.index( '@' ) ]
print(user_name)
domain_name = emp_email[emp_email.index('@') + 1:]
print(domain_name)
real_name = user_name.replace('.', ' ' )
print(real_name)

print('--------------- Looping :  Loop over letters of string -----------------------')
emp_email = 'yahia.momtaz@gmail.com'
for i in range(len(emp_email)):
    print(emp_email[i])
print('--------------------------------------------')

for letter in emp_email:
    print(letter)

print('------- Split function the String into List of Words -------')
my_courses = 'jave python oracle linux php ccna'
courses_list = my_courses.split()
print(courses_list)
courses_list.reverse()
courses_list.append('networking')
print(courses_list)

print('------ return the list back to string using join() function --------')
new_courses = '-' .join(courses_list)
print(new_courses)




print('---------- strip(), title(), swapcase(), find(), rfind() Self study   -------------------')





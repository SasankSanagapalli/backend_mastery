print('==Student details==')
student={}
i='yes'
while i!='no':
    name=input('enter name:')
    id=int(input('enter id:'))
    email=input('enter email id:')
    student[id]={'name':name,'email':email}
    i=input('do you want to continue(yes/no):').lower
print('==Final Student Dictionary==')
print(student)
     
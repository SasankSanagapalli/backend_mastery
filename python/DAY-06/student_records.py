import csv
while True:
    with open('students.csv','a',newline='') as fcsv:
        content=csv.writer(fcsv)
        content.writerow(['name','age','course'])
        name=input('enter student name:')
        age=int(input('enter age:'))
        course=input('enter course name:')
        content.writerow([name,age,course])
        print('completed')
        choice=int(input('enter 0 for exit:'))
        if choice==0:
            break
    with open('students.csv','r') as fcsv:
        content=fcsv.read()
        print(content)

a,b=int(input('enter 1st number:')),int(input('enter 2nd number: '))
print('1.add\n2.subtract\n3.multiply\n4.divide')
number=int(input('enter your choice:'))
def choice(number):
    if number==1:
        result=add(a,b)
    elif number==2:
        result=subtract(a,b)
    elif number==3:
        result=multiply(a,b)
    elif number==4:
        result=divide(a,b)
    else:
        print('Invlid number!!')
    print(result)
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
choice(number)


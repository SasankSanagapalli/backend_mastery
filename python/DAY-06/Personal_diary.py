def add():
    with open('diary.txt','a') as file:
        entry=input('enter to write')
        file.write(entry+'\n')
def view():
    with open('diary.txt','r') as f:
        content=f.read()
        print('The content:',content)
def menu():
    print('==Welcome to Diary==')
    print('1.Add entry')
    print('2.view diary')
    print('3.Exit')
    choice=int(input('choose an option:\n'))
    return choice
while True:
    choice=menu()
    if choice==1:
        add()
    elif choice==2:
         view()
    elif choice==3:
        print('See you again!')
        break
    else:
        print('Invalid choice.')
 


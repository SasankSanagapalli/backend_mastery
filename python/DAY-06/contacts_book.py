def load_contacts(filename='contacts.txt'):
    contacts={}
    try:
        with open(filename,'r') as f:
            for line in f:
                name,phone=line.strip().split(',')
                contacts[name]=phone
    except FileNotFoundError:
        pass
    return contacts
def save_contacts(contacts,filename='contacts.txt'):
    with open(filename,'a') as f:
         for name, phone in contacts.items():
            f.write(f"{name},{phone}\n")
def add(contacts):
        name=input('enter name:')
        phone=int(input('enter ph.no:'))
        contacts[name]=phone
        save_contacts(contacts)
        print('contact added!')
def search(contacts):
    name=input('enter name to search:')
    if name in contacts:
        print(f'{name} : {contacts[name]}')
    else:
        print('name not found')
def delete(contacts):
    name=input('enter name to delete:')
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print('deleted')
    else:
        print('nae not found.')
def show(contacts):
    if contacts:
        print('=====contacts list=====')
        for name,phone in contacts.items():
            print(f'{name} : {contacts[name]}')
    else:
        print('no contacts vailable.')

def menu():
    contacts=load_contacts()
    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Show Contacts")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add(contacts)
        elif choice == "2":
            search(contacts)
        elif choice == "3":
            delete(contacts)
        elif choice == "4":
            show(contacts)
        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print('invalid choice.try again!!')
if __name__=='__main__':
    menu()
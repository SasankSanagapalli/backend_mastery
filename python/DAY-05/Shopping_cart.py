cart=[]

while True:
    print('1.Add Item\n2.Remove Item\n3.View Cart\n4.Exit')
    choice=int(input('enter:'))
    if choice==1:
        cart.append(input('enter item: '))
        print('Entered')
    elif choice==2:
        item=input('enter item:')
        if item in cart:
            cart.remove(item)
            print('removed\n')
        else:
            print("the cart doesn't the item initially\n")
    elif choice==3:
        print('Cart:',cart)
    elif choice==4:
        print('Thank you.Visit again!!')
        break
    else:
        print('Invalid number')
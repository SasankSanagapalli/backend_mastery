Balance=250000
print('=====INFO=====')
print('1.Deposit')
print('2.Withdraw')
print('3.Check balance')
print('4.Exit')
user_input=int(input('enter your choice:'))
if user_input==1:
    amount=int(input('enter amount to deposit:'))
    if amount<0:
        print('Invalid.enter positive number')
    else:
        Balance+=amount
        print('New balance:',Balance)
if user_input==2:
    amount=int(input('enter amount to withdraw:'))
    if amount>Balance and amount<0:
        print('Insufficient balance.Try again')
    else:
        Balance-=amount
        print('Withdraw amonut=',amount,'\nNew balance=',Balance)
if user_input==3:
    print('Current Balance:',Balance)
if user_input==4:
    print('Thank you.Visit again!!')
    
    

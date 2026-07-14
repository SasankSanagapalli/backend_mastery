balance=10000
num=int(input('choose a number\n1.Deposit\n2.Withdraw\n3.Checkbalance: '))
if num==1:
    deposit_amt=int(input('enter amount to deposit:'))
    balance=balance+deposit_amt
    print('new balance= ',balance)
elif num==2:
    withdraw_amt=int(input('enter amount to withdraw:'))
    if withdraw_amt>balance:
        print('Insufficient amount to withdraw')
    else:
        balance=balance-withdraw_amt
        print('New balance after withdraw: ',balance)
elif num==3:
    print('Balance:',balance)
else:
    print('Invalid number')

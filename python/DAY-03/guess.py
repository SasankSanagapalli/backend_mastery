secret=27
while True:
    guess=int(input('enter guess number:'))
    if guess<secret:
        print('Too low')
    elif guess>secret:
        print('Too high')
    elif guess==secret:
        print('Correct')
        break
    else:
         print('Invalid')
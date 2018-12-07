#Python_Practice02(12/7/thu)
#I  changed "Numbers game"
import random
import sys

while True:
    secret_number = random.randint(1, 20)
    print('Please hit a number from 1 to 20')
    print('１から２０までの数字を当ててください')

    print('You have six chances')
    print('6回チャンスがあります')
    #six roop
    for guesses_taken in range(1,7):
        print('Enter the number')
        print('数字を入力してください')

        guess = int(input())

        if guess < secret_number:
            print('Small number')
            print('小さいです')
        elif guess > secret_number:
            print('Big number')
            print('大きいです')
        else:
            break

    if guess == secret_number:
        print('Congratulations！ You use '+str(guesses_taken)+' times.')
        print('当たり！'+str(guesses_taken)+'回で当たりました')
    else:
        print('Sorry...It is'+str(secret_number)+'')
        print('残念...正解は'+str(secret_number)+'でした')

    print('continue?[Enter y]')
    print('続けますか？[yを入力]')

    word = str(input())
    if word != 'y':
        sys.exit()

#Python_Practice02(12/7/thu)
#I use first time "sys" Sentence
import sys

while True:
    print('終了するにはexitと入力してください')
    print('If you want to finish, Please enter [exit]')
    response = input()
    if response == 'exit':
        sys.exit()
    print(response, 'と入力されました')
    print(response, 'entered')
    

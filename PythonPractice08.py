birthdays = {'アリス':'4/1','ボブ':'12/12'}
while True:
    print('名前を入力してください:(If you want to finish, please [Enter])')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(name +'の誕生日は'+birthdays[name])
    else:
        print(name + 'の誕生日は未登録です')
        print('誕生日を入力してください：◯/◯')
        dbday = input()
        if dbday.isdecimal():
            print('不正')
        else:
            birthdays[name] = dbday
            print('更新しました')

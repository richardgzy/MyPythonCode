plain = 'abcdefghijklmnopqrstuvwxyz'
cipher = 'THEQUICKBROWNFXJMPSVLAZYDG'

message = input('Enter message: ')

'Change message to lower case'

message = message.lower()

for char in message:
    if char in plain:
        position = plain.find(char)
        print (cipher[position], end ='')
    else:
        print(char,end ='')

with open('message.txt') as filp:
    string = filp.read()
    characters = [char for char in string]
    flag = ''

    for index in range(len(characters)):
        if(index % 3 == 0):
            flag += characters[index+2]
        else:
            flag += characters[index-1]

    print(flag)
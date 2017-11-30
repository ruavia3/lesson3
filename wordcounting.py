usr_msg = input("введите предложение:\n")
if usr_msg is None:
    print ("нужно ввести хоть что-то")
else:
    wcounting = (len(usr_msg.split()))
    if wcounting % 2 ==0:
        print (usr_msg + " " + str(wcounting) + " слова")
    else:
        print (usr_msg + " " + str(wcounting) + " слов")
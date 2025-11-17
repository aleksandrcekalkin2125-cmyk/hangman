import random

def hangman ():
    words = ["Электричество","Стол","Чайник","Машина","Дом","Ковёр","Аптека"]
    wrong = 0
    stages = ["",
              "_________      ",
              "|              ",
              "|        |     ",
              "|        0     ",
              "|       /|\    ",
              "|       / \    ",
              "|              ",
              "|              ",
              ]
    number = random.randirt(0,6)
    word = words[number]
    rletters = list (word)
    board = ["__"] * len (word)
    win = False
    print ("Добро пожаловать на казнь!")


    while wrong < len (stages) - 1:
        print("\n")
        msg = "Введите букву: "
        char = input(msg)

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters [cind] = '$'
            print("\n"," ".join(board),"\n","\n","Буква угадана верно, продолжаем :)")
            
        else:
            wrong += 1
            print((" ".join (board)))
            e = wrong + 1
            print("\n".join (stages [0: e]))

        if "__" not in board:
            print ("Вы выиграли! Было загадано слово: ")
            print(" ".join (board))
            win = True
            break

    if not win:
        print("\n".join(stages [0: wrong]))
        print ("Вы проиграли! Было загадано слово: {}.".format (word))
                

hangman ()

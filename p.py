# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 02:07:14 2022

@author: This PC
"""

import pygame, sys
from button import Button
from game import *
import random

pygame.init()

_SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("WORDACHE")

BG = pygame.image.load(
    r"F:\41\Lab\CSE 4110 (Artificial Intelligent lab)\Proposa;\Menu-System-PyGame-main\assets\Background.png")

#global turn
global _word_len
global possible_words
global words
global ss
possible_words = ['blue','word','exit','love','game','image','tired','opium','swine','blood','master','minute','python','violet','rattle']
print(possible_words)
words = possible_words


def minimax(string, str, player, rest):
    if (rest == 0):
        dic[(str, player)] = player
        return int(player);

    if player == 1:
        if (rest >= 2):
            l1 = int(len(str))
            strr1 = str + string[l1:l1 + 1]
            c1 = minimax(string, strr1, 1 - player, rest - 1)
            strr2 = str + string[l1:l1 + 2]
            c2 = minimax(string, strr2, 1 - player, rest - 2)
            dic[(str, player)] = max(c1, c2)
        elif (rest == 1):
            l1 = int(len(str))
            strr1 = str + string[l1:l1 + 1]
            c1 = minimax(string, strr1, 1 - player, rest - 1)
            dic[(str, player)] = c1
    else:
        if (rest >= 2):
            l1 = int(len(str))
            strr1 = str + string[l1:l1 + 1]
            c1 = minimax(string, strr1, 1 - player, rest - 1)
            strr2 = str + string[l1:l1 + 2]
            c2 = minimax(string, strr2, 1 - player, rest - 2)
            dic[(str, player)] = min(c1, c2)
        elif (rest == 1):
            l1 = int(len(str))
            strr1 = str + string[l1:l1 + 1]
            c1 = minimax(string, strr1, 1 - player, rest - 1)
            dic[(str, player)] = c1
    return dic[(str, player)]



def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font(
        r"F:\41\Lab\CSE 4110 (Artificial Intelligent lab)\Proposa;\Menu-System-PyGame-main\assets\font.ttf", size)

def show_board(bb,col):
    white = (255, 255, 255)
    huge_font = pygame.font.Font('freesansbold.ttf', 56)
    gray = (0,0,255)
    for col in range(0, col):
            for row in range(0, 1):
                pygame.draw.rect(_SCREEN, white, [col * 100 + 450, row * 100 + 300, 95, 95], 5, 10)
                piece_text = huge_font.render(bb[row][col], True, gray)
                _SCREEN.blit(piece_text, (col * 100 + 470, row * 100 + 315))
    pygame.display.update()
#

def four(turn):

    # ++++++++++++++++++++++++++++++++++++++  BOX  ++++++++++++++++++++++++++
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    gray = (0,0,255)
    ttt=turn
    # WIDTH = 1250
    # HEIGHT = 720
    # screen = pygame.display.set_mode([WIDTH, HEIGHT])
    global _SCREEN
    pygame.display.set_caption('Wordache')
    board = [[" ", " ", " ", " "]]

    fps = 60
    timer = pygame.time.Clock()
    huge_font = pygame.font.Font('freesansbold.ttf', 56)
    # secret_word = words.WORDS[random.randint(0, len(words.WORDS) - 1)]
    game_over = False
    letters = 0
    turn_active = True
    running = True


    # ++++++++++++++++++++++++++++++++++ choose word ++++++++++++++++++++++++
    temp = []
    for word in words:
        if len(word) == 4:
            temp.append(word)
    choose = random.randint(0, (len(temp) - 1))
    given_string = []
    strn = temp[choose]
    given_string.append(strn)
    rest = 4
    str = ""
    #
    # ++++++++++++++++++++++++++++++++++ choose word ++++++++++++++++++++++++

    while running:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        _SCREEN.fill("black")

        # PLAY_TEXT = get_font(45).render("Let's Play For \"Four\"", True, "Red")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
        # _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_TEXT = get_font(45).render(f"Let's Play For \"Four\"= {given_string[0]}", True, "Red")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
        _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        
        
        pygame.display.update()

        timer.tick(fps)
        
        str=""
        rest=int(len(given_string[0]))
        minimax(given_string[0], str, 1-turn, rest)
        print(dic)

        # check_words()
        for col in range(0, 4):
            for row in range(0, 1):
                pygame.draw.rect(_SCREEN, white, [col * 100 + 450, row * 100 + 300, 95, 95], 5, 10)
                piece_text = huge_font.render(board[row][col], True, gray)
                _SCREEN.blit(piece_text, (col * 100 + 470, row * 100 + 315))

        
        str=""
        string=given_string[0]
        pygame.display.update()
        plo=0
        
        while(1):              
            if(given_string[0]==str):
                if(turn==0):
                    PLAY_TEXT = get_font(45).render(f"Computer wins", True, "Green")
                    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 640))
                    _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                    print("Computer wins")
                else:
                   
                    PLAY_TEXT = get_font(45).render(f"Human wins", True, "Green")
                    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 640))
                    _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                    print("Human wins")
                pygame.display.update()
                PLAY_MOUSE_POS = pygame.mouse.get_pos()
                for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
            elif turn==0:
                ss=""
                lt=letters
                str1=str
                kk1=0
                tt=0
                while(1):
                    #print("MMM")  
                     for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                        if event.type == pygame.TEXTINPUT and turn_active and not game_over:
                            s = event.__getattribute__('text')
                            ss+=s
                            print(ss)
                            str1+=s
                            print(str1)
                            diff=int(len(string))-int(len(str))
                            print(diff)
                            if(int(len(ss))<=diff and int(len(ss))<=2):
                                board[0][lt] = s
                                lt+=1
                                show_board(board,4)
                                ll=int(len(str1))
                                if(str1!=string[0:ll]):
                                    tt=1
                                    PLAY_TEXT = get_font(45).render(f"Wrong input, you loss", True, "Red")
                                    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 640))
                                    _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                                    print("Wrong input")
                                    pygame.display.update()
                                    PLAY_MOUSE_POS = pygame.mouse.get_pos()
                                    for event in pygame.event.get():
                                         if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()
                            else:
                                tt=1
                                PLAY_TEXT = get_font(45).render(f"Invalid lenth", True, "Red")
                                PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 640))
                                _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                                print("Invalid length")
                                pygame.display.update()
                                pygame.time.delay(300)
                                _SCREEN.fill(black)
                                tt=0
                                PLAY_TEXT = get_font(45).render(f"Let's Play For \"Four\"= {given_string[0]}", True, "Red")
                                PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
                                _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                                kk=int(len(ss))
                                ss=""
                                if(kk==1):
                                    lt-=1
                                    board[0][lt] = ''
                                else:
                                    lt-=1
                                    board[0][lt]=''
                                    lt-=1
                                    board[0][lt]=''
                                show_board(board,4)
                                str1=str
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                print("YESSS")
                                if(int(len(ss))==0 and tt==0):
                                    PLAY_TEXT = get_font(45).render(f"First enter value", True, "Red")
                                    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 640))
                                    _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                                    pygame.display.update()
                                    # ++++++++++++++++++++++++++++++
                                    pygame.time.delay(300)
                                    _SCREEN.fill(black)
                                    tt = 0
                                    PLAY_TEXT = get_font(45).render(f"Let's Play For \"Four\"= {given_string[0]}", True,
                                                                    "Red")
                                    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
                                    _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                                    show_board(board, 4)
                                    pygame.display.update()
                                    # ++++++++++++++++++++++++++++++
                                    print("First enter value")
                                    pygame.display.update()
                                elif(tt==0):
                                    kk1=1
                                    print("Enter")
                                    break
                        
                     if(kk1):
                        str=str1
                        letters=lt
                        turn=1-turn
                        break
                #print(f"Event = {event}" )
                
            else:
                ll2=int(len(string))-int(len(str))
                p1=0
                p2=0
                if(ll2>=1):
                    l1=int(len(str))
                    strr1=str+string[l1:l1+1]
                    if(dic[(strr1,turn)]):
                        p1=1
                        print("Computers input: "+string[l1:l1+1])
                        print("The word become: "+strr1)
                        str=strr1
                        board[0][letters] = string[l1:l1+1]
                        letters+=1
                        show_board(board,4)
                if(ll2>=2 and p1==0):
                    l1=int(len(str))
                    strr2=str+string[l1:l1+2]
                    if(dic[(strr2, turn)]):                            
                        p2=1
                        print("Computers input: "+string[l1:l1+2])
                        print("The word become: "+strr2)
                        str=strr2
                        board[0][letters] = string[l1:l1+1]
                        letters+=1
                        board[0][letters] = string[l1+1:l1+2]
                        letters+=1
                        show_board(board,4)
                if(p1==0 and p2==0 and ll2>=1):
                    l1=int(len(str))
                    strr1=str+string[l1:l1+1]
                    print("Computers input: "+string[l1:l1+1])
                    print("The word become: "+strr1)
                    str=strr1
                    board[0][letters] = string[l1:l1+1]
                    letters+=1
                    show_board(board,4)
                turn=1-turn

            # control turn active based on letters
        pygame.display.update()
        if letters == 4:
            turn_active = False
        if letters < 4:
            turn_active = True

            # check if guess is correct, add game over conditions
        pygame.display.update()


        # ++++++++++++++++++++++++++++++++++++++  BOX  ++++++++++++++++++++++++++




def five(turn):

    # ++++++++++++++++++++++++++++++++++++++  BOX  ++++++++++++++++++++++++++
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    gray = (0,0,255)
    ttt=turn
    # WIDTH = 1250
    # HEIGHT = 720
    # screen = pygame.display.set_mode([WIDTH, HEIGHT])
    global _SCREEN
    pygame.display.set_caption('Wordache')
    board = [[" ", " ", " ", " "," "]]

    fps = 60
    timer = pygame.time.Clock()
    huge_font = pygame.font.Font('freesansbold.ttf', 56)
    # secret_word = words.WORDS[random.randint(0, len(words.WORDS) - 1)]
    game_over = False
    letters = 0
    turn_active = True
    running = True


    # ++++++++++++++++++++++++++++++++++ choose word ++++++++++++++++++++++++
    temp = []
    for word in words:
        if len(word) == 5:
            temp.append(word)
    choose = random.randint(0, (len(temp) - 1))
    given_string = []
    strn = temp[choose]
    given_string.append(strn)
    rest = 5
    str = ""
    #
    # ++++++++++++++++++++++++++++++++++ choose word ++++++++++++++++++++++++

    while running:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        _SCREEN.fill("black")

        # PLAY_TEXT = get_font(45).render("Let's Play For \"Four\"", True, "Red")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
        # _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_TEXT = get_font(45).render(f"Let's Play For \"Five\"= {given_string[0]}", True, "Red")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
        _SCREEN.blit(PLAY_TEXT, PLAY_RECT)


        pygame.display.update()

        timer.tick(fps)

        str=""
        rest=int(len(given_string[0]))
        minimax(given_string[0], str, 1-turn, rest)
        print(dic)

        # check_words()
        for col in range(0, 5):
            for row in range(0, 1):
                pygame.draw.rect(_SCREEN, white, [col * 100 + 450, row * 100 + 300, 95, 95], 5, 10)
                piece_text = huge_font.render(board[row][col], True, gray)
                _SCREEN.blit(piece_text, (col * 100 + 470, row * 100 + 315))


        str=""
        string=given_string[0]
        pygame.display.update()
        plo=0

        while(1):
            if(given_string[0]==str):
                if(turn==0):
                    PLAY_TEXT = get_font(45).render(f"Computer wins", True, "Green")
                    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 640))
                    _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                    print("Computer wins")
                else:

                    PLAY_TEXT = get_font(45).render(f"Human wins", True, "Green")
                    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 640))
                    _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                    print("Human wins")
                pygame.display.update()
                PLAY_MOUSE_POS = pygame.mouse.get_pos()
                for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
            elif turn==0:
                ss=""
                lt=letters
                str1=str
                kk1=0
                tt=0
                while(1):
                    #print("MMM")
                     for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if PLAY_RESTART.checkForInput(PLAY_MOUSE_POS):
                                four(ttt)
                            if PLAY_mm.checkForInput(PLAY_MOUSE_POS):
                                main_menu()
                        if event.type == pygame.TEXTINPUT and turn_active and not game_over:
                            s = event.__getattribute__('text')
                            ss+=s
                            print(ss)
                            str1+=s
                            print(str1)
                            diff=int(len(string))-int(len(str))
                            print(diff)
                            if(int(len(ss))<=diff and int(len(ss))<=2):
                                board[0][lt] = s
                                lt+=1
                                show_board(board,5)
                                ll=int(len(str1))
                                if(str1!=string[0:ll]):
                                    tt=1
                                    PLAY_TEXT = get_font(45).render(f"Wrong input, you loss", True, "Red")
                                    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 640))
                                    _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                                    print("Wrong input")
                                    pygame.display.update()
                                    PLAY_MOUSE_POS = pygame.mouse.get_pos()
                                    for event in pygame.event.get():
                                         if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()
                            else:
                                tt=1
                                PLAY_TEXT = get_font(45).render(f"Invalid lenth", True, "Red")
                                PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 640))
                                _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                                print("Invalid length")
                                pygame.display.update()
                                pygame.time.delay(300)
                                _SCREEN.fill(black)
                                tt=0
                                PLAY_TEXT = get_font(45).render(f"Let's Play For \"Five\"= {given_string[0]}", True, "Red")
                                PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
                                _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                                kk=int(len(ss))
                                ss=""
                                if(kk==1):
                                    lt-=1
                                    board[0][lt] = ''
                                else:
                                    lt-=1
                                    board[0][lt]=''
                                    lt-=1
                                    board[0][lt]=''
                                show_board(board,5)
                                str1=str
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                print("YESSS")
                                if(int(len(ss))==0 and tt==0):
                                    PLAY_TEXT = get_font(45).render(f"First enter value", True, "Red")
                                    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 640))
                                    _SCREEN.blit(PLAY_TEXT, PLAY_RECT)

                                    print("First enter value")
                                    pygame.display.update()
                                elif(tt==0):
                                    kk1=1
                                    print("Enter")
                                    break

                     if(kk1):
                        str=str1
                        letters=lt
                        turn=1-turn
                        break
                #print(f"Event = {event}" )

            else:
                ll2=int(len(string))-int(len(str))
                p1=0
                p2=0
                if(ll2>=1):
                    l1=int(len(str))
                    strr1=str+string[l1:l1+1]
                    if(dic[(strr1,turn)]):
                        p1=1
                        print("Computers input: "+string[l1:l1+1])
                        print("The word become: "+strr1)
                        str=strr1
                        board[0][letters] = string[l1:l1+1]
                        letters+=1
                        show_board(board,5)
                if(ll2>=2 and p1==0):
                    l1=int(len(str))
                    strr2=str+string[l1:l1+2]
                    if(dic[(strr2, turn)]):
                        p2=1
                        print("Computers input: "+string[l1:l1+2])
                        print("The word become: "+strr2)
                        str=strr2
                        board[0][letters] = string[l1:l1+1]
                        letters+=1
                        board[0][letters] = string[l1+1:l1+2]
                        letters+=1
                        show_board(board,5)
                if(p1==0 and p2==0 and ll2>=1):
                    l1=int(len(str))
                    strr1=str+string[l1:l1+1]
                    print("Computers input: "+string[l1:l1+1])
                    print("The word become: "+strr1)
                    str=strr1
                    board[0][letters] = string[l1:l1+1]
                    letters+=1
                    show_board(board,5)
                turn=1-turn

            # control turn active based on letters
        pygame.display.update()
        if letters == 5:
            turn_active = False
        if letters < 5:
            turn_active = True

            # check if guess is correct, add game over conditions
        pygame.display.update()


        # ++++++++++++++++++++++++++++++++++++++  BOX  ++++++++++++++++++++++++++


def six(turn):

    # ++++++++++++++++++++++++++++++++++++++  BOX  ++++++++++++++++++++++++++
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    gray = (0,0,255)
    ttt=turn
    # WIDTH = 1250
    # HEIGHT = 720
    # screen = pygame.display.set_mode([WIDTH, HEIGHT])
    global _SCREEN
    pygame.display.set_caption('Wordache')
    board = [[" ", " ", " ", " "," "," "]]

    fps = 60
    timer = pygame.time.Clock()
    huge_font = pygame.font.Font('freesansbold.ttf', 56)
    # secret_word = words.WORDS[random.randint(0, len(words.WORDS) - 1)]
    game_over = False
    letters = 0
    turn_active = True
    running = True


    # ++++++++++++++++++++++++++++++++++ choose word ++++++++++++++++++++++++
    temp = []
    for word in words:
        if len(word) == 6:
            temp.append(word)
    choose = random.randint(0, (len(temp) - 1))
    given_string = []
    strn = temp[choose]
    given_string.append(strn)
    rest = 6
    str = ""
    #
    # ++++++++++++++++++++++++++++++++++ choose word ++++++++++++++++++++++++

    while running:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        _SCREEN.fill("black")

        # PLAY_TEXT = get_font(45).render("Let's Play For \"Four\"", True, "Red")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
        # _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_TEXT = get_font(45).render(f"Let's Play For \"Six\"= {given_string[0]}", True, "Red")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
        _SCREEN.blit(PLAY_TEXT, PLAY_RECT)


        pygame.display.update()

        timer.tick(fps)

        str=""
        rest=int(len(given_string[0]))
        minimax(given_string[0], str, 1-turn, rest)
        print(dic)

        # check_words()
        for col in range(0, 6):
            for row in range(0, 1):
                pygame.draw.rect(_SCREEN, white, [col * 100 + 450, row * 100 + 300, 95, 95], 5, 10)
                piece_text = huge_font.render(board[row][col], True, gray)
                _SCREEN.blit(piece_text, (col * 100 + 470, row * 100 + 315))


        str=""
        string=given_string[0]
        pygame.display.update()
        plo=0

        while(1):
            if(given_string[0]==str):
                if(turn==0):
                    PLAY_TEXT = get_font(45).render(f"Computer wins", True, "Green")
                    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 640))
                    _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                    print("Computer wins")
                else:

                    PLAY_TEXT = get_font(45).render(f"Human wins", True, "Green")
                    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 640))
                    _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                    print("Human wins")
                pygame.display.update()
                PLAY_MOUSE_POS = pygame.mouse.get_pos()
                for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
            elif turn==0:
                ss=""
                lt=letters
                str1=str
                kk1=0
                tt=0
                while(1):
                    #print("MMM")
                     for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                        if event.type == pygame.TEXTINPUT and turn_active and not game_over:
                            s = event.__getattribute__('text')
                            ss+=s
                            print(ss)
                            str1+=s
                            print(str1)
                            diff=int(len(string))-int(len(str))
                            print(diff)
                            if(int(len(ss))<=diff and int(len(ss))<=2):
                                board[0][lt] = s
                                lt+=1
                                show_board(board,6)
                                ll=int(len(str1))
                                if(str1!=string[0:ll]):
                                    tt=1
                                    PLAY_TEXT = get_font(45).render(f"Wrong input, you loss", True, "Red")
                                    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 640))
                                    _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                                    print("Wrong input")
                                    pygame.display.update()
                                    PLAY_MOUSE_POS = pygame.mouse.get_pos()
                                    for event in pygame.event.get():
                                         if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()
                            else:
                                tt=1
                                PLAY_TEXT = get_font(45).render(f"Invalid lenth", True, "Red")
                                PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 640))
                                _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                                print("Invalid length")
                                pygame.display.update()
                                pygame.time.delay(300)
                                _SCREEN.fill(black)
                                tt=0
                                PLAY_TEXT = get_font(45).render(f"Let's Play For \"six\"= {given_string[0]}", True, "Red")
                                PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
                                _SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                                kk=int(len(ss))
                                ss=""
                                if(kk==1):
                                    lt-=1
                                    board[0][lt] = ''
                                else:
                                    lt-=1
                                    board[0][lt]=''
                                    lt-=1
                                    board[0][lt]=''
                                show_board(board,6)
                                str1=str
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                print("YESSS")
                                if(int(len(ss))==0 and tt==0):
                                    PLAY_TEXT = get_font(45).render(f"First enter value", True, "Red")
                                    PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 640))
                                    _SCREEN.blit(PLAY_TEXT, PLAY_RECT)

                                    print("First enter value")
                                    pygame.display.update()
                                elif(tt==0):
                                    kk1=1
                                    print("Enter")
                                    break

                     if(kk1):
                        str=str1
                        letters=lt
                        turn=1-turn
                        break
                #print(f"Event = {event}" )

            else:
                ll2=int(len(string))-int(len(str))
                p1=0
                p2=0
                if(ll2>=1):
                    l1=int(len(str))
                    strr1=str+string[l1:l1+1]
                    if(dic[(strr1,turn)]):
                        p1=1
                        print("Computers input: "+string[l1:l1+1])
                        print("The word become: "+strr1)
                        str=strr1
                        board[0][letters] = string[l1:l1+1]
                        letters+=1
                        show_board(board,6)
                if(ll2>=2 and p1==0):
                    l1=int(len(str))
                    strr2=str+string[l1:l1+2]
                    if(dic[(strr2, turn)]):
                        p2=1
                        print("Computers input: "+string[l1:l1+2])
                        print("The word become: "+strr2)
                        str=strr2
                        board[0][letters] = string[l1:l1+1]
                        letters+=1
                        board[0][letters] = string[l1+1:l1+2]
                        letters+=1
                        show_board(board,6)
                if(p1==0 and p2==0 and ll2>=1):
                    l1=int(len(str))
                    strr1=str+string[l1:l1+1]
                    print("Computers input: "+string[l1:l1+1])
                    print("The word become: "+strr1)
                    str=strr1
                    board[0][letters] = string[l1:l1+1]
                    letters+=1
                    show_board(board,6)
                turn=1-turn

            # control turn active based on letters
        pygame.display.update()
        if letters == 6:
            turn_active = False
        if letters < 6:
            turn_active = True

            # check if guess is correct, add game over conditions
        pygame.display.update()


        # ++++++++++++++++++++++++++++++++++++++  BOX  ++++++++++++++++++++++++++


def HUMAN_AI():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        _SCREEN.fill("black")

        PLAY_TEXT = get_font(60).render("Choose First Player", True, (0,0,128))
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
        _SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_Human = Button(image=None, pos=(640, 300),
                           text_input="HUMAN", font=get_font(50), base_color="Red", hovering_color="Green")

        PLAY_Human.changeColor(PLAY_MOUSE_POS)
        PLAY_Human.update(_SCREEN)
        PLAY_AI = Button(image=None, pos=(640, 460),
                           text_input="AI", font=get_font(50), base_color="Red", hovering_color="Green")

        PLAY_AI.changeColor(PLAY_MOUSE_POS)
        PLAY_AI.update(_SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_Human.checkForInput(PLAY_MOUSE_POS):
                    turn = 0
                    options(turn)
                if PLAY_AI.checkForInput(PLAY_MOUSE_POS):
                    turn = 1
                    options(turn)

        pygame.display.update()


def options(turn):
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        _SCREEN.fill("black")

        OPTIONS_TEXT = get_font(45).render("Select the word length.", True, (0,0,118))
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 160))
        _SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # OPTIONS_BACK = Button(image=None, pos=(640, 500),
        #                     text_input="BACK", font=get_font(50), base_color="Red", hovering_color="Green")
        #
        # OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        # OPTIONS_BACK.update(_SCREEN)
        """ME"""
        OPTIONS_FOUR = Button(image=None, pos=(350, 360),
                              text_input="4", font=get_font(75), base_color="Red", hovering_color="Green")

        OPTIONS_FOUR.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_FOUR.update(_SCREEN)
        OPTIONS_FIVE = Button(image=None, pos=(600, 360),
                              text_input="5", font=get_font(75), base_color="Red", hovering_color="Green")

        OPTIONS_FIVE.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_FIVE.update(_SCREEN)
        OPTIONS_SIX = Button(image=None, pos=(850, 360),
                             text_input="6", font=get_font(75), base_color="Red", hovering_color="Green")
        OPTIONS_SIX.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_SIX.update(_SCREEN)
        OPTIONS_BACK = Button(image=None, pos=(640, 500),
                              text_input="BACK", font=get_font(50), base_color="Red", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(_SCREEN)

        """ME"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    HUMAN_AI()
                if OPTIONS_FOUR.checkForInput(OPTIONS_MOUSE_POS):
                    _word_len = 4
                    four(turn)
                if OPTIONS_FIVE.checkForInput(OPTIONS_MOUSE_POS):
                    _word_len = 5
                    five(turn)
                if OPTIONS_SIX.checkForInput(OPTIONS_MOUSE_POS):
                    _word_len = 6
                    six(turn)


        pygame.display.update()


def main_menu():
    while True:
        _SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("WORDACHE", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 150))

        # PLAY_BUTTON = Button(image=pygame.image.load(
        #     r"F:\41\Lab\CSE 4110 (Artificial Intelligent lab)\Proposa;\Menu-System-PyGame-main\assets\Play Rect.png"),
        #                      pos=(640, 250),
        #                      text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load(
            r"F:\41\Lab\CSE 4110 (Artificial Intelligent lab)\Proposa;\Menu-System-PyGame-main\assets\Play Rect.png"),
                                pos=(640, 340),
                                text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load(
            r"F:\41\Lab\CSE 4110 (Artificial Intelligent lab)\Proposa;\Menu-System-PyGame-main\assets\Quit Rect.png"),
                             pos=(640, 500),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        _SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(_SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    HUMAN_AI()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()





print(
    "Welcome to Wordache Game.")
while (True):
    main_menu()

#
#     turn = ''
#     print("Decide who will be the first player")
#     # turn = input("Press c for computer or h for human to start the game:")
#     # word_len = input("Input your word length choice ")
#     turn = _turn
#     word_len = _word_len
#     temp = []
#     for word in words:
#         if len(word) == int(word_len):
#             temp.append(word)
#     choose = random.choice([0, len(temp) - 1])
#     given_string = []
#     strn = temp[choose]
#     given_string.append(strn)
#     rest = int(word_len)
#     str = ""
#
#     if (turn == 'c'):
#
#         print("Given string is: ", given_string[0])
#
#         minimax(given_string[0], str, 0, rest)
#         decision(given_string[0], str, 1)
#     elif (turn == 'h'):
#
#         print("Given string is: ", given_string)
#
#         minimax(given_string[0], str, 1, rest)
#         decision(given_string[0], str, 0)
#
# print("Good Bye")

#Підключення модуля
from menu_window import *
from main_window import *

from random import choice, shuffle #перемішує елементи списку
from time import sleep
#Клас запитання
class Question():

    def __init__(self, question, answer,wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question            #питання
        self.answer = answer                #
        self.wrong_answer1 = wrong_answer1  #
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

        self.actual = True
        self.attempts = 0
        self.correct = 0

    def got_right(self):
        #змінює статистику, отримавши правильну відповідь
        self.attempts += 1
        self.correct += 1

    def got_wrong(self):
        #змінюємо статистику, отримавши правильну відповідь
        self.attempts += 1
        


q1 = Question('як називається слово робота', 'job', 'boj', 'jib', 'jow')
q2 = Question('Tomorrow')
q3 = Question('')
q4 = Question('')
q5 = Question('')
q6 = Question('')
q7 = Question('')
q8 = Question('')
q9 = Question('')
q10 = Question('')
q11 = Question('')
q12 = Question('')
q13 = Question('')
q14 = Question('')
q15 = Question('')

#Список з перемикачів кнопок та питань
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15]

#функція що оберає запитання зі списку та показує на екрані
def new_question():
    global cur_question
    cur_question = choice(questions) #вибирає рандомне запитання

    lb_Question.setText(cur_question.question) #встановлює текст на віджеті
    lb_Correct.setText(cur_question.answer)

    shuffle(radio_list) #перемішує кнопки

    radio_list[0].setText(cur_question.wrong_answer1) #розміщуємо на них знов питання
    radio_list[1].setText(cur_question.wrong_answer2)
    radio_list[2].setText(cur_question.wrong_answer3) #
    radio_list[3].setText(cur_question.answer)
#функція для відпочинку
def rest():
    main_win.hide()
    n = box_Minutes.value() * 60
    sleep(n)
    main_win.show()
#функція кнопок меню
def show_menu():
    menu_win.show()
    main_win.hide()

def blak_menu():
    menu_win.hide()
    main_win.show()

def clear():
    txt_Question.clear()
    txt_Answer.clear()
    txt_Wrong1.clear()
    txt_Wrong2.clear()
    txt_Wrong3.clear()


btn_Menu.clicked.connect(show_menu)
btn_clear.clicked.connect(clear)
btn_Sleep.clicked.connect(rest)


main_win.show()
app.exec_()

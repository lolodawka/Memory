'''вікно для картки запитання'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])

#----------------------------------------------------------------------------------------------------------
#Створення вікна
#----------------------------------------------------------------------------------------------------------
main_win = QWidget()
main_win.resize(600, 500)             #розмір вікна
main_win.move(300, 300)               #кординати вікна
main_win.setWindowTitle("Питання")    #назва вікна


#----------------------------------------------------------------------------------------------------------
#Створення кнопок
#----------------------------------------------------------------------------------------------------------
btn_Menu = QPushButton('Меню')        # кнопка повернення до основного вікна
btn_Sleep = QPushButton('Відпочити')  # кнопка прибирає вікно та повертає його після закінчення таймеру
btn_OK = QPushButton('Відповісти')    # кнопка відповіді
box_Minutes = QSpinBox()              # введення кількості хвилин
box_Minutes.setValue(30)              # хвилини таймеру
lb_Question = QLabel('')              # текст питання

#----------------------------------------------------------------------------------------------------------
#Створюємо панель - із варіантами відповідей - групуємо
#----------------------------------------------------------------------------------------------------------

RadioGroupBox = QGroupBox("Варіанти відповдей:")  # Створення рамки та варіантів відповідей
RadioGroup = QButtonGroup()                       # Групуємо віджети кнопок

rbtn_1 = QRadioButton('')   # Створюємо віджети
rbtn_2 = QRadioButton('')   # Створюємо віджети
rbtn_3 = QRadioButton('')   # Створюємо віджети
rbtn_4 = QRadioButton('')   # Створюємо віджети

RadioGroup.addButton(rbtn_1)       #Додаємо віджети
RadioGroup.addButton(rbtn_2)       #Додаємо віджети
RadioGroup.addButton(rbtn_3)       #Додаємо віджети
RadioGroup.addButton(rbtn_4)       #Додаємо віджети

#-----------------------------------------------------------------------------------------------------------
#розміщуємо варіанти віповідей у стовпці всередині групи
#-----------------------------------------------------------------------------------------------------------

layout_ans1 = QHBoxLayout()    #вертикальні будуть усередині горизонтального
layout_ans2 = QVBoxLayout()    #вертикальні будуть усередині вертикальної
layout_ans3 = QVBoxLayout()    #вертикальні будуть усередині вертикальної

layout_ans2.addWidget(rbtn_1)    #Дві відповіді у перший стовпець
layout_ans2.addWidget(rbtn_2)    #Дві відповіді у перший стовпець
layout_ans3.addWidget(rbtn_3)    #Дві відповіді у другий стовпець
layout_ans3.addWidget(rbtn_4)    #Дві відповіді у другий стовпець


layout_ans1.addLayout(layout_ans2)     #прив'язуємо перемикачі до однієї горизонтальної направляючої лінії
layout_ans1.addLayout(layout_ans3)     #прив'язуємо перемикачі до однієї горизонтальної направляючої лінії
RadioGroupBox.setLayout(layout_ans1)   #прив'язуємо перемикачі до однієї горизонтальної направляючої лінії

#------------------------------------------------------------------------------------------------------------
#створюємо панель із результатом теста
#------------------------------------------------------------------------------------------------------------

AnsGroupBox = QGroupBox("Результат тесту:")
lb_Result = QLabel('')            # Напис "правильно"/неправильно"
lb_Correct = QLabel('')           # Текст правильної відповіді


                                       #розміщуємо

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()                        #можна приховати віджет


# ----------------------------------------------------------
# Розміщуємо всі віджети у головному вікні:
# ----------------------------------------------------------

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

# розмінюємо на 1 шій лінії (кнопки меню,сну,і надпис)
layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel("хвилин"))

# розмінюємо на 2 шій лінії надпис - питання
layout_line2.addWidget(lb_Question,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

# розмінюємо на 3  тій лінії Рамки
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)
# розмінюємо на 4 тій лінії кнопку відповісти
layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK,stretch=2)
layout_line4.addStretch(1)

# 4 горизонтальні на 1 вертикальну
layout_cards = QVBoxLayout()
layout_cards.addLayout(layout_line1,stretch=1)
layout_cards.addLayout(layout_line2,stretch=2)
layout_cards.addLayout(layout_line3,stretch=8)

layout_cards.addStretch(1)
layout_cards.addLayout(layout_line4,stretch=1)
layout_cards.addStretch(1)
layout_cards.setSpacing(5) # прогалини між вмістом

main_win.setLayout(layout_cards) # передаємо на головне вікно основний макет

main_win.show()
app.exec_()




from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])

main_win = QWidget()
main_win.resize(400,300)
main_win.setWindowTitle("Меню")
main_win
#Створюємо вікно

txt_Question = QLineEdit("")
txt_Answer = QLineEdit("")
txt_Wrong1 = QLineEdit("")
txt_Wrong2 = QLineEdit("")
txt_Wrong3 = QLineEdit("")

layout_from = QFormLayout()
layout_from.addRow("Введіть запитання: ", txt_Question)
layout_from.addRow("Введіть вірну відповідь: ",txt_Answer )
layout_from.addRow("Введіть першу хибну відповідь ",txt_Wrong1 )
layout_from.addRow("Введіть другу хибну відповідь  ",txt_Wrong2 )
layout_from.addRow("Введіть третю хибну відповідь  ",txt_Wrong3 )

btn_add_q = QPushButton("Додати запитання")
btn_back = QPushButton("Назад")
btn_clear = QPushButton("Очистити")

lbl_statistics = QLabel("")
lbl_statistics = QLabel("Статистика:\nПравильних відповідей: 0\nЗагальна кількість спроб: 0")

hbtn = QHBoxLayout()
hbtn.addWidget(btn_back)
hbtn.addWidget(btn_add_q)
hbtn.addWidget(btn_clear)

vline = QVBoxLayout()
vline.addLayout(layout_from)
vline.addLayout(hbtn)
vline.addWidget(lbl_statistics) #Додаємо його на макет

main_win.setLayout(vline)

main_win.show()
app.exec_()














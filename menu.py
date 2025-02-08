from PyQt5.QtWidgets import (QWidget, QLineEdit,
                             QPushButton, QVBoxLayout, QApplication)
from data import data



def show_menu():
    global window_menu, lines
    lines=[]
    def save_data():
        global lines
        print(lines)
        try:
            data.append(
                {
                    'question': lines[0].text(),
                    'right_answer': lines[1].text(),
                    'wrong_answers': [lines[2].text(), lines[3].text(), lines[4].text()]
                }
            )
            window_menu.close()
        except Exception as e:
            print(e)

    window_menu = QWidget()
    window_menu.setWindowTitle('Створення нового питання')

    v_line = QVBoxLayout()


    hints=["Питання", "Правильна відповідь", "Неправильна відповідь",
           "Неправильна відповідь", "Неправильна відповідь"]
    for i in range(5):
        lines.append(QLineEdit())

    btn_save = QPushButton('Зберегти питання')

    for line in lines:
        v_line.addWidget(line)
    for i in range(len(lines)):
        lines[i].setPlaceholderText(hints[i])

    v_line.addWidget(btn_save)
    window_menu.setLayout(v_line)

    btn_save.clicked.connect(save_data)
    window_menu.show()
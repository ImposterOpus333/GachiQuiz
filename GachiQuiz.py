from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QGroupBox, QPushButton, QMessageBox, QHBoxLayout, QLabel, QRadioButton, QVBoxLayout
import random

app = QApplication([])
main_win = QWidget()
loser_win = QWidget()
mode_selection = QWidget()
mode_selection.setWindowTitle('Выберите режим:')
practice = QPushButton('Гачи тренировка')
test = QPushButton('Гачи борьба')
btfs = QHBoxLayout()
t = QLabel('Выберите режим')
another_layout = QVBoxLayout()
btfs.addWidget(practice, alignment= Qt.AlignCenter)
btfs.addWidget(test, alignment= Qt.AlignCenter)
another_layout.addWidget(t, alignment= Qt.AlignCenter)
another_layout.addLayout(btfs)
mode_selection.setLayout(another_layout)
mode = False
def lightmode():
    global mode
    mode_selection.hide()
    mode = False
    main_win.show()
def hardmode():
    global mode
    mode_selection.hide()
    mode = True
    main_win.show()
practice.clicked.connect(lightmode)
test.clicked.connect(hardmode)
wrong_answers = []
text = QLabel('')
v1 = QRadioButton('')
v2 = QRadioButton('')
v3 = QRadioButton('')
v4 = QRadioButton('')
v_line = QVBoxLayout()
d_line = QHBoxLayout()
d_line2 = QHBoxLayout()
d_line3 = QHBoxLayout()
radiobox = QGroupBox()
d_line3.addWidget(
    text, alignment = Qt.AlignCenter
)
d_line.addWidget(
    v1,alignment = Qt.AlignCenter
)
d_line.addWidget(
    v2,alignment = Qt.AlignCenter
)
d_line2.addWidget(
    v3,alignment = Qt.AlignCenter
)
d_line2.addWidget(
    v4,alignment = Qt.AlignCenter
)
vv = QVBoxLayout()
vv.addLayout(d_line)
vv.addLayout(d_line2)
radiobox.setLayout(vv)
v_line.addLayout(
    d_line3, stretch = 12
)
v_line.addWidget(radiobox)
r = QButtonGroup()
r.addButton(v1)
r.addButton(v2)
r.addButton(v3)
r.addButton(v4)
c = None
crct = 0
progress = 0
def choose1():
    global c
    c = v1.text()
def choose2():
    global c
    c = v2.text()
def choose3():
    global c
    c = v3.text()
def choose4():
    global c
    c = v4.text()
progress = 0
def answer():
    global progress, c, v_line, text, main_win, v1, v2, v3, v4, wrong_answers, crct
    loser = QMessageBox()
    if mode:
        if c == None:
            pass
        else:
            if c == asks[progress].correct:
                progress += 1
                crct += 1
                c = None
                if progress == len(asks):
                    loser.setText('Поздравляем! Вы получаете 300 bucks')
                    loser.show()
                    loser.exec_()
                    print(0/0)
                else:
                    r.setExclusive(False)
                    v1.setChecked(False)
                    v2.setChecked(False)
                    v3.setChecked(False)
                    v4.setChecked(False)
                    r.setExclusive(True)
                    asks[progress].start()
            else:
                    L = QLabel(asks[progress].failtext)
                    ctr = QLabel('Отвечено на вопросов правильно: ' + str(progress))
                    ohno = QVBoxLayout()
                    ohno.addWidget(L, alignment= Qt.AlignCenter)
                    ohno.addWidget(ctr, alignment= Qt.AlignCenter, stretch= 3)
                    loser_win.resize(200,200)
                    loser_win.setWindowTitle('Oh shit! I am sorry')
                    loser_win.setLayout(ohno)
                    loser_win.show()
                    main_win.hide()
    else:
        if c == None:
            pass
        else:
            if c == asks[progress].correct:
                crct += 1
 
            else:
                wa = QLabel(asks[progress - 1].ask)
                wrong_answers.append(wa)
            c = None
            progress += 1
            print(progress)
            if progress == len(asks):
                L = QLabel('Тренировка окончена')
                ctr = QLabel('Отвечено на вопросов правильно: ' + str(crct) + ' из ' + str(len(asks)))
                note = QLabel('Вы неправильно ответили на следующие вопросы:')

                ohno = QVBoxLayout()
                ohno.addWidget(L, alignment= Qt.AlignCenter)
                if len(wrong_answers) > 0:
                    ohno.addWidget(note, alignment= Qt.AlignCenter)
                for wrong_answer in wrong_answers:
                    ohno.addWidget(wrong_answer, alignment= Qt.AlignCenter)
                ohno.addWidget(ctr, alignment= Qt.AlignCenter, stretch= 3)
                print('Статистика:', str(round((crct/len(asks))*100,2)) + '%')
                loser_win.resize(200,200)
                loser_win.setWindowTitle('Oh shit! I am sorry')
                loser_win.setLayout(ohno)
                loser_win.show()
                main_win.hide()
            else:
                r.setExclusive(False)
                v1.setChecked(False)
                v2.setChecked(False)
                v3.setChecked(False)
                v4.setChecked(False)
                r.setExclusive(True)
                asks[progress].start()

main_win.setWindowTitle('Конкурс от Crazy Dicks')
main_win.resize(400,400)
mode_selection.show()
yes = QPushButton('Ответить')
v_line.addWidget(
    yes, alignment = Qt.AlignCenter
)
no = QPushButton('Нет')
main_win.setLayout(v_line)
class Ask():
    def __init__(self, ask, answers, correct):
        self.ask = ask
        self.answers = answers
        self.correct = correct
        self.failtext = 'NOT!\nВы получаете SIX HOT LOADS!'
    
    def start(self):
        global text, v1,v2,v3,v4,yes
        block = [self.answers[0], self.answers[1], self.answers[2], self.answers[3]]
        random.shuffle(block)
        text.setText(self.ask)
        for v in v1,v2,v3,v4:
            k = random.choice(block)
            v.setText(k)
            block.remove(k)
        yes.clicked.connect(answer)
        v1.clicked.connect(choose1)
        v2.clicked.connect(choose2)
        v3.clicked.connect(choose3)
        v4.clicked.connect(choose4)
    #создание элементов интерфейса
ask1 = Ask(
    'В каком году Billy получил золотую latex glove от Nico-Nico?',
    ['2005','2010','2015','2020'],
    '2010',
)
ask2 = Ask(
    'Как зовут Босса Качалки?',
    ['Van Darkholme','Mark Wolff','Billy Herrington','Slave'],
    'Mark Wolff',
)
ask3 = Ask(
    'Сколько  bucks стоит Fisting?',
    ['300','1000','50','3000'],
    '300'
)
ask4 = Ask(
    'Как Босс Качалки назвал вторженца из клуба кожевников?',
    ['College boy', 'slave', 'leatherman', 'dungeon master'],
    'leatherman'
)
ask5 = Ask(
    'Как называется эпизод, где Билли Херрингтон играл шефа?',
    ['College boy', 'Дедовщина в армии', 'Босс качалки', 'Бойзбенд'],
    'Дедовщина в армии'
)
ask6 = Ask(
    'Какую фразу сказал Стив, встретив незнакомца с фразой "Oh shit! I am sorry"?',
    ['Sorry for what?', 'It is okay man', 'Fuck you', 'Our daddy told us not to be ashamed about dicks'],
    'Дедовщина в армии'
)
asks = [ask1,ask2,ask3,ask4,ask5,ask6]
random.shuffle(asks)
asks[progress].start()
app.exec_()
#расположение виджетов по лэйаутам

#обработка нажатий на переключатели
 
#отображение окна приложения 
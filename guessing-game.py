import random
import speech_recognition as sr
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor

class GuessingGame(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.chances = 10
        self.number = None
        self.initUI()
        
        self.setWindowIcon(QtGui.QIcon('icone.png'))
        
        self.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: white;
            }
            QPushButton {
                background-color: #00bfff;
                color: white;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
            }
            QLineEdit {
            font-size: 22px;
            font-weight: bold;
            background-color: #e6e6e6;
            border-radius: 5px;
            padding: 5px;
            color: black;
            }

        """)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(10, 161, 221))
        self.setPalette(p)

    def initUI(self):
        self.setWindowTitle('Jogo de Adivinhação')
        self.setGeometry(800, 400, 600, 400)
        
        self.label = QtWidgets.QLabel('Pense em um número de 0 a 100', self)
        self.label.setGeometry(QtCore.QRect(130, 120, 400, 30))

        self.button = QtWidgets.QPushButton('Falar', self)
        self.button.setGeometry(QtCore.QRect(230, 170, 120, 30))
        self.button.clicked.connect(self.speak)

        self.restart_button = QtWidgets.QPushButton('Reiniciar', self)
        self.restart_button.setGeometry(QtCore.QRect(230, 210, 120, 30))
        self.restart_button.clicked.connect(self.restart_game)
        self.restart_button.setDisabled(True)

        self.textbox = QtWidgets.QLineEdit(self)
        self.textbox.setGeometry(QtCore.QRect(230, 270, 120, 60))
        self.textbox.setReadOnly(True)

        self.score_label = QtWidgets.QLabel(self)
        self.score_label.setGeometry(QtCore.QRect(440, 40, 150, 30))
        self.score_label.setStyleSheet("font-weight: bold; color: white; font-size: 20px;")
        self.update_score_label()

        self.chances_label = QtWidgets.QLabel(self)
        self.chances_label.setGeometry(QtCore.QRect(20, 40, 150, 30))
        self.chances_label.setStyleSheet("font-weight: bold; color: white; font-size: 20px;")
        self.update_chances_label()

        self.show()

    def start_game(self):
        self.number = random.randint(0, 100)
        self.chances = 10
        self.update_chances_label()
        self.textbox.clear()
        self.label.setText('Pense em um número de 0 a 100')
        self.button.setDisabled(False)

    def update_score_label(self):
        self.score_label.setText(f'Pontuação: {self.score}')

    def update_chances_label(self):
        self.chances_label.setText(f'Chances restantes: {self.chances}')

    def speak(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                guess = int(r.recognize_google(audio, language='pt-BR'))
                self.chances -= 1
                self.update_chances_label()
                if guess < self.number:
                    self.label.setText('O número é maior')
                    self.label.setGeometry(QtCore.QRect(200, 120, 400, 30))
                elif guess > self.number:
                    self.label.setText('O número é menor')
                    self.label.setGeometry(QtCore.QRect(200, 120, 400, 30))
                else:
                    self.score += self.chances
                    self.update_score_label()
                    self.label.setText(f'Você acertou! Sua pontuação é {self.score}')
                    self.label.setGeometry(QtCore.QRect(133, 120, 400, 30))
                    self.button.setDisabled(True)
                    self.restart_button.setEnabled(True)
                    return
                self.textbox.setText(str(guess))
                if self.chances == 0:
                    self.label.setText(f'Você perdeu! O número era {self.number}')
                    self.label.setGeometry(QtCore.QRect(133, 120, 400, 30))
                    self.button.setDisabled(True)
                    self.restart_button.setEnabled(True)
            except sr.UnknownValueError:
                self.label.setText('Não entendi, tente novamente')
                self.label.setGeometry(QtCore.QRect(135, 120, 400, 30))
            except ValueError:
                self.label.setText('Por favor, fale um número válido')
                self.label.setGeometry(QtCore.QRect(135, 120, 400, 30))
   
    def restart_game(self):
        self.start_game()
        self.update_score_label()
        self.update_chances_label()
        self.button.setEnabled(True)
        self.restart_button.setEnabled(False)
        
    def update_score_label(self):
        self.score_label.setText(f'Pontuação: {self.score}')
        
    def update_chances_label(self):
        self.chances_label.setText(f'Chances: {self.chances}')

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    game = GuessingGame()
    game.restart_game()
    app.exec_()
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QSplitter, QVBoxLayout, QDialog, QPushButton, QApplication, QTextEdit, QLineEdit
import socket
from threading import Thread

tcpClientA = None


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.flag=0
        self.btnSend = QPushButton("Start", self)
        self.btnSend.resize(480, 30)
        self.btnSendFont = self.btnSend.font()
        self.btnSendFont.setPointSize(15)
        self.btnSend.setFont(self.btnSendFont)
        self.btnSend.move(10, 460)
        self.btnSend.setStyleSheet("background-color: #F7CE16")
        self.btnSend.clicked.connect(self.send)

        self.chatBody = QVBoxLayout(self)

        splitter = QSplitter(QtCore.Qt.Vertical)

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)

        splitter.addWidget(self.chat)
        splitter.setSizes([400, 100])

        splitter2=QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter)
        splitter2.addWidget(self.btnSend)
        splitter2.setSizes([200, 10])

        self.chatBody.addWidget(splitter2)

        self.setWindowTitle("Chat Application")
        self.resize(500, 500)

    def send(self):

        textFormatted = '{:>80} start'
        self.chat.append(textFormatted)
        tcpClientA.send('start'.encode())


# that is where we get data from server
class ClientThread(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.window = window

    def run(self):
        host = 'localhost'
        port = 8080
        BUFFER_SIZE = 4096
        global tcpClientA
        tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpClientA.connect((host, port))

        data =tcpClientA.recv(BUFFER_SIZE)
        window.chat.append(data.decode("utf-8"))

        while True:
            data = tcpClientA.recv(BUFFER_SIZE)
            window.chat.append(data.decode("utf-8"))

        tcpClientA.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    clientThread = ClientThread(window)
    clientThread.start()
    window.exec()
    sys.exit(app.exec_())


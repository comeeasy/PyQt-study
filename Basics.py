import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

class MyApp1(QWidget):
    '''
        Example 1 창 띄우기
    '''

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 400)
        self.show()

from PyQt5.QtGui import QIcon
class MyApp2(QWidget):
    '''
        Example 2 Application에 icon넣기
    '''
    def __init__(self):
        super(MyApp2, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('icons/016-neutron.png'))
        self.setGeometry(300, 300, 300, 200)
        self.show()

class MyApp3(QWidget):
    '''
    Example 3 창 닫기

    창을 닫는 가장 간단한 방법은 타이틀바의 오른쪽(Windows)또는 왼쪽(macOS)'X' 버튼을 클릭하는 것
    이번에는 프로그래밍을 통해 창을 닫느 법을 알아보겠습니다.
    Signal, Slot에 대해서도 간단하게 다룸
    '''

    def __init__(self):
        super(MyApp3, self).__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Quit', self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('Quit Button')
        self.setGeometry(300, 300, 300, 200)
        self.show()

# import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont

class MyApp4(QWidget):
    '''
        Example 4 Tooltip 나타내기
        - 툴팁은 어떤 위젯의 기능을 설명하는 등의 역할을 하는 말풍선 형태의 도움말이다.
        - 위젯에 있는 모든 구성 요소레 대해서 툴팁이 나타나도록 할 수 있습니다.
        - 이번에는 setToolTip() method를 이용해서 위젯에 툴팁을 만들어 본다.
    '''

    def __init__(self):
        super(MyApp4, self).__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setWindowTitle('Tooltips')
        self.setGeometry(300, 300, 300, 200)
        self.show()

from PyQt5.QtWidgets import QMainWindow
class MyApp5(QMainWindow):
    '''
        Example 5 status bar 만들기

        Main window는 menu bar, tool bar, status bar를 갖는 전형적인 어플리케이션 창이다.

        - Main window는 QMenuBar, QToolBar, QDockWidget, QStatusBar를 위한 고유의 layout이 존재함
        - 가운데 중심 위젯 Central widget을 위한 영역도 있다. 여기엔 어떠한 위젯도 들어올 수 있음.

        아래 예제는 status bar에 'READY'라는 상태를 띄우는 예제다.
    '''

    def __init__(self):
        super(MyApp5, self).__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('READY')

        self.setWindowTitle('Status bar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

from PyQt5.QtWidgets import QAction, qApp
class MyApp6(QMainWindow):
    '''
        Example 6 menubar 만들기

        - GUI application애서 menubar는 흔하게 사용된다.
        - 다양한 명령들의 모임이 메뉴바에 위치한다.
        - mac에서는  menubar.setNativeMenuBar(False)를 추가하여 예제와 같은 결과를 얻는다.
    '''

    def __init__(self):
        super(MyApp6, self).__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('icons/png/007-bat.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&Holy')
        filemenu.addAction(exitAction)

        self.setWindowTitle('Menu bar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

class MyApp7(QMainWindow):
    '''
        Example 7 Toolbar 만들기

        - menu가 app에서 사용되는 모든 명령의 모음이라면, toolbar는 자주 사용하는 명령들을 더 편리하게 사용할 수 있도록 해준다.
        - 폴더 안에 툴바의 각 기능에 해당하는 아이콘들을 저장해 둡니다.
    '''

    def __init__(self):
        super(MyApp7, self).__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('icons/png/007-bat.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit app')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

from PyQt5.QtWidgets import QDesktopWidget

class MyApp8(QMainWindow):
    '''
        Example 8 창을 화면의 가운데로
    '''

    def __init__(self):
        super(MyApp8, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('center')
        self.resize(500, 350)
        self.center() # 창이 화면의 가운데에 위치하게 된다.
        self.show()

    def center(self):
        qr = self.frameGeometry() # 창의 위치와 크기 정보를 가져온다.
        cp = QDesktopWidget().availableGeometry().center() # 사용하는 모니터 화면의 가운데 위치를 파악 후 cp(center point) return
        qr.moveCenter(cp) # 창의 직사각형 위치를 위에서 받아왔던 cp로 이동한다.

from PyQt5.QtCore import QDate, Qt
class MyApp9(QMainWindow):
    '''
        Example 9 날짜와 시간 표시하기

        - QtCore 모듈의 QDate, QTime, QDataTime class를 이용하여 app에 날짜와 시간을 표시할 수 있습니다.
    '''

    def __init__(self):
        super(MyApp9, self).__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle('Date')
        self.resize(300, 200)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

from PyQt5.QtWidgets import QLabel, QVBoxLayout
class MyApp10(QWidget):
    '''
        Example 10 스타일 꾸미기

        - setStyleSheet() 을 이용하면 app 안의 다양한 구성 요소들의 스타일을 자유롭게 꾸밀 수 있다.
    '''

    def __init__(self):
        super(MyApp10, self).__init__()
        self.initUI()

    def initUI(self):
        lbl_red = QLabel('Red')
        lbl_green = QLabel('Green')
        lbl_blue = QLabel('Blue')

        # lbl_red.setStyleSheet('color: red;'
        #                       'border-style: solid;'
        #                       'border-width: 2px;'
        #                       'border-color: #FA8072;'
        #                       'border-radius: 3px;')
        # lbl_green.setStyleSheet('color: green;'
        #                         'background-color: #7FFFD4;')
        # lbl_blue.setStyleSheet('color: blue;'
        #                        'background-color: #87CEFA;'
        #                        'border-style: dashed;'
        #                        'border-width: 3px;'
        #                        'border-color: #1E90FF;')

        lbl_red.setStyleSheet("color: red;"
                              "border-style: solid;"
                              "border-width: 2px;"
                              "border-color: #FA8072;"
                              "border-radius: 3px")
        lbl_green.setStyleSheet("color: green;"
                                "background-color: #7FFFD4")
        lbl_blue.setStyleSheet("color: blue;"
                               "background-color: #87CEFA;"
                               "border-style: dashed;"
                               "border-width: 3px;"
                               "border-color: #1E90FF")

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)

        self.setLayout(vbox)

        self.setWindowTitle('StyleSheet')
        self.resize(300, 200)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp10()
    sys.exit(app.exec_())
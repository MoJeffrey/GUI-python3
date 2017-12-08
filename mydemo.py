#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/10 上午11:27
# @Author  : hukezhu
# @Site    :
# @File    :
# @Software: PyCharm

import leancloud
import test1
import sys
from PyQt5 import QtWidgets
from test1 import Ui_MainWindow

class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setupUi(self)

    def submit(self):


        string = ''
        if self.tabWidget.currentIndex() == 0:
            todo = Todo()
            if len(self.lineEdit_14.text()) != 0 :
                if self.lineEdit_14.text() == 'iOS':
                    todo = iOS()
                elif self.lineEdit_14.text() == 'Android':
                    todo = Android()
                elif self.lineEdit_14.text() == 'Python':
                    todo = Python()
                elif self.lineEdit_14.text() == 'Java':
                    todo = Java()
                elif self.lineEdit_14.text() == 'C':
                    todo = C()
            string = '%s\n\n\n问答题:\n\n 问题:  %s \n\n 答案:    %s' %(self.lineEdit_14.text(),self.lineEdit.text(),self.textEdit.toPlainText())
            if len(self.lineEdit.text()) == 0:
                self.statusbar.showMessage('内容为空,不允许提交', msecs=0)
                return
            self.textBrowser.setPlainText(string)
            todo.set('questiontype', 5)
            todo.set('questiontype_text','问答题')
            todo.set('question', self.lineEdit.text())
            todo.set('questiondescribe', self.textEdit.toPlainText())
        elif self.tabWidget.currentIndex() == 1:
            todo = Todo()
            if len(self.lineEdit_14.text()) != 0 :
                if self.lineEdit_14.text() == 'iOS':
                    todo = iOS()
                elif self.lineEdit_14.text() == 'Android':
                    todo = Android()
                elif self.lineEdit_14.text() == 'Python':
                    todo = Python()
                elif self.lineEdit_14.text() == 'Java':
                    todo = Java()
                elif self.lineEdit_14.text() == 'C':
                    todo = C()
            print('现在选择的是选择题')
            string = '%s\n\n\n选择题:\n\n 问题:  %s \n\n 选项:    \n\n    %s\n    %s\n    %s\n    %s\n    %s \n\n问题描述:\n\n%s' %(self.lineEdit_14.text(),self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text(),self.lineEdit_5.text(),self.lineEdit_6.text(),self.lineEdit_7.text(),self.textEdit_2.toPlainText())
            if len(self.lineEdit_2.text()) == 0:
                self.statusbar.showMessage('内容为空,不允许提交', msecs=0)
                return

            # 判断输入的选项内容是否为空,这个做法好low #
            tkselectset = []
            if len(self.lineEdit_3.text()) != 0:
                tkselectset.append('A.' + self.lineEdit_3.text())
            if len(self.lineEdit_4.text()) != 0:
                tkselectset.append('B.' + self.lineEdit_4.text())
            if len(self.lineEdit_5.text()) != 0:
                tkselectset.append('C.' + self.lineEdit_5.text())
            if len(self.lineEdit_6.text()) != 0:
                tkselectset.append('D.' + self.lineEdit_6.text())
            if len(self.lineEdit_7.text()) != 0:
                tkselectset.append('E' + self.lineEdit_7.text())
            trueAnswer = ''
            if self.checkBox.isChecked():
                trueAnswer = 'A'
            if self.checkBox_2.isChecked():
                trueAnswer = 'B'
            if self.checkBox_3.isChecked():
                trueAnswer = 'C'
            if self.checkBox_4.isChecked():
                trueAnswer = 'D'
            if self.checkBox_5.isChecked():
                trueAnswer = 'E'

            if trueAnswer == '':
                self.statusbar.showMessage('请选择正确答案之后,再次提交!!!', msecs=2000)
                return
            self.textBrowser.setPlainText(string)
            todo.set('trueanswer',trueAnswer)
            todo.set('questiontype', 1)
            todo.set('questiontype_text', '选择题')
            todo.set('question', self.lineEdit_2.text())
            todo.set('tkselect',tkselectset)
            todo.set('questiondescribe', self.textEdit_2.toPlainText())

        elif self.tabWidget.currentIndex() == 2: #
            todo = banner()
            string = '标题 : %s \n 图片: %s \n 链接: %s' % (self.lineEdit_8.text(),self.lineEdit_9.text(),self.lineEdit_10.text())
            if len(self.lineEdit_9.text()) == 0:
                self.statusbar.showMessage('图片为空,不允许提交', msecs=0)
                return
            self.textBrowser.setPlainText(string)
            todo.set('imgUrl',self.lineEdit_9.text())
            todo.set('name',self.lineEdit_8.text().strip())
            todo.set('url',self.lineEdit_10.text())
        elif self.tabWidget.currentIndex() == 3:
            todo = textAd()
            string = '标题 : %s \n 链接: %s' % (self.lineEdit_12.text(),self.lineEdit_13.text())
            if len(self.lineEdit_12.text()) == 0:
                self.statusbar.showMessage('文字为空,不允许提交', msecs=0)
                return
            self.textBrowser.setPlainText(string)
            todo.set('adText',self.lineEdit_12.text().strip())
            todo.set('url',self.lineEdit_13.text())
        elif self.tabWidget.currentIndex() == 4:
            string = '图片地址: %s' % self.lineEdit_11.text()
            todo = home_img1()
            if len(self.lineEdit_11.text()) == 0:
                self.statusbar.showMessage('图片为空,不允许提交', msecs=0)
                return
            self.textBrowser.setPlainText(string)
            todo.set('imgUrl',self.lineEdit_11.text())
        elif self.tabWidget.currentIndex() == 5 :
            todo = video()
            if (len(self.lineEdit_42.text()) == 0) or (len(self.lineEdit_43.text()) == 0):
                self.statusbar.showMessage('内容为空,不允许提交', msecs=0)
                return
            string = '视频状态 : %s \n 名称 : %s \n 链接: %s' % (self.lineEdit_41.text(), self.lineEdit_42.text(),self.lineEdit_43.text())
            self.textBrowser.setPlainText(string)
            todo.set('state',self.lineEdit_41.text())
            todo.set('videoName',self.lineEdit_42.text())
            todo.set('videoUrl',self.lineEdit_43.text())
        todo.save()

        self.statusbar.showMessage('提交成功',msecs=2000)

        self.lineEdit.clear()
        self.textEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_12.clear()
        self.lineEdit_13.clear()
        self.lineEdit_42.clear()
        self.lineEdit_43.clear()

        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)


class Todo(leancloud.Object):
    pass

class iOS(leancloud.Object):
    pass

class Python(leancloud.Object):
    pass


class Android(leancloud.Object):
    pass

class C(leancloud.Object):
    pass

class Java(leancloud.Object):
    pass

class banner(leancloud.Object):
    pass

class textAd(leancloud.Object):
    pass

class home_img1(leancloud.Object):
    pass

class video(leancloud.Object):
    pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    leancloud.init("jRQRUX9jERMhnVedQNmgulIX-gzGzoHsz", master_key="1DXtrehIWMDGupIrw6g5YldD")
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())



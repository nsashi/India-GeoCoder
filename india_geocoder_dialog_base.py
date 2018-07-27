# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'india_geocoder_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IndiaGeocoderDialogBase(object):
    def setupUi(self, IndiaGeocoderDialogBase):
        IndiaGeocoderDialogBase.setObjectName("IndiaGeocoderDialogBase")
        IndiaGeocoderDialogBase.resize(580, 269)
        self.button_box = QtWidgets.QDialogButtonBox(IndiaGeocoderDialogBase)
        self.button_box.setGeometry(QtCore.QRect(210, 220, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.toolButton = QtWidgets.QToolButton(IndiaGeocoderDialogBase)
        self.toolButton.setGeometry(QtCore.QRect(520, 160, 26, 22))
        self.toolButton.setObjectName("toolButton")
        self.lineEdit = QtWidgets.QLineEdit(IndiaGeocoderDialogBase)
        self.lineEdit.setGeometry(QtCore.QRect(150, 160, 351, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(IndiaGeocoderDialogBase)
        self.label.setGeometry(QtCore.QRect(30, 160, 111, 21))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(IndiaGeocoderDialogBase)
        self.textBrowser.setGeometry(QtCore.QRect(30, 30, 521, 101))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(IndiaGeocoderDialogBase)
        self.button_box.accepted.connect(IndiaGeocoderDialogBase.accept)
        self.button_box.rejected.connect(IndiaGeocoderDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(IndiaGeocoderDialogBase)

    def retranslateUi(self, IndiaGeocoderDialogBase):
        _translate = QtCore.QCoreApplication.translate
        IndiaGeocoderDialogBase.setWindowTitle(_translate("IndiaGeocoderDialogBase", "India Geocoder"))
        self.toolButton.setText(_translate("IndiaGeocoderDialogBase", "..."))
        self.label.setText(_translate("IndiaGeocoderDialogBase", "Select Directory:"))
        self.textBrowser.setHtml(_translate("IndiaGeocoderDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#007000;\">This plugin requires HMIS data which can be obtained from NRHM website. Visit </span><span style=\" font-weight:600; color:#007000;\">https://nrhm-mis.nic.in/hmisreports/frmstandard_reports.aspx</span><span style=\" color:#007000;\">, go to </span><span style=\" font-family:\'Verdana,Helvetica,Arial,sans-serif\'; font-style:italic; color:#007000; background-color:#ffffff;\">Performance of Key HMIS Indicators(upto District Level)</span><span style=\" font-family:\'Verdana,Helvetica,Arial,sans-serif\'; color:#007000; background-color:#ffffff;\"> and download suitable directory. Enter the local path of the downloaded directory below.</span></p></body></html>"))


# -*- coding: utf-8 -*-
"""
/***************************************************************************
 IndiaGeocoderDialog
                                 A QGIS plugin
 This plugin is used for analysis of HMIS data
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-06-20
        git sha              : $Format:%H$
        copyright            : (C) 2018 by IIRS
        email                : kotishiva@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.core import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QPushButton, QDialogButtonBox, QAbstractItemView, QDialog, QMessageBox, QFileDialog

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'india_geocoder_dialog_base.ui'))

FORM_CLASS3, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'state_dialog.ui'))

FORM_CLASS4, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'visualisation_dialog.ui'))

FORM_CLASS5, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'search_keyword_dialog.ui'))

FORM_CLASS6, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'select_layers_dialog.ui'))


class IndiaGeocoderDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(IndiaGeocoderDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)


class StateDialog(QtWidgets.QDialog, FORM_CLASS3):
    def __init__(self, states, district, parent=None):
        super(StateDialog, self).__init__(parent)
        self.setupUi(self)

        self.states = states
        self.district = district
        self.selectedstate = states[0]
        self.populateDialogBox()
        self.show()

    def populateDialogBox(self):
        self.comboBox.addItems(self.states)
        self.label.setText(self.district + " is in " + str(len(self.states)) + " states")

    def accept(self):
        self.selectedstate = self.comboBox.currentText()
        QDialog.accept(self)

class VisualisationDialog(QtWidgets.QDialog, FORM_CLASS4):
    def __init__(self, parent=None):
        super(VisualisationDialog, self).__init__(parent)
        self.setupUi(self)


class MultipleInputDialog(QtWidgets.QDialog, FORM_CLASS5):
    def __init__(self, options, parent=None):
        """Constructor

        :param options: Exhaustive list of all fields in xls files
        :type options: list
        """
        super(MultipleInputDialog, self).__init__(parent)
        self.setupUi(self)

        self.model = None

        self.options = options      # Current list of fields (all fields for 1st time)
        self.all_fields = options

        self.selectedoptions = []

        # Additional buttons
        self.btnSelectAll = QPushButton(self.tr('Select all'))
        self.buttonBox.addButton(self.btnSelectAll,
                                 QDialogButtonBox.ActionRole)
        self.btnClearSelection = QPushButton(self.tr('Clear selection'))
        self.buttonBox.addButton(self.btnClearSelection,
                                 QDialogButtonBox.ActionRole)
        self.btnToggleSelection = QPushButton(self.tr('Toggle selection'))
        self.buttonBox.addButton(self.btnToggleSelection,
                                 QDialogButtonBox.ActionRole)

        self.btnSelectAll.clicked.connect(lambda: self.selectAll(True))
        self.btnClearSelection.clicked.connect(lambda: self.selectAll(False))
        self.btnToggleSelection.clicked.connect(self.toggleSelection)
        self.pushButton.clicked.connect(self.searchFields)

        self.lstLayers.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lstLayers.setDragDropMode(QAbstractItemView.InternalMove)

        self.populateList()
        self.show()

    def populateList(self):
        """Method to populate the list view with fields"""
        self.model = QStandardItemModel()
        for text in self.options:
            item = QStandardItem(text)
            # item.setData(value, Qt.UserRole)
            item.setCheckable(True)
            item.setCheckState(Qt.Unchecked)
            item.setDropEnabled(False)
            self.model.appendRow(item)

        self.lstLayers.setModel(self.model)

    def accept(self):
        """Updates selectedoptions list when "OK" is pressed"""
        # self.selectedoptions = ["ID", "Sub district"]
        self.selectedoptions = ["ID", "District"]
        model = self.lstLayers.model()
        for i in range(model.rowCount()):
            item = model.item(i)
            if item.checkState() == Qt.Checked:
                self.selectedoptions.append(item.text())
        QDialog.accept(self)

    def reject(self):
        """Invoked when "Cancel" is pressed"""
        self.selectedoptions = None
        QDialog.reject(self)

    def getItemsToModify(self):
        """
        :returns: List of items needed in selectAll() and toggleSelection()
        :rtype: list
        """
        items = []
        if len(self.lstLayers.selectedIndexes()) > 1:
            for i in self.lstLayers.selectedIndexes():
                items.append(self.model.itemFromIndex(i))
        else:
            for i in range(self.model.rowCount()):
                items.append(self.model.item(i))
        return items

    def selectAll(self, value):
        """Invoked when "Select all" is pressed. Checks all fields."""
        for item in self.getItemsToModify():
            item.setCheckState(Qt.Checked if value else Qt.Unchecked)

    def toggleSelection(self):
        """Invoked when "Toggle selecton" is pressed. Reverses the check state of fields."""
        for item in self.getItemsToModify():
            checked = item.checkState() == Qt.Checked
            item.setCheckState(Qt.Unchecked if checked else Qt.Checked)

    def searchFields(self):
        """Invoked when "Search" is pressed.
        Populates the list view using the keyword entered.
        """

        keyword = self.lineEdit.text().strip()
        self.options = []
        for field in self.all_fields:
            if keyword.lower() in field.lower():    # to make search case insensitive
                self.options.append(field)
        # Error dialog for invalid entry
        if len(self.options) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No field found containing keyword!")
            msg.setInformativeText("Enter valid attribute")
            msg.setWindowTitle("Error")
            msg.show()
            msg.exec_()
        else:
            self.populateList()

class SelectLayersDialog(QtWidgets.QDialog, FORM_CLASS6):
    def __init__(self, options, parent=None):
        """Constructor

        :param options: Exhaustive list of all layers present
        :type options: list
        """
        super(SelectLayersDialog, self).__init__(parent)
        self.setupUi(self)

        self.model = None

        self.options = options      # Current list of fields (all fields for 1st time)
        self.selectedoptions = []


        # Additional buttons
        self.btnSelectAll = QPushButton(self.tr('Select all'))
        self.buttonBox.addButton(self.btnSelectAll,
                                 QDialogButtonBox.ActionRole)
        self.btnClearSelection = QPushButton(self.tr('Clear selection'))
        self.buttonBox.addButton(self.btnClearSelection,
                                 QDialogButtonBox.ActionRole)
        self.btnToggleSelection = QPushButton(self.tr('Toggle selection'))
        self.buttonBox.addButton(self.btnToggleSelection,
                                 QDialogButtonBox.ActionRole)

        self.btnSelectAll.clicked.connect(lambda: self.selectAll(True))
        self.btnClearSelection.clicked.connect(lambda: self.selectAll(False))
        self.btnToggleSelection.clicked.connect(self.toggleSelection)

        self.lstLayers.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lstLayers.setDragDropMode(QAbstractItemView.InternalMove)

        self.populateList()
        self.show()

    def populateList(self):
        """Method to populate the list view with layers"""
        self.model = QStandardItemModel()
        for text in self.options:
            item = QStandardItem(text)
            # item.setData(value, Qt.UserRole)
            item.setCheckable(True)
            item.setCheckState(Qt.Unchecked)
            item.setDropEnabled(False)
            self.model.appendRow(item)

        self.lstLayers.setModel(self.model)

    def accept(self):
        """Updates selectedoptions list and renders image when "Save" is pressed"""
        self.selectedoptions = []
        model = self.lstLayers.model()
        for i in range(model.rowCount()):
            item = model.item(i)
            if item.checkState() == Qt.Checked:
                self.selectedoptions.append(item.text())
        # Error message if no layer is selected
        if len(self.selectedoptions) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No layer selected!")
            msg.setInformativeText("Select at least one layer to generate image of the map")
            msg.setWindowTitle("Error")
            msg.show()
            msg.exec_()
        else:
            layers = []
            for option in self.selectedoptions:
                layers.append(QgsProject.instance().mapLayersByName(option)[0])
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            # Store string of directory path, use interactive dialog to let user select the directory
            img_path, _ = QFileDialog.getSaveFileName(self, "Save Image", option, "PNG (*.png)", options=options)
            if img_path.endswith(".png"):
                pass
            else:
                img_path += ".png"
            # render map image
            settings = QgsMapSettings()
            settings.setOutputSize(QSize(512, 512))
            settings.setExtent(layers[0].extent())
            settings.setLayers(layers)
            job = QgsMapRendererSequentialJob(settings)
            job.start()
            job.waitForFinished()
            img = job.renderedImage()
            img.save(img_path, "png")
            QDialog.accept(self)

    # # def reject(self):
    # #     """Invoked when "Don't Save" is pressed"""
    # #     self.selectedoptions = None
    #     QDialog.reject(self)

    def getItemsToModify(self):
        """
        :returns: List of items needed in selectAll() and toggleSelection()
        :rtype: list
        """
        items = []
        if len(self.lstLayers.selectedIndexes()) > 1:
            for i in self.lstLayers.selectedIndexes():
                items.append(self.model.itemFromIndex(i))
        else:
            for i in range(self.model.rowCount()):
                items.append(self.model.item(i))
        return items

    def selectAll(self, value):
        """Invoked when "Select all" is pressed. Checks all fields."""
        for item in self.getItemsToModify():
            item.setCheckState(Qt.Checked if value else Qt.Unchecked)

    def toggleSelection(self):
        """Invoked when "Toggle selecton" is pressed. Reverses the check state of fields."""
        for item in self.getItemsToModify():
            checked = item.checkState() == Qt.Checked
            item.setCheckState(Qt.Unchecked if checked else Qt.Checked)

import copy
import json
from math import floor

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument, QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QFrame, QPushButton, QRadioButton, QLineEdit, QComboBox, \
    QInputDialog, QMessageBox


class PartTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setColumnMinimumWidth(0, 220)

        # Run functions to create all the little guys
        self._createTextFields()
        self._createLabels()
        self._createMisc()
        self._createButtons()

        self.partData = []
        self.fileName = "something"
        self.startData = 1000
        custom_font = QFont()
        custom_font.setWeight(38)
        self.setFont(custom_font)

    def _createTextFields(self):
        """
        Creates and positions the Line Edits on the tab
        :return: None
        """
        # Number of times to clone
        self.textAmount = QLineEdit()
        self.textAmount.setMaximumWidth(80)
        self.textAmount.setContentsMargins(25, 0, 0, 0)
        self.layout.addWidget(self.textAmount, 0, 1, alignment=Qt.AlignCenter)

        # ID Stuff
        self.textREF = QLineEdit()
        self.layout.addWidget(self.textREF, 2, 1, 1, 2)
        self.textCID = QLineEdit()
        self.layout.addWidget(self.textCID, 3, 1, 1, 2)

        # Position
        # Initial
        self.textXPosInit = QLineEdit()
        self.layout.addWidget(self.textXPosInit, 6, 1)
        self.textYPosInit = QLineEdit()
        self.layout.addWidget(self.textYPosInit, 6, 2)
        self.textZPosInit = QLineEdit()
        self.layout.addWidget(self.textZPosInit, 6, 3)

        # Increment
        self.textXPosInc = QLineEdit()
        self.layout.addWidget(self.textXPosInc, 7, 1)
        self.textYPosInc = QLineEdit()
        self.layout.addWidget(self.textYPosInc, 7, 2)
        self.textZPosInc = QLineEdit()
        self.layout.addWidget(self.textZPosInc, 7, 3)

        # Limit
        self.textXPosLimit = QLineEdit()
        self.layout.addWidget(self.textXPosLimit, 8, 1)
        self.textYPosLimit = QLineEdit()
        self.layout.addWidget(self.textYPosLimit, 8, 2)
        self.textZPosLimit = QLineEdit()
        self.layout.addWidget(self.textZPosLimit, 8, 3)

        # Rotation
        # Initial
        self.textXRotInit = QLineEdit()
        self.layout.addWidget(self.textXRotInit, 11, 1)
        self.textYRotInit = QLineEdit()
        self.layout.addWidget(self.textYRotInit, 11, 2)
        self.textZRotInit = QLineEdit()
        self.layout.addWidget(self.textZRotInit, 11, 3)

        # Increment
        self.textXRotInc = QLineEdit()
        self.layout.addWidget(self.textXRotInc, 12, 1)
        self.textYRotInc = QLineEdit()
        self.layout.addWidget(self.textYRotInc, 12, 2)
        self.textZRotInc = QLineEdit()
        self.layout.addWidget(self.textZRotInc, 12, 3)

        # Limit
        self.textXRotLimit = QLineEdit()
        self.layout.addWidget(self.textXRotLimit, 13, 1)
        self.textYRotLimit = QLineEdit()
        self.layout.addWidget(self.textYRotLimit, 13, 2)
        self.textZRotLimit = QLineEdit()
        self.layout.addWidget(self.textZRotLimit, 13, 3) \
 \
            # Scale
        # Initial
        self.textXScaleInit = QLineEdit()
        self.layout.addWidget(self.textXScaleInit, 16, 1)
        self.textYScaleInit = QLineEdit()
        self.layout.addWidget(self.textYScaleInit, 16, 2)
        self.textZScaleInit = QLineEdit()
        self.layout.addWidget(self.textZScaleInit, 16, 3)

        # Increment
        self.textXScaleInc = QLineEdit()
        self.layout.addWidget(self.textXScaleInc, 17, 1)
        self.textYScaleInc = QLineEdit()
        self.layout.addWidget(self.textYScaleInc, 17, 2)
        self.textZScaleInc = QLineEdit()
        self.layout.addWidget(self.textZScaleInc, 17, 3)

        # Limit
        self.textXScaleLimit = QLineEdit()
        self.layout.addWidget(self.textXScaleLimit, 18, 1)
        self.textYScaleLimit = QLineEdit()
        self.layout.addWidget(self.textYScaleLimit, 18, 2)
        self.textZScaleLimit = QLineEdit()
        self.layout.addWidget(self.textZScaleLimit, 18, 3)

        # Putting the initial boxes in a list, so it's easier to reference them
        self.textInitialList = [self.textXPosInit,
                                self.textYPosInit,
                                self.textZPosInit,
                                self.textXRotInit,
                                self.textYRotInit,
                                self.textZRotInit,
                                self.textXScaleInit,
                                self.textYScaleInit,
                                self.textZScaleInit]

        # Putting the increment boxes in a list, so it's easier to reference them
        self.textIncrementList = [self.textXPosInc,
                                  self.textYPosInc,
                                  self.textZPosInc,
                                  self.textXRotInc,
                                  self.textYRotInc,
                                  self.textZRotInc,
                                  self.textXScaleInc,
                                  self.textYScaleInc,
                                  self.textZScaleInc]
        # Filling all the increment values with 0 to start
        for text in self.textIncrementList:
            text.setText("0.0")

        # Putting the limit boxes in a list, so it's easier to reference them
        self.textLimitList = [self.textXPosLimit,
                              self.textYPosLimit,
                              self.textZPosLimit,
                              self.textXRotLimit,
                              self.textYRotLimit,
                              self.textZRotLimit,
                              self.textXScaleLimit,
                              self.textYScaleLimit,
                              self.textZScaleLimit]
        # Disabling the limit boxes at startup
        for text in self.textLimitList:
            text.setDisabled(True)

    def _createLabels(self):
        """
        Creates and positions the Labels on the tab
        :return: None
        """
        labelPlaceLimit = QLabel("Placement Limit:")
        self.layout.addWidget(labelPlaceLimit, 0, 0)
        labelREF = QLabel("Part ID (REF):")
        self.layout.addWidget(labelREF, 2, 0)
        labelCID = QLabel("Compartment (CID):")
        self.layout.addWidget(labelCID, 3, 0)
        labelPosHeader = QLabel("Position:")
        self.layout.addWidget(labelPosHeader, 5, 0)
        labelPosHeaderX = QLabel("X")
        self.layout.addWidget(labelPosHeaderX, 5, 1, alignment=Qt.AlignCenter)
        labelPosHeaderY = QLabel("Y")
        self.layout.addWidget(labelPosHeaderY, 5, 2, alignment=Qt.AlignCenter)
        labelPosHeaderZ = QLabel("Z")
        self.layout.addWidget(labelPosHeaderZ, 5, 3, alignment=Qt.AlignCenter)
        labelPosInit = QLabel("Initial:")
        self.layout.addWidget(labelPosInit, 6, 0)
        labelPosInc = QLabel("Increment:")
        self.layout.addWidget(labelPosInc, 7, 0)
        labelPosLimit = QLabel("Limit:")
        self.layout.addWidget(labelPosLimit, 8, 0)
        labelRotHeader = QLabel("Rotation:")
        self.layout.addWidget(labelRotHeader, 10, 0)
        labelRotHeaderX = QLabel("X")
        self.layout.addWidget(labelRotHeaderX, 10, 1, alignment=Qt.AlignCenter)
        labelRotHeaderY = QLabel("Y")
        self.layout.addWidget(labelRotHeaderY, 10, 2, alignment=Qt.AlignCenter)
        labelRotHeaderZ = QLabel("Z")
        self.layout.addWidget(labelRotHeaderZ, 10, 3, alignment=Qt.AlignCenter)
        labelRotInit = QLabel("Initial:")
        self.layout.addWidget(labelRotInit, 11, 0)
        labelRotInc = QLabel("Increment:")
        self.layout.addWidget(labelRotInc, 12, 0)
        labelRotLimit = QLabel("Limit:")
        self.layout.addWidget(labelRotLimit, 13, 0)
        labelScaleHeader = QLabel("Scale:")
        self.layout.addWidget(labelScaleHeader, 15, 0)
        labelScaleHeaderX = QLabel("X")
        self.layout.addWidget(labelScaleHeaderX, 15, 1, alignment=Qt.AlignCenter)
        labelScaleHeaderY = QLabel("Y")
        self.layout.addWidget(labelScaleHeaderY, 15, 2, alignment=Qt.AlignCenter)
        labelScaleHeaderZ = QLabel("Z")
        self.layout.addWidget(labelScaleHeaderZ, 15, 3, alignment=Qt.AlignCenter)
        labelScaleInit = QLabel("Initial:")
        self.layout.addWidget(labelScaleInit, 16, 0)
        labelScaleInc = QLabel("Increment:")
        self.layout.addWidget(labelScaleInc, 17, 0)
        labelScaleLimit = QLabel("Limit:")
        self.layout.addWidget(labelScaleLimit, 18, 0)

    def _createButtons(self):
        """
        Creates and positions the Buttons on the tab
        :return: None
        """
        buttonPasteInput = QPushButton("Input")
        buttonPasteInput.clicked.connect(self.inputPopup)
        self.layout.addWidget(buttonPasteInput, 1, 1, 1, 2)

        buttonClear = QPushButton("Clear")
        buttonClear.clicked.connect(self.clear)
        self.layout.addWidget(buttonClear, 19, 0, alignment=Qt.AlignBottom)

        buttonGo = QPushButton("GO!")
        buttonGo.clicked.connect(self.checkForBlanks)
        buttonGo.setMinimumSize(250, 100)
        self.layout.addWidget(buttonGo, 19, 2, 2, 2)

    def _createMisc(self):
        """
        Creates and positions the misc items on the tab
        :return: None
        """
        hLine1 = QFrame()
        hLine1.setFrameStyle(QFrame.HLine | QFrame.Plain)
        hLine1.setLineWidth(3)
        self.layout.addWidget(hLine1, 4, 0, 1, 4)
        hLine2 = QFrame()
        hLine2.setFrameStyle(QFrame.HLine | QFrame.Plain)
        hLine2.setLineWidth(3)
        self.layout.addWidget(hLine2, 9, 0, 1, 4)
        hLine3 = QFrame()
        hLine3.setFrameStyle(QFrame.HLine | QFrame.Plain)
        hLine3.setLineWidth(3)
        self.layout.addWidget(hLine3, 14, 0, 1, 4)

        self.radioGoUntil = QRadioButton("Go Until")
        self.radioGoUntil.toggled.connect(lambda: self.togglePlaceLimit(2))
        self.layout.addWidget(self.radioGoUntil, 0, 2)

        self.radioAmount = QRadioButton("Amount:")
        self.radioAmount.setChecked(True)
        self.radioAmount.setMaximumWidth(100)
        self.radioAmount.toggled.connect(lambda: self.togglePlaceLimit(1))
        self.layout.addWidget(self.radioAmount, 0, 1)

        self.radioBoth = QRadioButton("Both")
        self.radioBoth.setDisabled(True)
        self.radioBoth.setVisible(False)
        self.radioBoth.toggled.connect(lambda: self.togglePlaceLimit(3))
        self.layout.addWidget(self.radioBoth, 0, 3)

        self.comboGoUntil = QComboBox()
        self.comboGoUntil.addItems(
            ["X Position", "Y Position", "Z Position", "X Rotation", "Y Rotation", "Z Rotation", "X Scale", "Y Scale",
             "Z Scale"])
        self.comboGoUntil.setDisabled(True)
        self.comboGoUntil.currentIndexChanged.connect(self.toggleGoUntilLimit)
        self.layout.addWidget(self.comboGoUntil, 0, 2, alignment=Qt.AlignRight)

    def inputPopup(self):
        text, done = QInputDialog.getMultiLineText(self, "Input", "Input Starting Object:")
        if text and done:
            try:
                parsedPaste = self.parsePaste(text)
                self.textREF.setText(parsedPaste['REF'])
                self.textCID.setText(str(parsedPaste['CID']))
                for i in range(self.textInitialList.__len__()):
                    self.textInitialList[i].setText(str(parsedPaste["T"][i]))
                self.partData = parsedPaste['DAT']
            except:
                error = QMessageBox()
                error.setWindowTitle("JSON Parse Error")
                error.setText("There was an error interpreting the pasted text.")
                error.setInformativeText(
                    " Please make sure to only add one part, and that none of the brackets or quotes are missing. See Help for more info.")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Retry)
                error.buttonClicked.connect(self.inputPopup)
                error.exec_()

    def clear(self):
        for text in self.textInitialList:
            text.clear()
        for text in self.textIncrementList:
            text.setText("0.0")
        for text in self.textLimitList:
            text.clear()
        self.textREF.clear()
        self.textCID.clear()
        self.textAmount.clear()
        self.comboGoUntil.setCurrentIndex(0)
        self.radioAmount.setChecked(True)

    def togglePlaceLimit(self, butt):
        """
        Toggles the available input option for the place limit
        :param butt: 1 for Amount, 2 for Go Until
        :return: None
        """
        if butt == 1:
            self.comboGoUntil.setDisabled(True)
            self.textAmount.setDisabled(False)
            self.toggleGoUntilLimit(-1)
            for text in self.textIncrementList:
                text.setDisabled(False)
        elif butt == 2:
            self.comboGoUntil.setDisabled(False)
            self.textAmount.setDisabled(True)
            self.toggleGoUntilLimit(self.comboGoUntil.currentIndex())
        elif butt == 3:
            self.comboGoUntil.setDisabled(False)
            self.textAmount.setDisabled(False)
            self.toggleGoUntilLimit(self.comboGoUntil.currentIndex())
            self.textIncrementList[self.comboGoUntil.currentIndex()].setDisabled(True)

    def toggleGoUntilLimit(self, index):
        if self.radioBoth.isChecked():
            for text in self.textIncrementList:
                text.setDisabled(False)
            self.textIncrementList[index].setDisabled(True)
        if index == -1:
            for text in self.textLimitList:
                text.setDisabled(True)
        else:
            for text in self.textLimitList:
                text.setDisabled(True)
            self.textLimitList[index].setDisabled(False)

    def checkForBlanks(self):

        valid = True
        for text in self.textInitialList:

            try:
                if text.text().strip() == "":
                    error = QMessageBox()
                    error.setWindowTitle("Missing Data")
                    error.setText("There was an error entering data.")
                    error.setInformativeText(
                        " Please make sure that all initial boxes are filled.")
                    error.setIcon(QMessageBox.Warning)
                    error.setStandardButtons(QMessageBox.Retry)
                    error.exec_()
                    text.setStyleSheet("QLineEdit{background : red;color: white}")
                elif float(text.text().strip()):
                    text.setStyleSheet("QLineEdit{}")
            except:
                error = QMessageBox()
                error.setWindowTitle("Invalid Data")
                error.setText("There was an error entering data.")
                error.setInformativeText(
                    " Please make sure that all initial boxes are filled with valid numbers.")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Retry)
                text.setStyleSheet("QLineEdit{background : red;color: white}")
                error.exec_()
                valid = False

        try:
            if self.radioGoUntil.isChecked() and self.textLimitList[self.comboGoUntil.currentIndex()].text().strip() == "":
                error = QMessageBox()
                error.setWindowTitle("Missing Data")
                error.setText("There was an error entering data.")
                error.setInformativeText(
                    " Please make sure that the applicable limit box is filled.")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Retry)
                error.exec_()
                self.textLimitList[self.comboGoUntil.currentIndex()].setStyleSheet(
                    "QLineEdit{background : red;color: white}")
            elif self.radioGoUntil.isChecked() and float(self.textLimitList[self.comboGoUntil.currentIndex()].text().strip()):
                self.textLimitList[self.comboGoUntil.currentIndex()].setStyleSheet("QLineEdit{}")
        except:
            error = QMessageBox()
            error.setWindowTitle("Invalid Data")
            error.setText("There was an error entering data.")
            error.setInformativeText(
                " Please make sure that the applicable limit box is filled with valid numbers.")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Retry)
            self.textLimitList[self.comboGoUntil.currentIndex()].setStyleSheet(
                "QLineEdit{background : red;color: white}")
            error.exec_()
            valid = False

        for text in self.textIncrementList:
            try:
                if text.text().strip() == "":
                    text.setText("0.0")
                elif float(text.text().strip()):
                    text.setStyleSheet("QLineEdit{}")
            except:
                error = QMessageBox()
                error.setWindowTitle("Invalid Data")
                error.setText("There was an error entering data.")
                error.setInformativeText(
                    " Please make sure that all increment boxes are filled with valid numbers or 0.")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Retry)
                text.setStyleSheet("QLineEdit{background : red;color: white}")
                error.exec_()
                valid = False

        if self.radioAmount.isChecked() and self.textAmount.text().strip() == "":
            valid = False
            error = QMessageBox()
            error.setWindowTitle("Invalid Data")
            error.setText("There was an error entering data.")
            error.setInformativeText(
                " Please make sure that the amount box is filled with a valid non-negative number")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Retry)
            self.textAmount.setStyleSheet("QLineEdit{background : red;color: white}")
            error.exec_()

        if valid:
            self.checkValidAmount()

    def checkValidAmount(self):
        amount = 0
        if (self.radioAmount.isChecked() or self.radioBoth.isChecked()) and self.textAmount.text().strip() != "":
            amount = int(self.textAmount.text().strip())
        elif (self.radioGoUntil.isChecked() and self.textLimitList[
            self.comboGoUntil.currentIndex()].text().strip() != ""):
            if (float(self.textLimitList[self.comboGoUntil.currentIndex()].text().strip()) >
                float(self.textInitialList[self.comboGoUntil.currentIndex()].text().strip()) and
                float(self.textIncrementList[self.comboGoUntil.currentIndex()].text().strip()) > 0) or \
                    (float(self.textLimitList[self.comboGoUntil.currentIndex()].text().strip()) <
                     float(self.textInitialList[self.comboGoUntil.currentIndex()].text().strip()) and
                     float(self.textIncrementList[self.comboGoUntil.currentIndex()].text().strip()) < 0):
                amount = 1 + floor((abs(float(self.textLimitList[self.comboGoUntil.currentIndex()].text().strip()) - (
                    float(self.textInitialList[self.comboGoUntil.currentIndex()].text().strip())))) / abs(
                    float(self.textIncrementList[self.comboGoUntil.currentIndex()].text().strip())))
            else:
                error = QMessageBox()
                error.setWindowTitle("Increment/Limit Incompatible")
                error.setText("There was an error incrementing to your limit.")
                error.setInformativeText(
                    " Please make sure that the the increment and limit are in the same direction. See Help for more.")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Retry)
                self.textLimitList[self.comboGoUntil.currentIndex()].setStyleSheet(
                    "QLineEdit{background : red;color: white}")
                self.textIncrementList[self.comboGoUntil.currentIndex()].setStyleSheet(
                    "QLineEdit{background : red;color: white}")
                error.exec_()

        if amount > 0:
            self.checkScaleBeforeWrite(amount)

    def checkScaleBeforeWrite(self, amount):
        if self.textXScaleInit.text().strip() != "" and float(self.textXScaleInit.text().strip()) + \
                (float(self.textXScaleInc.text().strip()) * amount) <= 0:

            self.textXScaleInc.setStyleSheet("QLineEdit{background : red;color: white}")
            self.textYScaleInc.setStyleSheet("QLineEdit{}")
            self.textZScaleInc.setStyleSheet("QLineEdit{}")
            error = QMessageBox()
            error.setWindowTitle("Scale Increment")
            error.setText("There was an error incrementing the X scale.")
            error.setInformativeText(
                " Please make sure that the scale will not become negative or zero as a result of incrementing.")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Retry)
            error.exec_()

        elif self.textYScaleInit.text().strip() != "" and float(self.textYScaleInit.text().strip()) + \
                (float(self.textYScaleInc.text().strip()) * amount) <= 0:

            self.textYScaleInc.setStyleSheet("QLineEdit{background : red;color: white}")
            self.textXScaleInc.setStyleSheet("QLineEdit{}")
            self.textZScaleInc.setStyleSheet("QLineEdit{}")
            error = QMessageBox()
            error.setWindowTitle("Scale Increment")
            error.setText("There was an error incrementing the Y scale.")
            error.setInformativeText(
                " Please make sure that the scale will not become negative or zero as a result of incrementing.")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Retry)
            error.exec_()

        elif self.textZScaleInit.text().strip() != "" and float(self.textZScaleInit.text().strip()) + \
                (float(self.textZScaleInc.text().strip()) * amount) <= 0:

            self.textZScaleInc.setStyleSheet("QLineEdit{background : red;color: white}")
            self.textXScaleInc.setStyleSheet("QLineEdit{}")
            self.textYScaleInc.setStyleSheet("QLineEdit{}")
            error = QMessageBox()
            error.setWindowTitle("Scale Increment")
            error.setText("There was an error incrementing the Z scale.")
            error.setInformativeText(
                " Please make sure that the scale will not become negative or zero as a result of incrementing.")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Retry)
            error.exec_()

        else:
            self.textXScaleInc.setStyleSheet("QLineEdit{background : white;}")
            self.textYScaleInc.setStyleSheet("QLineEdit{background : white;}")
            self.textZScaleInc.setStyleSheet("QLineEdit{background : white;}")
            scalars = []
            for text in self.textIncrementList:
                scalars.append(float(text.text().strip()))
            self.writeToFile(self.loopIncrement(self.rebuildJson(), amount, scalars), self.fileName)

    def writeToFile(self, jsonList, fileName):
        listA = [jsonList]
        with open(fileName, 'w') as f:
            print(f.write(json.dumps(listA, indent=2)[6: -6]))

    def rebuildJson(self):
        json = {"REF": self.textREF.text().strip(),
                "CID": int(self.textCID.text().strip()),
                "T": [
                    float(self.textXPosInit.text().strip()),
                    float(self.textYPosInit.text().strip()),
                    float(self.textZPosInit.text().strip()),
                    float(self.textXRotInit.text().strip()),
                    float(self.textYRotInit.text().strip()),
                    float(self.textZRotInit.text().strip()),
                    float(self.textXScaleInit.text().strip()),
                    float(self.textYScaleInit.text().strip()),
                    float(self.textZScaleInit.text().strip()),
                    0.0
                ],
                "DAT": self.partData}
        return json

    def setFileName(self, nfileName):
        self.fileName = nfileName

    @staticmethod
    def parsePaste(bulkPaste):
        """
        Parses the bulk paste into data used by the text boxes
        :return: A dictionary containing the data
        """
        if (bulkPaste[-1] == ','):
            bulkPaste = bulkPaste[0:-1]
        parsedJson = json.loads(bulkPaste)
        return parsedJson

    def incrementCoords(self, scalars, oldJson):
        """
        Copies the given JSON and increments the coordinates by the values given
        :param scalars: List of factors to scale each value by
        :param oldJson: Previous JSON object
        :return: New JSON object with incremented coordinates
        """
        newJson = copy.deepcopy(oldJson)
        newJson['T'][0] += scalars[0]
        newJson['T'][1] += scalars[1]
        newJson['T'][2] += scalars[2]
        newJson['T'][3] += scalars[3]
        if newJson['T'][3] >= 360:
            newJson['T'][3] -= 360
        elif newJson['T'][3] < 0:
            newJson['T'][3] += 360
        newJson['T'][4] += scalars[4]
        if newJson['T'][4] >= 360:
            newJson['T'][4] -= 360
        elif newJson['T'][4] < 0:
            newJson['T'][4] += 360
        newJson['T'][5] += scalars[5]
        if newJson['T'][5] >= 360:
            newJson['T'][5] -= 360
        elif newJson['T'][5] < 0:
            newJson['T'][5] += 360
        newJson['T'][6] += scalars[6]
        newJson['T'][7] += scalars[7]
        newJson['T'][8] += scalars[8]

        for i,data in enumerate(newJson['DAT']):
            if data['id'] != "asset":
                if int(data['data'][6:-1]) < self.startData:
                    data['data'] = "{\"ID\":" + str(self.startData + i) + "}"
                else:
                    data['data'] = "{\"ID\":" + str(int(data['data'][6:-1]) + len(newJson['DAT'])) + "}"
                print(int(data['data'][6:-1]))
        return newJson

    def loopIncrement(self, firstJson, numTimes, scalars):
        """
        Increments the firstJson object numTimes times using given increments
        :param firstJson: The original Json pasted into the program
        :param numTimes: Number of times to copy, inclusive of first object
        :param scalars: List of factors to scale each value by
        :return: List of JSON objects after incrementing
        """
        jsonList = [firstJson]
        for i in range(numTimes - 1):
            jsonList.append(
                self.incrementCoords(scalars, jsonList[i]))
        #print(jsonList)
        return jsonList

    @staticmethod
    def prettyPrint(jsonList):
        """
        Prints the list of JSON objects to the console using the correct formatting
        :param jsonList: List of incremented JSON objects
        :return: None
        """
        print(json.dumps(jsonList, indent=2))

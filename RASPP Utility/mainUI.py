import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QTextDocument, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QMenuBar, QGridLayout, QTabWidget, QVBoxLayout, QAction, QFileDialog, \
    QDialog, QPlainTextEdit, QTextEdit, QInputDialog, QTextBrowser, QApplication, QMessageBox

from partTab import PartTab
from compartmentTab import CompartmentTab

class MainUI(QMainWindow):
    def __init__(self):
        """
        Init
        """
        QMainWindow.__init__(self)

        # Window Setup
        self.setMinimumSize(QSize(900, 900))
        self.setWindowTitle("RASPP Utility")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.setWindowIcon(QIcon(self.resourcePath("img\RASPP.ico")))

        # Tab Setup
        self._createTabs()

        # Menu Bar Setup
        self._createMenuBar()

        # Setting Default Font
        # TODO
        font = self.font()
        font.setPointSize(12)
        QApplication.instance().setFont(font)

        try:
            with open("RASPP.settings", "r") as f:

                if len(f.readlines()) < 2:
                    print(len(f.readlines()))
                    with open("RASPP.settings", "w") as f:
                        f.write("Sprocket_parts.txt\n")
                        f.write("1000")
                f.seek(0)
                try:
                    self.fileName = f.readline().strip()
                    if not self.isPathnameValid(self.fileName):
                        self.fileName = "Sprocket_parts.txt"
                        with open("RASPP.settings", "r") as f:
                            temp = f.readlines()
                            temp[0] = self.fileName.strip() + "\n"
                            with open("RASPP.settings", "w") as f:
                                f.writelines(temp)
                except Exception as e:
                    self.fileName = "Sprocket_parts.txt"
                    with open("RASPP.settings", "r") as f:
                        temp = f.readlines()
                        temp[0] = self.fileName.strip() + "\n"
                        with open("RASPP.settings", "w") as f:
                            f.writelines(temp)
                self.partTab.setFileName(self.fileName)

                try:
                    self.startData = int(f.readline())
                except:
                    self.startData = 1000
        except:
            with open("RASPP.settings", "w") as f:
                f.write("Sprocket_parts.txt\n")
                f.write("1000")

    def _createTabs(self):
        """
        Creates and add tabs to Main UI
        :return: None
        """
        widget = QWidget()
        widget.layout = QVBoxLayout(widget)
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(2)
        self.partTab = PartTab()
        self.compartmentTab = CompartmentTab()

        # Add tabs
        self.tabs.addTab(self.partTab, "In-game Parts")
        self.tabs.addTab(self.compartmentTab, "Compartments")

        widget.layout.addWidget(self.tabs)
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def _createMenuBar(self):
        """
        Make menu bar
        :return: Nothing bro
        """
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        fileMenu = menuBar.addMenu("&File")
        helpMenu = menuBar.addMenu("&Help")

        self.filePathAction = QAction("Change &Save Location")
        self.filePathAction.triggered.connect(self.changeFilePath)
        self.filePathAction.setShortcut("Ctrl+S")
        fileMenu.addAction(self.filePathAction)

        self.dataAction = QAction("Change Starting &Data Value")
        self.dataAction.triggered.connect(self.changeStartData)
        fileMenu.addAction(self.dataAction)

        self.exitAction = QAction("&Exit", self)
        self.exitAction.triggered.connect(QMainWindow.close)
        fileMenu.addAction(self.exitAction)
        
        self.guideAction = QAction("Quick Guide")
        self.guideAction.triggered.connect(self.openQuickGuide)
        
        self.FAQAction = QAction("FAQs")
        self.FAQAction.triggered.connect(self.openFAQ)

        self.helpfulMenu = helpMenu.addMenu("Helpful Stuff")
        self.helpfulMenu.addAction(self.guideAction)
        self.helpfulMenu.addAction(self.FAQAction)

        self.aboutAction = QAction("About...")
        self.aboutAction.triggered.connect(self.openAbout)
        helpMenu.addAction(self.aboutAction)

    def changeFilePath(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName1, _ = QFileDialog.getSaveFileName(self, "Change Save Location", self.fileName.strip(),
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName1:

            try:
                if self.isPathnameValid(self.fileName):
                    self.fileName = fileName1
                    self.partTab.setFileName(fileName1)
                    with open(fileName1.strip(), "w") as f:
                        f.write("")
                    with open("RASPP.settings", "r") as f:
                        temp = f.readlines()
                        temp[0] = fileName1.strip() + "\n"
                        with open("RASPP.settings", "w") as f:
                            f.writelines(temp)
                else:
                    error = QMessageBox()
                    error.setWindowTitle("File Path Error")
                    error.setText("There was an error interpreting your file path.")
                    error.setInformativeText(
                        " Please make sure your path is pointing to a valid location on your computer.")
                    error.setIcon(QMessageBox.Warning)
                    error.setStandardButtons(QMessageBox.Retry)
                    error.buttonClicked.connect(self.changeFilePath)
                    error.exec_()
            except:
                error = QMessageBox()
                error.setWindowTitle("File Path Error")
                error.setText("There was an error interpreting your file path.")
                error.setInformativeText(
                    " Please make sure your path is pointing to a valid location on your computer.")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Retry)
                error.buttonClicked.connect(self.changeFilePath)
                error.exec_()

    def changeStartData(self):
        """
        Opens a pane to let the user change the starting value of the ID list
        :return:
        """
        newData, done = QInputDialog.getInt(self, "Starting Data Value", "Enter a new starting data value. Only use this if you are getting red parts in your vehicles after generating a pattern.", int(self.startData))
        if newData and done:
            try:
                int(newData)
            except:
                error = QMessageBox()
                error.setWindowTitle("Data Value Error")
                error.setText("There was an error interpreting your data value.")
                error.setInformativeText(
                    " Please make sure your data value is a valid integer.")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Retry)
                error.buttonClicked.connect(self.changeStartData)
                error.exec_()
            self.startData = newData
            #self.partTab.
            with open("RASPP.settings", "r") as f:
                temp = f.readlines()
                temp[1] = str(self.startData) + "\n"
                with open("RASPP.settings", "w") as f:
                    f.writelines(temp)

    def openAbout(self):
        """
        Opens the About Panel
        :return:
        """
        aboutDialog = QDialog()
        aboutDialog.setWindowTitle("About RASPP Utility")
        aboutLabel = QTextBrowser(aboutDialog)
        aboutLabel.setMarkdown(r"""# Repeated Automated Sprocket Part Placement Utility (RASPP)
            Version 0.1.0
This tool allows you to easily place items in the game Sprocket in patterns by modifying the blueprint file for your vehicle. RASPP isn't meant to replace the game, rather be an add on for the people who like to use the blueprint files as a way to edit vehicles.
 ## Authors

 - The game Sprocket is developed by Hamish Dunn, a guy with a ton of skill. Links here:
    - Steam page: [https://store.steampowered.com/app/1674170/Sprocket/](https://store.steampowered.com/app/1674170/Sprocket/)
    - Hamish's GitHub: https://github.com/Muushy
    - Sprocket's Twitter: https://twitter.com/SprocketTheGame
 - A lot of the info for this project came from the official Sprocket Discord and the awesome people there. 
    - Link: https://discord.com/invite/baFH43keyR
- If you want to reach out to me about this program, the best way is to either add an issue to the GitHub repo, or you can contact me on Discord @bobby1321#0770. 
    - Link to GitHub repo: https://github.com/bobby1321/RASPP-Utility""")
        aboutLabel.setMinimumSize(500, 500)
        aboutLabel.setReadOnly(True)
        aboutLabel.setOpenExternalLinks(True)
        aboutDialog.exec_()
        
    def openQuickGuide(self):
        """
        Opens the Quick Guide Pane
        :return:
        """
        self.quickGuideDialog = QDialog()
        self.quickGuideDialog.setWindowTitle("Quick Guide to RASPP Utility")
        quickGuideLabel = QTextEdit(self.quickGuideDialog)
        quickGuideLabel.setMarkdown(r"""## How to use RASPP
Here is a not-so-quick guide on how to use RASPP:

 1. Place the desired part on your vehicle in Sprocket. Make sure to place it where you want the pattern to start, and that it is correctly rotated and scaled the way you want.
 2. Save the vehicle in Sprocket
 3. **SAVE A COPY OF THE VEHICLE BEFORE MAKING ANY CHANGES TO THE BLUEPRINT FILE!** I am not responsible for you messing up your blueprint.
 4. Open your Sprocket blueprints folder, which can be found at `C:\Users\[You]\Documents\My games\Sprocket\Factions\[Your Faction]\Blueprints\Vehicles`
 5. Open the `.blueprint` file of your vehicle
 6. Find the part that you want to clone. This can be tricky, so look at the part reference number (**REF**) (lookup table coming soon) and the compartment ID (**CID**), as well as the location/rotation/scale of the part to try to find the right one.
 7. Copy the part information into RASPP by pasting it in the `Input` popup. It should look like this:
	 ```
	 {
      "REF": "0633ffdf766e3394eb79f8e8a7be24ba",
      "CID": 0,
      "T": [
        -0.46639204,
        0.591725945,
        -3.118866,
        3.58584948E-05,
        89.99991,
        245.606354,
        0.799310863,
        0.500000238,
        0.9819551,
        0.0
      ],
      "DAT": []
    }, 
    ```
    After pasting the information, hit the `OK` button to automatically fill the information into the boxes in RASPP.
    
8. Use the buttons in the top row to select how you want the part to be cloned. You can enter either an amount of parts, or select an axis to move on until a certain coordinate is hit. 
9. Enter increment amounts for each axis you want to be incremented. This value changes how far apart each part is or how much more it is rotated or scaled.
10. Change any values that you want to change. You can move the part, rotate it or scale it (RASPP *cannot* scale parts beyond the limits of the game) however you like. 
11. Select where you want to save the output file and give it a name using `File -> Change Save Location` or `Ctrl + S`
12. Once you have all of your values filled, press the `Go!` button. The output file you saved before should now be populated with parts.
13. **Paste the output over the original part**. Otherwise, you can end up with stacked parts, or any changes you made to the part might not be saved.
14. Save and close the `.blueprint` file. 
15. In Sprocket, open the vehicle you changed. Even if it is already open, re-open it.
16. If you are happy with the changes, save your vehicle in-game. Otherwise, start over and change some numbers.""")
        quickGuideLabel.setMinimumSize(400, 500)
        quickGuideLabel.setReadOnly(True)
        self.quickGuideDialog.setModal(False)
        self.quickGuideDialog.show()

    def openFAQ(self):
        """
        Opens the FAQ Pane
        :return:
        """
        self.FAQDialog = QDialog()
        self.FAQDialog.setWindowTitle("FAQs about RASPP Utility")
        FAQLabel = QTextEdit(self.FAQDialog)
        FAQLabel.setMarkdown("""## FAQ

 - **Q: I have a really good idea of something to add to the program!** A: Great! Submit an issue on the GitHub Repo with the tag `suggestion` and I will try to look at it. If you do want to submit a suggestion, please try to include some rough code or logic that can make your suggestion easier for me to implement. Not required, but helpful.
 - **Q: Where do I find the blueprint files?** A: RTFM.
 - **Q: Where do I look in the file to find a part?** A: Parts are after the `Compartments` and  vehicle options (`SS, TRK, ENG, etc`) sections. If you scroll all the way down to the bottom of the `blueprint` file you can find them and go up from there. You can also look for the "ext" tag in whatever text editor you're using.
 - **Q: My output file is blank!** A: check to make sure that your amount is not zero, or that your limit is not inside of your increment (If you are trying to go from 0.75 to 1.25 in steps of 1, then you can't ever have a part, can you?). Also, make sure you are looking in the correct file. The file location can be found in `File -> Change Save Location`.
 - **Q: How do I know which axis is which / which way negative or positive is?** A: The values are ordered in the `blueprint` the same way they are ordered in RASPP: Position (X, Y, Z), Rotation (X, Y, Z), Scale (X, Y, Z). The X axis is from left to right, with right being positive, Y is up/down with up being positive, and Z is front/back with front being positive.  In the pictures below, X is red, Y is blue and Z is green.

<img src=\"""" + self.resourcePath("img/pos.png") + """\" alt="position" width="250"/> <img src=\"""" + self.resourcePath("img/rot.png") + """\" alt="position" width="250"/> <img src=\"""" + self.resourcePath("img/scale.png") + """\" alt="position" width="250"/> """)
        FAQLabel.setMinimumSize(400, 500)
        FAQLabel.setReadOnly(True)
        self.FAQDialog.setModal(False)
        self.FAQDialog.show()

    def isPathnameValid(self, pathname: str) -> bool:
        """
        `True` if the passed pathname is a valid pathname for the current OS;
        `False` otherwise.
        """

        try:
            if not isinstance(pathname, str) or not pathname:
                return False
            _, pathname = os.path.splitdrive(pathname)

            root_dirname = os.environ.get('HOMEDRIVE', 'C:') \
                if sys.platform == 'win32' else os.path.sep
            assert os.path.isdir(root_dirname)

            root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep

            for pathname_part in pathname.split(os.path.sep):
                try:
                    os.lstat(root_dirname + pathname_part)
                except OSError as exc:
                    if hasattr(exc, 'winerror'):
                        if exc.winerror == 123:
                            return False
                    elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                        return False
        except TypeError as exc:
            return False
        else:
            return True

    def resourcePath(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainUI()
    mainWin.show()
    sys.exit(app.exec_())

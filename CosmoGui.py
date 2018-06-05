#!/usr/bin/python3
# -*- coding: utf-8 -*-
# script CosmoGui.py

''' 
  A simple GUI to edit configuration files and start run via runCosmo.py
'''

import sys, os, time, yaml, threading, subprocess

# Form implementation generated from reading ui file 'CosmoGui.ui'
#    Created by: PyQt5 UI code generator 5.5.1
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CosmoWindow(object):
    def setupUi(self, CosmoWindow):
        CosmoWindow.setObjectName("CosmoWindow")
        CosmoWindow.resize(530, 537)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CosmoWindow.sizePolicy().hasHeightForWidth())
        CosmoWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(CosmoWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_Main = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_Main.setGeometry(QtCore.QRect(-11, 0, 541, 541))
        self.tab_Main.setStatusTip("")
        self.tab_Main.setObjectName("tab_Main")
        self.Tab_Control = QtWidgets.QWidget()
        self.Tab_Control.setWhatsThis("")
        self.Tab_Control.setObjectName("Tab_Control")
        self.label_Picture = QtWidgets.QLabel(self.Tab_Control)
        self.label_Picture.setGeometry(QtCore.QRect(131, 82, 280, 251))
        self.label_Picture.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_Picture.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_Picture.setText("")
        self.label_Picture.setPixmap(QtGui.QPixmap("images/picoCosmo_iconic.jpg"))
        self.label_Picture.setObjectName("label_Picture")
        self.label_caption = QtWidgets.QLabel(self.Tab_Control)
        self.label_caption.setGeometry(QtCore.QRect(90, 60, 401, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_caption.setFont(font)
        self.label_caption.setObjectName("label_caption")
        self.label_DAQconfig = QtWidgets.QLabel(self.Tab_Control)
        self.label_DAQconfig.setGeometry(QtCore.QRect(10, 360, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(11)
        self.label_DAQconfig.setFont(font)
        self.label_DAQconfig.setTextFormat(QtCore.Qt.PlainText)
        self.label_DAQconfig.setObjectName("label_DAQconfig")
        self.lE_DAQConfFile = QtWidgets.QLineEdit(self.Tab_Control)
        self.lE_DAQConfFile.setGeometry(QtCore.QRect(110, 360, 371, 32))
        self.lE_DAQConfFile.setText("")
        self.lE_DAQConfFile.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lE_DAQConfFile.setReadOnly(True)
        self.lE_DAQConfFile.setObjectName("lE_DAQConfFile")
        self.label = QtWidgets.QLabel(self.Tab_Control)
        self.label.setGeometry(QtCore.QRect(30, 470, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.lE_RunTag = QtWidgets.QLineEdit(self.Tab_Control)
        self.lE_RunTag.setGeometry(QtCore.QRect(110, 470, 113, 31))
        self.lE_RunTag.setObjectName("lE_RunTag")
        self.pB_StartRun = QtWidgets.QPushButton(self.Tab_Control)
        self.pB_StartRun.setGeometry(QtCore.QRect(430, 461, 101, 40))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/start.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_StartRun.setIcon(icon)
        self.pB_StartRun.setIconSize(QtCore.QSize(24, 24))
        self.pB_StartRun.setObjectName("pB_StartRun")
        self.pB_FileSelect = QtWidgets.QPushButton(self.Tab_Control)
        self.pB_FileSelect.setGeometry(QtCore.QRect(490, 360, 31, 34))
        self.pB_FileSelect.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/open-folder.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_FileSelect.setIcon(icon1)
        self.pB_FileSelect.setObjectName("pB_FileSelect")
        self.pB_abort = QtWidgets.QPushButton(self.Tab_Control)
        self.pB_abort.setGeometry(QtCore.QRect(454, -1, 80, 41))
        self.pB_abort.setAccessibleDescription("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/application-exit.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_abort.setIcon(icon2)
        self.pB_abort.setIconSize(QtCore.QSize(20, 20))
        self.pB_abort.setAutoDefault(False)
        self.pB_abort.setObjectName("pB_abort")
        self.lE_WorkDir = QtWidgets.QLineEdit(self.Tab_Control)
        self.lE_WorkDir.setGeometry(QtCore.QRect(110, 410, 371, 32))
        self.lE_WorkDir.setObjectName("lE_WorkDir")
        self.label_WorkDir = QtWidgets.QLabel(self.Tab_Control)
        self.label_WorkDir.setGeometry(QtCore.QRect(23, 413, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(11)
        self.label_WorkDir.setFont(font)
        self.label_WorkDir.setObjectName("label_WorkDir")
        self.pB_WDselect = QtWidgets.QPushButton(self.Tab_Control)
        self.pB_WDselect.setGeometry(QtCore.QRect(490, 410, 31, 34))
        self.pB_WDselect.setText("")
        self.pB_WDselect.setIcon(icon1)
        self.pB_WDselect.setObjectName("pB_WDselect")
        self.tab_Main.addTab(self.Tab_Control, "")
        self.Tab_Config = QtWidgets.QWidget()
        self.Tab_Config.setObjectName("Tab_Config")
        self.tabWidget = QtWidgets.QTabWidget(self.Tab_Config)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 821, 501))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(811, 0))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.OsciConfig = QtWidgets.QWidget()
        self.OsciConfig.setObjectName("OsciConfig")
        self.pTE_OsciConfig = QtWidgets.QPlainTextEdit(self.OsciConfig)
        self.pTE_OsciConfig.setGeometry(QtCore.QRect(0, 10, 521, 451))
        self.pTE_OsciConfig.setReadOnly(True)
        self.pTE_OsciConfig.setObjectName("pTE_OsciConfig")
        self.tabWidget.addTab(self.OsciConfig, "")
        self.BMconfig = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BMconfig.sizePolicy().hasHeightForWidth())
        self.BMconfig.setSizePolicy(sizePolicy)
        self.BMconfig.setObjectName("BMconfig")
        self.pTE_BMconfig = QtWidgets.QPlainTextEdit(self.BMconfig)
        self.pTE_BMconfig.setGeometry(QtCore.QRect(4, 10, 521, 451))
        self.pTE_BMconfig.setReadOnly(True)
        self.pTE_BMconfig.setObjectName("pTE_BMconfig")
        self.tabWidget.addTab(self.BMconfig, "")
        self.PulseFilterConfig = QtWidgets.QWidget()
        self.PulseFilterConfig.setObjectName("PulseFilterConfig")
        self.pTE_PFconfig = QtWidgets.QPlainTextEdit(self.PulseFilterConfig)
        self.pTE_PFconfig.setGeometry(QtCore.QRect(0, 10, 521, 451))
        self.pTE_PFconfig.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pTE_PFconfig.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pTE_PFconfig.setReadOnly(True)
        self.pTE_PFconfig.setObjectName("pTE_PFconfig")
        self.tabWidget.addTab(self.PulseFilterConfig, "")
        self.rB_EditMode = QtWidgets.QRadioButton(self.Tab_Config)
        self.rB_EditMode.setGeometry(QtCore.QRect(410, 0, 91, 30))
        self.rB_EditMode.setObjectName("rB_EditMode")
        self.tab_Main.addTab(self.Tab_Config, "")
        self.Tab_Help = QtWidgets.QWidget()
        self.Tab_Help.setObjectName("Tab_Help")
        self.TE_Help = QtWidgets.QTextEdit(self.Tab_Help)
        self.TE_Help.setGeometry(QtCore.QRect(10, 30, 521, 471))
        self.TE_Help.setUndoRedoEnabled(False)
        self.TE_Help.setReadOnly(True)
        self.TE_Help.setPlaceholderText("")
        self.TE_Help.setObjectName("TE_Help")
        self.PB_Help = QtWidgets.QPushButton(self.Tab_Help)
        self.PB_Help.setGeometry(QtCore.QRect(10, 0, 88, 31))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/flagUK.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PB_Help.setIcon(icon3)
        self.PB_Help.setObjectName("PB_Help")
        self.PB_Hilfe = QtWidgets.QPushButton(self.Tab_Help)
        self.PB_Hilfe.setGeometry(QtCore.QRect(110, 0, 88, 31))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/flagDE.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PB_Hilfe.setIcon(icon4)
        self.PB_Hilfe.setObjectName("PB_Hilfe")
        self.tab_Main.addTab(self.Tab_Help, "")
        CosmoWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CosmoWindow)
        self.tab_Main.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CosmoWindow)

    def retranslateUi(self, CosmoWindow):
        _translate = QtCore.QCoreApplication.translate
        CosmoWindow.setWindowTitle(_translate("CosmoWindow", "CosmoGui"))
        self.tab_Main.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>Output  / Configuration / Help</p></body></html>"))
        self.Tab_Control.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>Control Panel</p></body></html>"))
        self.label_caption.setText(_translate("CosmoWindow", "Kamiokanne & CosMO Detector with PicoScope"))
        self.label_DAQconfig.setText(_translate("CosmoWindow", "DAQ config:"))
        self.lE_DAQConfFile.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>DAQ configuration file (type .daq)</p></body></html>"))
        self.label.setText(_translate("CosmoWindow", "Run Tag:"))
        self.lE_RunTag.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>Name for the run</p></body></html>"))
        self.lE_RunTag.setText(_translate("CosmoWindow", "CosmoRun"))
        self.pB_StartRun.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>Start Runinng Oscilloscope, Buffer Manager and Pulse Filter</p></body></html>"))
        self.pB_StartRun.setText(_translate("CosmoWindow", "StartRun"))
        self.pB_FileSelect.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>selecd daq configuration file</p></body></html>"))
        self.pB_abort.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>Exit CosmoGui</p></body></html>"))
        self.pB_abort.setText(_translate("CosmoWindow", "Abort"))
        self.label_WorkDir.setText(_translate("CosmoWindow", "Work Dir:"))
        self.pB_WDselect.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>select working directory (where ouput is stored)</p></body></html>"))
        self.tab_Main.setTabText(self.tab_Main.indexOf(self.Tab_Control), _translate("CosmoWindow", "Control"))
        self.Tab_Config.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>Config Panel</p></body></html>"))
        self.tabWidget.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>Configuration Files</p></body></html>"))
        self.pTE_OsciConfig.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>Comnfiguration File for Oscilloscope</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.OsciConfig), _translate("CosmoWindow", "OsciConfig"))
        self.pTE_BMconfig.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>Configuration File for Buffer Manager</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BMconfig), _translate("CosmoWindow", "BMconfig"))
        self.pTE_PFconfig.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>Configuration File for Pulse Filter and Analysis</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PulseFilterConfig), _translate("CosmoWindow", "PulseFilterConfig"))
        self.rB_EditMode.setText(_translate("CosmoWindow", "Edit Mode"))
        self.tab_Main.setTabText(self.tab_Main.indexOf(self.Tab_Config), _translate("CosmoWindow", "Configuration"))
        self.Tab_Help.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>Info &amp; Help</p></body></html>"))
        self.PB_Help.setText(_translate("CosmoWindow", "English"))
        self.PB_Hilfe.setText(_translate("CosmoWindow", "Deutsch"))
        self.tab_Main.setTabText(self.tab_Main.indexOf(self.Tab_Help), _translate("CosmoWindow", "Help / Hilfe"))



# --> code not generated by designer-qt5 and pyuic5 starts here --> 

        self.Window = CosmoWindow

# set help 
        self.setHelp_EN()

# set font for plainTextEdit to monospace
        monofont = QtGui.QFont()
        monofont.setStyleHint(QtGui.QFont.TypeWriter)
        monofont.setFamily("unexistentfont")        
        self.pTE_OsciConfig.setFont(monofont)
        self.pTE_BMconfig.setFont(monofont)
        self.pTE_PFconfig.setFont(monofont)

# set default Working Directory
        self.WDname = os.getenv('HOME')
        self.lE_WorkDir.setText(self.WDname)

# define actions
        self.pB_abort.clicked.connect(QtCore.QCoreApplication.instance().quit) 
        self.rB_EditMode.clicked.connect(self.actionEditConfig) 
        self.pB_StartRun.clicked.connect(self.actionStartRun) 
        self.pB_FileSelect.clicked.connect(self.selectConfigFile)
        self.pB_WDselect.clicked.connect(self.selectWD)
        self.PB_Help.clicked.connect(self.setHelp_EN)
        self.PB_Hilfe.clicked.connect(self.setHelp_DE)

    def setHelp_DE(self):
      self.TE_Help.setText(open('doc/Hilfe.html', 'r').read() ) 

    def setHelp_EN(self):
      self.TE_Help.setText(open('doc/help.html', 'r').read() )

    def initDAQ(self, DAQconfFile):
      try:
        with open(DAQconfFile) as f:
          DAQconfdict=yaml.load(f)
      except:
        print('     failed to read DAQ configuration file ' + DAQconfFile)
        exit(1)

      self.lE_DAQConfFile.setText(DAQconfFile)
      print('   - DAQ configuration from file ' + DAQconfFile)

      if "DeviceFile" in DAQconfdict: 
        PSfile = DAQconfdict["DeviceFile"] # configuration file for scope
      else:
        print('     no device configuration file - exiting')
        exit(1)

      if "BMfile" in DAQconfdict: 
        BMfile = DAQconfdict["BMfile"] # Buffer Manager configuration file 
      else:
        print('     no BM configuration file - exiting')
        exit(1)

      if "PFfile" in DAQconfdict: 
        PFfile = DAQconfdict["PFfile"] # Buffer Manager configuration file 
      else:
        print('     no pulse filter configuration file - exiting')
        exit(1)

   # display config data in GUI
      self.pTE_OsciConfig.setPlainText(open(PSfile, 'r').read() )
      self.pTE_BMconfig.setPlainText(open(BMfile, 'r').read() )
      self.pTE_PFconfig.setPlainText(open(PFfile, 'r').read() )

# - end iniDAQ

    def selectConfigFile(self):
      path2File = QtWidgets.QFileDialog.getOpenFileName(None,
         'DAQ config', './', 'DAQ(*.daq)')
      FileName = str(path2File[0])
      if FileName is not '' :
        # print('selected File ' + str(FileName) )
        self.initDAQ(FileName)

    def selectWD(self):
      path2WD = QtWidgets.QFileDialog.getExistingDirectory(None, '~')
      WDname = str(path2WD)
      if WDname is not '' :
        # print('selected Directory' + WDname )
         self.lE_WorkDir.setText(WDname)
         self.WDname = WDname

    def actionEditConfig(self):
        checked = self.rB_EditMode.isChecked()
        self.pTE_OsciConfig.setReadOnly(not checked)
        self.pTE_BMconfig.setReadOnly(not checked)
        self.pTE_PFconfig.setReadOnly(not checked)

    def actionStartRun(self):
        # start script runCosmo.py in subdirectory

        # time stamp for this run
        datetime=time.strftime('%y%m%d-%H%M', time.localtime())
        RunTag = str(self.lE_RunTag.text() ).replace(' ','')

        # retrieve actual configuration from GUI
        PSconf = self.pTE_OsciConfig.toPlainText() 
        BMconf = self.pTE_BMconfig.toPlainText() 
        PFconf = self.pTE_PFconfig.toPlainText() 

        # generate config files for new run in dedicated subdirectory
        self.runDir = (RunTag + '_' + datetime)
        if not os.path.exists(self.WDname + '/' + self.runDir): 
          os.makedirs(self.WDname + '/' + self.runDir)

        PSfile = RunTag + '_PSconf.yaml'
        fPS = open(self.WDname + '/' + self.runDir + '/' + PSfile, 'w')
        print(PSconf, file = fPS )
        fPS.close()

        BMfile = RunTag + '_BMconf.yaml'
        fBM = open(self.WDname + '/' + self.runDir + '/' + BMfile, 'w')
        print(BMconf, file = fBM )
        fBM.close()

        PFfile = RunTag + '_PFconf.yaml'
        fPF = open(self.WDname + '/' +self.runDir + '/' + PFfile, 'w')
        print(PFconf, file = fPF )
        fPF.close()

        self.DAQfile = RunTag + '.daq'
        fDAQ = open(self.WDname + '/' + self.runDir + '/' + self.DAQfile,'w')
        print('DeviceFile: ' + PSfile + '\n' +
              'BMfile: ' + BMfile + '\n' +
              'PFfile: ' + PFfile + '\n',
               file = fDAQ )
        fDAQ.close()
        print("   - files for this run stored in directory "\
               + self.WDname + '/' + self.runDir) 
    # close GUI window and start runCosmo 
        print('\n*==* CosmoGui: closing window and starting runCosmo.py')
        self.Window.close()

        # start runCosmo
        self.start_runCosmo()

        QtCore.QCoreApplication.instance().quit()
        print('*==* CosmoGui: exit \n')
              
    def start_runCosmo(self):
        CosmoDir = os.getcwd()
        subprocess.call([CosmoDir + '/runCosmo.py ' + self.DAQfile],
                      cwd = self.WDname + '/' + self.runDir, shell = True)
        
# - end Class Ui_CosmoWindow

if __name__ == "__main__": # - - - - - - - - - - - - - - - - - - - -

  print('\n*==* ' + sys.argv[0] + ' running \n')

# check for / read command line arguments
  # read DAQ configuration file
  if len(sys.argv)==2:
    DAQconfFile = sys.argv[1]
  else: 
    DAQconfFile = 'default.daq'

# start GUI
  app = QtWidgets.QApplication(sys.argv)
  MainWindow = QtWidgets.QMainWindow()
  ui = Ui_CosmoWindow()
  ui.setupUi(MainWindow)

  ui.initDAQ(DAQconfFile)

  MainWindow.show()
  sys.exit(app.exec_())

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
        CosmoWindow.resize(500, 515)
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
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 881, 461))
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
        self.pTE_OsciConfig.setGeometry(QtCore.QRect(10, 10, 491, 471))
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
        self.pTE_BMconfig.setGeometry(QtCore.QRect(10, 10, 491, 461))
        self.pTE_BMconfig.setReadOnly(True)
        self.pTE_BMconfig.setObjectName("pTE_BMconfig")
        self.tabWidget.addTab(self.BMconfig, "")
        self.PulseFilterConfig = QtWidgets.QWidget()
        self.PulseFilterConfig.setObjectName("PulseFilterConfig")
        self.pTE_PFconfig = QtWidgets.QPlainTextEdit(self.PulseFilterConfig)
        self.pTE_PFconfig.setGeometry(QtCore.QRect(10, 10, 491, 461))
        self.pTE_PFconfig.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pTE_PFconfig.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pTE_PFconfig.setReadOnly(True)
        self.pTE_PFconfig.setObjectName("pTE_PFconfig")
        self.tabWidget.addTab(self.PulseFilterConfig, "")
        self.pB_StartRun = QtWidgets.QPushButton(self.centralwidget)
        self.pB_StartRun.setGeometry(QtCore.QRect(390, 465, 101, 40))
        self.pB_StartRun.setObjectName("pB_StartRun")
        self.rB_EditMode = QtWidgets.QRadioButton(self.centralwidget)
        self.rB_EditMode.setGeometry(QtCore.QRect(10, 456, 91, 30))
        self.rB_EditMode.setObjectName("rB_EditMode")
        self.lE_RunTag = QtWidgets.QLineEdit(self.centralwidget)
        self.lE_RunTag.setGeometry(QtCore.QRect(259, 471, 113, 31))
        self.lE_RunTag.setObjectName("lE_RunTag")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(205, 471, 51, 30))
        self.label.setObjectName("label")
        CosmoWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CosmoWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(CosmoWindow)

    def retranslateUi(self, CosmoWindow):
        _translate = QtCore.QCoreApplication.translate
        CosmoWindow.setWindowTitle(_translate("CosmoWindow", "CosmoGui"))
        self.tabWidget.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>Configuration Files</p></body></html>"))
        self.pTE_OsciConfig.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>Comnfiguration File for Oscilloscope</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.OsciConfig), _translate("CosmoWindow", "OsciConfig"))
        self.pTE_BMconfig.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>Configuration File for Buffer Manager</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BMconfig), _translate("CosmoWindow", "BMconfig"))
        self.pTE_PFconfig.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>Configuration File for Pulse Filter and Analysis</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PulseFilterConfig), _translate("CosmoWindow", "PulseFilterConfig"))
        self.pB_StartRun.setToolTip(_translate("CosmoWindow", "<html><head/><body><p>Start Runinng Oscilloscope, Buffer Manager and Pulse Filter</p></body></html>"))
        self.pB_StartRun.setText(_translate("CosmoWindow", "StartRun"))
        self.rB_EditMode.setText(_translate("CosmoWindow", "Edit Mode"))
        self.lE_RunTag.setText(_translate("CosmoWindow", "CosmoRun"))
        self.label.setText(_translate("CosmoWindow", "Run Tag:"))


# --> code not generated by designer-qt5 and pyuic5 starts here --> 

# set font for plainTextEdit to monospace
        monofont = QtGui.QFont()
        monofont.setStyleHint(QtGui.QFont.TypeWriter)
        monofont.setFamily("unexistentfont")        
        self.pTE_OsciConfig.setFont(monofont)
        self.pTE_BMconfig.setFont(monofont)
        self.pTE_PFconfig.setFont(monofont)

# define actions
        self.rB_EditMode.clicked.connect(self.actionEditConfig) 
        self.pB_StartRun.clicked.connect(self.actionStartRun) 

    def actionEditConfig(self):
        checked = self.rB_EditMode.isChecked()
        self.pTE_OsciConfig.setReadOnly(not checked)
        self.pTE_BMconfig.setReadOnly(not checked)
        self.pTE_PFconfig.setReadOnly(not checked)

    def actionStartRun(self):
        # start script runCosmo.py in subdirectory

        # time stamp for this run
        datetime=time.strftime('%y%m%d-%H%M', time.localtime())
        RunTag = str(self.lE_RunTag.text() )
        self.runDir = (RunTag + '_' + datetime)
        if not os.path.exists(self.runDir): os.makedirs(self.runDir)

        # retrieve configuration
        PSconf = self.pTE_OsciConfig.toPlainText() 
        BMconf = self.pTE_BMconfig.toPlainText() 
        PFconf = self.pTE_PFconfig.toPlainText() 
        # generate config files for new run in dedicated subdirectory
        fPS = open(self.runDir + '/PSconf.yaml', 'w')
        fBM = open(self.runDir + '/BMconf.yaml', 'w')
        fPF = open(self.runDir + '/PFconf.yaml', 'w')
        fDAQ = open(self.runDir + '/DAQconf.yaml', 'w')
        print(PSconf, file = fPS )
        print(BMconf, file = fBM )
        print(PFconf, file = fPF )
        print('DeviceFile: PSconf.yaml \n' +
              'BMfile: BMconf.yaml \n' +
              'PFfile: PFconf.yaml \n',
               file = fDAQ )
        fDAQ.close()
        fPS.close()
        fBM.close()
        fPF.close()

        print("CosmoGui: files for this run stored in directory " + self.runDir) 
        t = threading.Thread(target=self.spawn_runCosmo)
        t.daemon = True
        t.start()

        # quit from this GUI
        print('*==* CosmoGui: ending')
        QtCore.QCoreApplication.instance().quit()

    def spawn_runCosmo(self):
      # start runCosmo
      subprocess.call(['../runCosmo.py' + ' DAQconf.yaml'], 
                      cwd = self.runDir, shell = True)

# - end Class Ui_CosmoWindow

if __name__ == "__main__": # - - - - - - - - - - - - - - - - - - - -

  print('\n*==* ' + sys.argv[0] + ' running \n')

# check for / read command line arguments
  # read DAQ configuration file
  if len(sys.argv)==2:
    DAQconfFile = sys.argv[1]
  else: 
    DAQconfFile = 'DAQconfig.yaml'
  print('    DAQconfiguration from file ' + DAQconfFile)
  try:
    with open(DAQconfFile) as f:
      DAQconfdict=yaml.load(f)
  except:
    print('     failed to read DAQ configuration file ' + DAQconfFile)
    exit(1)

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

# initialization 
  txt_OscConfig = open(PSfile, 'r').read()
  txt_BMconfig = open(BMfile, 'r').read()
  txt_PFconfig = open(PFfile, 'r').read()
  
# start GUI
  app = QtWidgets.QApplication(sys.argv)
  MainWindow = QtWidgets.QMainWindow()
  ui = Ui_CosmoWindow()
  ui.setupUi(MainWindow)

# display config data in GUI
  ui.pTE_OsciConfig.setPlainText(txt_OscConfig)
  ui.pTE_BMconfig.setPlainText(txt_BMconfig)
  ui.pTE_PFconfig.setPlainText(txt_PFconfig)

  MainWindow.show()
  sys.exit(app.exec_())


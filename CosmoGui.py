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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 530)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(-10, -10, 881, 501))
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
        self.pTE_OsciConfig.setGeometry(QtCore.QRect(10, 10, 481, 471))
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
        self.pTE_BMconfig.setGeometry(QtCore.QRect(10, 10, 481, 461))
        self.pTE_BMconfig.setReadOnly(True)
        self.pTE_BMconfig.setObjectName("pTE_BMconfig")
        self.tabWidget.addTab(self.BMconfig, "")
        self.PulseFilterConfig = QtWidgets.QWidget()
        self.PulseFilterConfig.setObjectName("PulseFilterConfig")
        self.pTE_PFconfig = QtWidgets.QPlainTextEdit(self.PulseFilterConfig)
        self.pTE_PFconfig.setGeometry(QtCore.QRect(10, 10, 481, 461))
        self.pTE_PFconfig.setReadOnly(True)
        self.pTE_PFconfig.setObjectName("pTE_PFconfig")
        self.tabWidget.addTab(self.PulseFilterConfig, "")
        self.pB_StartRun = QtWidgets.QPushButton(self.centralwidget)
        self.pB_StartRun.setGeometry(QtCore.QRect(307, 490, 171, 34))
        self.pB_StartRun.setObjectName("pB_StartRun")
        self.rB_EditMode = QtWidgets.QRadioButton(self.centralwidget)
        self.rB_EditMode.setGeometry(QtCore.QRect(10, 490, 91, 23))
        self.rB_EditMode.setObjectName("rB_EditMode")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CosmoGui"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p>Configuration Files</p></body></html>"))
        self.pTE_OsciConfig.setToolTip(_translate("MainWindow", "<html><head/><body><p>Comnfiguration File for Oscilloscope</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.OsciConfig), _translate("MainWindow", "OsciConfig"))
        self.pTE_BMconfig.setToolTip(_translate("MainWindow", "<html><head/><body><p>Configuration File for Buffer Manager</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BMconfig), _translate("MainWindow", "BMconfig"))
        self.pTE_PFconfig.setToolTip(_translate("MainWindow", "<html><head/><body><p>Configuration File for Pulse Filter and Analysis</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PulseFilterConfig), _translate("MainWindow", "PulseFilterConfig"))
        self.pB_StartRun.setToolTip(_translate("MainWindow", "<html><head/><body><p>Start Runinng Oscilloscope, Buffer Manager and Pulse Filter</p></body></html>"))
        self.pB_StartRun.setText(_translate("MainWindow", "StartRun"))
        self.rB_EditMode.setText(_translate("MainWindow", "Edit Mode"))

# --> code not generated by designer-qt5 and pyuic5 starts here --> 


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
        self.rDir = ('CosmoRun' + '_' + datetime)
        if not os.path.exists(self.rDir): os.makedirs(self.rDir)

        # retrieve configuration
        PSconf = self.pTE_OsciConfig.toPlainText() 
        BMconf = self.pTE_BMconfig.toPlainText() 
        PFconf = self.pTE_PFconfig.toPlainText() 
        # generate config files for new run in dedicated subdirectory
        fPS = open(self.rDir + '/PSconf.yaml', 'w')
        fBM = open(self.rDir + '/BMconf.yaml', 'w')
        fPF = open(self.rDir + '/PFconf.yaml', 'w')
        fDAQ = open(self.rDir + '/DAQconf.yaml', 'w')
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

        t = threading.Thread(target=self.spawn_runCosmo)
        t.daemon = True
        t.start()

        # quit from this GUI
        print('*==* CosmoGui: ending')
        QtCore.QCoreApplication.instance().quit()

    def spawn_runCosmo(self):
    # start runCosmo
      subprocess.call(['../runCosmo.py' + ' DAQconf.yaml'], 
                      cwd = self.rDir, shell = True)

# - end Class Ui_MainWindow

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
  ui = Ui_MainWindow()
  ui.setupUi(MainWindow)

# display config data in GUI
  ui.pTE_OsciConfig.setPlainText(txt_OscConfig)
  ui.pTE_BMconfig.setPlainText(txt_BMconfig)
  ui.pTE_PFconfig.setPlainText(txt_PFconfig)

  MainWindow.show()
  sys.exit(app.exec_())


# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:36:13 2016
@author: Mateusz Grzeliński
"""
import sys, os, json
from time import clock
from random import randint
#from PyQt4 import QtOpenGL
from PyQt4 import QtGui, QtCore
from GameUI20 import Ui_MainWindow
from WindowRules1 import Ui_RuleEditorWidget


class CellItem(QtGui.QGraphicsRectItem):
    def __init__(self, a,b,c,d,i=0,j=0 ):
        super().__init__(a,b,c,d)
        self._i= i
        self._j= j                  #do kliknięcia
        self._status=False
        self._status_prev=False     #do liczenia kolejnego pokolenia 
        self._plag=False
        self._plag_prev=False
        self._backup_gen=False      #do guzika Back to begining
        self._backup_gen_plag=False #do guzika Back to begining

    def changeCell(self):
        if self._status == True:
            self._status_prev = False
            self._status = False
            self._plag = False
            self._plag_prev = False
        else:
            self._status_prev = True
            self._status = True
    def changeCellPlag(self):
        if ( ui.PlagueCheckBox.isChecked()  ):
            if self._plag == True:
                self._plag = False
                self._plag_prev = False
            else:
                self._plag = True
                self._plag_prev = True
                self._status_prev = True
                self._status = True
    def mousePressEvent(self, event):
        global BOXES
        if event.button() == QtCore.Qt.LeftButton:
            self.changeCell()
        if event.button() == QtCore.Qt.RightButton:
            self.changeCellPlag()
        ui.DrawChangeSingle(self._i,self._j)
   
class MeasureTime():
    _time = 0.0
    _startTime = 0.0
    def start(self):
        self._startTime= clock()
    def stop(self):
        self._time = clock() - self._startTime
    def getTime(self):
        return self._time
                   
class MainWindow(QtGui.QMainWindow,  Ui_MainWindow):
    RulesTabDies = "0,1,4,5,6,7"   #ktore komorki umieraj, a musza tu byc te zmienne, bez self.
    RulesTabBorn = "3"        #ktore komorki rodza sie  
    def __init__(self):
        global BOXES
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        if (not os.path.exists("GamePresets/")):
            os.mkdir("GamePresets/")
        if (not os.path.exists("RulePresets/")):
            os.mkdir("RulePresets/")
        self.last_rules_preset="Normal" #czemu nie laduje za pierwszym razem?
        self.generation = 0
        self.rows       = 10
        self.columns    = 10
        self.cel_size   = 20
        self.checked    = QtGui.QBrush(QtGui.QColor(220,220,240))
        self.unchecked  = QtGui.QBrush(QtGui.QColor(40,40,45))
        self.plague     = QtGui.QBrush(QtGui.QColor(220,100,150))
        self.fps        = 1000/self.FPSSpinBox.value()
        self.watch      = MeasureTime()
        self.timer      = QtCore.QTimer()    #do autogeneracji
        self.timer.timeout.connect(self.WhichTick)
        #self.setMouseTracking(True) niepotrzebne
        self.graphicsScene = QtGui.QGraphicsScene()
        self.graphicsScene.setSceneRect(0,0,400,300)
        self.graphicsView.setScene(self.graphicsScene)
#        self.graphicsView.setViewport(QtOpenGL.QGLWidget()) #obliczenia na karcie graficznej- nie zmienia duzo
        #init cells:
        BOXES = [ [CellItem(self.cel_size*j,self.cel_size*i,self.cel_size,self.cel_size, i, j) for j in range(self.columns)] for i in range(self.rows)]
        self.DrawGrid()
        
        self.LoadPresetsNames()
        self.RemovePreset.clicked.connect(self.DeletePreset)
        self.SaveState.clicked.connect(self.SavePreset)
        self.ChoicePresets.activated.connect(self.ReadPreset)
        self.EditRules.clicked.connect(self.EditRulesWindow)
        self.FPSSpinBox.valueChanged.connect(self.UpdateFPS)
        self.StartStop.clicked.connect(self.ToogleAutoGen)
        self.RandomInfection.clicked.connect(self.RandomizePlag)
        self.RandomStart.clicked.connect(self.Randomize)
        self.ToBegin.clicked.connect(self.ToBeginning)
        self.Blank.clicked.connect( self.NewLife )
        self.PlagueCheckBox.stateChanged.connect(self.PlagRandomActivate)
        self.RowsColumsCheckBox.stateChanged.connect(self.SetSquare)
        self.RowsSpinBox.valueChanged.connect(self.UpdateValues)
        self.ColumnsSpinBox.valueChanged.connect(self.UpdateValues)
        self.Tick.clicked.connect(self.WhichTick)
        self.graphicsView.setSceneRect(0,0,self.cel_size*self.rows,self.cel_size*self.columns)
        #self.graphicsView.setSceneRect(self.graphicsScene.itemsBoundingRect())
        self.ScaleIn.clicked.connect(self.scaleViewIn)
        self.ScaleOut.clicked.connect(self.scaleViewOut)
    def LoadPresetsNames(self): #add presets to ComboBox
        for file in os.listdir("GamePresets"):
            self.ChoicePresets.addItem(os.path.splitext(file)[0])  #nazwy plikow bez rozszerzen
    def SavePreset(self):
        filename, ok = QtGui.QInputDialog.getText(self, 'Save Game Preset', 'Enter preset name:')
        flag=True 
        if ok:
            if (len(filename)==1 or ('.' in filename)): #sprawdz czy nazwa wprowadzona jest dobrze
                flag=False
                msg = QtGui.QMessageBox()
                msg.setIcon(QtGui.QMessageBox.Warning)
                msg.setWindowTitle("Error!")
                msg.setText("Preset not saved!\nFile name specified incorrectly")
                msg.Ok
                msg.exec_()    
            else: #sprawdz czy plik juz istnieje
                for file in os.listdir("GamePresets"):
                    if filename in os.path.splitext(file)[0] :
                        flag=False
                        msg = QtGui.QMessageBox()
                        msg.setIcon(QtGui.QMessageBox.Warning)
                        msg.setWindowTitle("Error!")
                        msg.setText("Preset not saved!\nFile with this name arleady exsists ")
                        msg.Ok
                        msg.exec_()
                        break
        if flag: 
            global BOXES
            self.ChoicePresets.addItem(filename)
            self.ChoicePresets.setCurrentIndex(self.ChoicePresets.findText(filename))
            with open("GamePresets/"+filename, 'w') as newfile:
                status = [[json.dumps(BOXES[i][j]._status) for i in range(self.rows)] for j in range(self.columns)]
                json.dump(self.rows, newfile)
                newfile.write('\n')
                json.dump(self.columns, newfile)
                newfile.write('\n')
                json.dump(self.RowsColumsCheckBox.isChecked(), newfile)
                newfile.write('\n')
                json.dump(status, newfile)
                newfile.write('\n')
                json.dump(self.PlagueCheckBox.isChecked(), newfile)
                newfile.write('\n') 
                if self.PlagueCheckBox.isChecked() :
                    plag   = [[json.dumps(BOXES[i][j]._plag)   for i in range(self.rows)] for j in range(self.columns)]
                    json.dump(plag, newfile)
                    
    def ReadPreset(self):
        global BOXES
        with open("GamePresets/"+self.ChoicePresets.currentText(), 'r') as readfile: 
            self.rows   = json.loads( readfile.readline() ) #ilosc wierszy 
            self.columns= json.loads( readfile.readline() ) #ilosc kolumn
            self.RowsColumsCheckBox.setChecked( json.loads( readfile.readline() ))
            #self.RowsSpinBox.setProperty("value", self.rows)
            if self.RowsColumsCheckBox.isChecked() :
                self.RowsSpinBox.setValue(self.rows)
            else:
                self.RowsSpinBox.setValue(self.rows)
                self.ColumnsSpinBox.setValue(self.columns)
            self.UpdateValues()
            
            tmp = json.loads( readfile.readline() ) #status komorek(tablica)
            for i in range(self.rows):
                for j in range(self.columns):
                    if tmp[i][j]=="true" :
                        BOXES[i][j]._status = True
                        BOXES[i][j]._status_prev   = True
                    else:
                        BOXES[i][j]._status = False
                        BOXES[i][j]._status_prev   = False
            self.PlagueCheckBox.setChecked( json.loads( readfile.readline() )) #wczytuje status checkboxa do plagi
            self.PlagRandomActivate() #aktywuje lub dezaktywuje plage
            if self.PlagueCheckBox.isChecked() :
                tmp=json.loads( readfile.readline() ) #wczytuje tablice plagi
                for i in range(self.rows):
                    for j in range(self.columns):
                        if tmp[i][j]=="true" :
                            BOXES[i][j]._plag = True
                            BOXES[i][j]._plag_prev   = True
                        else:
                            BOXES[i][j]._plag = False
                            BOXES[i][j]._plag_prev   = False
        self.DrawChange() #zmienia ustawienia rows, columns, rysuje siatke i kolory
        
    def DeletePreset(self):
        choice = QtGui.QMessageBox.question(self, 'Delete preset: '+ self.ChoicePresets.currentText(), "Are you sure?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Deleting current preset...",self.ChoicePresets.currentText())
            os.remove("GamePresets/"+self.ChoicePresets.currentText())
            self.ChoicePresets.removeItem(self.ChoicePresets.currentIndex())
    def UpdateFPS(self):    
        self.fps = 1000/self.FPSSpinBox.value()
        self.ToogleAutoGen() #zresetuj zegar
        self.ToogleAutoGen()
    def ToogleAutoGen(self):
        if self.timer.isActive()==True:
            self.timer.stop()
        else:
            self.timer.start( self.fps )
    def PlagRandomActivate(self):
        if ( self.PlagueCheckBox.isChecked() ):
            self.RandomInfection.setEnabled(True)
        else:
            global BOXES
            self.RandomInfection.setEnabled(False)
            for i in range(self.rows):      #wymaz wszyskie plagi
                for j in range(self.columns):
                    BOXES[i][j]._plag = False
                    BOXES[i][j]._plag_prev = False
            self.DrawChange()
    def Randomize(self):
        global BOXES
        for i in range(self.rows):
            for j in range(self.columns):
                if (randint(-50,25)>0): #ustawianie prawdopodobienstwa
                    BOXES[i][j]._status = True
                    BOXES[i][j]._status_prev = True
                else:
                    BOXES[i][j]._status =False
                    BOXES[i][j]._status_prev =False
        self.DrawChange()
    def RandomizePlag(self):
        global BOXES
        for i in range(self.rows):
            for j in range(self.columns):
                if (randint(-50,3)>0 and BOXES[i][j]._status):
                    BOXES[i][j]._plag = True
                    BOXES[i][j]._plag_prev = True
                else:
                    BOXES[i][j]._plag = False
                    BOXES[i][j]._plag_prev = False
        self.DrawChange()
        
    def ToBeginning(self):
        global BOXES
        self.timer.stop()
        self.generation=0
        self.LGeneration.setText("Generation: "+str(self.generation) )
        for i in range(self.rows):
            for j in range(self.columns):
                BOXES[i][j]._status     = BOXES[i][j]._backup_gen
                BOXES[i][j]._status_prev= BOXES[i][j]._backup_gen
                BOXES[i][j]._plag       = BOXES[i][j]._backup_gen_plag
                BOXES[i][j]._plag_prev  = BOXES[i][j]._backup_gen_plag
        self.DrawChange()
        
    def UpdateValues(self):
        global BOXES
        self.rows = self.RowsSpinBox.value()
        if( self.RowsColumsCheckBox.isChecked() ):
            self.columns = self.rows
            self.ColumnsSpinBox.setValue(self.columns)
        else:
            self.columns = self.ColumnsSpinBox.value()
        BOXES = [ [CellItem(self.cel_size*j,self.cel_size*i,self.cel_size,self.cel_size, i, j) for j in range(self.columns)] for i in range(self.rows)]
        self.DrawGrid()

    def getAmountOfNeighbs(self,x,y):
        neighbors = 0
        global BOXES        
        for diffX in {-1,0,1}:
            for diffY in {-1,0,1}:
                nX = x + diffX
                nY = y + diffY
                #czy jestem dalej w obszarze tablicy:
                if nX >= 0 and nY >= 0 and nX < self.rows and nY < self.columns:
                    if (BOXES[nX][nY]._status_prev==True and not (diffX == diffY == 0)) :
                        neighbors += 1
        #if neighbors>0: 
            #print ("sasiad: ",x,y,neighbors,IsSick,)
        return neighbors
    def WhichTick(self):
        self.watch.start()
        if (self.generation==0): #ustawianie pkt powrotu Back to beginning 
            for i in range(self.rows):
                for j in range(self.columns):
                    BOXES[i][j]._backup_gen = BOXES[i][j]._status 
                    BOXES[i][j]._backup_gen_plag = BOXES[i][j]._plag
        #----------------------------------------------------------------------
        if self.PlagueCheckBox.isChecked():
            self.TickGenPlag()  #wolniejsza wersja
        else:
            self.TickGen()      #szybsza wersja
        #----------------------------------------------------------------------
        for i in range(self.rows): #potrzebne do generacji kolejnego pokolenia
            for j in range(self.columns):#zwykle przepisanie wartosci
                BOXES[i][j]._status_prev = BOXES[i][j]._status
                BOXES[i][j]._plag_prev   = BOXES[i][j]._plag
        self.DrawChange()
        self.watch.stop()
        self.generation+=1
        self.LGeneration.setText("Generation: "+str(self.generation) )
        if (1/self.FPSSpinBox.value()<self.watch.getTime()):
            self.LDelay.setText("Last generation took:\n"+ "{0:.3f}".format(self.watch.getTime()) + " sec.to calculate"+"\nNot reatlime")
        else:
            self.LDelay.setText("Last generation took:\n"+ "{0:.3f}".format(self.watch.getTime()) + " sec.to calculate")
        
    def TickGen(self):
        global BOXES
        for i in range(self.rows): 
            for j in range(self.columns):
                neighbours = self.getAmountOfNeighbs(i,j)
                if  ( (str(neighbours) in self.RulesTabDies)):
                    BOXES[i][j]._status  = False
                elif ( (str(neighbours) in self.RulesTabBorn)):
                    BOXES[i][j]._status = True
                
    def IfSick(self, x, y): #czy komorka bedzie chora
        sick = False
        #czy w okolo komorki jest zarazona komorka
        for diffX in {-1,0,1}:
            for diffY in {-1,0,1}:
                nX = x + diffX
                nY = y + diffY
                if nX >= 0 and nY >= 0 and nX < self.rows and nY < self.columns:
                    if BOXES[nX][nY]._plag_prev and not (diffX==diffY==0):
                        sick = True
                        return sick
        return sick
    def TickGenPlag(self):
        global BOXES
        for i in range(self.rows): 
            for j in range(self.columns):
                neighbours = self.getAmountOfNeighbs(i,j)
                if  ((str(neighbours) in self.RulesTabDies)) or BOXES[i][j]._plag_prev:
                    BOXES[i][j]._status  = False
                    BOXES[i][j]._plag    = False
                elif (str(neighbours) in self.RulesTabBorn) :
                    BOXES[i][j]._status = True
                if BOXES[i][j]._status: #czy kom zyje
                    sick = self.IfSick(i,j) #czy kom edzie chora
                    if sick : #czy zyjaca komorka stanie sie chora
                        BOXES[i][j]._plag = True
        
    def NewLife(self):  #zresetuj wszystko oprocz wartosci 
        global BOXES
        self.timer.stop() #zatrzymuje automatuczna generacje
        self.generation=0
        self.LGeneration.setText("Generation: "+str(self.generation) )
        for i in range(self.rows):
            for j  in range(self.columns):
                BOXES[i][j]._status = False
                BOXES[i][j]._status_prev = False
                BOXES[i][j]._plag = False
        self.DrawChange()
                
                
    def DrawGrid(self):     #wywolywane wtedu gdy zmienia sie rozmiar tablicy
        #todo zmienic definicje tablicy na append i del, dodać remove item i usunac scene.clear()
        global BOXES
        self.graphicsView.setSceneRect(0,0,self.cel_size*self.columns, self.cel_size*self.rows)
        self.graphicsScene.clear() #potrzebne gdy usuwam elementy
        for i in range(self.rows):
            for j  in range(self.columns):
                self.graphicsScene.addItem(BOXES[i][j])
        #self.graphicsView.centerOn(BOXES[self.rows//2][self.columns//2])
        self.DrawChange()
    
    def DrawChange(self):   #rysuje wszystkie kolory dla calej tablicy
        global BOXES
        for i in range(self.rows):
            for j  in range(self.columns):
                if( BOXES[i][j]._plag ):
                    BOXES[i][j].setBrush(self.plague)
                elif BOXES[i][j]._status :
                    BOXES[i][j].setBrush(self.checked)
                else:
                    BOXES[i][j].setBrush(self.unchecked)
                    
    def DrawChangeSingle(self, i, j):   #rysuje wszystkie kolory dla JEDNEJ komorki
        global BOXES
        if( BOXES[i][j]._plag ):
            BOXES[i][j].setBrush(self.plague)
        elif BOXES[i][j]._status :
            BOXES[i][j].setBrush(self.checked)
        else:
            BOXES[i][j].setBrush(self.unchecked)

    def SetSquare(self):
        global BOXES
        if( self.RowsColumsCheckBox.isChecked() ):
            self.columns = self.rows
            self.ColumnsSpinBox.setValue(self.columns)
            self.LColums.setEnabled(False) 
            self.ColumnsSpinBox.setEnabled(False)
            BOXES = [ [CellItem(self.cel_size*j,self.cel_size*i,self.cel_size,self.cel_size, i, j) for j in range(self.columns)] for i in range(self.rows)]
        else:
            self.LColums.setEnabled(True) 
            self.ColumnsSpinBox.setEnabled(True)
            self.columns = self.ColumnsSpinBox.value()
            BOXES = [ [CellItem(self.cel_size*j,self.cel_size*i,self.cel_size,self.cel_size, i, j) for j in range(self.columns)] for i in range(self.rows)]
        self.DrawGrid()
            
    def wheelEvent(self,event):
        if(event.delta() > 0):
            self.scaleViewIn()
        else:
            self.scaleViewOut()
    def scaleViewIn(self):
        self.graphicsView.scale(1.15,1.15)
    def scaleViewOut(self):
        self.graphicsView.scale(0.85,0.85)
    def closeEvent(self, event):
        self.WindowRulesEditor.close()
    def EditRulesWindow(self):
        self.WindowRulesEditor = RuleEditorWidget()
        
class RuleEditorWidget( Ui_RuleEditorWidget, MainWindow): 
    #dziedziczy z qwidget(wMainWindow) aby postawic okno, Ui_RuleEditorWidget aby postawic UI,
    #z MainWindow aby miec dostep do RulesTabBorn, RulesTabDies 
    def __init__(self):
        #super(RuleEditorWidget,self).__init__() można tez tak jak nizej
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)
        self.move(0,500)
        #self.RulePresetsComboBox.setCurrentIndex(self.RulePresetsComboBox.findText(MainWindow.last_rules_preset))
        #self.CellBornLineEdit.setText( MainWindow.RulesTabBorn )
        #self.CellDiesLineEdit.setText( MainWindow.RulesTabDies )
        self.CellBornLineEdit.textChanged.connect( self.UpdateBorn )
        self.CellDiesLineEdit.textChanged.connect( self.UpdateDies )
        self.RemovePreset.clicked.connect(self.DeleteRulesPreset)
        self.AddPreset.clicked.connect(self.AddRulesPresetPopup)
        self.RulePresetsComboBox.activated.connect(self.UpdateRules)
        self.LoadRulesNames()
        try:
            self.RulePresetsComboBox.setCurrentIndex(self.RulePresetsComboBox.findText(MainWindow.last_rules_preset))
        except:
            print("Nie udalo sie wczytac presetu rules 'Normal'. Nie wiem czemu to nie dziala")
        self.UpdateRules()
        self.show()
    def UpdateBorn(self):
        for i in range(0,8): #sprawdza walidacje wprowadzonych danych
            if (str(i) in self.CellBornLineEdit.text() and str(i) in self.CellDiesLineEdit.text()) :
                self.CellBornLineEdit.setText(MainWindow.RulesTabBorn)
        MainWindow.RulesTabBorn = self.CellBornLineEdit.text()
    def UpdateDies(self):
        for i in range(0,8):
            if (str(i) in self.CellBornLineEdit.text() and str(i) in self.CellDiesLineEdit.text()) :
                self.CellDiesLineEdit.setText(MainWindow.RulesTabDies)
        MainWindow.RulesTabDies = self.CellDiesLineEdit.text()
    def LoadRulesNames(self): #add presets to ComboBox
        for file in os.listdir("RulePresets"):
            #print(os.path.splitext(file)[0] ) #nazwy plikow bez rozszerzen
            self.RulePresetsComboBox.addItem(os.path.splitext(file)[0])
    def AddRulesPresetPopup(self):
        filename, ok = QtGui.QInputDialog.getText(self, 'Save Rule Preset', 'Enter preset name:')
        flag=True 

        if ok:
            if (len(filename)==1 or ('.' in filename)): #sprawdz czy nazwa wprowadzona jest dobrze
                flag=False
                msg = QtGui.QMessageBox()
                msg.setIcon(QtGui.QMessageBox.Warning)
                msg.setWindowTitle("Error!")
                msg.setText("Preset not saved!\nFile name specified incorrectly")
                msg.Ok
                msg.exec_()    
            else: #sprawdz czy plik juz istnieje
                for file in os.listdir("RulePresets"):
                    if filename in os.path.splitext(file)[0] :
                        flag=False
                        msg = QtGui.QMessageBox()
                        msg.setIcon(QtGui.QMessageBox.Warning)
                        msg.setWindowTitle("Error!")
                        msg.setText("Preset not saved!\nFile with this name arleady exsists ")
                        msg.Ok
                        msg.exec_()
                        break
        if flag: #jesli plik nie istnieje to zapisz
            self.RulePresetsComboBox.addItem(filename)
            with open("RulePresets/"+filename, 'w') as newfile:
                print(json.dumps( self.CellBornLineEdit.text() ) )
                json.dump(self.CellBornLineEdit.text(), newfile)
                newfile.write('\n')
                json.dump(self.CellDiesLineEdit.text(), newfile)   
                json.dump(MainWindow.last_rules_preset,newfile)
                self.RulePresetsComboBox.setCurrentIndex(self.RulePresetsComboBox.findText(filename))
                
      
    def DeleteRulesPreset(self):
        choice = QtGui.QMessageBox.question(self, 'Delete preset: '+ self.RulePresetsComboBox.currentText(), "Are you sure?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Deleting current preset...",self.RulePresetsComboBox.currentText())
            os.remove("RulePresets/"+self.RulePresetsComboBox.currentText())
            self.RulePresetsComboBox.removeItem(self.RulePresetsComboBox.currentIndex())
            
    def UpdateRules(self): #w razie zmiany, zladuj nowe ustawienia
        with open("RulePresets/"+self.RulePresetsComboBox.currentText(), 'r') as readfile: 
            MainWindow.RulesTabBorn, MainWindow.RulesTabDies = [json.loads(line) for line in readfile ]
        self.CellBornLineEdit.setText(MainWindow.RulesTabBorn)
        self.CellDiesLineEdit.setText(MainWindow.RulesTabDies)
    def closeEvent(self, event):
        MainWindow.last_rules_preset=self.RulePresetsComboBox.currentText()
        self.close()
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit( app.exec_() )
#layout = QVBoxLayout(self)
#layout.add(everything)
#do skalowania na cały ekran   
    
    
    
    
    
    
    
    
    
    
    
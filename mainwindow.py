from PySide2.QtWidgets import QMainWindow, QFileDialog , QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
from ui_mainwindow import Ui_MainWindow
from particulacap.particula import Particula
from particulacap.main import Part
from random import randint
from pprint import pprint, pformat
import math
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.part = Part()


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregarfinal_pushButton.clicked.connect(self.click_agregar)
        self.ui.agregarinicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.pushButton.clicked.connect(self.click_mostrar)

        
        self.ui.actionAbrir.triggered.connect(self.actionAbrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.actionGuardar_archivo)

        self.ui.mostrar__tabla_pushButton_3.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton_2.clicked.connect(self.buscar_ide)
#Pantalla grafica botones
        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
#Ordenar
        self.ui.id_botonorde.clicked.connect(self.ordenarid)
        self.ui.distancia_botonorde.clicked.connect(self.ordenardistancia)
        self.ui.velocidad_boton_orde.clicked.connect(self.ordenarvelocidad)

#Grafo
        self.ui.grafos_pushButton_2.clicked.connect(self.grafomostrar)
        self.ui.busqueda_pushButton_2.clicked.connect(self.grafobusqueda)
        self.ui.buspro_pushButton_2.clicked.connect(self.grafobusquedapro) 

    
    @Slot()

    def buscar_ide(self):
        ide = self.ui.buscar_lineEdit.text()
        encontrado = False
        for particula_no in self.part:
            if ide == particula_no.ide:
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)
                
                ide_widget = QTableWidgetItem(particula_no.ide)
                origen_x_widget = QTableWidgetItem(str(particula_no.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula_no.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula_no.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula_no.destino_y))
                velocidad_widget = QTableWidgetItem(particula_no.velocidad)
                red_widget = QTableWidgetItem(str(particula_no.red))
                green_widget = QTableWidgetItem(str(particula_no.green))
                blue_widget = QTableWidgetItem(str(particula_no.blue))
                distancia_widget = QTableWidgetItem(str(particula_no.distancia))
            
                self.ui.tabla.setItem(0, 0, ide_widget)
                self.ui.tabla.setItem(0, 1, origen_x_widget)
                self.ui.tabla.setItem(0, 2, origen_y_widget)
                self.ui.tabla.setItem(0, 3, destino_x_widget)
                self.ui.tabla.setItem(0, 4, destino_y_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)
                
                encontrado = True
                return 

        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'El Id "{ide}" no se encontro'

            )

    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["Id","origen_x","origen_y","destino_x","destino_y","velocidad","red","green","blue","distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        #tamaño de las particulas para la tabla
        self.ui.tabla.setRowCount(len(self.part))

        row = 0
        for particula_no in self.part:
            ide_widget = QTableWidgetItem(particula_no.ide)
            origen_x_widget = QTableWidgetItem(str(particula_no.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula_no.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula_no.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula_no.destino_y))
            velocidad_widget = QTableWidgetItem(particula_no.velocidad)
            red_widget = QTableWidgetItem(str(particula_no.red))
            green_widget = QTableWidgetItem(str(particula_no.green))
            blue_widget = QTableWidgetItem(str(particula_no.blue))
            distancia_widget = QTableWidgetItem(str(particula_no.distancia))
          
            self.ui.tabla.setItem(row, 0, ide_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1

    @Slot()
    def actionAbrir_archivo(self):
        #print('abrir_archivo')
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.part.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrio el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Ocurrio un error con el archivo " + ubicacion
            )

    @Slot()
    def actionGuardar_archivo(self):
        #print('guardar_archivo')
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]

        print(ubicacion)
        if self.part.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo" + ubicacion
            )


    @Slot()
    def click_mostrar(self):
        #self.part.mostrar()
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.part))

    @Slot()
    def click_agregar(self):
        ide = self.ui.ide_lineEdit.text()
        origen_x = self.ui.origenx_spinBox_2.value()
        origen_y = self.ui.origeny_spinBox_3.value()
        destino_x = self.ui.destinox_spinBox_4.value()
        destino_y = self.ui.destinoy_spinBox_5.value()
        velocidad = self.ui.velocidad_lineEdit_2.text()
        red = self.ui.red_spinBox_7.value()
        green = self.ui.green_spinBox_8.value()
        blue = self.ui.blue_spinBox_9.value()
        distancia = math.sqrt(((destino_x-origen_x)*2)+((destino_y-origen_y)*2))
        particula = Particula(ide,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue,distancia)
        
        self.part.agregar_final(particula)

    def click_agregar_inicio(self):
        ide = self.ui.ide_lineEdit.text()
        origen_x = self.ui.origenx_spinBox_2.value()
        origen_y = self.ui.origeny_spinBox_3.value()
        destino_x = self.ui.destinox_spinBox_4.value()
        destino_y = self.ui.destinoy_spinBox_5.value()
        velocidad = self.ui.velocidad_lineEdit_2.text()
        red = self.ui.red_spinBox_7.value()
        green = self.ui.green_spinBox_8.value()
        blue = self.ui.blue_spinBox_9.value()
        distancia = math.sqrt(((destino_x-origen_x)*2)+((destino_y-origen_y)*2))
        particula = Particula(ide,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue,distancia)
        
        self.part.agregar_inicio(particula)



        #print(ide,orix,oriy,desx,desy,vel,red,green,blue)
        #self.ui.plainTextEdit.insertPlainText(ide+str(orix)+str(oriy)+str(desx)+str(desy)+vel+str(red)+str(green)+str(blue))
   
    def wheeEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ii.graphicsView.scale(0.8, 0.8)
    #Dinuja los puntos en la escena
    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for ori in self.part:
            r = ori.red
            g = ori.green
            b = ori.blue
            color = QColor(r,g,b)
            pen.setColor(color)

            self.scene.addEllipse(ori.origen_x, ori.origen_y, 3, 3, pen)
            self.scene.addEllipse(ori.destino_x, ori.destino_y, 3, 3,pen)
            self.scene.addLine(ori.origen_x+3, ori.origen_y+3, ori.destino_x, ori.destino_y, pen)
            #print(r,g,b)
    #Boton limpiar, limpiamos los puntos
    @Slot()
    def limpiar(self):
        self.scene.clear()

    @Slot()
    def ordenarid(self):
        sort(key=self.part.sort_by_id)
        
    @Slot()
    def ordenardistancia(self):
        print('Ordenar distancia')
    @Slot()
    def ordenarvelocidad(self):
        print('Ordenar velocidad')

    @Slot()
    def grafomostrar(self):
        #self.ui.plainTextEdit.clear()
        #self.ui.grafos_plainTextEdit_2.insertPlainText(str(self.part.grafos)
        #print('grafo')
        grafo = dict()

        for key in self.part:

            #origen = str(key.origen_x) + ',' + str(key.origen_y)
            #destino = str(key.destino_x) + ',' + str(key.destino_y)

            origen = (key.origen_x,key.origen_y)
            destino = (key.destino_x,key.destino_y,key.distancia)

            


            if origen in grafo:
                grafo[origen].append(destino)
            else:
                grafo[origen] = [destino]
        

        
        str = pformat(grafo, width=70, indent=1)
        #print(str)
        
        self.ui.grafos_plainTextEdit_2.clear()
        self.ui.grafos_plainTextEdit_2.insertPlainText("Grafo: "+str)

    @Slot()
    def grafobusqueda(self):
        self.ui.grafos_plainTextEdit_2.clear()
        grafo = dict()
        xbus = self.ui.xbus_spinBox.value()
        ybus = self.ui.ybus_spinBox_2.value()
        for key in self.part:

            #origen = str(key.origen_x) + ',' + str(key.origen_y)
            #destino = str(key.destino_x) + ',' + str(key.destino_y)

            origen = (key.origen_x,key.origen_y)
            destino = (key.destino_x,key.destino_y)

            if origen in grafo:
                grafo[origen].append(destino)
            else:
                grafo[origen] = [destino]
        
        
        print("Muestra el grafo antes del recorrido: \n")
        for key, lista in grafo.items():
            print(key , lista)
  
                
        visitados = []
        cola = []

        origen = (xbus, ybus)
        print("\nLista de recorrido en anchura\n")
        cola.append(origen)
        #mientras la cola este vacia

        while cola:
            actual = cola.pop(0)

            if actual not in visitados:
                #imprime el vertice recorrido
                print("Vertice actual -> ", actual)
                #imprime en la interfas grafica
                self.ui.grafos_plainTextEdit_2.insertPlainText(str(actual)+"\n")
                
                visitados.append(actual)
            
            for key, lista in grafo.items():
                if key not in visitados:
                    cola.append(key)
    @Slot()
    def grafobusquedapro(self):
        self.ui.grafos_plainTextEdit_2.clear()
        grafo = dict()
        xbus = self.ui.xbus_spinBox.value()
        ybus = self.ui.ybus_spinBox_2.value()
        for key in self.part:

            #origen = str(key.origen_x) + ',' + str(key.origen_y)
            #destino = str(key.destino_x) + ',' + str(key.destino_y)

            origen = (key.origen_x,key.origen_y)
            destino = (key.destino_x,key.destino_y)

            if origen in grafo:
                grafo[origen].append(destino)
            else:
                grafo[origen] = [destino]
        print("Muestra el grafo antes del recorrido: \n")
        for key, lista in grafo.items():
            print(key, lista)
 
                
        visitados = []
        pila = []

        origen = (xbus, ybus)
        print("\nLista de recorrido en profundidad\n")
        #Paso 1: SE COLOCA EL VÉRTICE ORIGEN EN UNA PILA
        pila.append(origen)
        #Paso 2: MIENTRAS LA PILA NO ESTE VACÍA
        while pila:
            #paso 3: DESAPILAR UN VÉRTICE, ESTE SERÁ AHORA EL VÉRTICE ACTUAL
            
            actual = pila.pop()
            #FORMA ALTERNATIVA PARA DESAPILAR:
            #actual = pila[-1]
            #pila.remove(pila[-1])

            #paso 4: SI EL VÉRTICE ACTUAL NO HA SIDO VISITADO
            if actual not in visitados:
                #paso 5: PROCESAR (IMPRIMIR) EL VÉRTICE ACTUAL
                print("Vertice actual -> ", actual)
                #paso 6: COLOCAR VÉRTICE ACTUAL EN LA LISTA DE VISITADOS
                self.ui.grafos_plainTextEdit_2.insertPlainText(str(actual)+"\n")
                visitados.append(actual)
            #paso 7: PARA CADA VÉRTICE QUE EL VÉRTICE ACTUAL TIENE COMO DESTINO,
            #        Y QUE NO HA SIDO VISITADO:
            #        APILAR EL VERTICE
            for key, lista in grafo.items():
                if key not in visitados:
                    pila.append(key)

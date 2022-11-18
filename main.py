from tkinter import *
from tkinter import ttk
from Conexion import *
import mysql.connector
from tkinter import messagebox
from datetime import date
from datetime import datetime
from datetime import timedelta

ventana = Tk()
ventana.title("Clinica Veterinaria")
ventana.iconbitmap('iconos\\clinica.ico')

#  Obtenemos el largo y  ancho de la pantalla
wtotal = ventana.winfo_screenwidth()
htotal = ventana.winfo_screenheight()
wventana = 1200
hventana = 800
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)
ventana.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
#ventana.geometry("1200x800+0+0")
ventana.resizable(0,0)
ventana.config(bg='#6699CC')

#titulo aplicacion
Label(ventana,text="Clinica Veterinaria",bg='#6699CC',font=("Arial", 18)).place(x=420,y=20,width=200,height=50)


#marco principal de informacion
marcoPrincipal = LabelFrame(ventana,bg='#9999CC')
#marcoPrincipal.place(x=25,y=75, width=750, height=500)
marcoPrincipal.place(x=25,y=75, width=750, height=550)

#marco añadir dueño
marcoDueno = LabelFrame(ventana,bg='#9999CC')
marcoDueno.place(x=790,y=75, width=400, height=250)

#marco añadir animal
marcoAnimal = LabelFrame(ventana,bg='#9999CC')
marcoAnimal.place(x=790,y=400, width=400, height=250)


#etiquetas para añadir dueño
labelTutuloDueno = Label(marcoDueno,bg='#9999CC').grid(row=0,column=0)
DNI = StringVar()
labelDNI = Label(marcoDueno,text="DNI",bg='#9999CC').grid(row=0,column=0)
txtDNI = Entry(marcoDueno,textvariable=DNI)
txtDNI.grid(row=0,column=1,padx=10,pady=6)

nombre = StringVar()
labelNombre = Label(marcoDueno,text="Nombre",bg='#9999CC').grid(row=1,column=0,padx=15)
txtNombre = Entry(marcoDueno,textvariable=nombre)
txtNombre.grid(row=1,column=1,padx=10,pady=6)

apellido = StringVar()
labelApellido = Label(marcoDueno,text="Apellido",bg='#9999CC').grid(row=2,column=0)
txtApellido = Entry(marcoDueno,textvariable=apellido)
txtApellido.grid(row=2,column=1,padx=10,pady=6)

telefono = StringVar()
labelTelefono = Label(marcoDueno,text="Telefono",bg='#9999CC').grid(row=3,column=0)
txtTelefono = Entry(marcoDueno,textvariable=telefono)
txtTelefono.grid(row=3,column=1,padx=10,pady=6)

correo = StringVar()
labelCorreo = Label(marcoDueno,text="Correo",bg='#9999CC').grid(row=4,column=0)
txtCorreo = Entry(marcoDueno,textvariable=correo)
txtCorreo.grid(row=4,column=1,padx=10,pady=6)

localidad = StringVar()
labelLocalidad = Label(marcoDueno,text="Localidad",bg='#9999CC').grid(row=5,column=0)
txtLocalidad = Entry(marcoDueno,textvariable=localidad)
txtLocalidad.grid(row=5,column=1,padx=10,pady=6)

#tabla de los animales

def seleccionAnimal(event):
    limpiarAniamal()
    id = tablaAnimales.selection()[0]
    txtpesDNIduenoMascota.insert(0, tablaAnimales.item(id, "values")[7])
    txtnombreMascota.insert(0,tablaAnimales.item(id,"values")[1])
    txttipoMascota.insert(0, tablaAnimales.item(id, "values")[2])
    txtrazaMascota.insert(0, tablaAnimales.item(id, "values")[3])
    txtpesMascota.insert(0, tablaAnimales.item(id, "values")[4])
    if (tablaAnimales.item(id, "values")[5] == "Grande"):
        combo.current(0)
    elif (tablaAnimales.item(id, "values")[5] == "Mediano"):
        combo.current(1)
    elif (tablaAnimales.item(id, "values")[5] == "Pequeño"):
        combo.current(2)
    txtcolorMascota.insert(0, tablaAnimales.item(id, "values")[6])

tablaAnimales = ttk.Treeview(marcoPrincipal)
tablaAnimales.grid(row=0,column=0,padx=15,pady=15)
tablaAnimales["columns"] = ("Identificador","Nombre","Tipo","Raza","Peso",
                            "Tamaño","Color","Dueño")
tablaAnimales.column("#0",width=0,stretch=NO)
tablaAnimales.column("Identificador",width=100, anchor=CENTER)
tablaAnimales.column("Nombre",width=100, anchor=CENTER)
tablaAnimales.column("Tipo",width=100, anchor=CENTER)
tablaAnimales.column("Raza",width=100, anchor=CENTER)
tablaAnimales.column("Peso",width=75, anchor=CENTER)
tablaAnimales.column("Tamaño",width=75, anchor=CENTER)
tablaAnimales.column("Color",width=75, anchor=CENTER)
tablaAnimales.column("Dueño",width=100, anchor=CENTER)
tablaAnimales.heading("#0",text="",anchor=CENTER)
tablaAnimales.heading("Identificador",text="Identificador",anchor=CENTER)
tablaAnimales.heading("Nombre",text="Nombre",anchor=CENTER)
tablaAnimales.heading("Tipo",text="Tipo",anchor=CENTER)
tablaAnimales.heading("Raza",text="Raza",anchor=CENTER)
tablaAnimales.heading("Peso",text="Peso",anchor=CENTER)
tablaAnimales.heading("Tamaño",text="Tamaño",anchor=CENTER)
tablaAnimales.heading("Color",text="Color",anchor=CENTER)
tablaAnimales.heading("Dueño",text="Dueño",anchor=CENTER)
tablaAnimales.bind("<<TreeviewSelect>>",seleccionAnimal)

#tabla dueño
def seleccionDueno(event):
    clearDueno()
    id = tablaDueno.selection()[0]
    txtDNI.insert(0, id)
    txtNombre.insert(0, tablaDueno.item(id, "values")[1])
    txtApellido.insert(0, tablaDueno.item(id, "values")[2])
    txtTelefono.insert(0, tablaDueno.item(id, "values")[3])
    txtCorreo.insert(0, tablaDueno.item(id, "values")[4])
    txtLocalidad.insert(0, tablaDueno.item(id, "values")[5])

tablaDueno = ttk.Treeview(marcoPrincipal)
tablaDueno.grid(row=2,column=0,pady=15)
tablaDueno["columns"] = ("DNI","Nombre","Apellido","Telefono","Correo","Localidad")
tablaDueno.column("#0",width=0,stretch=NO)
tablaDueno.column("DNI",width=100, anchor=CENTER)
tablaDueno.column("Nombre",width=100, anchor=CENTER)
tablaDueno.column("Apellido",width=100, anchor=CENTER)
tablaDueno.column("Telefono",width=100, anchor=CENTER)
tablaDueno.column("Correo",width=100, anchor=CENTER)
tablaDueno.column("Localidad",width=100, anchor=CENTER)
tablaDueno.heading("#0",text="",anchor=CENTER)
tablaDueno.heading("DNI",text="DNI",anchor=CENTER)
tablaDueno.heading("Nombre",text="Nombre",anchor=CENTER)
tablaDueno.heading("Apellido",text="Apellido",anchor=CENTER)
tablaDueno.heading("Telefono",text="Telefono",anchor=CENTER)
tablaDueno.heading("Correo",text="Correo",anchor=CENTER)
tablaDueno.heading("Localidad",text="Localidad",anchor=CENTER)
tablaDueno.bind("<<TreeviewSelect>>",seleccionDueno)

#botones de accion para añadir datos y limpiar
    #boton dueno

imgBotonClearDueno = PhotoImage(file="iconos\\limpiar.png")
imgBotonAddDueno = PhotoImage(file="iconos\\veterinario.png")
btnAddDueno = Button(marcoDueno, text="Añadir",bg='#6699FF', command=lambda:addDueno(),image=imgBotonAddDueno,compound=LEFT).grid(row=6,column=0,pady=15,padx=10)
Button(marcoDueno, text="Limpiar",bg='#6699FF', command=lambda:clearDueno(),image=imgBotonClearDueno,compound=LEFT).grid(row=6,column=1,pady=15,padx=10)
    #boton para tabla

#radiobutton
FrameRadioButton = LabelFrame(ventana)
FrameRadioButton.config(bg='#9999FF')
FrameRadioButton.place(x=20,y=700)
FrameRadioButton.place(width=655,height=60)
x = IntVar()
y = IntVar()
x.set(value=1)
y.set(value=1)
laberTablaDueno = Label(FrameRadioButton, text="Seleccione como ordenar los dueños: ",bg='#9999FF').grid(row=0,column=0,padx=5)
ordenarDNI = Radiobutton(FrameRadioButton,text="DNI",variable=x,value=1,command=lambda:ordenar(),bg='#9999FF').grid(row=0,column=1,padx=5)
ordenarNombre = Radiobutton(FrameRadioButton,text="Nombre",variable=x,value=2,command=lambda:ordenar(),bg='#9999FF').grid(row=0,column=2,padx=5)

laberTablaAnimal = Label(FrameRadioButton, text="Seleccione como ordenar los animales: ",bg='#9999FF').grid(row=1,column=0,padx=5)
ordenarNombreAnimal = Radiobutton(FrameRadioButton,text="Nombre",variable=y,value=1,command=lambda:ordenar(),bg='#9999FF').grid(row=1,column=1,padx=5)
ordenarTipo = Radiobutton(FrameRadioButton,text="Tipo",variable=y,value=2,command=lambda:ordenar(),bg='#9999FF').grid(row=1,column=2,padx=5)
ordenarRaza = Radiobutton(FrameRadioButton,text="raza",variable=y,value=3,command=lambda:ordenar(),bg='#9999FF').grid(row=1,column=3,padx=5)
ordenarPeso = Radiobutton(FrameRadioButton,text="peso",variable=y,value=4,command=lambda:ordenar(),bg='#9999FF').grid(row=1,column=4,padx=5)
ordenarDueno = Radiobutton(FrameRadioButton,text="Dueño",variable=y,value=5,command=lambda:ordenar(),bg='#9999FF').grid(row=1,column=5,padx=5)
#fin radiobutton

#formulario animales
nombreMascota = StringVar()
labelnombreMascota = Label(marcoAnimal,text="Nombre",bg='#9999CC').grid(row=0,column=0)
txtnombreMascota = Entry(marcoAnimal,textvariable=nombreMascota)
txtnombreMascota.grid(row=0,column=1,padx=10,pady=6)

tipoMascota = StringVar()
labeltipoMascota = Label(marcoAnimal,text="Tipo",bg='#9999CC').grid(row=1,column=0)
txttipoMascota = Entry(marcoAnimal,textvariable=tipoMascota)
txttipoMascota.grid(row=1,column=1,padx=10,pady=6)

razaMascota = StringVar()
labelrazaMascota = Label(marcoAnimal,text="Raza",bg='#9999CC').grid(row=1,column=2)
txtrazaMascota = Entry(marcoAnimal,textvariable=razaMascota)
txtrazaMascota.grid(row=1,column=3,padx=10,pady=6)

pesMascota = StringVar()
labelrazaMascota = Label(marcoAnimal,text="Peso",bg='#9999CC').grid(row=2,column=0)
txtpesMascota = Entry(marcoAnimal,textvariable=pesMascota)
txtpesMascota.grid(row=2,column=1,padx=10,pady=6)

tamanoMascota = StringVar()
labelTamanoMascota = Label(marcoAnimal,text="Tamaño",bg='#9999CC').grid(row=3,column=0)
combo = ttk.Combobox(marcoAnimal,
                     state="readonly",
                     values=["Grande", "Mediano", "Pequeño"]
                     ,textvariable=tamanoMascota)
combo.grid(row=3,column=1,padx=10,pady=6)
combo.current(0)

colorMascota = StringVar()
labelColorMascota = Label(marcoAnimal,text="Color",bg='#9999CC').grid(row=3,column=2)
txtcolorMascota = Entry(marcoAnimal,textvariable=colorMascota)
txtcolorMascota.grid(row=3,column=3,padx=10,pady=6)

DNIdueno = StringVar()
labelTamanoMascota = Label(marcoAnimal,text="DNI dueño",bg='#9999CC').grid(row=4,column=0)
txtpesDNIduenoMascota = Entry(marcoAnimal,textvariable=DNIdueno)
txtpesDNIduenoMascota.grid(row=4,column=1,padx=10,pady=6)
imgBotonAddAnimal = PhotoImage(file="iconos\\veterinario.png")
imgBotonClearAnimal = PhotoImage(file="iconos\\limpiar.png")
imgBotonEditar = PhotoImage(file="iconos\\portapapeles.png")
Button(marcoAnimal, text="Añadir", command=lambda:addAnimal(),bg='#6699FF',image=imgBotonAddAnimal,compound=LEFT).grid(row=5,column=0,padx=10,pady=15)
Button(marcoAnimal, text="Limpiar", command=lambda:limpiarAniamal(),bg='#6699FF',image=imgBotonClearAnimal,compound=LEFT).grid(row=5,column=1,padx=10,pady=15)
boton3 =Button(marcoAnimal, text="Editar", command=lambda:updateAnimal(),bg='#6699FF',image=imgBotonEditar,compound=LEFT).grid(row=5,column=2,padx=2,pady=10)
#fin formulario animales

#botones para movernos por la aplicacion
marcoNavegador = LabelFrame(ventana)
marcoNavegador.config(bg='#9999CC')
#marcoPrincipalBotones.place(x=790,y=590)
marcoNavegador.place(x=25,y=10)
marcoNavegador.place(width=210,height=50)
imgBotonInicio = PhotoImage(file="iconos\\medicina.png")
imgBotonConsulta = PhotoImage(file="iconos\\salud.png")
#imgBotonEditar = PhotoImage(file="iconos\\portapapeles.png")
boton1 =Button(marcoNavegador, text="Inicio", command=lambda:accionesBotones(1),bg='#6699FF',image=imgBotonInicio,compound=LEFT,state=DISABLED).grid(row=0,column=0,padx=15,pady=10)
boton2 =Button(marcoNavegador, text="Consultas", command=lambda:ConsultaVentana(),bg='#6699FF',image=imgBotonConsulta,compound=LEFT).grid(row=0,column=1,padx=15,pady=10)
#boton3 =Button(marcoNavegador, text="Editar", command=lambda:accionesBotones(3),bg='#6699FF',image=imgBotonEditar,compound=LEFT).grid(row=0,column=2,padx=15,pady=10)
#fin botones para movernos

#buscasdor en las tablas
marcoBuscador = LabelFrame(ventana)
marcoBuscador.config(bg='#9999CC')
marcoBuscador.place(x=790,y=10)
marcoBuscador.place(width=400,height=50)

DNIbuscador = StringVar()
txtnombreMascotaBuscador = Entry(marcoBuscador,textvariable=DNIbuscador)
txtnombreMascotaBuscador.grid(row=0,column=2,padx=10,pady=6)
imgbuscar = PhotoImage(file="iconos\\dermatologia.png")
Button(marcoBuscador, text="Buscar",bg='#6699FF', command=lambda:buscador(),image=imgbuscar,compound=LEFT).grid(row=0,column=3,padx=5,pady=5)
Z = IntVar()
ordenarDNI = Radiobutton(marcoBuscador,text="Mascota",variable=Z,value=1,bg='#9999CC').grid(row=0,column=1,padx=5)
ordenarNombre = Radiobutton(marcoBuscador,text="Dueño",variable=Z,value=2,bg='#9999CC').grid(row=0,column=0,padx=5)

#fin de buscador en tablas

def ordenar():
    vaciarTabla(tablaDueno)
    if x.get() == 1:
        sql = "select * from dueno order by DNI;"
    elif x.get() == 2:
        sql = "select * from dueno order by nombre;"
    consulta = hacerConsulta(sql)
    for fila in consulta:
        DNIdueno = fila[0]
        tablaDueno.insert("", END, DNIdueno, text=DNIdueno, values=fila, )

    vaciarTabla(tablaAnimales)
    if y.get() == 1:
        sql = "select * from mascota order by nombreMascota;"
    elif y.get() == 2:
        sql = "select * from mascota order by tipoAnimal;"
    elif y.get() == 3:
        sql = "select * from mascota order by raza;"
    elif y.get() == 4:
        sql = "select * from mascota order by peso;"
    elif y.get() == 5:
        sql = "select * from mascota order by DNIdueno;"
    consulta = hacerConsulta(sql)
    for fila in consulta:
        DNIdueno = fila[7]
        tablaAnimales.insert("", END, text=DNIdueno, values=fila, )

marcoPrincipalBotones = Frame(ventana)
marcoPrincipalBotones.config(bg='#6699CC')
#marcoPrincipalBotones.place(x=790,y=590)
marcoPrincipalBotones.place(x=20,y=640)
marcoPrincipalBotones.place(width=700,height=50)

imgBotonClear = PhotoImage(file="iconos\\boton-eliminar.png")
Button(marcoPrincipalBotones, text="Eliminar mascota",bg='#993333', command=lambda:eliminarAnimal(),image=imgBotonClear,compound=LEFT).grid(row=0,column=0,padx=20)
Button(marcoPrincipalBotones, text="Eliminar Dueño",bg='#993333', command=lambda:eliminarDueno(),image=imgBotonClear,compound=LEFT).grid(row=0,column=1,padx=20)

imgBotonBuscar = PhotoImage(file="iconos\\dermatologia.png")
Button(marcoPrincipalBotones, text="Buscar dueño",bg='#99CCFF', command=lambda:buscarDueno(),image=imgBotonBuscar,compound=LEFT).grid(row=0,column=2,padx=20)
Button(marcoPrincipalBotones, text="Buscar mascotas",bg='#99CCFF', command=lambda:buscarMascota(),image=imgBotonBuscar,compound=LEFT).grid(row=0,column=3,padx=20)

imgBotonActualizar = PhotoImage(file="iconos\\sincronizar.png")
btnActualizar = Button(marcoPrincipalBotones, text="Actualizar tablas",bg='#66CC99', command=lambda:listartablas(),image=imgBotonActualizar)
btnActualizar.grid(row=0,column=4,padx=20)


def vaciarTabla(tabla):
    filas = tabla.get_children()
    for fila in filas:
        tabla.delete(fila)

def datosTableAnimales():
    vaciarTabla(tablaAnimales)
    sql="select * from mascota"
    consulta = hacerConsulta(sql)
    for fila in consulta:
        id = fila[0]
        DNIdueno = fila[7]
        tablaAnimales.insert("",END, text=DNIdueno, values=fila)

def datosTableDueno():
    vaciarTabla(tablaDueno)
    sql="select * from dueno"
    consulta = hacerConsulta(sql)
    for fila in consulta:
        id = fila[0]
        tablaDueno.insert("",END,id, text=id, values=fila)

datosTableDueno()
datosTableAnimales()

def eliminarDueno():
    id = tablaDueno.selection()[0]
    sql="delete from dueno where DNI='"+id+"';"
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='', db='clinicaVeterinaria')
    cur = miConexion.cursor()
    cur.execute(sql)
    miConexion.commit()
    tablaDueno.delete(id)
    messagebox.showinfo(message="Cliente eliminado "+ id +" correctamente", title="Información")

def eliminarAnimal():
    id = tablaAnimales.selection()[0]
    sql="delete from mascota where idMascotar='"+id+"';"
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='', db='clinicaVeterinaria')
    cur = miConexion.cursor()
    cur.execute(sql)
    miConexion.commit()
    tablaAnimales.delete(id)
    messagebox.showinfo(message="Animal eliminado "+ id +" correctamente", title="Información")

#buscador en tabla
def buscarDueno():
    id = tablaAnimales.selection()[0]
    DNI =tablaAnimales.item(id, "values")[7]
    sql="select distinct * from dueno due inner join mascota mas on mas.DNIdueno=due.DNI where mas.DNIdueno='"+DNI+"' LIMIT 1;"
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='', db='clinicaVeterinaria')
    cur = miConexion.cursor()
    cur.execute(sql)
    vaciarTabla(tablaDueno)
    for fila in cur.fetchall():
        id = fila[0]
        tablaDueno.insert("",END,id, text=id, values=fila)

def buscarMascota():
    id = tablaDueno.selection()[0]
    sql= "select * from mascota where DNIdueno='"+id+"';"
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='', db='clinicaVeterinaria')
    cur = miConexion.cursor()
    cur.execute(sql)
    vaciarTabla(tablaAnimales)
    for fila in cur.fetchall():
        id = fila[7]
        tablaAnimales.insert("", END, text=id, values=fila)

def addDueno():
    val = (DNI.get(), nombre.get(), apellido.get(), telefono.get(), correo.get(), localidad.get())
    sql = "insert into dueno (DNI,nombre,apellido,telefono,correo,localidad) values('"+val[0]+"','"+val[1]+"','"+val[2]+"',"+val[3]+",'"+val[4]+"','"+val[5]+"')"
    print(sql)
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='', db='clinicaVeterinaria')
    cur = miConexion.cursor()
    cur.execute(sql)
    miConexion.commit()
    messagebox.showinfo(message="Nuevo dueño: " + DNI.get(), title="Información")


def buscador():
     if Z.get() == 1:
         DNI = DNIbuscador.get()
         sql = "select * from mascota where DNIdueno='" + DNI + "';"
         consulta = hacerConsulta(sql)
         vaciarTabla(tablaAnimales)
         for fila in consulta:
             id = fila[0]
             DNIdueno = fila[7]
             tablaAnimales.insert("", END, text=DNIdueno, values=fila, )
     elif Z.get() == 2:
         DNI = DNIbuscador.get()
         sql = "select * from dueno where DNI='" + DNI + "';"
         consulta = hacerConsulta(sql)
         vaciarTabla(tablaDueno)
         for fila in consulta:
             id = fila[0]
             DNI = fila[0]
             tablaDueno.insert("", END, DNI, text=DNI, values=fila, )

def limpiarAniamal():
    print("entro")
    txtnombreMascota.delete(0,END)
    txttipoMascota.delete(0, END)
    txtrazaMascota.delete(0, END)
    txtpesMascota.delete(0, END)
    txtcolorMascota.delete(0, END)
    txtpesDNIduenoMascota.delete(0, END)
    combo.current(0)

def addAnimal():
    val = (nombreMascota.get(), tipoMascota.get(), razaMascota.get(), pesMascota.get(), tamanoMascota.get(),colorMascota.get(), DNIdueno.get())
    sql = "insert into mascota (nombreMascota,tipoAnimal,raza,peso,tamano,color,DNIdueno) values('" + val[0] + "','" + val[1] + "','" + val[2] + "'," + val[3] + ",'" + val[4] + "','" + val[5] + "','" + val[6] + "')"
    print(sql)
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='', db='clinicaVeterinaria')
    cur = miConexion.cursor()
    cur.execute(sql)
    miConexion.commit()
    messagebox.showinfo(message="Nuevo animal: " + nombreMascota.get() + " con dueño: " + DNIdueno.get() , title="Información")


#messagebox.showinfo(message="Nuevo animal,: " + DNI.get(), title="Información")


def clearDueno():
    txtDNI.delete(0, END)
    txtNombre.delete(0, END)
    txtApellido.delete(0, END)
    txtTelefono.delete(0, END)
    txtCorreo.delete(0, END)
    txtLocalidad.delete(0, END)

def accionesBotones(x):
    pass

def updateAnimal():
    val = (nombreMascota.get(), tipoMascota.get(), razaMascota.get(), pesMascota.get(), tamanoMascota.get(),colorMascota.get(), DNIdueno.get())
    id = tablaAnimales.selection()[0]
    identificador = tablaAnimales.item(id, "values")[0]
    sql = "update mascota set nombreMascota='"+val[0]+"', tipoAnimal='"+val[1]+"', raza='"+val[2]+"', peso ="+val[3]+" , tamano='"+val[4]+"' ,color='"+val[5]+"', DNIdueno='"+val[6]+"' where idMascotar = " + identificador
    print(sql)
    miConexion = mysql.connector.connect(host='localhost', user='root', passwd='', db='clinicaVeterinaria')
    cur = miConexion.cursor()
    cur.execute(sql)
    miConexion.commit()
    messagebox.showinfo(message="Cambios realizados: " + nombreMascota.get() + " con dueño: " + DNIdueno.get(),
                        title="Información")



def listartablas():
    vaciarTabla(tablaAnimales)
    datosTableAnimales()
    vaciarTabla(tablaDueno)
    datosTableDueno()

#master = Tk()
#master.geometry("200x200")
#################################################################################################################################################################################################




def ConsultaVentana():
    def seleccionCrearCita(event):
        id = tablaConsulta.selection()[0]
        horaconsulta = tablaConsulta.item(id, "values")[0]
        DNI = tablaConsulta.item(id, "values")[1]
        nombreMas = tablaConsulta.item(id, "values")[2]
        print(DNI)
        txtcolorMascota.delete(0, END)
        txtcolorMascota.insert(0, DNI)
        #txtcolorMascota.insert(0, tablaConsulta.item(id, "values")[1])
        sql="select mas.nombreMascota from mascota mas inner join dueno due on due.DNI=mas.DNIDueno where mas.DNIdueno='"+DNI+"';"
        array = hacerConsulta(sql)
        print(array)
        comboConsultaAnimal.config(values=array)
        comboConsultaAnimal.current(0)
        dniactual.config(text=DNI)
        nombreactual.config(text=nombreMas)
        horaactual.config(text=horaconsulta)
        #idconsulta.config(text=id)
        #print(id)
        IDconsulta.set(id)



    ventana.withdraw()
    newWindow = Toplevel(ventana)
    newWindow.iconbitmap('iconos\\clinica.ico')
    wtotal = newWindow.winfo_screenwidth()
    htotal = newWindow.winfo_screenheight()
    wventana = 1200
    hventana = 800
    pwidth = round(wtotal / 2 - wventana / 2)
    pheight = round(htotal / 2 - hventana / 2)
    newWindow.geometry(str(wventana) + "x" + str(hventana) + "+" + str(pwidth) + "+" + str(pheight))
    # ventana.geometry("1200x800+0+0")
    newWindow.resizable(0, 0)
    newWindow.config(bg='#6699CC')

    marcoNavegador = LabelFrame(newWindow)
    marcoNavegador.config(bg='#9999CC')
    marcoNavegador.place(x=25, y=10)
    marcoNavegador.place(width=210, height=50)



    boton1VistaConsulta = Button(marcoNavegador, text="Inicio", command=lambda: cambioVista(newWindow), bg='#6699FF',
                    image=imgBotonInicio, compound=LEFT).grid(row=0, column=0, padx=15, pady=10)
    boton2VistaConsulta = Button(marcoNavegador, text="Consultas", command=lambda: pruebaVentana(), bg='#6699FF',
                    image=imgBotonConsulta, compound=LEFT, state=DISABLED).grid(row=0, column=1, padx=15, pady=10)
    marcoConsulta = LabelFrame(newWindow, bg='#9999CC')
    marcoConsulta.place(x=25, y=75, width=425, height=590)
    Label(marcoConsulta, text=fechaHoy(), bg='#9999CC').grid(row=0, column=0)
    tablaConsulta = ttk.Treeview(marcoConsulta)
    tablaConsulta.grid(row=1, column=0, pady=15,padx=15)
    tablaConsulta["columns"] = ("Hora", "DNI", "Nombre animal", "Raza")
    tablaConsulta.column("#0", width=0, stretch=NO)
    tablaConsulta.column("Hora", width=100, anchor=CENTER)
    tablaConsulta.column("DNI", width=100, anchor=CENTER)
    tablaConsulta.column("Nombre animal", width=100, anchor=CENTER)
    tablaConsulta.column("Raza", width=100, anchor=CENTER)
    tablaConsulta.heading("#0", text="", anchor=CENTER)
    tablaConsulta.heading("Hora", text="Hora", anchor=CENTER)
    tablaConsulta.heading("DNI", text="DNI", anchor=CENTER)
    tablaConsulta.heading("Nombre animal", text="Nombre animal", anchor=CENTER)
    tablaConsulta.heading("Raza", text="Raza", anchor=CENTER)
    tablaConsulta.bind("<<TreeviewSelect>>", seleccionCrearCita)
    Label(marcoConsulta, text="Proxima cita", bg='#9999CC').grid(row=2, column=0)
    Label(marcoConsulta, text="Dia:", bg='#9999CC').grid(row=3, column=1)
    vaciarTabla(tablaConsulta)
    sql = "select mascon.hora,due.DNI,mas.nombreMascota, mas.raza,con.idConsulta from mascotaconsulta mascon" \
          " inner join mascota mas on mas.idMascotar=mascon.idMascotar " \
          "inner join dueno due on due.DNI=mas.DNIdueno " \
          "inner join consulta con on con.idConsulta=mascon.idConsulta " \
          "where mascon.fecha=curdate() and con.estado='Pendiente';"
    consulta = hacerConsulta(sql)
    for fila in consulta:
        id = fila[4]
        tablaConsulta.insert("", END, text=id, values=fila,iid=id)
    dia = StringVar()
    comboConsulta = ttk.Combobox(marcoConsulta,
                         state="readonly",
                         values=diasCita()
                         , textvariable=dia)
    comboConsulta.grid(row=3, column=0,pady=5)
    comboConsulta.current(0)
    Label(marcoConsulta, text="Dueño:", bg='#9999CC').grid(row=4, column=0,pady=5)
    DNIConsulta = StringVar()
    txtcolorMascota = Entry(marcoConsulta, textvariable=DNIConsulta)
    txtcolorMascota.grid(row=5, column=0, pady=5)
    Label(marcoConsulta, text="Nombre del Animal:", bg='#9999CC').grid(row=6, column=0, pady=5)
    nombreAnimal = StringVar()
    comboConsultaAnimal = ttk.Combobox(marcoConsulta,
                                 state="readonly",
                                 values=""
                                 , textvariable=nombreAnimal)
    comboConsultaAnimal.grid(row=7, column=0, pady=5)
    hora = ("10:00","10:30","11:00","11:30","12:00","12:30","13:00","16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00")
    seleccionHora = StringVar()
    Label(marcoConsulta, text="Hora de la cita:", bg='#9999CC').grid(row=8, column=0, pady=5)
    comboConsultaHora = ttk.Combobox(marcoConsulta,
                                       state="readonly",
                                       values=hora
                                       , textvariable=seleccionHora)
    comboConsultaHora.grid(row=9, column=0, pady=5)
    comboConsultaHora.current(0)
    botonCita = Button(marcoConsulta, text="Dar cita", command=lambda: darCitaProxima(), bg='#6699FF',image=imgBotonConsulta, compound=LEFT).grid(row=10, column=0, pady=10)


    marcoHistorial = LabelFrame(newWindow, bg='#9999CC')
    marcoHistorial.place(x=470, y=75, width=400, height=300)
    treeview = ttk.Treeview(marcoHistorial,columns=425)
    treeview.heading("#0", text="Historial de consultas")

    # pruebas scroll
    scroll = Scrollbar(newWindow)
    scroll.pack(side=RIGHT, fill=Y)
    treeview.pack(side=LEFT, fill=Y)
    scroll.config(command=treeview.yview)
    treeview.config(yscrollcommand=scroll.set)
    # fin pruebas
    sql="select distinct fecha from mascotaconsulta where fecha < curdate() order by fecha desc;"
    consulta = hacerConsulta(sql)
    for fila in consulta:
        item = treeview.insert("", END, text=fila)
        sql="select distinct due.DNI from mascotaconsulta mascon inner join mascota mas on mas.idMascotar=mascon.idMascotar inner join dueno due on due.DNI=mas.DNIdueno where mascon.fecha='"+str(fila[0])+"';"
        consultados = hacerConsulta(sql)
        for filados in consultados:
            item2 =treeview.insert(item, END, text=filados)
            sql="select mascon.hora , mas.nombreMascota from mascotaconsulta mascon inner join mascota mas on mas.idMascotar=mascon.idMascotar" \
                " inner join dueno due on due.DNI=mas.DNIdueno where mascon.fecha='"+str(fila[0])+"' and due.DNI='"+str(filados[0])+"' order by mascon.hora asc;"
            consultatres = hacerConsulta(sql)
            for filatres in consultatres:
                 item3 = treeview.insert(item2, END, text=filatres)
                 sql="select con.tratamient, con.descripcion from mascotaconsulta mascon " \
                     "inner join mascota mas on mas.idMascotar=mascon.idMascotar inner join dueno due on due.DNI=mas.DNIdueno" \
                     " inner join consulta con on con.idConsulta=mascon.idConsulta where mascon.fecha='"+str(fila[0])+"' and due.DNI='"+str(filados[0])+"' and mas.nombreMascota='"+str(filatres[1])+"';"
                 consultacuatro = hacerConsulta(sql)
                 for filacuatro in consultacuatro:
                     treeview.insert(item3, END, text="Descripción: " + str(filacuatro[1]))
                     treeview.insert(item3, END, text="Medicamento: " + str(filacuatro[0]))
                     treeview.pack()

    marcoProximasCitas = LabelFrame(newWindow, bg='#9999CC')
    marcoProximasCitas.place(x=470, y=385, width=400, height=300)
    treeviewcitasProximas = ttk.Treeview(marcoProximasCitas, columns=425)
    treeviewcitasProximas.pack(side=LEFT, fill=Y)
    treeviewcitasProximas.config(yscrollcommand=scroll.set)
    treeviewcitasProximas.heading("#0", text="Proximas citas")

    sql = "select distinct fecha from mascotaconsulta where fecha > curdate() order by fecha asc;"
    consulta = hacerConsulta(sql)
    for fila in consulta:
        item = treeviewcitasProximas.insert("", END, text=fila)
        sql = "select distinct due.DNI from mascotaconsulta mascon inner join mascota mas on mas.idMascotar=mascon.idMascotar inner join dueno due on due.DNI=mas.DNIdueno where mascon.fecha='" + str(
            fila[0]) + "';"
        consultados = hacerConsulta(sql)
        for filados in consultados:
            item2 = treeviewcitasProximas.insert(item, END, text=filados)
            sql = "select mascon.hora , mas.nombreMascota from mascotaconsulta mascon inner join mascota mas on mas.idMascotar=mascon.idMascotar" \
                  " inner join dueno due on due.DNI=mas.DNIdueno where mascon.fecha='" + str(
                fila[0]) + "' and due.DNI='" + str(filados[0]) + "' order by mascon.hora asc;"
            consultatres = hacerConsulta(sql)
            for filatres in consultatres:
                item3 = treeviewcitasProximas.insert(item2, END, text=filatres)
                sql = "select con.tratamient, con.descripcion from mascotaconsulta mascon " \
                      "inner join mascota mas on mas.idMascotar=mascon.idMascotar inner join dueno due on due.DNI=mas.DNIdueno" \
                      " inner join consulta con on con.idConsulta=mascon.idConsulta where mascon.fecha='" + str(
                    fila[0]) + "' and due.DNI='" + str(filados[0]) + "' and mas.nombreMascota='" + str(
                    filatres[1]) + "';"
                consultacuatro = hacerConsulta(sql)
                for filacuatro in consultacuatro:
                    treeviewcitasProximas.insert(item3, END, text="Descripción: " + str(filacuatro[1]))
                    treeviewcitasProximas.insert(item3, END, text="Medicamento: " + str(filacuatro[0]))
                    treeviewcitasProximas.pack()

    marcoNuevaCita = LabelFrame(newWindow, bg='#9999CC')
    marcoNuevaCita.place(x=880, y=75, width=300, height=170)
    Label(marcoNuevaCita, text="Consulta actual:", bg='#9999CC').grid(row=0, column=0)
    Label(marcoNuevaCita, text="DNI:", bg='#9999CC').grid(row=1, column=0)
    Label(marcoNuevaCita, text="Nombre mascota:", bg='#9999CC').grid(row=2, column=0)
    Label(marcoNuevaCita, text="Tratamiento:", bg='#9999CC').grid(row=3, column=0)
    Label(marcoNuevaCita, text="Observación:", bg='#9999CC').grid(row=4, column=0)

    dniactual = Label(marcoNuevaCita, bg='#9999CC')
    dniactual.grid(row=1, column=1)
    nombreactual = Label(marcoNuevaCita, bg='#9999CC')
    nombreactual.grid(row=2, column=1)
    horaactual = Label(marcoNuevaCita, bg='#9999CC')
    horaactual.grid(row=0, column=1)
    Tratamiento = StringVar()
    txtTratamiento = Entry(marcoNuevaCita, textvariable=Tratamiento)
    txtTratamiento.grid(row=3, column=1)
    Observacion = StringVar()
    txtObservacion = Entry(marcoNuevaCita, textvariable=Observacion)
    txtObservacion.grid(row=4, column=1)
    IDconsulta = StringVar()

    Button(marcoNuevaCita, text="Acabar cita", command=lambda: acabarCita(), bg='#6699FF',image=imgBotonConsulta, compound=LEFT).grid(row=5, column=0,pady=10)
    Button(marcoNuevaCita, text="Limpiar", command=lambda: limpiarCitaActual(), bg='#6699FF',image=imgBotonClear, compound=LEFT).grid(row=5, column=1, pady=10)

    def acabarCita():
        print(Tratamiento.get())
        print(Observacion.get())
        print(IDconsulta.get())
        sql="update consulta set tratamient='"+Tratamiento.get()+"', estado='Terminada', observacion='"+Observacion.get()+"' where idConsulta="+IDconsulta.get()+";"
        miConexion = mysql.connector.connect(host='localhost', user='root', passwd='', db='clinicaVeterinaria')
        cur = miConexion.cursor()
        cur.execute(sql)
        miConexion.commit()
        messagebox.showinfo(message="Fin de la cita.")

    def limpiarCitaActual():
        txtTratamiento.delete(0,END)
        txtObservacion.delete(0,END)

    def seleccionDNI(event):
        sql="select nombreMascota from mascota where DNIdueno='"+DNICita.get()+"';"
        consulta = hacerConsulta(sql)
        combocita.config(values=consulta)
        combocita.current(0)
        combocitahora.current(0)
        combocitadia.current(0)

    marcoCitaProxima = LabelFrame(newWindow, bg='#9999CC')
    marcoCitaProxima.place(x=880, y=300, width=300, height=220)
    Label(marcoCitaProxima, text="Nueva cita", bg='#9999CC').grid(row=0, column=0)
    Label(marcoCitaProxima, text="DNI:", bg='#9999CC').grid(row=1, column=0)
    DNICita = StringVar()
    txtDNICita = Entry(marcoCitaProxima,textvariable=DNICita)
    txtDNICita.grid(row=1,column=1)
    txtDNICita.bind("<KeyRelease>", seleccionDNI)
    Label(marcoCitaProxima, text="Nombre Animal:", bg='#9999CC').grid(row=2, column=0)
    nombreanimalCita = StringVar()
    combocita = ttk.Combobox(marcoCitaProxima, state="readonly", textvariable=nombreanimalCita)
    combocita.grid(row=2, column=1,pady=10)
    diaCita = StringVar()
    Label(marcoCitaProxima, text="Dia cita:", bg='#9999CC').grid(row=3, column=0)
    combocitadia = ttk.Combobox(marcoCitaProxima,values=diasCita(), state="readonly", textvariable=diaCita)
    combocitadia.grid(row=3, column=1, pady=5)
    horaCita = StringVar()
    hora = ("10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30","19:00", "19:30", "20:00")
    Label(marcoCitaProxima, text="Hora cita:", bg='#9999CC').grid(row=4, column=0)
    combocitahora = ttk.Combobox(marcoCitaProxima,values=hora, state="readonly", textvariable=horaCita)
    combocitahora.grid(row=4, column=1, pady=5)
    Label(marcoCitaProxima, text="Asunto cita:", bg='#9999CC').grid(row=5, column=0)
    asuntoCita = StringVar()
    txtAsustoCita = Entry(marcoCitaProxima, textvariable=asuntoCita)
    txtAsustoCita.grid(row=5, column=1)
    Button(marcoCitaProxima, text="Dar cita", command=lambda: darcitaNueva(), bg='#6699FF', image=imgBotonConsulta,compound=LEFT).grid(row=6, column=0, pady=5)
    Button(marcoCitaProxima, text="Limpiar", command=lambda: limpiarNuevaCita(), bg='#6699FF',image=imgBotonClear, compound=LEFT).grid(row=6, column=1, pady=10)

    def limpiarNuevaCita():
        txtDNICita.delete(0,END)
        txtAsustoCita.delete(0,END)
        combocitahora.current(0)
        combocitadia.current(0)
        combocita.config(values=['  '])
        combocita.current(0)
        pass
    def darcitaNueva():
        fecha_dt = datetime.strptime(diaCita.get(), '%d/%m/%Y')
        fecha = fecha_dt.date()
        sql="insert into consulta (descripcion,estado) values ('"+asuntoCita.get()+"','Pendiente');"
        hacerConsulta(sql)
        sql="insert into mascotaconsulta values((select idConsulta from consulta order by idConsulta desc limit 1)," \
            "(select idMascotar from mascota where nombreMascota='"+str(nombreanimalCita.get())+"' and DNIdueno='"+str(DNICita.get())+"'),'"+str(fecha)+"','"+str(horaCita.get())+"')"
        hacerConsulta(sql)
        messagebox.showinfo(message="Nueva consulta añadida para el dia: " + str(fecha) + " a las "+ str(horaCita.get()))

    def darCitaProxima():
        dia.get()
        fecha_dt = datetime.strptime(dia.get(), '%d/%m/%Y')
        fecha =fecha_dt.date()
        nombreAnimal.get()
        seleccionHora.get()
        DNIConsulta.get()
        sql ="select idMascotar from mascota where DNIdueno='"+DNIConsulta.get()+"' and nombreMascota = '"+nombreAnimal.get()+"';"
        consulta = hacerConsulta(sql)
        miConexion = mysql.connector.connect(host='localhost', user='root', passwd='', db='clinicaVeterinaria')
        for fila in consulta:
            fila[0]
            sql="insert into consulta (estado) values ('Pendiente');"
            cur = miConexion.cursor()
            cur.execute(sql)
            miConexion.commit()
            sql="insert into mascotaconsulta values((select idConsulta from  consulta order by idConsulta desc limit 1),"+str(fila[0])+",'"+str(fecha)+"','"+str(seleccionHora.get())+"')"
            cur = miConexion.cursor()
            cur.execute(sql)
            miConexion.commit()
            messagebox.showinfo(message="Nueva cita lista para la fecha:" + str(fecha) + " y hora: " + seleccionHora.get())



def cambioVista(ventanaVista):
    ventanaVista.withdraw()
    ventana.deiconify()


def fechaHoy():
    today = date.today()
    return format(today.day)+"/"+format(today.month)+"/"+format(today.year)


def diasCita():
    datetime.today().weekday()
    lista = []
    for x in range(1,32):
        now = datetime.now()
        new_date = now + timedelta(days=x)
        if  new_date.weekday() ==5 or new_date.weekday() ==6:
            pass
        else:
            lista.insert(x, new_date.strftime('%d/%m/%Y'))
    return lista
ventana.mainloop()
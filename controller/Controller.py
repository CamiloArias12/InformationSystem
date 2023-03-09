from Connection import Connection
from  Lote import Lote
from Agricultor import Agricultor
from Produccion import Produccion
from TipoDePapa import TipoDePapa
from Siembra import Siembra
from Produccion import Produccion
m= Connection('localhost','root','root','PapaProduccion')









def tipoPapa():    
        tipoPapa=TipoDePapa(3,m,'Superior',"adfasdfsadfsdfsdfsadf")
        #RegistrarTipoDePapa
        if(tipoPapa.registrarTipoDePapa()):
            print("Se ha registrado el TipoDePapa")
        else:
            print ("TipoDePapa ya existe")

        #ActualizarTipoDePapa
        #l.set_value(1500012)
        #l.set_variable("id")

        #actualizarTipoDePapa
        #l=TipoDePapa(id=2,conection=m,variable="ancho",value=2211.45)
        #l.actualizarTipoDePapa()

        #consultarTipoDePapa

        for a in tipoPapa.consultarTipoDePapa():
            print(a)



def agricultor():
        agricultorO=Agricultor(4,m,'Juan','Castellanos','Cr12n43-12',321312,'juanas','camilo','Boyaca','Soraca')
        #RegistrarAgricultorif
        if(agricultorO.registrarAgricultor()):
            print("Se ha registrado el Agricultor")
        else:
            print ("Agricultor ya existe")

        #ActualizarAgricultor
        #agricultor.set_value(1500012)
        #l.set_variable("codigoPostal")

        #actualizarAgricultor
        #l=Agricultor(id=2,conection=m,variable="ancho",value=2211.45)
        ##agricultor.actualizarAgricultor()

        #consultarAgricultor
        for a in agricultorO.consultarAgricultor():
            print(a)

def lote():
        
        loteO=Lote(1,m,23.3,21321.4,1500012,'Boyaca','Soraca',1)
        #RegistrarLote
        if(loteO.registrarLote()):
            print("Se ha registrado el lote")
        else:
            print ("Lote ya existe")

        #ActualizarAgricultor
        #agricultor.set_value(1500012)
        #l.set_variable("codigoPostal")

        #actualizarAgricultor
        #l=Agricultor(id=2,conection=m,variable="ancho",value=2211.45)
        ##agricultor.actualizarAgricultor()


        #consultarLote
        for a in loteO.consultarLote():
            print(a)

def siembra():

        siembraO=Siembra(1,m,"2021-02-02",1,2)
        #RegistrarLote
        if(siembraO.registrarSiembra()):
            print("Se ha registrado la siembra")
        else:
            print ("Siembra ya existe")

        for a in siembraO.consultarSiembra():
            print(a)


def produccion():

        produccionO=Produccion(1,m,"2023-02-01",45.3)
        #RegistrarLote
        if(produccionO.registrarProduccion()):
            print("Se ha registrado la produccion")
        else:
            print ("Produccion ya existe")

        for a in produccionO.consultarProduccion():
            print(a)





tipoPapa()

agricultor()

lote()

siembra()

produccion()



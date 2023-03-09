
class Lote():
        
    def __init__(self,id,conection,ancho=None,largo=None,codigoPostal=None,departamento=None,municipio=None,id_agricultor=None,value=None,variable=None):
        self.id=id
        self.ancho=ancho
        self.largo=largo
        self.codigoPostal=codigoPostal
        self.departamento=departamento
        self.municipio=municipio
        self.id_agricultor=id_agricultor
        self.value=value
        self.variable=variable
        self.conection=conection

    def  registrarLote(self):
        if(len(self.buscarLote())==0):
            self.conection.executeSelect("id","departamentos","where nombre",self.departamento)
            idDep=self.conection.fetchall()
            self.conection.executeSelect("id","municipios","where nombre",self.municipio)
            idMun=self.conection.fetchall()
            tupleVal=(self.id,self.ancho,self.largo,self.codigoPostal,idDep[0][0],idMun[0][0],self.id_agricultor)
            self.conection.executeInsert("Lote","%s,%s,%s,%s,%s,%s,%s",tupleVal)
            self.conection.commit()
            return True
        else:
            return False


    def actualizarLote(self):
        self.consultarLote()
        print(self.id)
        self.conection.executeUpdate("Lote",self.variable,self.value,self.id)
        self.conection.commit()

    def consultarLote(self):
        self.buscarLote()
        self.conection.executeSelect("*","Lote","where id",self.id)
        return self.conection.fetchall()

    def buscarLote(self):
        self.conection.executeSelect("id","Lote","where id",self.id)
        return self.conection.fetchall()

    #getters and setters
    def get_id(self):
        return self.id
    
    def set_id(self,id):
        self.id=id

    def get_value(self):
        return self.value
    
    def set_value(self,value):
        self.value=value

    def get_variable(self):
        return self.variable
    
    def set_variable(self,variable):
        self.variable=variable






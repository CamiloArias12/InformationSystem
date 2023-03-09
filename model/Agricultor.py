class Agricultor():
        
    def __init__(self,cedula,conection,nombres=None,apellidos=None,direccion=None,telefono=None,nickname=None,contrasena=None,departamento=None,municipio=None,value=None,variable=None):
        self.cedula=cedula
        self.nombres=nombres
        self.apellidos=apellidos
        self.direccion=direccion
        self.telefono=telefono
        self.nickname=nickname
        self.contrasena=contrasena
        self.departamento=departamento
        self.municipio=municipio
        self.variable=variable
        self.value=value
        self.conection=conection

    def  registrarAgricultor(self):
        if(len(self.buscarAgricultor())==0):
            self.conection.executeSelect("id","departamentos","where nombre",self.departamento)
            idDep=self.conection.fetchall()
            self.conection.executeSelect("id","municipios","where nombre",self.municipio)
            idMun=self.conection.fetchall()
            tupleVal=(self.cedula,self.nombres,self.apellidos,self.direccion,self.telefono,self.nickname,self.contrasena,idMun[0][0],idDep[0][0])
            self.conection.executeInsert("Agricultor","%s,%s,%s,%s,%s,%s,%s,%s,%s",tupleVal)
            self.conection.commit()
            return True
        else:
            return False


    def actualizarAgricultor(self):
        self.consultarAgricultor()
        self.conection.executeUpdate("Agricultor",self.variable,self.value,self.cedula)

    def consultarAgricultor(self):
        self.buscarAgricultor()
        self.conection.executeSelect("*","Agricultor","where cedula",self.cedula)
        return self.conection.fetchall()
 


    def buscarAgricultor(self):
        self.conection.executeSelect("cedula","Agricultor","where cedula",self.cedula)
        return self.conection.fetchall()


    #setters and getters

    def get_cedula(self):
        return self.cedula
    
    def set_cedula(self,cedula):
        self.cedula=cedula

    def get_value(self):
        return self.value
    
    def set_value(self,value):
        self.value=value

    def get_variable(self):
        return self.variable
    
    def set_variable(self,variable):
        self.variable=variable



class TipoDePapa():
        
    def __init__(self,id,conection,nombre=None,descripcion=None,value=None,variable=None):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.value=value
        self.variable=variable
        self.conection=conection

    def  registrarTipoDePapa(self):
        if(len(self.buscarTipoDePapa())==0):
            tupleVal=(self.id,self.nombre,self.descripcion)
            self.conection.executeInsert("TipoDePapa","%s,%s,%s",tupleVal)
            self.conection.commit()
            return True
        else:
            return False


    def actualizarTipoDePapa(self):
        self.consultarTipoDePapa()
        self.conection.executeUpdate("TipoDePapa",self.variable,self.value,self.id)

    def consultarTipoDePapa(self):
        self.buscarTipoDePapa()
        self.conection.executeSelect("*","TipoDePapa","where id",self.id)
        return self.conection.fetchall()
 

    def buscarTipoDePapa(self):
        self.conection.executeSelect("id","TipoDePapa","where id",self.id)
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




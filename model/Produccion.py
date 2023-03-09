
class Produccion():
        
    def __init__(self,id,conection,fecha=None,produccion=None,value=None,variable=None):
        self.id=id
        self.fecha=fecha
        self.produccion=produccion
        self.value=value
        self.variable=variable
        self.conection=conection

    def  registrarProduccion(self):
        if(len(self.buscarProduccion())==0):
            tupleVal=(self.id,self.fecha,self.produccion)
            self.conection.executeInsert("Produccion","%s,%s,%s",tupleVal)
            self.conection.commit()
            return True
        else:
            return False

    def consultarProduccion(self):
        self.buscarProduccion()
        self.conection.executeSelect("*","Produccion","where id",self.id)
        return self.conection.fetchall()
 


    def buscarProduccion(self):
        self.conection.executeSelect("id","Produccion","where id",self.id)
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





class Siembra():
        
    def __init__(self,id,conection,fecha=None,value=None,variable=None,id_lote=None,id_tipoPapa=None):
        self.id=id
        self.fecha=fecha
        self.id_lote=id_lote
        self.id_tipoPapa=id_tipoPapa
        self.value=value
        self.variable=variable
        self.conection=conection

    def  registrarSiembra(self):
        if(len(self.buscarSiembra())==0):
            tupleVal=(self.id,self.fecha,self.id_lote,self.id_tipoPapa)
            self.conection.executeInsert("Siembra","%s,%s,%s,%s",tupleVal)
            self.conection.commit()
            return True
        else:
            return False

    def consultarSiembra(self):
        self.buscarSiembra()
        self.conection.executeSelect("*","Siembra","where id",self.id)
        return self.conection.fetchall()
 


    def buscarSiembra(self):
        self.conection.executeSelect("id","Siembra","where id",self.id)
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




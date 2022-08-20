class Human:
    numberOfPeople=0
    def __init__(self,name,age,nik,profession):
        self.name=name
        self.age=age
        self.__nik=nik
        self.profession=profession
        Human.numberOfPeople+=1
    @property
    def info(self):
        return f"Nama saya {self.name}"
        
    @property
    def nik():
        pass

    @nik.getter
    def nik(self):
        return self.__nik

    @nik.setter
    def nik(self,newNik):
        self.__nik=newNik
        
    @classmethod   #@staticmethod # @classmethod 
    def getNumberOfPeople(sel):
        return sel.numberOfPeople
    
    def getName(self):
        return f"Nama saya {self.name}"

    def setName(self):
        self.name="Koko"

    def setAgeSibling(self,saudara):
        saudara.age=5

    def setAge(self,newAge):
        self.age=newAge



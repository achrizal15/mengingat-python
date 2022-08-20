class Human:
    numberOfPeople=0
    def __init__(self,name,age,nik,profession):
        self.name=name
        self.age=age
        self.__nik=nik
        self.profession=profession
        Human.numberOfPeople+=1
   
    def getNik(self):
        return self.__nik
        
    @staticmethod   #@staticmethod # @classmethod 
    def getNumberOfPeople():
        return Human.numberOfPeople
    
    def getName(self):
        return f"Nama saya {self.name}"

    def setName(self):
        self.name="Koko"

    def setAgeSibling(self,saudara):
        saudara.age=5

    def setAge(self,newAge):
        self.age=newAge



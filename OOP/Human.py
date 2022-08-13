class Human:
    numberOfPeople=0
    def __init__(self,name,age,profession):
        self.name=name
        self.age=age
        self.profession=profession
        Human.numberOfPeople+=1
        
    def getNumberOfPeople(self):
        return Human.numberOfPeople
    
    def getName(self):
        return f"Nama saya {self.name}"

    def setName(self):
        self.name="Koko"

    def setAgeSibling(self,saudara):
        saudara.age=5

    def setAge(self,newAge):
        self.age=newAge

mahasiswa=Human(name="Ach Rizal",age=10,profession="Mahasiswa")
pengacara=Human(name="Widya Agustina",age=10,profession="Pengacara")
print(pengacara.getNumberOfPeople())


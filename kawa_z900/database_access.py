import os

database_file = "kawa_z900\kawa_z900_parts.txt"

class Part:
    def __init__(self,part_name:str,part_type:str,part_id:int,part_prize:float,part_dealer:str) -> None:
        self.name  = part_name
        self.type  = part_type
        self.id    = part_id
        self.prize = part_prize
        self.dealer  = part_dealer

    def setName(self,set_name:str) -> None:
        self.name = set_name
    def getName(self) -> str:
        return self.name
    
    def setType(self,set_type:str) -> None:
        self.type = set_type
    def getTpye(self) -> str:
        return self.type
    
    def setId(self,set_id:int) -> None:
        self.id = set_id
    def getId(self) -> int:
        return self.id
    
    def setPrize(self,set_prize:float) -> None:
        self.name = set_prize
    def getName(self) -> float:
        return self.prize
    
    def setDealer(self,set_dealer:str) -> None:
        self.name = set_dealer
    def getDealer(self) -> str:
        return self.dealer
    def openDealer(self) -> None:
        command = "start " + self.getDealer()
        os.system(command)
    
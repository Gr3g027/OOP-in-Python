from os import sep
from random import randint
import csv
from cane import *

class CaneCorsa(Cane):
    def __init__(self, name='Fuffi', distanza=0, vittorie=0):
        super().__init__(name)
        self.distanza = distanza
        self.vittorie = vittorie

    def avanza(self):
        self.distanza += randint(1,10)

    def reset(self):
        self.distanza = 0

    def vince(self):
        if self.distanza > 1000:
            self.vittorie += 1
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name} {self.distanza}m "
    
    def to_csv(self):
        return f"{self.name},{self.distanza}\n"

    def to_csv_vitt(self):
        return f"{self.name},{self.vittorie}\n"

    def save(self):
        with open("vincitori.csv","a") as file:
            file.write(self.to_csv())
            file.close()                

    def save_num_vitt(cani):
            with open("numvittorie.csv","a") as file:
                for cane in cani:
                    file.write(cane.to_csv_vitt())
                    file.close()

if __name__ == "__main__":
    running = True
    cane1 = CaneCorsa("Black")
    cane2 = CaneCorsa("Polpetta")
    cane3 = CaneCorsa("Thor")
    cane4 = CaneCorsa("Otto")

    cani = [cane1, cane2, cane3, cane4]

    while(True):
        while(running): 
            for cane in cani :
                cane.avanza()
                if cane.vince():
                    print("Vince " + cane.name + "! Distanza percorsa: " + str(cane.distanza) + "m")
                    cane.save()
                    running = False
        print("[ Classifica ]")
        cani.sort(key=lambda cane : cane.distanza, reverse=True)
        for cane in cani:
            print(cane)
        
        next = input("\nAltra gara? (s/n): ")
        if next not in ['S', 's']:
            break
        else:
            for cane in cani: 
                cane.reset()
            running = True
        
        '''
        file = open("vincitori.csv", "a")
        file.write(cani[0].__str__())
        file.close()

        with open("vincitori.csv","a") as file:
            file.write(cani[0].to_csv())
            file.close()
        '''
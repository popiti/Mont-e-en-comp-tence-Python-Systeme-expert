## EL MEJJAD Walid

import numpy as np 

class Jeu_Hanoi:
        
    def __init__(self, nb_pic, nb_palet):
        self.pic = (np.zeros([nb_pic, nb_palet],dtype= int))
        self.nombre_palet = (np.zeros(nb_pic, dtype= int))
        self.nombre_palet[0] = nb_palet
        
        for i in range(nb_palet):
            self.pic[0, i] = nb_palet - i
    
    def situation(self):
        return str(self.pic)
    

    def pic_vide(self, indice_pic):
        return self.nombre_palet[indice_pic] == 0
                
    def regle_jeu(self, indice_pic1, indice_pic2):
        if self.pic_vide(indice_pic1):
            return False
        elif (self.pic_vide(indice_pic2)) or self.pic[indice_pic1, self.nombre_palet[indice_pic1] - 1] < self.pic[indice_pic2, self.nombre_palet[indice_pic2] - 1]:
            return True 
        else:
            return False


    def effectue_deplacement(self, indice_pic1, indice_pic2):

        self.pic[indice_pic2, self.nombre_palet[indice_pic2]] = self.pic[indice_pic1, self.nombre_palet[indice_pic1] - 1]
        self.pic[indice_pic1, self.nombre_palet[indice_pic1] - 1] = 0

        self.nombre_palet[indice_pic1] = self.nombre_palet[indice_pic1] - 1
        self.nombre_palet[indice_pic2] = self.nombre_palet[indice_pic2] + 1
                

    def situation_non_vue(self, indice_pic1, indice_pic2, situation_etudiee):

        self.effectue_deplacement(indice_pic1, indice_pic2)

        for situation in situation_etudiee:
            if np.array_equal(self.pic, situation):
                self.effectue_deplacement(indice_pic2, indice_pic1)
                return True

        self.effectue_deplacement(indice_pic2, indice_pic1)
        return False
    

    def moteur_inference(self):
        situation_etudiee = []
        coups = 0
        
        # Ajout de la situation initiale
        situation_etudiee.append(np.copy(self.pic))
        
        # Tant que la situation finale n'est pas atteinte c'est à dire tous les palets sur le dernier pique
        while self.nombre_palet[2] != self.pic[0].size:            
            # ajout de regle pour optimiser
            if not self.pic_vide(0) and self.regle_jeu(0, 2) and not self.situation_non_vue(0, 2, situation_etudiee):
                self.effectue_deplacement(0, 2)
                coups += 1
                print(f"Déplacement de 0 à 2 (Coup {coups})")
            elif not self.pic_vide(0) and self.regle_jeu(0, 1) and not self.situation_non_vue(0, 1, situation_etudiee):
                self.effectue_deplacement(0, 1)
                coups += 1
                print(f"Déplacement de 0 à 1 (Coup {coups})")
            elif not self.pic_vide(1) and self.regle_jeu(1, 2) and not self.situation_non_vue(1, 2, situation_etudiee):
                self.effectue_deplacement(1, 2)
                coups += 1
                print(f"Déplacement de 1 à 2 (Coup {coups})")
            elif not self.pic_vide(2) and self.regle_jeu(2, 1) and not self.situation_non_vue(2, 1, situation_etudiee):
                self.effectue_deplacement(2, 1)
                coups += 1
                print(f"Déplacement de 2 à 1 (Coup {coups})")
            elif not self.pic_vide(1) and self.regle_jeu(1, 0) and not self.situation_non_vue(1, 0, situation_etudiee):
                self.effectue_deplacement(1, 0)
                coups += 1
                print(f"Déplacement de 1 à 0 (Coup {coups})")
            
            # Afficher la situation actuelle
            print(self.situation())
            situation_etudiee.append(np.copy(self.pic))

        print(f"Problème résolu en {coups} coups !")
        

    
            
# Main
if __name__ == "__main__":

    # Teste
    print("Teste initialisation")
    jeu_test = Jeu_Hanoi(3, 3)
    print("Teste liste des situations étudiées ")
    situations_etudiees = [jeu_test.pic.copy()]

    # Situation initiale
    print("Situation initiale :")
    print(jeu_test.situation())

    # Déplacement de 0 à 1, puis test si cette nouvelle situation a déjà été vue
    if jeu_test.situation_non_vue(0, 1, situations_etudiees):
        print("La situation après déplacement de 0 à 1 a déjà été vue.")
    else:
        print("La situation après déplacement de 0 à 1 est nouvelle.")
        situations_etudiees.append(jeu_test.pic.copy())  # Ajouter la nouvelle situation aux étudiées

    # Afficher la situation après le premier test
    print("Situation après le test de déplacement de 0 à 1 :")
    print(jeu_test.situation())

    # Déplacement de 1 à 2, puis test si cette nouvelle situation a déjà été vue
    if jeu_test.situation_non_vue(1, 2, situations_etudiees):
        print("La situation après déplacement de 1 à 2 a déjà été vue.")
    else:
        print("La situation après déplacement de 1 à 2 est nouvelle.")
        situations_etudiees.append(jeu_test.pic.copy())  # Ajouter la nouvelle situation aux étudiées

    # Afficher la situation après le deuxième test
    print("Situation après le test de déplacement de 1 à 2 :")
    print(jeu_test.situation())

    # Test à nouveau le déplacement 0 -> 1 (qui devrait déjà être vu)
    if jeu_test.situation_non_vue(0, 1, situations_etudiees):
        print("La situation après le déplacement de 0 à 1 est déjà vue.")
    else:
        print("La situation après le déplacement de 0 à 1 est nouvelle.")


    # Teste du moteur d'inférence
    print()
    print("Demo")
    jeu = Jeu_Hanoi(3, 3)
    jeu.moteur_inference()
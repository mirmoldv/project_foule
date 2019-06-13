# -*- coding: utf-8 -*-
import random
#Methodes
class Point():
    """
    une classe pour les points
    """
    def __init__(self,x,y):
        self.x = x         
        self.y = y       

    def __str__(self):
        return 'Coordonnées du point : ' + '(' + str(self.x) + ";" + str(self.y) + ')'
        

class Vecteur():
    """
    une classe pour le vecteur vitesse
    """
    def __init__(self,vx,vy):
        self.vx = vx         
        self.vy = vy       

    def __str__(self):
        return 'Vecteur vitesse : ' + '(' + str(self.vx) + ";" + str(self.vy) + ')'


class Element():
    """
    une classe pour définir les éléments sur la carte
    """
    def __init__(self,position):     # Position de l'objet dans la carte
        self.pos = position         
    
    def __str__(self):
        return 'Position : ' + '(' + str(self.pos.x) + ";" + str(self.pos.y) + ')'


class Obstacle(Element):
    """
    une classe pour définir un Obstacle sur la carte
    """
    

class Voyageur(Element):
    """
    une classe pour définir un Voyageur sur la carte
    """
    def __init__(self,position,destination):     # Position courante et destination
        self.pos = position         
        self.dest = destination

    
    def __str__(self):
        return 'Position courante : ' + '(' + str(self.pos.x) + ";" + str(self.pos.y) + ')' + '\n' + 'Destination : ' + '(' + str(self.dest.x) + ";" + str(self.dest.y) + ')'

    def setPos(self,newPosition):               # Méthode permettant de changer la position du voyageur
        self.pos=newPosition
    
    


class Carte():
    """
    une classe pour la carte qui va contenir les éléments (obstacles et voyageurs) de la carte
    ainsi que la grille (matrice) positionnant les éléments
    """
    def __init__(self,dimensionsCarte,dimensionsGrille):
        self.dimCarte = dimensionsCarte          # dimension (largeur et hauteur) de la carte en pixels
        self.dimGrille = dimensionsGrille        # dimension (nombre de lignes et nombre de colonnes) de la grille
        self.elements = []                      # liste qui va contenir tous les élements de la carte
        self.grille = [[False]*self.dimGrille.y for i in range(self.dimGrille.x)]  # Matrice dont chaque élément vaut true (si un élément) ou false sinon 
        
    def ajouter_element(self,element):  # Méthode pour ajouter un élément à la carte
        self.grille[element.pos.x][element.pos.y]=True    # On indique dans grille qu'un élément est présent en (x,y)
        self.elements.append(element)                   # On ajoute cet élément à la liste des éléments de la carte 
        
    def retirer_element(self,element):  # Méthode pour retirer un élément de la carte
        self.grille[element.pos.x][element.pos.y]=False  # On indique dans grille que l'élément n'est plus présent en (x,y) 
        self.elements.remove(element) # On retire cet élément de la liste des éléments de la carte

    def deplacer_element(self,element):    # Fonction qui déplace un élément dans la carte
        dx = element.dest.x - element.pos.x
        dy = element.dest.y - element.pos.y
        if dx > 0 :
            dx = 1
        elif dx == 0 :
            dx = 0
        else:
            dx=-1
        if dy > 0 :
            dy = 1
        elif dy == 0 :
            dy = 0
        else:
            dy=-1
        if dx==0 and dy==0:
            self.retirer_element(element)
            return True
        else:
            if self.presence_element(element.pos.x+dx,element.pos.y+dy)==False:
				self.grille[element.pos.x][element.pos.y]=False
				element.pos.x=element.pos.x+dx
				element.pos.y=element.pos.y+dy
				self.grille[element.pos.x][element.pos.y]=True
				return 1
            else:
				if self.presence_element(element.pos.x+dx,element.pos.y)==False:
				    self.grille[element.pos.x][element.pos.y]=False
				    element.pos.x=element.pos.x+dx
				    element.pos.y=element.pos.y
				    self.grille[element.pos.x][element.pos.y]=True
				    return 1
				elif self.presence_element(element.pos.x,element.pos.y+dy)==False:
				    self.grille[element.pos.x][element.pos.y]=False
				    element.pos.x=element.pos.x
				    element.pos.y=element.pos.y+dy
				    self.grille[element.pos.x][element.pos.y]=True
				    return 1
				else:
				    return 0		
    
    def presence_element(self,x,y):    #detection de présence d'un élément
		if self.grille[x][y]==True:
			return True
		else:
			return False

    def affiche_grille(self):			#affichage de la grille
        for x in range(self.dimGrille.x):
            out=""
            for y in range(self.dimGrille.y):
                if self.grille[x][y] == True :
                    out+="1 "
                else:
                    out+="0 "
            print(out)
			
    def __str__(self):
        return 'Carte=' + '(' + str(self.dimCarte.x) + ";" + str(self.dimCarte.y) + ')' + '\n' + 'Grille=' + '(' + str(self.dimGrille.x) + ";" + str(self.dimGrille.y) + ')' + '\n' + 'Nb éléments : ' + str(len(self.elements))
     


dimension = Point(10,10)
plan=Carte(dimension,dimension)
for i in range(5):
	destination = Point(random.randint(0,9),random.randint(0,9))
	position_personne= Point(random.randint(0,9),random.randint(0,9))
	personne = Voyageur(position_personne,destination)
	plan.ajouter_element(personne)
	print personne

print(plan)
plan.affiche_grille()
plan.ajouter_element(personne)
print("Debut")
while(len(plan.elements)>0):
    compte=0
    for pers in plan.elements:
        compte+=plan.deplacer_element(pers)
#        print(pers)
#    plan.affiche_grille()
    if compte==0 :
		break
plan.affiche_grille()
print(plan)
	
	


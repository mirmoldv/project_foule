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
    def __init__(self,position,destination,nom):     # Position courante et destination
        self.pos = position         
        self.dest = destination
        self.nom = nom

    
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
        self.grille = [[0]*self.dimGrille.y for i in range(self.dimGrille.x)]  # Matrice dont chaque élément vaut true (si un élément) ou false sinon 
        
    def ajouter_element(self,element):  # Méthode pour ajouter un élément à la carte
        self.grille[element.pos.x][element.pos.y]=element.nom    # On indique dans grille qu'un élément est présent en (x,y)
        self.elements.append(element)                   # On ajoute cet élément à la liste des éléments de la carte 
        
    def ajouter_obstacle(self,x,y):
		self.grille[x][y]="#"

    def retirer_element(self,element):  # Méthode pour retirer un élément de la carte
        self.grille[element.pos.x][element.pos.y]=0  # On indique dans grille que l'élément n'est plus présent en (x,y) 
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
				self.grille[element.pos.x][element.pos.y]=0
				element.pos.x=element.pos.x+dx
				element.pos.y=element.pos.y+dy
				self.grille[element.pos.x][element.pos.y]=element.nom
				return 1
            else:
				if self.presence_element(element.pos.x+dx,element.pos.y)==False:
				    self.grille[element.pos.x][element.pos.y]=0
				    element.pos.x=element.pos.x+dx
				    element.pos.y=element.pos.y
				    self.grille[element.pos.x][element.pos.y]=element.nom
				    return 1
				elif self.presence_element(element.pos.x,element.pos.y+dy)==False:
				    self.grille[element.pos.x][element.pos.y]=0
				    element.pos.x=element.pos.x
				    element.pos.y=element.pos.y+dy
				    self.grille[element.pos.x][element.pos.y]=element.nom
				    return 1
				elif self.presence_element(element.pos.x+(dx^1),element.pos.y+dy)==False:
				    self.grille[element.pos.x][element.pos.y]=0
				    element.pos.x=element.pos.x+(dx^1)
				    element.pos.y=element.pos.y+dy
				    self.grille[element.pos.x][element.pos.y]=element.nom
				    return 1
				elif self.presence_element(element.pos.x+dx,element.pos.y+(dy^1))==False:
				    self.grille[element.pos.x][element.pos.y]=0
				    element.pos.x=element.pos.x+dx
				    element.pos.y=element.pos.y+(dy^1)
				    self.grille[element.pos.x][element.pos.y]=element.nom
				    return 1
				elif self.presence_element(element.pos.x-(dx^1),element.pos.y+dy)==False:
				    self.grille[element.pos.x][element.pos.y]=0
				    element.pos.x=element.pos.x-(dx^1)
				    element.pos.y=element.pos.y+dy
				    self.grille[element.pos.x][element.pos.y]=element.nom
				    return 1
				elif self.presence_element(element.pos.x+dx,element.pos.y-(dy^1))==False:
				    self.grille[element.pos.x][element.pos.y]=0
				    element.pos.x=element.pos.x+dx
				    element.pos.y=element.pos.y-(dy^1)
				    self.grille[element.pos.x][element.pos.y]=element.nom
				    return 1
				elif self.presence_element(element.pos.x+dx,element.pos.y-dy)==False:
				    self.grille[element.pos.x][element.pos.y]=0
				    element.pos.x=element.pos.x+dx
				    element.pos.y=element.pos.y-dy
				    self.grille[element.pos.x][element.pos.y]=element.nom
				    return 1
				elif self.presence_element(element.pos.x-dx,element.pos.y+dy)==False:
				    self.grille[element.pos.x][element.pos.y]=0
				    element.pos.x=element.pos.x-dx
				    element.pos.y=element.pos.y+dy
				    self.grille[element.pos.x][element.pos.y]=element.nom
				    return 1			    
				else:
				    return 0		
    
    def presence_element(self,x,y):    #detection de présence d'un élément
		if x<self.dimGrille.x and x>-1 and y<self.dimGrille.y and y>-1:
			if self.grille[x][y]!=0:
				return True
			else:
				return False
		else:
			return True

    def affiche_grille(self):			#affichage de la grille
        for x in range(self.dimGrille.x):
            out=""
            for y in range(self.dimGrille.y):
                out+=str(self.grille[x][y])+' '
            print(out)
			
    def __str__(self):
        return 'Carte=' + '(' + str(self.dimCarte.x) + ";" + str(self.dimCarte.y) + ')' + '\n' + 'Grille=' + '(' + str(self.dimGrille.x) + ";" + str(self.dimGrille.y) + ')' + '\n' + 'Nb éléments : ' + str(len(self.elements))
     

dmax=30
dimension = Point(dmax,dmax)
plan=Carte(dimension,dimension)
"""
obstacle
"""
def etoile(x,y):
	plan.ajouter_obstacle(x,y)
	plan.ajouter_obstacle(x+1,y)
	plan.ajouter_obstacle(x+2,y)
	plan.ajouter_obstacle(x-1,y)
	plan.ajouter_obstacle(x-2,y)
	plan.ajouter_obstacle(x,y+1)
	plan.ajouter_obstacle(x,y+2)
	plan.ajouter_obstacle(x,y-1)
	plan.ajouter_obstacle(x,y-2)
	plan.ajouter_obstacle(x+1,y+1)
	plan.ajouter_obstacle(x-1,y+1)
	plan.ajouter_obstacle(x+1,y-1)
	plan.ajouter_obstacle(x-1,y-1)

etoile(10,5)
etoile(15,15)
etoile(10,20)
"""
voyageur
"""
for i in range(40):
	destination = Point(0,0)#random.randint(0,9))
	vx=random.randint(round(dmax/2)+6,dmax-1)
	vy=random.randint(round(dmax/2)+6,dmax-1)
	position_personne= Point(vx,vy)
	if plan.presence_element(vx,vy)==False :
		personne = Voyageur(position_personne,destination,2)
		plan.ajouter_element(personne)
		print personne
for i in range(0):
	destination = Point(29,29)#random.randint(0,9))
	vx=random.randint(0,round(dmax/2)-1)
	vy=random.randint(0,round(dmax/2)-1)
	position_personne= Point(vx,vy)
	if plan.presence_element(vx,vy)==False :
		personne = Voyageur(position_personne,destination,3)
		plan.ajouter_element(personne)
		print personne
print(plan)
plan.affiche_grille()
plan.ajouter_element(personne)
print("Debut")
essai=0
while(len(plan.elements)>0):
    compte=0
    for pers in plan.elements:
        if plan.deplacer_element(pers)!=0:
			compte+=1
        print(pers)
    plan.affiche_grille()
    if compte==0 :
        if essai == len(plan.elements):
            essai=0
            break
        else:
            essai+=1
print("Position finale")
plan.affiche_grille()
print(plan)
	
	


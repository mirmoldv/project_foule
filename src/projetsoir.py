# -*- coding: utf-8 -*-
import random
import Tkinter as tk
import time
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

class Voyageur():
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
    def __init__(self,dimensionsCarte,dimensionsGrille,canvas):
        self.dimCarte = dimensionsCarte          # dimension (largeur et hauteur) de la carte en pixels
        self.dimGrille = dimensionsGrille        # dimension (nombre de lignes et nombre de colonnes) de la grille
        self.elements = []                      # liste qui va contenir tous les élements de la carte
        self.grille = [['v']*self.dimGrille.y for i in range(self.dimGrille.x)]  # Matrice dont chaque élément vaut true (si un élément) ou false sinon 
        self.can = canvas
        self.dessin = []
        
    def ajouter_element(self,element):  # Méthode pour ajouter un élément à la carte
        self.grille[element.pos.x][element.pos.y]=element.nom    # On indique dans grille qu'un élément est présent en (x,y)
        self.elements.append(element)                   # On ajoute cet élément à la liste des éléments de la carte 
        
    def ajouter_obstacle(self,x,y):
		self.grille[x][y]="#"

    def retirer_element(self,element):  # Méthode pour retirer un élément de la carte
        self.grille[element.pos.x][element.pos.y]='v'  # On indique dans grille que l'élément n'est plus présent en (x,y) 
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
                self.grille[element.pos.x][element.pos.y]='v'
                element.pos.x=element.pos.x+dx
                element.pos.y=element.pos.y+dy
                self.grille[element.pos.x][element.pos.y]=element.nom
                return 1
            else:
                if self.presence_element(element.pos.x+dx,element.pos.y)==False:
                    self.grille[element.pos.x][element.pos.y]='v'
                    element.pos.x=element.pos.x+dx
                    element.pos.y=element.pos.y
                    self.grille[element.pos.x][element.pos.y]=element.nom
                    return 1
                elif self.presence_element(element.pos.x,element.pos.y+dy)==False:
                    self.grille[element.pos.x][element.pos.y]='v'
                    element.pos.x=element.pos.x
                    element.pos.y=element.pos.y+dy
                    self.grille[element.pos.x][element.pos.y]=element.nom
                    return 1
                elif self.presence_element(element.pos.x+(dx^1),element.pos.y+dy)==False:
                    self.grille[element.pos.x][element.pos.y]='v'
                    element.pos.x=element.pos.x+(dx^1)
                    element.pos.y=element.pos.y+dy
                    self.grille[element.pos.x][element.pos.y]=element.nom
                    return 1
                elif self.presence_element(element.pos.x+dx,element.pos.y+(dy^1))==False:
                    self.grille[element.pos.x][element.pos.y]='v'
                    element.pos.x=element.pos.x+dx
                    element.pos.y=element.pos.y+(dy^1)
                    self.grille[element.pos.x][element.pos.y]=element.nom
                    return 1
                elif self.presence_element(element.pos.x-(dx^1),element.pos.y+dy)==False:
                    self.grille[element.pos.x][element.pos.y]='v'
                    element.pos.x=element.pos.x-(dx^1)
                    element.pos.y=element.pos.y+dy
                    self.grille[element.pos.x][element.pos.y]=element.nom
                    return 1
                elif self.presence_element(element.pos.x+dx,element.pos.y-(dy^1))==False:
                    self.grille[element.pos.x][element.pos.y]='v'
                    element.pos.x=element.pos.x+dx
                    element.pos.y=element.pos.y-(dy^1)
                    self.grille[element.pos.x][element.pos.y]=element.nom
                    return 1
                elif self.presence_element(element.pos.x+dx,element.pos.y-dy)==False:
                    self.grille[element.pos.x][element.pos.y]='v'
                    element.pos.x=element.pos.x+dx
                    element.pos.y=element.pos.y-dy
                    self.grille[element.pos.x][element.pos.y]=element.nom
                    return 1
                elif self.presence_element(element.pos.x-dx,element.pos.y+dy)==False:
                    self.grille[element.pos.x][element.pos.y]='v'
                    element.pos.x=element.pos.x-dx
                    element.pos.y=element.pos.y+dy
                    self.grille[element.pos.x][element.pos.y]=element.nom
                    return 1			    
                else:
                    return 0		

    def presence_element(self,x,y):    #detection de présence d'un élément
        if x<self.dimGrille.x and x>-1 and y<self.dimGrille.y and y>-1:
            if self.grille[x][y]!='v':
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
    def anim_grille(self,taille):
        for x in range(self.dimGrille.x):
            for y in range(self.dimGrille.y):
                if self.grille[x][y]=="#":
                    rect=self.can.create_rectangle((y*taille),(x*taille),((y+1)*taille),((x+1)*taille),fill="white")
                    self.dessin.append(rect)
                elif self.grille[x][y][0]=='p':
                    rect=self.can.create_oval(y*taille, x*taille, ((y+1)*taille),((x+1)*taille), width=1, fill="red")
                    self.dessin.append(rect)
                elif self.grille[x][y][0]=='d':
                    rect=self.can.create_oval(y*taille, x*taille, ((y+1)*taille),((x+1)*taille), width=1, fill="blue")
                    self.dessin.append(rect)
    def efface(self):
        for rect in self.dessin:
            self.can.delete(rect)	   

			
    def __str__(self):
        return 'Carte=' + '(' + str(self.dimCarte.x) + ";" + str(self.dimCarte.y) + ')' + '\n' + 'Grille=' + '(' + str(self.dimGrille.x) + ";" + str(self.dimGrille.y) + ')' + '\n' + 'Nb éléments : ' + str(len(self.elements))
     


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

def rectangle(x,y,fx,fy):
	for i in range(fx):
		for j in range(fy):
			plan.ajouter_obstacle(x+i,y+j)

"""
fonctions
"""
def create_personne():
    global go
    go=1
    for i in range(20):
        destination = Point(0,0)#random.randint(0,9))
        vx=random.randint(round(dmax/2)+7,dmax-1)
        vy=random.randint(round(dmax/2)+7,dmax-1)
        position_personne= Point(vx,vy)
        if plan.presence_element(vx,vy)==False :
            personne = Voyageur(position_personne,destination,"p"+str(i))
            plan.ajouter_element(personne)
    for i in range(20):
        destination = Point(29,29)#random.randint(0,9))
        vx=random.randint(0,round(dmax/2)-7)
        vy=random.randint(0,round(dmax/2)-7)
        position_personne= Point(vx,vy)
        if plan.presence_element(vx,vy)==False :
            personne = Voyageur(position_personne,destination,"d"+str(i))
            plan.ajouter_element(personne)
def anim_personne():
    global go
    if go==1:
        compte=0
        for pers in plan.elements:
            if plan.deplacer_element(pers)!=0:
                compte+=1
        plan.efface()
        plan.anim_grille(taille)
    id=can.after(500,anim_personne)
def stop():
	global go
	go=0

go=0
fen = tk.Tk()
fen.title("Simulateur de foule")
dmax=30
taille=20
dimension = Point(dmax,dmax)
can = tk.Canvas(fen,bg='dark grey',height=dmax*taille, width=dmax*taille)
plan=Carte(dimension,dimension,can)
etoile(12,5)
etoile(17,15)
etoile(10,22)
rectangle(22,15,2,12)
rectangle(5,5,2,12)
rectangle(22,15,8,2)

can.pack(side="left", padx='5', pady = '5')
bou1= tk.Button(fen, text='Démarrer', width =8, command=create_personne)
bou1.pack()
bou2 = tk.Button(fen, text='Arrêter', width =8, command=stop)
bou2.pack()
bou3= tk.Button(fen, text='Quitter', width =8, command=fen.destroy)
bou3.pack(side="bottom")
can.after(500,anim_personne)

fen.mainloop()
fen.destroy()
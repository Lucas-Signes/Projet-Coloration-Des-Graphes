import random #On import random pour le generateur de graphe aleatoire
import string #On import le module string
sommet = list(string.ascii_lowercase) #de string on prend une liste de toutes les lettres de l'sommet dans une variable sommet

#######################################################

class Graphe:

    def __init__(self, L):
        '''
        Methode pour initialiser un objet graphe comme une liste donne et le nombre de sommet N_sommet comme la longeur de la liste
        '''
        self.graphe = L #le graphe est egale a une liste
        self.N_sommet = len(L) #les nombre de sommet de la liste N_sommet est egale a la longeur de la liste

    def parcours_larg(self):
        '''
        Methode qui parcours un graphe par la largeur et retourne la liste de sommets parcourus 
        '''
        F = [0]
        L_sommets_parcourus = []
        while F != []:
            sommet_courrant = F.pop(0) #Dans la boucle while F n'est pas vide on donne la variable sommet_courrant la valeur de enelever la premier valuer de F

            if not(sommet_courrant in L_sommets_parcourus):
                L_sommets_parcourus.append(sommet_courrant) #Si le sommet_courrant ne fait pas partie de la liste des sommet parcourrus alors on append le sommet courrant

                for voisin in self.graphe[sommet_courrant]: #puis la boucle for que les nombre de voisins sont dans la postion du sommer courrant du graphe on append un voisin a la liste F
                    F.append(voisin)

        return L_sommets_parcourus #On retourne la liste de sommet parcourrus

    def parcours_prof(self):
        '''
        Methode qui parcours un graphe par la profondeur et on retourne la liste de sommets parcourus 
        '''
        P = [0]
        L_sommets_parcourus = []
        while P != []:
            sommet_courrant = P.pop() #Dans la boucle while F n'est pas vide on donne la variable sommet_courrant la valeur de enelever la premier valuer de P

            if not(sommet_courrant in L_sommets_parcourus):
                L_sommets_parcourus.append(sommet_courrant) #Si le sommet_courrant ne fait pas partie de la liste des sommet parcourrus alors on append le sommet courrant

                for voisin in self.graphe[sommet_courrant]: #puis la boucle for que les nombre de voisins sont dans la postion du sommer courrant du graphe on append un voisin a la liste P
                        P.append(voisin)

        return L_sommets_parcourus

    def successeur_matrix_oriente(self, N): #On retourne la liste de sommet parcourrus
        '''
        Methode qui trouve tout les successeurs d'un sommet donne d'un graphe de type matrice donne 
        '''
        L = []
        for i in range(len(self.graphe)): #On fait une boucle for la longeur de la liste car dans une matrice longeur = largeur
            
            if self.graphe[N][i] > 0: #Chaque fois qu'on a un sommet superieur a 0 on append cette liaison a une liste
                L.append(sommet[i])

        return L

    def predecesseur_matrix_oriente(self, N):
        '''
        Methode qui trouve tout les predecesseur d'un sommet donne d'un graphe de type matrice donne 
        '''
        L = []
        for i in range(len(self.graphe)): #On fait une boucle for la longeur de la liste car dans une matrice longeur = largeur

            if self.graphe[i][N] > 0: # Pour chaque sommet on verifie si il ya une valeur positive pour la valeur N donne et si oui on ajoute la lisison a la liste
                L.append(sommet[i])

        return L

    def conv_matrix_a_adj_nonoriente(self):
        '''
        Methode qui transforme un graphe de type matrice en graphe de type liste d'adjacence non oriente
        '''
        L = [[]for i in range(len(self.graphe))] #On cree une liste vide qui a autant de sommet vide que la longeur du graphe
        for i in range(len(self.graphe)):

            for j in range(len(self.graphe)): #On fait 2 boucles for pour traverser le graphe en matrice en entier

                if self.graphe[i][j] > 0: #Si il y'a une liaison on append cette liaison a la liste 
                    L[i].append(j)

        self.graphe = L #On dit que notre graphe est egale a la nouvelle liste

    def conv_matrix_a_adj_oriente(self):
        '''
        Methode qui transforme un graphe de type matrice en graphe de type liste d'adjacence oriente
        '''
        L = [] #On set L comme une liste vide 
        for i in range(len(self.graphe)):
            vertex = []

            for j in range(len(self.graphe)): #On fait 2 boucles for pour traverser le graphe en matrice en entier

                if self.graphe[i][j] > 0: #Si il y'a une liaison on append cette liaison et l'orientation du graphe a la liste
                    vertex.append([sommet[j], self.graphe[i][j]]) 

            L.append(vertex) #On dit que notre graphe est egale a la nouvelle liste

        self.graphe = L #On dit que notre graphe est egale a la nouvelle liste

    def successeur_adj_oriente(self, N):
        '''
        Methode qui trouve tout les successeurs d'un sommet donne d'un graphe de type de liste d'adjacence donne 
        '''
        L = []
        for i in range(len(self.graphe[N])): #On fait une boucle for pour traverser la liste d'adjacence du sommet donne
            L.append(self.graphe[N][i][0]) #On append toutes les valeurs a la liste L

        return L

    def predecesseur_adj_oriente(self, N):
        '''
        Methode qui trouve tout les predecesseur d'un sommet donne d'un graphe de type liste d'adjacence donne 
        '''
        L = []
        for i in range(len(self.graphe)):

            for j in range(len(self.graphe[i])): #On fait 2 boucles for pour traverser le graphe en entier

                if self.graphe[i][j][0] == sommet[N]: #Si il ya une valeur d'un sommet qui appel le sommet donne alors on l'append a la liste
                    L.append(sommet[i])

        return L 

    def conv_adj_nonoriente_a_matrix(self):
        '''
        Methode qui transforme un graphe de type liste d'adjacence non oriente en graphe de type matrice
        '''
        L = [[0 for i in range(len(self.graphe))] for j in range(len(self.graphe))] #On cree une liste de 0 de longeur et largeur la longeur de la liste
        for i in range(len(self.graphe)):

            for j in self.graphe[i]: #On fait 2 boucles for pour traverser le graphe en entier
                L[i][j] = 1 #Pour chaque liaison on met que cet valeur vaut '1' pour la matrice 

        self.graphe = L #On dit que notre graphe est egale a la nouvelle liste

    def conv_adj_oriente_a_matrix(self):
        '''
        Methode qui transforme un graphe de type liste d'adjacence oriente en graphe de type matrice
        '''
        L = [[0 for i in range(len(self.graphe))] for j in range(len(self.graphe))] #On cree une liste de 0 de longeur et largeur la longeur de la liste
        for i in range(len(self.graphe)):

            for elem in self.graphe[i]: #On fait 2 boucles for pour traverser le graphe en entier
                idx = sommet.index(elem[0]) #On dit que la variable idx vaut la l'index de l'element de position 0 
                L[i][idx] = elem[1] #On dit que la position de idx dans le sommet i vaut l'element de position 1

        self.graphe = L #On dit que notre graphe est egale a la nouvelle liste

    def nmb_liaison(self):
        '''
        Methode qui prend en parametre un graphe de type liste dadjacence pour le parcourir et fait la somme du nombre de liaison qu'a chaque sommet du graphe et le retourne
        '''
        lsn = 0 #On set le nombre de liaison lsn a '0'
        for i in range(len(self.graphe)):

            for j in self.graphe[i]: #2 boucle for pour parcourir la longeur de la liste d'adjacence puis parcourir le nombre de liaison de chaque sommet
                lsn += 1 #On ajoute '1' chaque fois qu'on passe par une liaison d'un sommet de la liste d'adjacence

        return lsn

#######################################################

def generateur_graphe_adj_aleatoire(N_sommet):
    '''
    Fonction qui prend en parametre une valeur N_sommet pour generer aleatoirement un graphe de liste d'adjacence avec N_sommet comme longeur
    '''
    G = []
    for i in range(N_sommet): #On fait un boucle For pour le nombre de sommet donne
        L = random.sample(range(0, N_sommet),random.randint(1,N_sommet)) #On cree une liste random de range N_sommet et de longeur random entre 1 et N_sommet

        for j in range(len(L)-1): #On fait une boucle for in range pour chaque nouvelle liste cree

            if L[j] == i: #Si un liaison d'une liste s'appelle elle meme on l'enleve de la liste
                L.pop(j)

        L.sort() #On sort la liste et
        G.append(L) #On append la liste a la liste qui represente le graphe

    return G

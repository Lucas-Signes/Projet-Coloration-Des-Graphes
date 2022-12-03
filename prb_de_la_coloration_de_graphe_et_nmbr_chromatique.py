from graphes import * #On import le fichier avec la classe Graphe 

#######################################################

def permutations(N_sommet, K_clrs):
    '''
    Fonction qui prend en parametre le Nombre de sommet voulus, le nombre de couleurs voulues et l'sommet pour representer les differnets couleurs ou on va retourner une liste de string du nombre de permuatations possible de K couleurs pour N sommets (soit k**N)
    '''
    clrs = [] #set clrs comme une liste vide pour les couleurs
    for p in range(K_clrs):
        clrs.append(sommet[p]) #dans une boucle for on ajoute les K couleurs voulue en forme de string a la liste clrs

    perms = clrs # comme on modifie la liste de couleurs on set perms comme la liste de couleurs
    for i in range(N_sommet-1): #On fait tourner le programme le nombre de fois qu'il ya de sommets dans le graphe
        nv_perms = perms #On donne la variable Nv_clrs la liste perms qui prend le role du nouvelle liste de couleurs a modifier
        perms = [] #perms devient une liste vide pour toutes les permuatations de couleurs par rapporta au nombre de sommet

        for i in range(len(nv_perms)): #On fait une boucle for qui est in range la lomgeur de la liste Nv_perms des couleurs

            for j in range(len(clrs)): #On fait une boucle for qui est in range la longeur de la liste de couleurs
                perms.append(nv_perms[i]+clrs[j]) #On append a la liste perms la valeur i de la liste Nv_perms et la valeur j de la liste clrs comme string 

    return perms

def prb_de_decidabilite(G, K_clrs):
    '''
    Fonction qui prend en parametre un graphe et le nombre de couleurs voulues pour faire un test de deidibilite qui retourne un boolen qui donne True si il ya dans le graphe donne une combinaison possible avec ce nombre de couleurs et sinon donne False
    '''
    g = Graphe(G)
    perms = permutations(g.N_sommet, K_clrs) #On donne comme valeur la variable perms la liste de permutations possible par rapport au nombre de sommet N du graphe (la length du graphe) et le nombre k de couleurs voulu
    T = []
    for k in range(len(perms)): #On fait une boucle pour pour tester le graphe par le nombre de permutations qu'il ya
        cpt = 0 #On set le compteur cpt a '0'

        for i in range(len(g.graphe)):

            for j in g.graphe[i]: #On fait 2 boucles for pour parcourrir le graphe
                if perms[k][i] == perms[k][j]: #On teste si la liaison d'un sommet a un voisin de la même couleur par rapport a la liste de permutations
                    bol = 0  #Si oui le booleen prend comme valeur 0
                    T.append(perms[k]+' = Faux car les voisins: '+str(i)+" et "+str(j)+' sont de même couleur')

                else : 
                    bol = 1 #Sinon le booleen prend comme valeur 1
                    cpt += 1

                    if cpt == g.nmb_liaison(): #On ajoute a cpt 1 a chaque fois qu'une liaison n'a pas de voisin de même couleur et si cela est vrai pour le nombre de liaison qu'il ya dans le graphe alors on retourne True
                        T.append(perms[k]+" = Vrai car il n'a pas de voisins de même couleur")
                        return True, T #On retourne True comme booleen pour verifier qu'il y'a une instance ou il n'y a pas de voisin de même coulerus, on retourne aussi la liste T pour voir quel instance fonctionnent pas et celle qui fonctionne
                    
                if bol == 0 : break  #Si pour une iteration de la permutation il y'a une combinaison de couleur ou 2 voisin on la même couleur on break les boucle qui parcours le graphe pour passer a la prochaine iteration 
            if bol == 0 : break 

    return False, T #Si il n'existe aucune iteration de la permuation du graphe donne ou 2 voisin ne sont pas de même couleur alors on retourne False et on retourne la liste T pour montrer toutes les instances qui ne marchent pas

def prb_de_calculabilite(G):
    '''
    Fonction qui prend en parametre un graphe et fait un test de calculabilite pour savoir le nombre minimum de couleurs qu'il faut pour colorier ce graphe pour que 2 sommet voisins n'ont la même couleur
    '''
    cpt = 0 #On set le compteur cpt a '0'
    clrs = [] #on set la liste clrs de coulerus comme une liste vide
    while cpt > -1: #la boucle while tourne a l'infini jusqu'a qu'il trouve une liste de permutation avec au moins une iteration ou 2 sommet voisin n'ont pas la même couleurs
        clrs.append(sommet[cpt]) #A chqaue iteration de la boucle on ajoute une couleurs en string a la liste clrs
        res, test = prb_de_decidabilite(G, len(clrs))

        if res == True: #On test a chaque iteration de boucle si dans ce graphe par rapport au permutations de la liste de couleurs qui augmente si il ya une iteration de permutation dans ce graphe ou 2 voisin ne sont pas voisins
            return cpt+1, test  #Si le graphe_color_test retourne True alors on print que le nombre minimum de couleurs pour colorier se graphe est 'cpt+1' et on retourne cpt+1 et la variable test pour etre utilise dans les test de verification d'iteration ou de resolution du probleme
        
        else:
            cpt += 1 #Sinon on ajoute '1' a cpt pour rajouter une couleurs a perms pour la prochaine iteration de boucle

#######################################################

def suivie_de_verification_iter_donnee_d(G, K_clrs): 
    '''
    Fonction qui prend en parametre le graphe et le nombre de k couleurs a tester, et imprime la suive de la verification de la solution d'une iteration donne d'un probleme de decidabilite etape par etape
    '''
    print("\nLe graphe utilise :",G,"\nNombre de couleurs pour ce graphe :",K_clrs)

    perms = permutations(len(G), K_clrs)
    print("\nles permutations pour",K_clrs,"couleurs et",len(G),"sommets : ", end = "") #On imprime toutes les permuatations du graphe pour K couleurs
    print(*perms, sep = ", ") #On print toutes les permutations en affichant la variable perms

    res, test = prb_de_decidabilite(G, K_clrs)
    print("\nOn verifie chaque permutation de couleurs jusqu'a qu'on en trouve une positive", *test, sep = ', ')
    print("Le resultat du test de decidiblite :", res) #On le booleen pour verifier si il ya une instance ou 2 sommets voisin n'ont pas la même couleur
    if res == True: #Verifie si la resolution du probleme de decidabilite est vrai alors on indique que le graphe est coloriable avec K coulerus sinon on imprime que c'est impossible
        print("\nLe graphe donné est coloriable avec",K_clrs,"couleur(s) sans que deux voisins soit de même couleur.")
    
    else:
        print("\nLe graphe donné n'est pas coloriable avec",K_clrs,"couleur(s) sans que deux voisins soit de même couleur.")
    print("_________________________________________________________")

def suivie_de_res_complete_du_prb_c(G):
    '''
    Fonction qui prend en parametre le graphe et imprime la suive de la resolution complete d'un probleme de calculabilite etape par etape
    '''
    clrs = [] # On set clrs une liste vide pour les couleurs du graphe
    print("\nLe graphe utilise :",G) #On imprime le graphe
    
    res, test = prb_de_calculabilite(G)
    for i in range(res): #On fait une boucle for pour chaque serie de couleur jusqu'a celle qui a assez pour colorier le graphe donne
        clrs.append(sommet[res]) #On append pour chaque iteration de la boucle une nouvelle couleur a la liste clrs
        
        perms = permutations(len(G), len(clrs))
        print("les permutations pour",i+1,"couleurs et",len(G),"sommets : ", end = "") #On imprime toutes les permuatations du graphe pour K couleurs
        print(*perms, sep = ", ") #On print toutes les permutations en affichant la variable perms

        res0, test = prb_de_decidabilite(G, i+1) #On appel le probleme de decidabilite pour 'i+1' couleurs
        print("On verifie chaque permutation de couleurs jusqu'a qu'on en trouve une positive", *test, sep = ', ') #On imprime etape par etape tout les cas de la permutation pour 'i+1' couleurs pour verifier si il y'a une instance ou 2 sommet voisins on la même couleur
        print("\nLe resultat du test de decidiblite est donc :", res0,"\n") #On imrpime  le booleen pour verifier si il ya une instance ou 2 sommets voisin ont la même couleur
    
    print("D'apres le probleme de calulabilite Le graphe donné est coloriable avec au moins",res,"couleur(s) sans que deux voisins soit de même couleur.") #On imprime le nombre K de couleurs minimum pour que le graphe a une permutation ou 2 voisins n'ont pas la même couleurs
    print("_________________________________________________________")

def suivie_de_res_complete_du_prb_c0(G):
    '''
    Fonction qui prend en parametre le graphe et imprime la suive de la resolution complete d'un probleme de calculabilite etape par etape
    '''
    clrs = [] # On set clrs une liste vide pour les couleurs du graphe
    print("\nLe graphe utilise :",G) #On imprime le graphe
    
    res, test = prb_de_calculabilite(G)
    for i in range(res): #On fait une boucle for pour chaque serie de couleur jusqu'a celle qui a assez pour colorier le graphe donne
        clrs.append(sommet[res]) #On append pour chaque iteration de la boucle une nouvelle couleur a la liste clrs
        
        suivie_de_verification_iter_donnee_d(G,i+1)    
    print("D'apres le probleme de calulabilite Le graphe donné est coloriable avec au moins",res,"couleur(s) sans que deux voisins soit de même couleur.") #On imprime le nombre K de couleurs minimum pour que le graphe a une permutation ou 2 voisins n'ont pas la même couleurs
    print("_________________________________________________________")
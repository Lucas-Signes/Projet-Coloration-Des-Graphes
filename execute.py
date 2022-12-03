from prb_de_la_coloration_de_graphe_et_nmbr_chromatique import * #On import les fonction du fichier pour le fonctionnement du projet

#######################################################

#Voici trois example de graphe generer de facon aleatoire, G0 un graphe a 3 sommet, G1 un graphe a 4 sommet et G2 un graphe a 5 sommet :
G0 = [
    [1,2],
    [0],
    [0]
    ]

G1 = [
    [1,2],
    [0,2],
    [0,1,3],
    [2]
    ]

G2 = [
    [1,4],
    [0,2,3,4],
    [1,3,4],
    [1,2],
    [0,1,2]
    ]

#Le Graphe Gt (pour Graphe Test) est un graphe de type liste d'adjacence que l'utilisateur est libre de cree et modifier pour le tester a sa guise :
Gt = [
    []                         
    ]

#L'utilisateur peut modifier N_sommet pour generer un graphe random pour tester librement les fonctions de suivie de verification d'iteration donne et de resolution complete du probleme avec le graphe generer aleatoirement :
N_sommet = 0
Gr = generateur_graphe_adj_aleatoire(N_sommet)

#Ces 3 fonctions sont des tests du graphe 1 ou pour le probleme de decidabilite on a une reponse negative, puis une postive et on test egalement le graphe avec le probleme de calculabilite (Il peuvent etre modifier par l'utilisateur pour tester les autres graphes ou changer le nombres de couleurs tester) : 
suivie_de_verification_iter_donnee_d(G0, 1)
suivie_de_verification_iter_donnee_d(G0, 3)
suivie_de_res_complete_du_prb_c0(G0)

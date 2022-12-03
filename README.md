# Projet-Coloration-Des-Graphes

Projet Coloration d'un Graphe - Lucas Signes

Aborescence :
- Graphe_class.py: Le fichier contient la classe graphe, dont les methodes pour parcourrir un graphe, les successeurs et
  predecesseurs d'un graphe, et le conversions de graphe matrice a des graphes de type d'adjacence. Ainsi que la fonction
  pour generer un graphe de liste d'adjacence aleatoire.
- Prb_de_la_coloration_de_graphe_et_nmbr_chromatique.py : Le fichier contient les fonctions permettant de generer
  iterativement toutes les permutations du probleme, résolvant par force brute la version décidabilité du problème de graphes 
  k-coloration, résolvant par force brute la version calculabilité du problème de nombre chromatique et les fonctions 
  permettant de suivre étape par étape la résolution complète du problème et la vérification d’une instance 
  donnée.
- Execute.py: Le fichier est sense etre executer et modifier par l'utilisateur, Il contient trois examples de Graphe a 3, 4,
  et 5 sommet, un Graphe test qui peut etre cree par l'utilisateur et un generateur de graphe type liste d'adjacence 
  non-oriente modifiable. Il contient aussi l'appel des fonctions qui print etape par etape une instance du probleme de decidabilite
  negative, une positive et une d'une resolution de probleme de calculabilite.

Explications :
  Il faut executer le fichier Execute.py pour afficher etape par etape une instance du probleme de decidabilite negative, une positive
  et une d'une resolution de probleme de calculabilite (l'example utiliser dans le fichier utilise le graphe G0).
  Pour les examples du fonctionnement du programme le graphe 0 a ete utilise mais l'utilisateur peut, bien evidement, changer
  le graphe utilise en example pour un autre, ainsi que changer le nomber de K couleurs utilise dans le 2 premiers test, cree son propre
  graphe de type liste d'adjacence non-oriente ou generer un graphe de type liste d'adjacence non-oriente aleatoire grace a la fonction 
  dans le fichier execute (Il faut juste inserer la valeur de N_sommet voulu pour generer le nouveau graphe).
  Remarque: Il est fortement deconseiller de generer un graphe avec plus de 15 sommet ou tester plus que 15 couleurs pour assurer le bon
  fonctionement du programme et de votre ordinateur (La limite de couleur possible est de 26).

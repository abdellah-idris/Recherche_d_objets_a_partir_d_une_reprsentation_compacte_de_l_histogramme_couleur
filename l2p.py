# importation des bibliothéques
"""
sys — Paramètres et fonctions propres à des systèmes

Ce module fournit un accès à certaines variables utilisées et maintenues par l'interpréteur,
et à des fonctions interagissant fortement avec ce dernier.
"""
import sys

"""
os.path — manipulation courante des chemins

Ce module implémente certaines fonctions utiles sur le nom des chemins. 
Pour lire ou écrire des fichiers, et pour accéder au système de fichier, voir le module os.
Les paramètres de chemin d’accès peuvent être passés sous forme de chaînes de caractères ou 
de chaîne d'octets. Les programmes sont encouragés à représenter les noms de fichiers 
en tant que chaînes de caractères Unicode.
"""
import os.path

"""
NumPy est une bibliothèque pour langage de programmation Python, destinée à manipuler des matrices ou tableaux
multidimensionnels ainsi que des fonctions mathématiques opérant sur ces tableaux.
"""
import numpy as np  # importation de numpy

"""
OpenCV est une bibliothèque graphique libre, initialement développée par Intel,
 spécialisée dans le traitement d'images en temps réel.
"""

import cv2 as cv  # importation de opencv


r"""
étudier et adapter, une approche simple et efficace de reconnaissance entre images fondée 
sur une représentation de l’histogramme couleur des images RGB.

                                -------------------------------------
Version Finale

                                -------------------------------------
Définitions:
----------

bin :
Un bin est une plage qui représente la largeur d'une seule barre de l'histogramme le long de l'axe des X.
On pourrait également appeler cela l'intervalle. 



paramétres:
----------
numero : choix d'un numero pour l'image requête 
categorie : choix de la catégorie de l'image
image_similaires : Dictionnaire contenat les images similaires(key) et leurs distance (value)

-----
name_image_requete : nom de l'image requete
imagerequete : tableau 3D des valeurs des pixels en BGR (bleu, vert, rouge)
resizedrequete : image redimensionner,tableau 3D de 49152(128*128*3) valeurs des pixels en BGR (bleu, vert, rouge)
tab_requete_1d : tableau 1D contenant les valeurs du tableau 3D resizedrequete
requete_masque-n° : Tableau avec masque sur zone d'interet de la valeur n


Sortie :- Affichage des images similaires
        Affichage console:
        - nom : valeur de la distance ---  pour les 10 images les plus proches
Cu :    categorie doit être comprise entre 1 et 100 inclus
        numero doit  être un multiple de 5 strictement inférieur à 365
        bins doit être comprise entre 20 et 255 inclus 

"""

##############################################

#Dictionnaire contenant les images similaires et leurs distances
#il sera trié selon les clés et en renvoi la liste des images similaires
image_similaires={}

# variable distance
distance = 0

# Lecture de l'image Requête

print("choix de l'image Requête")
#valeur d'initialisation
#permet la saisie utilisateur
categorie=-1
"""
Gestion d'exception
l’exemple suivant, demande une saisie à l’utilisateur jusqu’à ce qu’un entier valide ait été entré,
 mais permet à l’utilisateur d’interrompre le programme (en utilisant Control-C ou un autre raccourci
  que le système accepte).
  
 L’instruction try fonctionne comme ceci :

    premièrement, la clause try (instruction(s) placée(s) entre les mots-clés try et except) 
    est exécutée ;
    
    si aucune exception n’intervient, la clause except est sautée et l’exécution de l’instruction
     try est terminée ;
    
    si une exception intervient pendant l’exécution de la clause try, le reste de cette clause 
    est sauté. Si le type d’exception levée correspond à un nom indiqué après le mot-clé except, 
    la clause except correspondante est exécutée, puis l’exécution continue après l’instruction try ;
    
    si une exception intervient et ne correspond à aucune exception mentionnée dans la clause
    except, elle est transmise à l’instruction try de niveau supérieur ; si aucun gestionnaire
    d’exception n’est trouvé, il s’agit d’une exception non gérée et l’exécution s’arrête avec
    un message comme indiqué ci-dessus.
    
    
exception ValueError:

    Levée lorsqu'une opération ou fonction native reçoit un argument qui possède 
    le bon type mais une valeur inappropriée, et que la situation n'est pas décrite 
    par une exception plus précise telle que IndexError.

"""
while True:
    try:
        # si la saisie est fausse on redemande une nouvelle saisie
        while (categorie < 1 or categorie > 100):
            categorie = int(input("Entrer un entier positive représentant la catégorie de l'image Requête:"
                                  " entre 1 et 100 "))
        break
    except ValueError:
        #message d"erreur
        print("veiller saisir un entier")




#Transtypage explicite de int en string
#but : concaténation de string

cat = str(categorie)
#valeur d'initialisation
#permet la saisie utilisateur
numero=-1

while True:
    try:
        #si la saisie est fausse on redemande une nouvelle saisie
        while (numero % 5 != 0 or numero > 356 or numero <0):
            numero = int(input('Entrer un entier positive multiple de 5 inférieur à 356'))
        break
    except ValueError:
        print("veiller saisir un entier")
# Transtypage explicite de int en string
# but : concaténation de string
num = str(numero)

"""
On demande à l'utilisateur la saisie du nombre de bins.
Cette liberté permettra à l'utilisateur de voir la différence 
des résultats obtenus sur la même image requête
"""
# valeur d'initialisation
#permet la saisie utilisateur
bins=-1

while True:
    try:
        #si la saisie est fausse on redemande une nouvelle saisie
        while (bins< 20 or bins > 255):
            bins = int(input('Entrer un entier positive entre 20 et 255 représentant le nombre de bins'))
        break
    except ValueError:
        print("veiller saisir un entier entre 20 et 255")



# Concatenation afin d'obtenir le chemin de l’image requete
name_image_requete = 'coil-100/obj'+ cat +'__' + num + '.ppm'



"""
 os.path.isdir(path)

    Renvoi True si le chemin(path) du dossier existe.
"""
"""
sys.exit([arg])
    Quitte Python. C'est implémenté en levant l'exception SystemExit, afin que toutes les actions 
    de nettoyage spécifiées par des clauses finally des instructions try soient correctement 
    exécutées. Il est aussi possible d'intercepter la tentative de sortie à un niveau au dessus.
    
    L'argument optionnel arg peut être un nombre entier donnant l'état de sortie (zéro par défaut),
    ou un autre type d'objet. Pour les shells (et autres), si c'est un entier, zéro signifie "terminé
    avec succès", et toutes les autres valeurs signifient "terminé anormalement". La plupart des 
    systèmes imposent qu'il se situe dans la plage 0--127, et leur comportement n'est pas défini
    pour les autres cas. Certains systèmes peu communs ont pour convention d'assigner un sens
    particulier à des valeur spécifiques. Les programmes Unix utilisent généralement 2 pour
    les erreurs de syntaxe dans les arguments de la ligne de commande, et 1 pour toutes les
    autres erreurs. Si un autre type est passé, None est équivalent à zéro, et tout autre
    objet est écrit sur stderr et donne un code de sortie 1. Typiquement, 
    sys.exit("some error message") est un moyen rapide de quitter un programme en cas d'erreur.

    Puisque la fonction exit() ne fait "que" lever une exception, elle ne fera quitter
    le processus que si elle est appelée depuis le fil d'exécution principal, et que l'exception
    n'est pas interceptée.

    Modifié dans la version 3.6: Si une erreur survient lors du nettoyage après que l'interpréteur
    Python ait intercepté un SystemExit (typiquement une erreur en vidant les tampons des sorties 
    standard), le code de sortie est changé à 120.


"""
#On vérifie si la base de données a été téléchargée sinon on quitte python

if os.path.isdir("coil-100")==False:
    #Message d'erreur
    print("la base de données coil-100 doit être téléchargé")
    #quitter python
    sys.exit()


"""
La méthode cv2.imread() charge une image à partir du fichier spécifié. Si l'image ne peut pas être lue 
(à cause d'un fichier manquant, de permissions incorrectes, d'un format non supporté ou invalide), 
cette méthode renvoie une matrice vide.

    Syntaxe : cv2.imread(path, flag)

    Paramètres :
    ------------
    path : Une chaîne représentant le chemin de l'image à lire.
    flag : Il spécifie la manière dont l'image doit être lue. Sa valeur par défaut est cv2.IMREAD_COLOR

    Valeur de retour : Cette méthode renvoie une image qui est chargée à partir du fichier spécifié.
Note : Dans le cas d'images en couleur, les images décodées auront les canaux stockés dans l'ordre B G R.

"""


imagerequete = cv.imread(name_image_requete)


"""
	cv.resize( src, dsize[, dst[, fx[, fy[, interpolation]]]] ) -> dst

La fonction resize permet de redimensionner l'image src vers le bas ou vers le haut à la taille spécifiée. 
Au lieu de cela, la taille et le type sont dérivés de src,dsize,fx, et fy.
 Paramètres :
 ------------
    src [obligatoire]: image source/entrée
    dsize [obligatoire] : taille souhaitée pour l'image de sortie
    fx [facultatif] : facteur d'échelle le long de l'axe horizontal
    fy [facultatif] : facteur d'échelle sur l'axe vertical
    interpolation [facultatif]:  drapeau qui prend l'une des méthodes suivantes. INTER_NEAREST - une interpolation du plus 
        proche voisin INTER_LINEAR - une interpolation bilinéaire (utilisée par défaut) INTER_AREA - un rééchantillonnage 
        utilisant la relation entre la surface des pixels. C'est peut-être la méthode préférée pour la 
        décimation d'images, car elle donne des résultats sans moirage. Mais lorsque l'image est zoomée, elle est 
        similaire à la méthode INTER_NEAREST. INTER_CUBIC - une interpolation bicubique sur un voisinage de 4×4 pixels 
        INTER_LANCZOS4 - une interpolation de Lanczos sur un voisinage de 8×8 pixels

"""
# Redimensionnement de l'image
resizedrequete = cv.resize(imagerequete, (128, 128))


"""
cv::imshow 	( const String &  winname, InputArray  	mat ) 	
cv.imshow() pour afficher une image dans une fenêtre. La fenêtre s'adapte automatiquement à la taille de l'image.

"""
#Affichage de l'image
cv.imshow("image requete",resizedrequete)



"""
 ndarray.flatten(order='C')

    Renvoie une copie du tableau aplati en une seule dimension. 1D

    Paramètres:
    ----------
        order{'C', 'F', 'A', 'K'}, facultatif

            C' signifie que le tableau doit être aplati dans l'ordre des lignes majeures (style C).
            F" permet d'aplatir dans l'ordre des colonnes (style Fortran). 
            A" signifie que l'aplatissement se fait dans l'ordre des colonnes si a est contigu en mémoire Fortran, 
            dans l'ordre des lignes sinon. 
            K' signifie quel'on aplatit a dans l'ordre où les éléments apparaissent en mémoire.
            La valeur par défaut est 'C'.

    Retourne:
    --------
        Une copie du tableau d'entrée, aplati à une dimension.


"""
#Transformation en tableau 1D
tab_requete_1d=resizedrequete.flatten()

"""
numpy.delete(arr, obj, axis=None)

Renvoie un nouveau tableau dont les sous-réseaux le long d'un axe sont supprimés. Pour un tableau à une dimension,
cela renvoie les entrées qui ne sont pas renvoyées par `arr[obj]`.

    Paramètres
    ----------
    arr : tableau_like
        Tableau d'entrée.
    obj : tranche, int ou tableau d'ints
        Indique les indices des sous-réseaux à supprimer le long de l'axe spécifié.
        ... versionchanged: : 1.19.0
            Les indices booléens sont maintenant traités comme un masque des éléments à supprimer, plutôt que d'être convertis en entiers 0 et 1.
    axis : int, facultatif
        L'axe le long duquel supprimer le sous-réseau défini par `obj`.
        Si `axis` est None, `obj` est appliqué au tableau aplati.
    Retourne
    -------
    out : ndarray
        Une copie de `arr` avec les éléments spécifiés par `obj` supprimés. Notez
        que `delete` ne se produit pas in-place. Si `axis` est None, `out` est un tableau un tableau aplati.

"""

"""
 numpy.where(condition[, x, y])¶

    Renvoie des éléments choisis parmi x ou y selon la condition.

    Paramètres:
    -----------
    condition array, bool:
        Si Vrai, retourne x, sinon retourne y.
    
    x, y tableau:
        Valeurs parmi lesquelles choisir. x, y et la condition doivent pouvoir être diffusés sous une forme quelconque.

    Retourne:
    --------
        Un tableau contenant des éléments de x lorsque la condition est vraie, et des éléments de y ailleurs.

"""

"""
Pour supprimer par valeur:

modified_array = np.delete(original_array, np.where(original_array == value_to_delete))

"""
# masque sur zone d'interet valeur 230
requete_masque_230 = np.delete(tab_requete_1d, np.where(tab_requete_1d == 230))
# masque sur zone d'interet valeur 50
requete_masque_50 = np.delete(requete_masque_230, np.where(requete_masque_230 == 50))
# masque sur zone d'interet valeur 154
requete_masque_154 = np.delete(requete_masque_50, np.where(requete_masque_50 == 154))
# masque sur zone d'interet valeur 25
requete_masque_25 = np.delete(requete_masque_154, np.where(requete_masque_154 == 25))
# masque sur zone d'interet valeur 61
requete_masque_64 = np.delete(requete_masque_25, np.where(requete_masque_25 == 64))

"""
np.histogram: La fonction histogramme de Numpy ne dessine pas l'histogramme, mais elle calcule les occurrences
 de données d'entrée qui se trouvent dans chaque case.

"""

"""
numpy.histogram(a, bins=10, range=None, normed=None, weights=None, density=None)
   Calcule l'histogramme d'un ensemble de données.
   
   Paramètres
   ----------
   a : tableau
       Données d'entrée. L'histogramme est calculé sur le tableau aplati -1D.
    bins : int ou séquence de scalaires ou str, optionnel
       Si `bins` est un int, il définit le nombre d'intervalles d'égale largeur
       largeur égale dans l'intervalle donné (10, par défaut). Si `bins` est une 
       séquence, il définit un tableau croissant monotone de bords de bacs,
       y compris le bord le plus à droite, permettant des largeurs de bacs non uniformes.
       .. versionadded: : 1.11.0
       Si `bins` est une chaîne de caractères, il définit la méthode utilisée pour calculer la largeur optimale des cases, comme défini par `histogram_bin_edges`.

    
    range : (float, float), optionnel
       Les plages inférieure et supérieure des bacs.  Si elle n'est pas fournie, la plage est simplement ``(a.min(), a.max())``.  Les valeurs situées en dehors de l'intervalle sont ignorées. Le premier élément de l'intervalle doit être inférieur ou égal au second.
       . L'option `range` affecte également le bin automatique. Alors que la largeur des cases est calculée pour être optimale en fonction des données réelles de `l'intervalle`, le nombre de cases remplir  l'ensemble de la plage, y compris les portions ne contenant aucune donnée.

    normed : bool, optionnel
       .. déprécié : : 1.6.0
       Ceci est équivalent à l'argument `density`, mais produit des résultats incorrects pour des largeurs de binaires inégales. Il ne devrait pas être utilisé.
       ... versionchanged: : 1.15.0
           Les avertissements de dépréciation sont effectivement émis.
    weights : tableau, optionnel
       Un tableau de poids, de la même forme que `a`.  Chaque valeur dans
       `a` ne contribue que le poids qui lui est associé pour le nombre de cases
       (au lieu de 1). Si `density` est True, les poids sont
       poids sont normalisés, de sorte que l'intégrale de la densité sur l'échelle
       reste égale à 1.


    density : bool, optionnel
       Si ``False``, le résultat contiendra le nombre d'échantillons dans chaque bin.
       . Si ``True``, le résultat est la valeur de la fonction de densité de probabilité au niveau de la case, normalisée de telle sorte que
       que l'intégrale sur la plage soit égale à 1.
       valeurs de l'histogramme ne sera pas égale à 1, à moins que des bins de largeur unitaire soit chosis
    Remplace le mot-clé ``normed`` s'il est donné.

    Retourne
   -------
    hist : tableau
       Les valeurs de l'histogramme. Voir `densité` et `poids` pour une
       description des sémantiques possibles.
    bin_edges : tableau de dtype float
       Retourne les bords de la case ``(longueur(hist)+1)``.

"""
#Calcul de l'histogramme
histrequete, binedge= np.histogram(requete_masque_64,bins=bins,density=False)

"""
numpy.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None)
Enregistre un tableau dans un fichier texte.
    
    Paramètres
    ----------
        fname : filename or file handle
          Si le nom de fichier se termine par ``.gz``, le fichier est automatiquement enregistré
            en format compressé gzip.  `loadtxt` comprend les fichiers gzippés de manière transparente.
    X : tableau 1D ou 2D
        Données à sauvegarder dans un fichier texte.
    fmt : str ou séquence de strs, optionnel
        Un seul format (%10.5f), une séquence de formats, ou une chaîne de
        ou une chaîne multiformat, par exemple 'Iteration %d -- %10.5f'.
        cas, `delimiter` est ignoré. Pour les `X` complexes, les options légales
        légales pour `fmt` sont :
        * un seul spécificateur, `fmt='%.4e'`, ce qui donne des nombres formatés comme
          comme `' (%s+%sj)' % (fmt, fmt)``.
        * une chaîne complète spécifiant chaque partie réelle et imaginaire, par exemple
          `' %.4e %+.4ej %.4e %+.4ej %.4e %+.4ej'` pour 3 colonnes
        * une liste de spécificateurs, un par colonne - dans ce cas, la partie réelle et la partie imaginaire doivent avoir des spécificateurs séparés.
          réelle et imaginaire doivent avoir des spécificateurs séparés,
          par exemple, `['%.3e + %.3ej', '(%.15e%+.15ej)']` pour 2 colonnes
    delimiter : str, facultatif
        Chaîne ou caractère séparant les colonnes.
    newline : str, optional
        Chaîne ou caractère séparant les lignes.
        ... versionadded: : 1.5.0
    header : str, optionnel
        Chaîne qui sera écrite au début du fichier.
        ... versionadded: : 1.7.0
    footer : str, optionnel
        Chaîne de caractères qui sera écrite à la fin du fichier.
        ... versionadded: : 1.7.0
    comments : str, optional
        Chaîne qui sera ajoutée aux chaînes ``header`` et ``footer`',
        pour les marquer comme des commentaires. Par défaut : '#', comme attendu par exemple par
        ``numpy.loadtxt``.


"""

"""
exception FileNotFoundError

    Levé lorsqu'un fichier ou un répertoire est demandé mais n'existe pas. Correspond à errno ENOENT.
"""



#On vérifie que le dossier histogramme a bien été créer
#Sauvegarde des valeurs de l'histogramme

"""
La méthode os.mkdir() en Python est utilisée pour créer un répertoire nommé path avec le mode numérique spécifié. Cette méthode lève FileExistsError si le répertoire  existe déjà.

    Syntaxe : os.mkdir(path, mode = 0o777, *, dir_fd = None)

Paramètre :
path : Un objet de type chemin représentant un chemin d'accès au système de fichiers. Un objet de type chemin est soit 
une chaîne, soit un objet d'octets représentant un chemin.
mode (facultatif) : Une valeur entière représentant le mode du répertoire à créer. Si ce paramètre est omis, la valeur 
par défaut Oo777 est utilisée.
dir_fd (optionnel) : Un descripteur de fichier faisant référence à un répertoire. La valeur par défaut de ce paramètre 
est None.
Si le chemin spécifié est absolu, le paramètre dir_fd est ignoré.


Note : Le '*' dans la liste des paramètres indique que tous les paramètres suivants (ici dans notre cas 'dir_fd') sont 
des paramètres à mot-clé seulement et ils peuvent être fournis en utilisant leur nom, pas comme paramètre positionnel.

Type de retour : Cette méthode ne renvoie aucune valeur.


"""
"""
Si le répertoire existe déjà l'exception FileNotFoundError ne sera pas levée
"""
b= (str)(bins)

while True:
    try:
        np.savetxt("histogramme/coil-100_obj"+ cat +"__" + num+"_"+b+"_bins.txt",histrequete, fmt="%s")
        break
    except FileNotFoundError:
        #Message d'erreur
        print("Créer le dossier histogramme ")
        # création du dossier histogramme
        os.mkdir("histogramme")
        np.savetxt("histogramme/coil-100_obj" + cat + "__" + num + "_" + b + "_bins.txt", histrequete, fmt="%s")


#################################################################""

"""
Parcours des images et calcule des distances

"""
for i in range (1,101):
    for n in range(0,356,5):
        #n augmente de 5 à chaque itération tant qu'il est inférieur à 356
        # la condition permet de ne pas calculer la distance de l'image requête avec elle-même
        # différent de l'image image requete
        if (n != numero and i!= categorie):

            # on réinitialise la distance à chaque boucle
            distance=0
            # Transtypage : représente le numéro de l'image requête
            n = str(n)
            #Transtypage : la catégorie de l'image requête
            c = str (i)
            image = cv.imread('coil-100/obj'+ c +'__' + n + '.ppm')

            # Redimensionnement de l'image
            resized = cv.resize(image, (128, 128))

            tab_1d = resized.flatten() # Tableau resized transformer en tableau 1D
            # masque sur zone d'interet valeur 130
            masque_230 = np.delete(tab_1d, np.where(tab_1d == 230))
            # masque sur zone d'interet valeur 50 ( le masque 230 est toujours effectif)
            masque_50 = np.delete(masque_230, np.where(masque_230 == 50))
            # masque sur zone d'interet valeur 154
            masque_154 = np.delete(masque_50, np.where(masque_50 == 154))
            # masque sur zone d'interet valeur 25
            masque_25 = np.delete(masque_154, np.where(masque_154 == 25))
            # masque sur zone d'interet valeur 64
            masque_64 = np.delete(masque_25, np.where(masque_25 == 64))

            #calcul de l'histogramme
            histogram, binedge = np.histogram(masque_64, bins=bins, density=False)

            #Sauvegarde des valeurs de l'histogramme
            np.savetxt("histogramme/coil-100_obj"+ c +"__"+ n+"_" +b+"_bins.txt", histogram, fmt="%s")

            """
            absolute(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
            Calcule la valeur absolue par élément.
            np.abs est un raccourci pour cette fonction.
            """
            #valeur absolue
            d = abs( histogram - histrequete)/ 256

            """
            numpy.sum(a, axis=None, dtype=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)
            
            Somme des éléments du tableau sur un axe donné.
            Paramètres:
             ----------
             a : tableau
              Eléments à additionner.
            axis : None ou int ou tuple of ints, facultatif
                Axe ou axes le long desquels une somme est effectuée.  La valeur par défaut,
                axis=None, additionnera tous les éléments du tableau d'entrée.  Si
                axis est négatif, il compte du dernier au premier axe.
                .. versionadded: : 1.7.0
                Si axis est un tuple d'entiers, une somme est effectuée sur tous les axes spécifiés dans le tuple au lieu d'une somme unique.
                spécifiés dans le tuple au lieu d'un seul axe ou de tous les axes comme
                comme auparavant.
            dtype : dtype, facultatif
                Le type du tableau retourné et de l'accumulateur dans lequel les éléments sont additionnés.
                éléments sont additionnés.  Le dtype de `a` est utilisé par défaut, sauf si `a`
                ait un dtype integer de moins de précision que la plateforme par défaut
                par défaut.  Dans ce cas, si `a` est signé alors l'entier de la plateforme
                plateforme est utilisé, alors que si `a` est non signé, un entier non signé de la même
                même précision que l'entier de la plate-forme est utilisé.
            out : ndarray, optionnel
                Tableau de sortie alternatif dans lequel placer le résultat. Il doit avoir
                la même forme que la sortie attendue, mais le type des valeurs de la sortie
                valeurs de sortie sera converti si nécessaire.
            keepdims : bool, optionnel
                Si cette option vaut True, les axes qui sont réduits sont laissés dans le résultat en tant que dimensions de taille un.
                dans le résultat en tant que dimensions de taille 1. Avec cette option
                le résultat sera diffusé correctement par rapport au tableau d'entrée.
                Si la valeur par défaut est passée, alors le `keepdims` ne sera pas
                ne sera pas transmise à la méthode `sum` des sous-classes de
                `ndarray`, mais toute valeur autre que celle par défaut le sera.  Si la méthode de la
                méthode de la sous-classe n'implémente pas `keepdims`, toute exceptions seront levées.
            initial : scalaire, optionnel   
                Valeur de départ pour la somme. Voir `~numpy.ufunc.reduce` pour plus de détails.
            
            """
            # Somme toutes les valeurs de la différénce entre  histogram - histrequete
            distance = np.sum(d)

            ###################################
            #si la distance est inférieur à 100 donc en inclus le nom de l'image (key) et la distance (value)
            # dans le dictionnaire
            if (distance < 100):
                image_similaires['coil-100/obj' + c +'__' + n + '.ppm'] = distance

"""
   sorted(iterable, *, key=None, reverse=False)

  Renvoie une nouvelle liste triée depuis les éléments d'iterable.

  A deux arguments optionnels qui doivent être nommés.
  Paramètres:
  ----------

  key spécifie une fonction d'un argument utilisé pour extraire une clé de comparaison de chaque élément de l'itérable .
  La valeur par défaut est None (compare les éléments directement).
  Dans la fonction key = lambda x: x[1] nous permet de comparer les valeurs représantant les distances dans notre programe.

  reverse, une valeur booléenne. Si elle est True, la liste d'éléments est triée comme si toutes les comparaisons étaient inversées.
  Utilisez functools.cmp_to_key() pour convertir l'ancienne notation cmp en une fonction key.
  La fonction native sorted() est garantie stable. Un tri est stable s'il garantit de ne pas changer 
  l'ordre relatif des éléments égaux entre eux. C'est utile pour trier en plusieurs passes (par exemple par département puis par salaire).

  Lors du bouclage des dictionnaires, la clé et la valeur 
  correspondante peuvent être récupérées en même temps à l'aide de la méthode items().

  """
"""
lambda est utilisé pour déclarer une fonction anonyme. Une fonction anonyme se réfère à une fonction déclarée sans nom. 
Bien que syntaxiquement elles soient différentes, les fonctions lambda se comportent de la même manière que les 
fonctions régulières qui sont déclarées en utilisant le mot-clé def.
Cette approche est le plus souvent utilisée pour transmettre une fonction simple comme argument à une autre fonction. 

"""

print("Liste des images similaires :")
# a  servira à limiter le nombre d'images renvoyées
a=0
for k, v in sorted(image_similaires.items(), key=lambda x: x[1]):

    # Affichage des 10 images les plus proches
    if(a<10):
        print("%s: %s" % (k, v))
        similaire = cv.imread(k)
        #Affichage
        cv.imshow("image similaire n "+str(a),similaire)

        a += 1

"""
cv::waitKey 	( 	int  	delay = 0	) 	
La fonction waitKey attend un événement de touche de manière infinie (lorsque delay≤0 ) 
ou pendant delay millisecondes, lorsqu'il est positif. 
delay Délai en millisecondes. 0 est la valeur spéciale qui signifie "pour toujours". 
"""
cv.waitKey(0)
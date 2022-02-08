# Computer vision project based on swainballard Color Indexing book

## INFO:
I couldn't find my first code using loops, which was very slow when calculating and obtaining the resulting images.

## Contexte:
Dans de nombreux domaines d’application en imagerie, les quantités d’images deviennent de plus en plus importantes, formant de véritables masses de données.
Les systèmes de recherche d'images par le contenu (Content Based Image Retrieval ou CBIR) nécessitent l’utilisation de descripteurs de formes discriminants
et rapides à calculer. L’idée est de présenter une image au système (par exemple une voiture) et de faire ressortir les images les plus proches dans la base.

## Objectifs :
Nous proposons, dans ce projet d’étudier et d’adapter, une approche simple et efficace de reconnaissance entre images fondée sur une représentation de l’histogramme 
couleur des images RGB. Les étapes à suivre sont les suivantes :

    -Lecture d’une image en couleur.
    -Définition de masque sur des zones d’intérêt
    -Calcul d’une nouvelle représentation fondée sur une représentation simplifiée de l’histogramme couleur de la zone d’intérêt.
    -Calcul de distance (comparaison de deux images à partir de leur histogramme) et test sur la base entière avec classement en
      fonction de la proximité par rapport à l’image requête.

#coding utf-8

#1. Il faut d'abord importer correctement notre fichier .csv contenant les données concernant les thèses et mémoires à l'étude.

import csv

fichier = "concordia1.csv"
f1 = open(fichier)

# "lignes" désigne ici l'ensemble des données disponibles dans notre fichier "concordia.csv"
lignes = csv.reader(f1)
# "next" nous permet d'éviter de traiter la toute première ligne du document .csv, qui contient les en-têtes
next(lignes)

#2.1 Je crée un dictionnaire qui contient l'équivalence de chaque nombre arabe en chiffres romains, de 1 à 70. Après avoir recherché les possibilités une à une dans le fichier .csv ouvert
#  dans Sublime Text, il semble que le nombre le plus élevé de pages liminaires soit 62. J'ai l'intuition que la tâche monastique de créer un dictionnaire exhaustif avec chacune des entrées
#  permettrait d'éviter les problèmes liés à l'ordre des chiffres romains. Autrement dit, en n'attribuant des valeurs qu'à "i", "v", "x" et "l", "xl" serait égal à "lx".
d = {
     "i" : "1",
     "ii" : "2",
     "iii": "3",
     "iv" : "4",
     "v" : "5",
     "vi" : "6",
     "vii" : "7",
     "viii" : "8",
     "ix" : "9",
     "x" : "10",
     "xi" : "11",
     "xii" : "12",
     "xiii" : "13",
     "xiv" : "14",
     "xv" : "15",
     "xvi" : "16",
     "xvii" : "17",
     "xviii" : "18",
     "xix" : "19",
     "xx" : "20",
     "xxi" : "21",
     "xxii" : "22",
     "xxiii" : "23",
     "xxiv" : "24",
     "xxv" : "25",
     "xxvi" : "26",
     "xxvii" : "27",
     "xxviii" : "28",
     "xxix" : "29",
     "xxx" : "30",
     "xxxi" : "31",
     "xxxii" : "32",
     "xxxiii" : "33",
     "xxxiv" : "34",
     "xxxv" : "35",
     "xxxvi" : "36",
     "xxxvii" :"37",
     "xxxviii" : "38",
     "xxxix" : "39",
     "xl" : "40",
     "xli" : "41",
     "xlii" : "42",
     "xliii" : "43",
     "xliv" : "44",
     "xlv" : "45",
     "xlvi" : "46",
     "xlvii" : "47",
     "xlviii": "48",
     "xlix" : "49",
     "l" : "50",
     "li" : "51",
     "lii" : "52",
     "liii" : "53",
     "liv" : "54",
     "lv" : "55",
     "lvi" : "56",
     "lvii" : "57",
     "lviii" : "58",
     "lix" : "59",
     "lx" : "60",
     "lxi" : "61",
     "lxii" : "62",
     "lxiii" : "63",
     "lxiv" : "64",
     "lxv" : "65",
     "lxvi" : "66",
     "lxvii" : "67",
     "lxviii" : "68",
     "lxix" : "69",
     "lxx" : "70",
}     

# 2.2 En parcourant le document .csv, Jean-Philippe Guilbault a trouvé des entrées fautives de pages liminaires. Les nombres romains fautifs "vix" et "ivx" sont du lot. Après avoir téléchargé
# les mémoires «Family ties : a case study of a character education program at a local Montreal elementary school» et «The design and marketing of QSound : a case study of the relationship
# between technological innovation and musical culture» en format .pdf, il semble que la correction de "vix" pages liminaires soit "ix", et que celle de "ivx" soit "iv". J'ai corrigé le
# document .csv en conséquence.

# 3. Nous définissons ici les variables dans une boucle, de manière à ce qu'elles soient relatives à chaque ligne de l'ensemble des lignes.
for ligne in lignes:
    # 3.1. La variable "titre" est créée pour aller chercher le titre de mémoire/thèse contenu à chaque ligne, dans la troisième colonne (donc la colonne #2). J'ai décidé de lui appliquer la
    # fonction "strip" afin de retirer les espaces qui pourraient s'être glissées après le titre.
    titre = str.strip(ligne[2])
    
    # 3.2. La variable "longTitre" est créée pour aller chercher la longueur de chaque titre. Elle est obtenue en appliquant la fonction 
    # "len" à la variable "titre" précédemment définie.
    longTitre = (len(titre))
   
    # 3.3. Il nous faut maintenant attribuer une condition à notre variable typeTexte; la variable correspond au bout de phrase «La thèse doctorale» si les caractères "Ph.D", "Ph. D" ou "PhD"
    # apparaissent à la colonne d'une ligne donnée. Ces caractères ont été identifiés comme des critères de démarcation entre les thèses doctorales et les mémoires de maîtrise
    # en lisant le fichier concordia1.csv dans Sublime Text. Ils tiennent compte des erreurs d'inscription.
    if "Ph.D" in ligne[6] or "Ph. D" in ligne[6] or "PhD" in ligne[6]:
        typeTexte = ("La thèse doctorale")
    else:
        typeTexte = ("Le mémoire de maîtrise")

    # 3.4. La variable "nbPages" est créée pour aller chercher le nombre de pages contenu à chaque ligne, dans la sixième colonne (donc la colonne #5).
    
    # if (chiffreRomain) in ligne[5]:
    #     nbPages = (ligne[5] + (chiffreArabe))
    # elif ligne[5].startswith(""):
    #      nbPages = (ligne[5])
    # else:
    #     nbPages = "Problème"

    # Après plus d'une dizaine d'heures d'essais vains et autres tentatives d'intégrer la traduction clés-valeurs du dictionnaire "d" à ligne[5], je m'avoue vaincu. J'ai consulté plusieurs pages
    # d'aide sur le forum Stack Overflow et certaines pistes auraient suggéré une fonction intégrée de traduction de chiffres romains en nombres "integers". La fonction str.startswith() aurait
    # peut-être agi comme un critère approprié de condition "if" pour distinguer les nombres de pages contenant des pages liminaires de ceux qui n'en contiennent pas.
    nbPages = ligne[5]
    
    # 3.5. La variable "nomAuteur" est créée pour aller chercher le prénom de l'auteur (colonne #1 de chaque ligne) et l'additionner au nom de famille 
    # de l'auteur (colonne #2 de chaque ligne).
    nomAuteur = (ligne[1] + " " + ligne[0])
    
    # 3.6. Nous imprimerons la phrase fixe attendue entre guillemets anglais. Celle-ci contiendra des accolades {} aux endroits où le résultat des variables appliquées à chaque ligne
    #  devrait apparaître. Les variables sont entrées dans la fonction ".format()"", en ordre d'apparition dans la phrase à imprimer.
    print("{} de {} compte {} pages. Son titre est «{}», long de {} caractères.".format(typeTexte, nomAuteur, nbPages, titre, longTitre))
    
    
# J'avoue avoir très hâte de connaître la solution attendue et de constater à quel point elle repose sur les notions apprises dans les premiers cours.
# Je serais un déçu que le segment ardu (conversion des chiffres romains) soit entièrement ou en grande partie réalisable grâce à des
# notions uniquement exposées sur des forums de programmeurs. 

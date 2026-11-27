# Mini\-Projet Python : Mots anglais dans le protéome humain

## Description

Ce projet a pour objectif de rechercher des mots anglais fréquents dans les séquences protéiques du protéome humain.

À partir d'une liste de mots anglais courants et d'un fichier contenant les séquences protéiques humaines, le programme identifie les mots présents dans les protéines, calcule leur fréquence d'apparition et détermine les mots les plus représentés dans le protéome.

## Objectifs

- Lire les mots anglais les plus fréquents depuis un fichier texte.
- Filtrer les mots de longueur supérieure ou égale à 3 caractères.
- Convertir les mots en majuscules.
- Lire les séquences protéiques humaines au format FASTA.
- Rechercher la présence des mots dans les protéines.
- Déterminer le mot présent dans le plus grand nombre de protéines.
- Calculer le pourcentage de protéines contenant ce mot.
- Compter le nombre total d'occurrences de chaque mot dans le protéome.
- Présenter les résultats à l'utilisateur.

---

## Structure du projet

MiniProjet/

│

├── english\-common\-words.txt

├── human\-proteome.fasta

├── words\_in\_proteome.py

└── README.md

### Fichiers

- **english\-common\-words.txt** : liste des mots anglais fréquents.
- **human\-proteome.fasta** : séquences du protéome humain au format FASTA.
- **words\_in\_proteome.py** : programme principal.
- **README.md** : documentation du projet.

---

## Fonctions principales

### read\_words(filename)

Lit les mots du fichier texte, les convertit en majuscules et conserve uniquement ceux contenant au moins trois caractères.

### read\_sequences(filename)

Lit le fichier FASTA et construit un dictionnaire contenant les identifiants des protéines et leurs séquences.

### search\_words\_in\_proteome(words, proteome)

Recherche chaque mot dans l'ensemble des protéines et détermine dans combien de protéines il apparaît.

### find\_most\_frequent\_word(results)

Détermine le mot présent dans le plus grand nombre de protéines.

### count\_word\_occurrences(words, proteome)

Compte le nombre total d'occurrences de chaque mot dans toutes les séquences du protéome.

---

## Exécution

Depuis un terminal :

python words\_in\_proteome.py

ou

python3 words\_in\_proteome.py

---

## Exemple de résultat

Nombre de mots sélectionnés : 2450

Mot le plus fréquent : AGE

Présent dans : 1523 protéines

Pourcentage du protéome : 37.8 %

Nombre total d'occurrences : 4872

---

## Technologies utilisées

- Python 3
- Structures de données : listes et dictionnaires
- Gestion de fichiers texte
- Format FASTA
- Tkinter 

---

## Auteur

Maram Triki

Chahed Ben Aissa

Mini\-projet réalisé dans le cadre du module Python.

# API développer par NOUICER Nadir et BAADJI Ilias

## Instructions

pour mieux utiliser l'api il est recommender de créer un environement virtual pour çela a partir d'un terminal lancer la commande suivante :

    python -m venv PyramidApi

une fois l'environement créer, faudra l'activer pour çela toujours sur le terminale lancer les commandes suivantes:

    cd Pyramid
    Scripts\activate

maintenant si vous voyez (PyramidApi) dans votre terminal c'est que votre environement est bien activer vous pouvez continue:

afin d'utiliser l'api commencer par installer les packages nécessaires comme suit :

    pip install -r requirements.txt

çela installera toute les librairies nécessaire pour votre projet.

vous pouvez lancer votre serveur avec la commande suivante : 
    
    python api.py

çela lancera votre serveur sur l'adresse 127.0.0.1 et le port 8000.



## Genrer un nombre aleatoir [/val{?nb}]

### Genrer un nombre aleatoir [GET]

+ Parameters
    + nb (number, optional) - combien de valeurs aleatoire faudra generer.

+ Request

    + Headers
    
            Content-Type: application/json

+ Response 200 (application/json)

    + Attributes
        - tableau (array[number], optional): qui retourne du code json contenant 
un tableau de n valeurs entières aléatoires comprises en -1000 et +1000

+ Response 400 (application/json)

    + Attributes
        - message: "veuilez inserer le bon paramètre"

## La somme de deux nombre [/calc/add{?n1,n2}]

### La somme de deux nombre [GET]

+ Parameters
    + n1 (number, required) - le premier nombre
    + n2 (number, required) - le deuxième nombre

+ Request

    + Headers
    
            Content-Type: application/json

+ Response 200 (application/json)

    + Attributes
        - result (number): la somme des deux nombre

+ Response 400 (application/json)

    + Attributes
        - message: "veuillez inserer les bons paramètres"


## Le Produit de deux nombre [/calc/prod{?n1,n2}]

### Le Produit de deux nombre [GET]

+ Parameters
    + n1 (number, required) - le premier nombre
    + n2 (number, required) - le deuxième nombre

+ Request

    + Headers
    
            Content-Type: application/json

+ Response 200 (application/json)

    + Attributes
        - result (number): le produit des deux nombres

+ Response 400 (application/json)

    + Attributes
        - message: "veuillez inserer les bons paramètres"

## les informations station [/stations_velo{?id,addr,cap}]

### les informations station [GET]

+ Parameters
    + id (string, required) - l'id de la station.
    + addr (boolean, optional) - si disponible, retourne l'address de la station.
    + cap (boolean, optional) - si disponible, retourne la capacity de la station.

+ Exemple 

    + /stations_velo?id=10&addr
    + /stations_velo?id=10&addr

+ Request

    + Headers
    
            Content-Type: application/json

+ Response 200 (application/json)

    + Attributes
        - station  : les information d'une station çelon l'id.
        - address (string, optional): l'address de la station (si paramètre fournit).
        - capacity (number, optional): la capacity d'une station (si paramètre fournit).
        - totla station : le nombre total des stations si l'id est égale a "toutes".
+ Response 400 (application/json)

    + Attributes
        - message: "veuillez inserer les bons paramètres"
        
## l'adresse d'une station [/stations_velo/n/addr]

### recuperer l'adresse d'une station [GET]

+ Parameters
    + n (string) : l'id de la station

+ Request

    + Headers
    
            Content-Type: application/json

+ Response 200 (application/json)

    + Attributes
        - address (string, optional): l'address de la station.
        
## la capacity d'une station [/stations_velo/n/cap]

### recupere la capcity d'une station [GET]

+ Parameters
    + n (string) : l'id de la station

+ Request

    + Headers
    
            Content-Type: application/json

+ Response 200 (application/json)

    + Attributes
        - - capacity (number, optional): la capacity d'une station.
        
## la capacity de toute les stations [/stations_velo/toutes/cap]

### recupere la capcity de toutes les stations [GET]

+ Request

    + Headers
    
            Content-Type: application/json

+ Response 200 (application/json)

    + Attributes
        - capacity (number, optional): la capacity d'une station.



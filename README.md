# Projet DBT avec Airflow

Ce projet utilise DBT pour la modélisation des données et Airflow pour l'orchestration des tâches.

## Installation

1. Clonez ce dépôt :

    ```bash
    git clone https://github.com/votre_utilisateur/votre_projet.git
    cd votre_projet
    ```

2. Lancez Airflow avec Docker Compose :

    ```bash
    docker compose up
    ```

3. Accédez au webserver d'Airflow :

    Ouvrez votre navigateur et accédez à [http://localhost:8080](http://localhost:8080)

## Dossiers

- `dags/`: Contient les fichiers DAG pour Airflow.
- `users/`: Contient les fichiers de configuration et de modèle pour DBT.

## Fichier JSON

Le fichier JSON a été généré à partir de DBT Docs.

## Utilisation de DBT

1. Entrez dans le container Airflow :

    ```bash
    sudo docker exec -it <container_id> /bin/bash
    ```

2. Accédez au répertoire DBT :

    ```bash
    cd ~/users
    ```
NB : copiez les fichiers my_dbt_project + ./dbt du local vers le container pour avoir la même configuration

3. Exécutez les commandes DBT :

    ```bash
    dbt init                  # Initialisez un nouveau projet DBT
    dbt debug                 # Vérifiez la configuration de DBT
    dbt run                   # Exécutez les modèles DBT
    dbt seed                  # Exécutez les seeds DBT
    dbt snapshot              # Exécutez les snapshots DBT
    dbt docs generate         #Exécutez la doc DBT
    ```


## Snapshots

Dans le répertoire `snapshots/`, vous trouverez :

- Chargement de la table `orders` avec DBT seed à l'aide d'un fichier csv
- Création d'un snapshot pour la table `snapshot_orders` avec `dbt snapshot`.
- Modification de la table `orders` en changeant le statut de la commande pour `id = 1`.
- Exécution de `dbt snapshot`.
- Chargement de la table `snapshot_orders` pour observer la modification de `dbt_valid_to`.
- Création d'une vue stg_orders pour afficher uniquement `dbt_valid_to`.

![image](https://github.com/IkramKheopsys/dbt/assets/113558455/93c7871e-9834-430e-882d-a188f0bbc077)
![image](https://github.com/IkramKheopsys/dbt/assets/113558455/8099d349-1709-47f1-b7c9-1283dc1442ed)
![image](https://github.com/IkramKheopsys/dbt/assets/113558455/e50a272f-512e-4d19-9e81-41f3d4c51004)
![image](https://github.com/IkramKheopsys/dbt/assets/113558455/6597476e-19ea-45f9-8410-563f36377ad4)

1. Entrez dans le container Airflow en mode root pour executer les commandes sudo :

    ```bash
    sudo docker exec -u 0 -it 7fb29f54367b bash
    ```


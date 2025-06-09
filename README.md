# Projet-FastAPI

Une API RESTful développée avec FastAPI pour gérer des données météorologiques. Elle utilise MongoDB Atlas comme base de données et sécurise les accès avec des jetons JWT.

## Pour lancer l'API localement :
### Prérequis 
```bash
pip install fastapi uvicorn pymongo
```
### Démarrage

```bash
uvicorn main:app --reload
```
Un fichier server.key contient la clé secrète pour signer les JWT. Il doit être créé manuellement à la racine du projet avec une chaîne de caractères secrète.
Une fois ceci fait, dans Endpoint POST / login, entrer :
```bash
{
  "username": "admin",
  "password": "123"
}
```
Puis ajouter le token dans l'en-tête ```Authorization``` des requêtes

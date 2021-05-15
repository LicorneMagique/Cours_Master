# Rapport

## Rappel des projets

Je participe au développement de trois projets, **Main** notre application principale, **crossroads** notre produit dirrigeant (idéalement l'avenir de Finalgo) et **finsearch** une sorte de Main simplifié dont nous gérons le développement et la maintenance pour l'un de nos clients.

En terme de code chaque application possède un front Angular et un back Java Spring qui fonctionne sous forme d'une API REST. Le back est le même pour Main et pour Crossroads, puis Finsearch possède un front et un back ce qui nous fait 5 projets.

![.](projets.svg)

\* Les doubles flèches symbolisent les échanges de données entre front et back

---

## Tâches

### Tâche Finsearch

finsearch : parler de l'écran backoffice + du dev persistance plateforme de connexion des utilisateurs

### Tâche SSO

- SSO Cafpi
- SSO Crossroads Intuit
- SSO Crossroads Google
- Refacto : enum générique, getJsonObjectFromPath

Début du développement du système de connexion SSO avec Microsoft Azure pour l'un de nos clients (main back)

Début de l'implémentation de la connexion par SSO Microsoft Azure (main front)

Mise en place d'un système de connexion SSO / OpenID Connect sur notre application pour que les utilisateurs du client Cafpi puissent se connecter avec leur compte Microsoft Azure

ajout de la connexion sso de Google (back et front)

Mise en place d'une connexion SSO OAUTH2 avec la plateforme Quickbooks / Intuit

Tentative de connexion SSO SAML avec Google (encore en cours)

réécriture du code de sso à l'aide d'un component spécifique (front)

factorisation des fonctions de vérification des tokens sso de Google Microsoft (back)

factorisation des fonctions de traitement des connexion sso d'intuit et de Google (back)

Fin implémentation sso google en mode développement

### Tâche antivirus

- Code front
- Code back
- Page wiki
- Cron
- Logs

MAJ du code antivirus (main back)

Mise en place du redémarrage et des mises à jour automatique du service antivirus sur notre serveur

### IText

- fichiers json

Implémentation d'un système générique pour la génération de la couverture des notes de synthèse avec du contenu dynamique, librairie IText

### Produit subvention

Mise en place d'un service Java permettant de manipuler l'API REST Open Data du site aides-entreprises.fr
Réécriture du formulaire de recherche de financements dans le but de séparer la partie formulaire générique de la partie recherche de financements
Création d'un nouveau formulaire de recherche de suventions pour les entreprises
Mise en place d'une API de recherche des subventions
Mise en place d'un système de questions dynamiques dont une partie du contenu est récupéré depuis l'API de recherche des subventions
Mise en place d'un algorithme de filtre des subventions en fonction des réponses de l'utilisateur
Réécriture de la page résultats dans le but de séparer la partie page de résultats générique de la partie résultats de financements
Création d'une nouvelle page de résultats pour les subventions

Crossroads front
    Formulaire générique :
    Ajout d'options pour passer certaines questions en choix multiple
    Ajout d'une barre de recherche sur les questions de type dropdown
    Implémentation d'un système de sauvegarde des captions des réponses du formulaire
    
    Formulaire spécifique subventions :
    Implémentation d'un mode debug qui affiches des informations spécifiques aux subventions
    Création d'un algorithme de recherche de contact dans les données de l'API (que Bertrand a corrigé)

Crossroads back
    Subvention :
    Ajout et suppressions de critères dans l'API des subvention
    Ajout d'un système de filtre intelligent pour obtenir 100 de couverture sur les départements, qui par défaut sont inférieurs à 100%
    Génération de statistiques de pertinence des critères de filtre des subvention
    Révision de la priorité de chaque critère de filtre des subvention en fonction de ces résultats
    Page wiki

PostMan (j'ai mangé leur BD)
Traitement / analyse des données de l'API subvention, notamment des territoires avec PostMan

Dans le formulaire des subvention, remplissage automatique de certaines questions à partir des informations du code siret qu'on récupère depuis l'API de l'INSEE
Création de table de convertion code effectif siret -> code effectif aides-entreprises et code postal -> code territoire aides-entreprises

ajout des informations récupérées par le code siret dans le mode debug du front (front et back)
ajout d'un système de recherche de subvention par mots clés (back)
ajout de la question pour récupérer les mots clés (front)
récupération automatique du profil aides-entreprises à partir du numéro de siret (back)
ajout d'un système de niveau de priorité des paramètres aides-entreprises pour améliorer l'algorithme de relachement des contraintes

Ajout système de copie quotidien de la base de données des subventions avec un cron
Enregistrement de certaines informations des subventions dans notre base de données
Envoi de ces informations à notre front
Ajout d'un système de traitement spécifique des subventions pour ajouter de nouveaux critères que l'API aides-entreprises.fr ne prend pas en charge
Création d'un algorithme de nettoyage des caractères spéciaux dans le texte : balises html, escape html, escape unicode
Récupération de tous les mots distincts utilisés dans la base de données subvention, avec un objectif d'IA sur les mots

### Stripe

Refactoring du système de gestion des acticles Stripe pour quelque chose de plus généique et typé (permettant de détecter plus d'erreurs qu'avant) (crossroads)
Réimplémentation de toute l'API Stripe avec la dernière version, l'ancienne version était complètement dépréciée (crossroads)

Récupération automatique des captions des utilisateurs depuis leur facture Stripe
Debug de Stripe dont le callback était bloqué par notre JwtFilter

### Fonctionnalités spécifiques variés

#### Système d'unité des OCA

Ajout d'un système d'unité (mois, %, €, année(s)) dans les OCA (système de stockage ressemblant à du NoSQL) (main back)

Ajout du système d'unité des OCA sur les ITE (propagation du système d'unité dans le front) (main front)

#### Conservation du GET sur Crossroads

Ajout d'un système de conservation des paramètres GET de l'URL

#### Génération enum depuis csv d'Araud

génération d'une class enum java à partir d'un fichier csv et de nodejs

#### Fix session context -> request context

Fix du problème de récupération de l'utilisateur connecté en back (bug avec les variables de session partagées)

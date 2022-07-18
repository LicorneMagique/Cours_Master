# Notes

## Consignes

se focaliser sur les tâches les plus techniques ou caractéristiques de ce qu'on fait
localiser entreprise, projet
MAX 25 pages, moins d'annexe possible, uniquement des captures d'écran en cas de nécessité absolue
montrer qu'on est technique niveau M2, entrer dans le détail sans le montrer style bugs super chelou, travail de fourmis, architecture et décision techniques, montrer les tâches avec un très haut niveau de recul
avoir casi fini avant fin juillet pour que medini puisse le relire

20 minutes de présentation + questions, moins de contenu que le rapport

## REX 0

### Activité et tâches confiées

#### Améliorations diverses des plateformes de Finalgo

- ajout de nouvelles fonctionalités,
- correction de bugs,
- maintenance,
- participer aux formations internes de équipe (soit comme formateur soit pour me faire former).

#### Objectifs à atteindre en fin d'année universitaire

Étant donné l'évolution rapide des produits de Finalgo, il est compliqué de donner des objectifs précis.

Globalement,

- améliorer les applications de Finalgo,
- monter en compétence sur les technologies que nous utilisons,
- avoir suivi les actualités en rapport avec nos technologies.

### ENVIRONNEMENT DU POSTE DE TRAVAIL

#### Place au sein de la structure (hiérarchie, organigramme)

La hiérarchie est très horizontale, chaque membre de l'équipe est référent dans ses domaines de prédilection.

#### Personnes avec lesquelles je suis en relation (internes et externes)

Je travail beaucoup avec l'équipe technique constituée de Bertrand, Iskander, Jade et Valentin.

Je travail également avec Arnaud dans une moindre mesure.

#### Moyens mis à ma dispositions (machines, équipements, locaux ...)

J'ai à ma disposition un ordinateur portable performant pour travailler et j'ai accès à un open space où nous allons travailler deux jours par semaines. Le reste du temps nous sommes en distanciel, il s'agit d'une volonté de l'équipe.

#### Contraintes à respecter (hygiène, sécurité, délais, horaires, procédures ...)

Pas de contraintes particulières.

## REX de l'année

J'ai travaillé sur l'indépendance de notre produit Subvention par rapport à l'API d'aides-entreprise.fr qui est utilisé par notre produit pour rechercher des subvention.

- Copie quotidienne de la base de données subvention sous forme de fichiers JSON
- Chargement automatique des données de ces fichiers en base de données dans les OCA
- Nettoyage automatique des données invalides
- Algo de recherche de subventions fait pour utiliser les OCA au lieu de l'API

---

Refonte du système de tâches / notifications : suppression de l'ancien système devenu redondant avec notre base de logs, création d'un système de transfert, refactoring du code pour utiliser uniquement nos logs, optimisation du chargement des données en front, réécriture de la requête dans le DAO pour minimiser les appels à la base de données

---

- fix du téléchargement des dossiers qui était bloqué chez certaines banques
- corrections de bugs en tous genres : magiclinks, mode debug, log UserActions, redirections automatiques, SSO
- ajout de la date de création dans l'une de nos entités
- création du mail des résultats de la recherche de financements
- configuration quickbooks pour mettre Automate sur le store
- mise en place des objets en vue du refactoring objet générique
- migration de l'entité utilisateur sur les objets génériques
- refactoring des projets en vue de la migration sur les objets génériques

---

J'ai travaillé sur la migration des données stockées dans les OCA (structure de stockage interne) vers un nouveau système plus performant.

J'ai essentiellement supprimé des classes, refactoré du du code et migré des données.

Plus précisément, j'ai déplacé un certain nombre d'attributs vers les anciens OCA dans différentes entités, puis j'ai migré les OCA de ces entités vers le nouveau système à la fois en terme de mapping/code et de base de données.

---

Suite du refactoring de notre implémentation de persistence des données,
réalisation de tâches pour l'intégration de notre plateforme dans QuickBooks :
Expiration des JWT
Renouvellement des JWT
et résolution d'un bug de persistence qui empêchait la récupération d'informatios depuis l'API SIRENE (code siret).

---

Fix de bugs, refactoring et amélioration de performance
- fix d'un bug de redirection infinie
- refacto système de connexion
- fix de bugs dans le système de redirection d'url de crossroads (redirectURI)
- fix du delete qui ne marchait plus sur le type ocaVariable
- optimisation d'API trop lentes (minimisation d'appels à la base de données -> de plusieurs secondes on est passé à quelques dizièmes)
- refactoring lié aux generic objects (derniers REX)
- changement de types en base de données pour stocker plus d'informations dans certains champs
- suppression d'une barre de recherche devenue obsolète

Fonctionnalités diverses :
- pré remplissage des formulaires si donnée déjà connue sur Crossroads
- Suppression des logs verbeux du broken pipe
- tentative d'installation de checkstyle en back
- branchement de certains logs dans un nouveau channel slack

Intégration de QuickBooks dans Crossroads :
- ajout boutons connexion / déconnexion
- appel des api de fermeture de session
- ajout mode debug
- ajout d'un système de renouvellement automatique des JWT (non spécifique à QB)

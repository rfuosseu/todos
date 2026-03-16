# TodoAPI

Une API REST simple pour gérer des todos, construite avec **FastAPI**.  
Projet fil rouge de la formation *Fondamentaux Git & GitHub*.

---

## Installation

### Prérequis

- Python 3.11+
- pip

### Étapes

```bash
# 1. Cloner ou initialiser le projet
cd todoapi

# 2. Créer un environnement virtuel
python -m venv .venv

# 3. Activer l'environnement virtuel
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Lancer le serveur
uvicorn main:app --reload
```

L'API est disponible sur : http://localhost:8000  
La documentation interactive (Swagger) : http://localhost:8000/docs

---

## Description des endpoints

### Health

| Méthode | Route | Description |
|---------|-------|-------------|
| GET | `/health` | Vérifie que l'API est opérationnelle |

**Réponse :**
```json
{ "status": "ok" }
```

---

### Todos

| Méthode | Route | Description |
|---------|-------|-------------|
| GET | `/todos` | Récupérer tous les todos |
| POST | `/todos` | Créer un nouveau todo |
| GET | `/todos/{id}` | Récupérer un todo par son ID |
| DELETE | `/todos/{id}` | Supprimer un todo |
| PUT | `/todos/{id}` | Mettre à jour un todo |
| PATCH | `/todos/{id}/complete` | Marquer un todo comme terminé |
| GET | `/todos?status=done` | Filtrer les todos par statut |
| GET | `/todos?q=keyword` | Rechercher dans les todos |

---

### Modèle Todo

```json
{
  "id": 1,
  "title": "Mon premier todo",
  "description": "Une description optionnelle",
  "completed": false,
  "created_at": "2024-01-15T10:30:00"
}
```

### Créer un todo (body attendu)

```json
{
  "title": "Mon todo",
  "description": "Description optionnelle"
}
```

---

## Structure du projet

```
todoapi/
├── main.py              ← Point d'entrée de l'application
├── requirements.txt     ← Dépendances Python
├── .gitignore
├── README.md
├── routers/
│   └── todos.py         ← Définition des routes
├── models/
│   └── todo.py          ← Modèles Pydantic
└── storage/
    └── database.py      ← Stockage en mémoire
```

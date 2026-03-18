from typing import List

from todo import Todo

# Base de données en mémoire — simple liste Python
todos: list[Todo] = []

# Compteur pour générer les IDs
counter: int = 0


def next_id() -> int:
    """Retourne le prochain ID disponible."""
    global counter
    counter += 1
    return counter

import numpy as np

def calculate(list):
    # 1. Vérifier si la liste contient exactement 9 éléments
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # 2. Convertir la liste en un tableau Numpy 3x3
    matrix = np.array(list).reshape(3, 3)

    # 3. Calculer les statistiques
    # np.tolist() est utilisé car freeCodeCamp exige des listes Python standards
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(), # Moyenne par colonne (Axis 1 dans le résultat final)
            matrix.mean(axis=1).tolist(), # Moyenne par ligne (Axis 2 dans le résultat final)
            matrix.mean().tolist()        # Moyenne totale (Flattened)
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().tolist()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().tolist()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().tolist()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().tolist()
        ]
    }

    return calculations
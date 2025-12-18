import mean_var_std

# Test avec la liste exemple
try:
    print(mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
except ValueError as e:
    print(e)

# Test de l'erreur
try:
    print(mean_var_std.calculate([0, 1, 2]))
except ValueError as e:
    print(e)
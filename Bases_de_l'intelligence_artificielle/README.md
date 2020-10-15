# Bases de l'intelligence artificielle

[Page du cours](https://perso.liris.cnrs.fr/marie.lefevre/enseignement-BIA.html)

## Modélisation et résolution du problème avec OR-Tools

```python
# Import de la librairie Python de OR-Tools
from ortools.sat.python import cp_model

# Création du model
model = cp_model.CpModel()

# Initialisation des variables sur [0, 201[
a = model.NewIntVar(0, 201, 'a')
b = model.NewIntVar(0, 201, 'b')

# Objectif : formule de Z à maximiser
model.Maximize(350 * a + 300 * b)

# Ajout des contraintes arithmétiques
model.Add(a+b <= 200)
model.Add(9 * a + 6 * b <= 1566)
model.Add(12 * a + 16 * b <= 2880)

# Résolution du problème
solver = cp_model.CpSolver()
solver.Solve(model)

print("Z =", solver.ObjectiveValue())
print("a =", solver.Value(a))
print("b =", solver.Value(b))

```

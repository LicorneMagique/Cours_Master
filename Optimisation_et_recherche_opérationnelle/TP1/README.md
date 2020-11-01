# TP1

À rendre le 18 décembre

## Lancement

```shell
# Pour checker le fuites de mémoire
make clean; make; valgrind --leak-check=full --show-leak-kinds=all ./mincut -i data/graphEL_as2000 -o output
```

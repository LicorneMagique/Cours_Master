# Interopérabilité

[Page du cours](https://perso.liris.cnrs.fr/angela.bonifati/teaching/TIW2-2021-2022/)

## Notes

### Les flèches

![exemple 1](./exemple_1.png)

**Flèche noire** : représente le chemin de la variable exportée de sa position de départ à sa position d'arrivée

- Dans `D(e,m) -> M(m)` le `m` est la variable exportée de `D.2` à `M.1`
- Dans `M(m) -> ∃e D(e,m)` le `m` est la variable exportée de `M.1` à `D.2`
- Dans `E(x,y) -> ∃z E(y,z)` le `y` est la variable exportée de `E.2` à `E.1`

**Flèche rouge** : représente le départ de la variable exportée et l'arrivée de la variable du *il existe*

- Dans `M(m) -> ∃e D(e,m)` le `m` est la variable exportée de `M.1` et `D.1` est l'arrivée de la variable `e` du *il existe*
- Dans `E(x,y) -> ∃z E(y,z)` le `y` est la variable exportée de `E.2` et `E.2` est l'arrivée de la variable `z` du *il existe*

### Neo4J

```txt
eyJhbGciOiJQUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Ii4rQC4rIiwibWl4cGFuZWxJZCI6IjE3Y2RmZDg0ZjEzNDktMGZlNDYyYjZkZjYzMzUtMTQyNDEyMDktMWZhNDAwLTE3Y2RmZDg0ZjE0MzUiLCJtaXhwYW5lbFByb2plY3RJZCI6IjRiZmIyNDE0YWI5NzNjNzQxYjZmMDY3YmYwNmQ1NTc1Iiwib3JnIjoiLioiLCJwdWIiOiJuZW80ai5jb20iLCJyZWciOiIgIiwic3ViIjoibmVvNGotZGVza3RvcCIsImV4cCI6MTY2NzM3OTExMiwidmVyIjoiKiIsImlzcyI6Im5lbzRqLmNvbSIsIm5iZiI6MTYzNTg0MzExMiwiaWF0IjoxNjM1ODQzMTEyLCJqdGkiOiJydU8zaXhHdEYifQ.qgQRTIL9XjJJIzGrNZqpzc84CwouzTNGvgymwh7yTKElOf2IUpSDaVGDO8QInoGL-sI_ifgj2ENMDKfGnC0raN3-huigcPBnjf0PfjcrPoEt6k4XxdEvtzM8l2z6kuGkxxI1iSFXNV7rJ-R0FdchugfpS7_zZ79iqJpyCQtFcXdlswGaOtSCMnS_JvVHZ0iZmeBCXFoM_2zuh_hXbqPJK7TzlP1rpEmk5kZZ56Y_Rs0DvP1tFcB81C9OApBlZAyGqthNPKpXjLiPAXKMvs-o8RhMpYIx7Z7jZfrh0rFsygF_7rVHLa3MnFM72UX3Iyc1ym4-7o90M7Rk9lJRDCvGnA
```

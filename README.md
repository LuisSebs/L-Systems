# Lindenmayer Systems (L-Systems)

## Autor: Arrieta Mancera Luis Sebastian

Un sistema L es un sistema de reescritura paralelo y un tipo de gramática formal que consta de un alfabeto de símbolos que se pueden utilizar para formar cadenas. Además son usados para generar imágenes gráficas usando los gráficos de tortuga.

# Ejecución

Para correr el programa ejecuta el archivo `L-Systems.py` con el siguiente comando desde terminal:

```bash
python3 L-Systems.py
```

Si no funciona ejecuta el siguiente comando:

```bash
python L-Systems.py
```

Si se tiene problemas para correr el programa, favor de ejecutarlo con un editor de código como VSC.

Se mostrara en terminal un menu con las opciones para crear alguno de los siguientes sistemas. 

**Nota:** de preferencia esperar hasta que se terminen de dibujar los sitemas, al finalizar puedes cerrar la pestaña o dar click en la ventana para cerrar.


# Fractal Binary Tree
![Fractal Binary Tree](https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/automatas_celulares/tarea2/fractal_binary_tree.png)

**Axioma**

    - 0

**Gramática:**

    - 1 -> 11
    - 0 -> 1[0]0

# Koch Curve
![Fractal Binary Tree](https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/automatas_celulares/tarea2/koch_curve.png)

**Axioma**

    - F

**Gramática:**

    - F -> F+F-F-F+F

# Sierpinski Triangle
![Fractal Binary Tree](https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/automatas_celulares/tarea2/sierpinski_triangle.png)

**Axioma**

    - F-G-G

**Gramática:**

    - F -> F-G+F+G-F
    - G -> GG

# Dragon Curve
![Fractal Binary Tree](https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/automatas_celulares/tarea2/dragon_curve.png)

**Axioma**

    - F

**Gramática:**

    - F -> F+G
    - G -> F-G

# Fractal Plant
![Fractal Binary Tree](https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/automatas_celulares/tarea2/fractal_plant.png)

**Axioma**

    - X

**Gramática:**

    - X -> F+[[X]-X]-F[-FX]+X
    - F -> FF

# Fuentes de Consulta:

- [Simulador L-Systems](https://www.kevs3d.co.uk/dev/lsystems)
- [Ejemplo python](http://opensask.ca/Python/Strings/LSystems.html)
- [L-Systems](https://en.m.wikipedia.org/wiki/L-system)
# Ejercicio del Bootcamp de Ciencias de la Computación - AST
## _AST - Abstract Sintax Tree_

El programa permite evaluar una serie de expresiones como las siguientes:

```py
  # var a = 5
  BinaryOp('=', VarDec('a'), 5),

  # var b = 8
  BinaryOp('=', VarDec('b'), 8),

  # var res = a * 2 + b / 4
  BinaryOp('=', 
    VarDec('res'), 
    BinaryOp('+', 
             BinaryOp('*', 
                      VarName('a'), 2), 
              BinaryOp('/', 
                      VarName('b'), 4))),

  # var res2 = a + b
  BinaryOp('=', 
           VarDec('res2'), 
           BinaryOp('+', 
                    VarName('a'), 
                    VarName('b'))),

  # var res3 = 24 / res + res2 * a
  BinaryOp('=', 
           VarDec('res3'), 
           BinaryOp('+', 
                    BinaryOp('/', 
                             24, 
                             VarName('res')), 
                    BinaryOp('*', 
                             VarName('res2'), 
                             VarName('a'))))
```

## Pruebas
- Clona el repositorio
- Desde una terminal ejecuta el archivo ast.py
```sh
py ast.py

var a = 5
var b = 8
var res = a * 2 + b / 4       
var res2 = a + b
var res3 = 24 / res + res2 * a
{'a': 5, 'b': 8, 'res': 12.0, 'res2': 13, 'res3': 67.0}
```


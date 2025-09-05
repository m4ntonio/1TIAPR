# Manual de Padrões Python

## Pirâmide de estrelas
**Descrição:** Imprime uma pirâmide de estrelas centralizada usando '* '

**Código:**
```python
rows = 5
for i in range(1, rows+1):
    print(" "*(rows-i) + "* " * i)
```
**Saída:**
```
    * 
   * * 
  * * * 
 * * * * 
* * * * * 

```

## Triângulo numérico
**Descrição:** Imprime números em triângulo crescente por linha

**Código:**
```python
rows = 5
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
```
**Saída:**
```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

```

## Triângulo invertido numérico
**Descrição:** Triângulo decrescente de números

**Código:**
```python
rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
```
**Saída:**
```
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 

```

## Diamante de estrelas
**Descrição:** Pirâmide completa com metade superior e inferior formando um diamante

**Código:**
```python
rows = 5
for i in range(1, rows+1):
    print(" "*(rows-i) + "* " * i)
for i in range(rows-1, 0, -1):
    print(" "*(rows-i) + "* " * i)
```
**Saída:**
```
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 

```

## Quadrado de números
**Descrição:** Imprime um quadrado de números com linhas e colunas iguais

**Código:**
```python
rows = 5
for i in range(1, rows+1):
    for j in range(1, rows+1):
        print(j, end=" ")
    print()
```
**Saída:**
```
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 

```

## Diagonal de números
**Descrição:** Imprime números apenas na diagonal, espaços nos outros lugares

**Código:**
```python
rows = 5
for i in range(1, rows+1):
    for j in range(1, rows+1):
        if i == j:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print()
```
**Saída:**
```
1         
  2       
    3     
      4   
        5 

```

## Pirâmide invertida
**Descrição:** Pirâmide de estrelas invertida

**Código:**
```python
rows = 5
for i in range(rows, 0, -1):
    print(" "*(rows-i) + "* " * i)
```
**Saída:**
```
* * * * * 
 * * * * 
  * * * 
   * * 
    * 

```

## Triângulo de letras
**Descrição:** Imprime um triângulo crescente com letras do alfabeto

**Código:**
```python
rows = 5
import string
letters = string.ascii_uppercase
for i in range(1, rows+1):
    print(" ".join(letters[:i]))
```
**Saída:**
```
A
A B
A B C
A B C D
A B C D E

```

## Pirâmide de números com espaço
**Descrição:** Pirâmide de números centralizada

**Código:**
```python
rows = 5
for i in range(1, rows+1):
    print(" "*(rows-i) + " ".join(str(j) for j in range(1, i+1)))
```
**Saída:**
```
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5

```

## Quadrado de asteriscos
**Descrição:** Quadrado sólido de '*'

**Código:**
```python
rows = 5
for i in range(rows):
    print("* " * rows)
```
**Saída:**
```
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

```


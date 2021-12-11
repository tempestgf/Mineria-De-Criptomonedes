# Minador de Criptomonedes Miner
Importem hashlib, la llibreria on conté l'algoritme criptogràfic SHA-256.

```
import hashlib
```

Importem time, la llibreria de Python que conta quan comença o acaba una funció del codi, posteriorment l'anomenem 't' per cridar-la més fàcilment en el codi.

```
import time as t
```

Li diem al programa que el límit de números que pot provar per desxifrar el minat és 10000000000.

```
NONCE_LIMIT = 10000000000
```

Establim el nombre de zeros en aquest cas a 4, segons la dificultat donada.

```
zeros = 4
```

Definim 3 variable d'execució amb def (definir) com el número de bloc el número de transacció i el hash anterior a la transacció.

```
def mina(numero_de_bloc, transaccions, hash_anterior):
```

Dintre de la funció def utilitzarem un bucle 'for' per realitzar el que s'anomena força bruta per esbrinar el hash utilitzant l'anteriorment establert com a límit en un rang d'intents.

```
for nonce in range(NONCE_LIMIT):
```

Dintre del bucle for li direm que ajunti en text_base les tres variables donades (numero_de_bloc, transaccions, hash_anterior) més el numero nonce en què s'establirà a partir de diferents intents de l'1 al 10000000000.

```
text_base = str(numero_de_bloc) + transaccions + hash_anterior + str(nonce)
```

Dintre del bucle for seguit del text_base encriptarem amb l'algoritme SHA-256 el text_base

```
hash_try = hashlib.sha256(text_base.encode()).hexdigest()
```

Afegim el condicional 'if' per crear una condició per quan trobi mitjançant força bruta el hash que contingui els 0 x anteriorment establerts com a 4.

```
if hash_try.startswith('0' * zeros):
```

Dintre de la condició fem una impressió a la consola del número nonce que hi ha permès trobar el hash amb els x zeros.

```
print(f"Hash trobat amb Nonce: {nonce}")
```

Dintre de la condició seguida de l'anterior impressió a consola fem una altra impressió, però aquesta vegada amb el hash trobat utilitzant Formatted string literals print(f" value not formatted {value}") cosa que ens permet imprimir un text més el valor de hash_try.

```
print(f"El hash es:  {hash_try}")
```

Escrivim return per acabar el condicional.

```
return
```

En el bucle for si el programa prova els 10000000000 números i no troba el hash farem enviar al programa un missatge d'error amb return -1.

```
return -1
```

Comencem l'instant temps perquè comenci a comptar quan s'executi el miner. Cal remarcar que és anomenat començament sense c trencada, ja que el codi se sol escriure en angles i no un altre idioma, ja que si utilitzem caràcters que no processa el llenguatge els podria interpretar erròniament i, per tant, no fer funcional el programa.

```
comensament=t.time()
```

Ara hem de cridar a la funció 'miner' perquè executi el que hem definit en el def anteriorment.

```
miner(numero_de_bloc, transaccions, hash_anterior)
```

Per acabar aturem el temps.

```
temps_donat = t.time()- comensament
```

I imprimim a consola el temps entre el començament d'execució del programa fins al final.

```
print("\nEl procces de minar a durat ",temps_donat,"segons")
```


















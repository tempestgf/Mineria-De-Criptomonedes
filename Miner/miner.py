import hashlib 
import time as t

print('''\n
 /$$      /$$ /$$$$$$ /$$   /$$ /$$$$$$$$ /$$$$$$$ 
| $$$    /$$$|_  $$_/| $$$ | $$| $$_____/| $$__  $$
| $$$$  /$$$$  | $$  | $$$$| $$| $$      | $$  \ $$
| $$ $$/$$ $$  | $$  | $$ $$ $$| $$$$$   | $$$$$$$/
| $$  $$$| $$  | $$  | $$  $$$$| $$__/   | $$__  $$
| $$\  $ | $$  | $$  | $$\  $$$| $$      | $$  \ $$
| $$ \/  | $$ /$$$$$$| $$ \  $$| $$$$$$$$| $$  | $$
|__/     |__/|______/|__/  \__/|________/|__/  |__/                                                                                                                                                                                                                                  
	''')

print("Simulació de mineria de criptomonedes creada per estudiants d'IES El Castell Enric Vidal i Guillem Farriols.")

NONCE_LIMIT = 10000000000

while True:
	try:
	   zeros = int(input('\nDificultat (Número de zeros exemple 4): '))      
	except ValueError:
	   print("La Dificultat ha de ser establerta amb un nombre enter, torna a provar.")
	   continue
	else:
	   break 

numero_de_bloc = input('\nNúmero de bloc (exemple 24): ')
transaccions = input('\nNúmero de transacció (exemple 76123fcc2141): ')
hash_anterior = input('\nNúmero del hash anterior (exemple 876de875b967c87): ')

def miner(numero_de_bloc, transaccions, hash_anterior):
	for nonce in range(NONCE_LIMIT):
		text_base = str(numero_de_bloc) + transaccions + hash_anterior + str(nonce)
		hash_try = hashlib.sha256(text_base.encode()).hexdigest()
		if hash_try.startswith('0' * zeros):
			print(f"\nHash trobat amb Nonce: {nonce}")
			print(f"\nEl hash és:  {hash_try}")
			return 

	return -1

comensament = t.time()

miner(numero_de_bloc, transaccions, hash_anterior)

temps_donat = t.time()- comensament
print("\nEl procés de minar ha durat",temps_donat,"segons\n")

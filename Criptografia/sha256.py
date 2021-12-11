# En "ABC" és possible canviar de paraula en comptes d'ABC introduir "Hola" entre les comes"".
from hashlib import sha256
print(sha256("ABC".encode("ascii")).hexdigest())

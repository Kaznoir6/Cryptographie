import sys, time
from cryptography.hazmat.primitives.serialization import load_pem_private_key
cle = open(sys.argv[1], "rb").read()
debut = time.time()
for n, mot in enumerate(open(sys.argv[2], encoding="utf-8").read().split(), 1):
    try:
        load_pem_private_key(cle, password=mot.encode())
        print(f"Passphrase trouvée : {mot!r} après {n} essais en {time.time()-debut:.2f} s")
        break
    except (ValueError, TypeError):
        pass
else:
    print(f"Aucune passphrase trouvée ({n} essais, {time.time()-debut:.2f} s)")

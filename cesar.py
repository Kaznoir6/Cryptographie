#!/usr/bin/env python3
"""Chiffre de César — TD 1.

Usage :
    python3 cesar.py chiffrer  3 "BONJOUR"
    python3 cesar.py dechiffrer 3 "ERQMRXU"
    python3 cesar.py force-brute message_intercepte.txt

À COMPLÉTER : les fonctions decaler() et force_brute().
"""
import sys

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def decaler(texte: str, cle: int) -> str:
    """Décale chaque lettre majuscule de `cle` positions (modulo 26).
    Les autres caractères (espaces, chiffres, ponctuation) sont conservés."""
    resultat = []
    for c in texte.upper():
        if c in ALPHABET:
            # TODO : calculer la nouvelle position de la lettre (indice : ALPHABET.index(c))
            raise NotImplementedError("À compléter")
        else:
            resultat.append(c)
    return "".join(resultat)


def force_brute(texte: str) -> None:
    """Affiche les 25 déchiffrements possibles (une ligne par clé)."""
    # TODO : une boucle sur les clés 1 à 25, en réutilisant decaler()
    raise NotImplementedError("À compléter")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    action = sys.argv[1]
    if action == "chiffrer":
        print(decaler(sys.argv[3], int(sys.argv[2])))
    elif action == "dechiffrer":
        print(decaler(sys.argv[3], -int(sys.argv[2])))
    elif action == "force-brute":
        with open(sys.argv[2], encoding="utf-8") as f:
            force_brute(f.read().strip())
    else:
        sys.exit(__doc__)

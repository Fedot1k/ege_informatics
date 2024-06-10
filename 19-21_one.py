from functools import lru_cache

def moves(s):
    return s + 3, s * 2

@lru_cache(maxsize=100000)

def game(s):
    if s >= 33:
        return 'W'
    if any(game(m) == 'W' for m in moves(s)): return 'P1'
    if all(game(m) == 'P1' for m in moves(s)): return 'B1'
    if any(game(m) == 'B1' for m in moves(s)): return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(s)): return 'B2'

for s in range(1, 33):
    if game(s) == 'B2':
        print(s, game(s))
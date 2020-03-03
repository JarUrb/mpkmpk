from math import sqrt

import przystanki

mapowanie = {}

for mpk in przystanki.MPK_LODZ_PL:
    szer_mpk = mpk[1]
    dlug_mpk = mpk[2]
    tymczasowa_lista = []
    for rozklady in przystanki.ROZKLADY_LODZ_PL:
        szer_rozklady = rozklady[1]
        dlug_rozklady = rozklady[2]
        odleglosc = sqrt((szer_mpk - szer_rozklady) ** 2 + (dlug_mpk - dlug_rozklady) ** 2)
        tymczasowa_lista.append((rozklady, odleglosc))
    mapowanie[mpk] = min(tymczasowa_lista, key=lambda x: x[1])[0]

print('MAPPING = {')
for a, b in sorted(mapowanie.items(), key=lambda x: x[0][0]):
    print('    {}: {},'.format(int(a[0]), b[0]))
print('}')

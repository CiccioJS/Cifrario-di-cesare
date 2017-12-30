def cripto(testo_chiaro, chiave):
    testo_criptato = ''
    chiave_copia = chiave
    for char in testo_chiaro:
        car = ord(char)
        car += chiave
        if car >= 123:
            chiave_copia = 97 + (car - 123)
            car = chiave_copia
            a = chr(car)
            testo_criptato += a
        else:
            a = chr(car)
            testo_criptato += a
    return testo_criptato

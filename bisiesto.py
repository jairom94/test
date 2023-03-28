def isBisiesto(year):
    if ((year % 4) == 0 or (year % 400) == 0 ) and (year % 100) != 0:
        return True
    return False
    
print('Año Bisiesto' if isBisiesto(2004) else 'No es un año bisiesto')

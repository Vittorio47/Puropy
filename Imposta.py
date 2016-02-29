#price = eval (input ("inserisci un valore per il prezzo: "))
#vat = eval (input ("inserisci un valore per tassazione: "))

def calculate_price_with_vat(price, vat): # imposta la funzione con price e vat
    return price * (100 + vat) / 100        # ritorna il calcolo

print()                                     #crea una riga vuota
print('risultato del prezzo + la tassa:')    
print(calculate_price_with_vat(800, 22))    # stampa il risultato della funzione con i valori immessi 





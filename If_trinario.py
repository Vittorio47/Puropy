ordine_totale =1000
sconto = 25 if ordine_totale > 100 else 0
print (('ordine totale:'), (ordine_totale)) 
print (('sconto :'), (sconto))
print (('prezzo netto:'), (ordine_totale)-(sconto))
# con python 3.5.1
valore = input("come ti chiami? ".title())
# print (valore)
print("ciao ".capitalize() + (valore.capitalize()) + (" ,piacere di conoserti"))
print("vorrei sapere di più su di te...")
alfa = input("dove abiti? ")
print("sai che a " + (alfa) + (" ci sono stato?, è una città molto bella!"))
beta = input("sei sposato? ")
if beta == "si":
    print("complimenti!".upper())
elif beta == "no":
    print("c'è sempre tempo...")
elif beta == "fidanzato":
    print("sei ancora in tempo a salvarti!")
else:
    print("uomo libero!")
print("ora ti devo salutare, arrivederci presto")

# numero = eval (input ("inserisci un valore numerico:"))
# print (numero*numero)

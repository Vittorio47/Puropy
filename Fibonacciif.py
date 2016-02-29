def fib (n):
	"""stampa qui sotto una lista contenente la serie di fibonacci fino a 'n':  """
	a, b = 0, 1
	while a < n:
		print (a, end=' ')
		a, b = b, a+b
	
	#print()

print(fib.__doc__) 
print() #per creare una riga vuota

fib(500) #ora chiamo la funzione 'fib' mettendo tra parentesi il valore che assegno a'n'

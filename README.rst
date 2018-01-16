Bestemmie.org Python API
=============================

Simple Bestemmie.org rest api wrapper

----

To install ::
	pip install bestemmie
	
Function :

	-Get all bestemmie
		all(*)
			Option: Bool (True/False) for uppercase o lowercase. Default: False
	-Get random bestemmia
		bestemmia(*)
			Option: Bool (True/False) for uppercase o lowercase. Default: False
	-Get bestemmia
		bestemmia_id(int id)
		

Use ::
	import bestemmie as b
	
	all=b.all()
	print(all) # print all bestemmie in uppercase
	
	all=b.all(True)
	print(all) # print all bestemmie in lowercase
	
	b.bestemmia_id(12)
	print bestemmia whith the passed id
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
KeyboardInterrupt
>>> thisdict={
	F:ord("F"),
	G:ord("G"),
	H:ord("H"),
	I:ord("I"),
	J:ord("J"),
	K:ord("K"),
	L:ord("L"),
	M:ord("M"),
	N:ord("N"),
	O:ord("O"),
	P:ord("P"),
	}
Traceback (most recent call last):
  File "<pyshell#4>", line 2, in <module>
    F:ord("F"),
NameError: name 'F' is not defined
>>> thisdict={
	"F":ord("F"),
	"G":ord("G"),
	"H":ord("H"),
	"I":ord("I"),
	"J":ord("J"),
	"K":ord("K"),
	"L":ord("L"),
	"M":ord("M"),
	"N":ord("N"),
	"O":ord("O"),
	"P":ord("P"),
	}
>>> print(thisdict)
{'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80}
>>> 

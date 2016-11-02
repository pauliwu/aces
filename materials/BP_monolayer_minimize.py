from aces.materials.POSCAR import structure as material
class structure(material):
	def getPOSCAR(self):
		return """ACES POSCAR                             
   1.00000000000000     
     4.6181507140501452    0.0000000000000000    0.0000000000000000
     0.0000000000000000    3.2990243696272366    0.0000000000000000
     0.0000000000000000    0.0000000000000000   19.9966745051477623
   P 
     4
Direct
  0.0890026531505678  0.2500000000000000  0.4473684554803318
  0.4109973468498373  0.7500000000000000  0.4473684554803318
  0.5890026531501628  0.7500000000000000  0.5526315445196681
  0.9109973468498372  0.2500000000000000  0.5526315445196681
"""
			
		
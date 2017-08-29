numeros = ['As','2','3','4','5','6','7','8','9','10','J','Q','K']
naipes=['ouros', 'paus','copas','espadas']

class Carta:
	def __init__(self, a, b):
		if(a in numeros and b in naipes ):
			self.numero = a		
			self.naipe = b
		if(a in range(len(numeros)) and b in range(len(naipes))):
			self.numero = numeros[a]
			self.naipes = naipes[b]
		else:
			raise
class Mao:
	def __init__(self,a):
		numero_de_cartas = a
	cartas = [0.0 for i in range(numero_de_cartas-1)]
	def mostrar():
		for i in self.cartas:
			print i.numero+'de'+ i.naipe
			
baralho = mao(52)
for i in numeros:
	for j in naipes:
		baralho.cartas[k] = Carta(i,j)
baralho.mostrar()

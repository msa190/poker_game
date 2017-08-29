naipes=['ouros', 'paus','copas','espadas']
numeros = ['As','2','3','4','5','6','7','8','9','10','J','Q','K']
class Carta:
	def __init__(self, a, b):
		self.numero = numeros[a]		
		self.naipe = naipes[b]

class Mao:
	def __init__(self,a):
		numero_de_cartas = a
	cartas = [0.0 for i in range(numero_de_cartas-1)]
	def mostrar():
		for i in self.cartas:
			print i.numero+'de'+ i.naipe
baralho = mao(52)
for k,i in enumerate(numeros):
	for j in naipes:
		baralho.cartas[k] = Carta(i,j)
baralho.mostrar()

numeros = ['As','2','3','4','5','6','7','8','9','10','J','Q','K']
naipes=['ouros', 'paus','copas','espadas']

class Carta:
	def __init__(self, a, b):
		if(a in numeros and b in naipes ):
			self.numero = a		
			self.naipe = b
		if(a in range(len(numeros)) and b in range(len(naipes))):
			self.numero = numeros[a]
			self.naipe = naipes[b]
class Mao(list):
	def __init__(self,a):
		numeroDeCartas = a
	
	#cartas = [Carta('foo','foo') for i in range(52)]
	cartas = []
	def mostrar(self):
		for i in self.cartas:
			print i.numero+' de '+ i.naipe
			
baralho = Mao(52)
for k,i in enumerate(numeros):
	for j in naipes:
		baralho.cartas.append(Carta(i,j))
baralho.mostrar()
#mao_um = Mao(3)
#mao_um.cartas[0] = Carta(1,1)
#mao_um.cartas[1] = Carta(1,2)
#mao_um.cartas[2] = Carta(1,3)
#mao_um.cartas[3] = Carta(1,4)
#mao_um.mostrar()

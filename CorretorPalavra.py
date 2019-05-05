db = open("db.txt","r").read().split("\n")
import operator
def main ():
	palavra = raw_input("palavra :")
	pla = {}
	for x in db:
		if len(x) == len(palavra):
			temp = 0
			errado = 0
			acerto = 0
			for letra in x:
				if letra == palavra[temp]:
					acerto += 1
				else:
					errado += 1
				temp += 1
			
			if errado < acerto:
				pla.update({x:str(acerto-errado)})
			
	try:
		melhor = max(pla.iteritems(), key=operator.itemgetter(1))[0]
	except:
		melhor = palavra
	print "voce quis dizer : "+melhor
main()

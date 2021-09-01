from string import maketrans
import string

#create source alphabet
alp = list(string.ascii_lowercase)
ALP = list(string.ascii_uppercase)
intab = ''.join(alp+ALP)

#create destination alphabet
def outab(key):
	a = map(lambda x: alp[(alp.index(x)+key)%26], alp)
	b = map(lambda x: ALP[(ALP.index(x)+key)%26], ALP)
	return ''.join(a+b)

if __name__ == '__main__':
	messg = open('cipher.txt','r').read()
	for key in range(1, 25):
		print('Key = %d'%key + ' ='*30)
		print(messg.translate(maketrans(intab, outab(key)))+'\n')
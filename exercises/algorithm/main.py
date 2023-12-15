from caesars_cipher import CaesarsCipher
from file import file
from binary_search import binary_search


filename_r = 'data/data.txt'
filename_cipher = 'data/cipher.txt'
filename_decipher = 'data/decipher.txt'


"""
    Cifra de Cezar
    Leitura e escrita em arquivo
"""

print('Cifra de Cezar:')

f = file()
print(' Leitura do texto principal')
text = f.reader(filename_r)

key = 5
delimiter = [32, 126]
cc = CaesarsCipher()


print(' Cifrando o texto')
t = list(map(lambda x: cc.cipher(x, key, delimiter), text))

f.writer(filename_cipher, t)

text = f.reader(filename_cipher)

print(' Decifrando o texto')
t = list(map(lambda x: cc.decipher(x, key, delimiter), text))

f.writer(filename_decipher, t)


"""
    Busca Binaria
"""

arr = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9, 10]
number = 5
v = binary_search(arr, number)

print('Busca Binaria: ')
print(' Numero: ', number)
print(' Resultado da busca: ', v)



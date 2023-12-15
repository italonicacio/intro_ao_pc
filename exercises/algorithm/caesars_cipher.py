import doctest
from string import *


class CaesarsCipher:

    def cipher(self, phrase, key = 0, delimiter=None):

        aux = list(phrase)
       
        if delimiter:
            min_value = delimiter[0] - 1
            max_value = delimiter[1] 

        lim = max_value - min_value + 1
    
        for i in range(len(aux)):
            number_char = ord(aux[i]) + key - min_value

       
            if delimiter:
                    # number_char %= max_value
                    number_char %= lim

            number_char += min_value   
            aux[i] = chr(number_char)


        return ''.join(aux)
  

    def decipher(self, phrase, key = 0, delimiter=None):
  
        aux = list(phrase)

        if delimiter:
            min_value = delimiter[0] - 1
            max_value = delimiter[1] 
        
        lim = max_value - min_value + 1

        for i in range(len(aux)):
            number_char = ord(aux[i]) - key - min_value
            
            if delimiter:
                number_char %= lim
    
                
            number_char += min_value            
            
            aux[i] = chr(number_char)

        
        return ''.join(aux)





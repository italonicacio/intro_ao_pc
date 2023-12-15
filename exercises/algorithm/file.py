
class file:

    def reader(self, filename):
        f = open(filename)
        aux = f.readlines()
        aux = map(lambda x: x.rstrip(), aux)
        f.close
        return list(aux)
        


    def writer(self, filename, to_save):
        f = open(filename, 'w')
        text_to_save = map(lambda x: x+'\n', to_save)
        
        f.writelines(text_to_save)
        f.close()

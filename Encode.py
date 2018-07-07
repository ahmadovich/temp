
import codecs
blocksize = 500

def fixenc():
    
    with open(r'C:\Users\ahmad\Desktop\s.txt','r',encoding='cp1256') as infile:
        with open(r'C:\Users\ahmad\Desktop\a.txt','w',encoding = 'utf-8') as outfile:
            line = infile.read(1)
            while line:
                outfile.write(line)
                line=infile.read(blocksize)
    return
        
if __name__ == '__main__' : fixenc()
        

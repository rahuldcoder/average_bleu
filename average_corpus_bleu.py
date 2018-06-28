import nltk
from nltk.translate.bleu_score import sentence_bleu
import sys
def readfile(filename):
    
    textlist = list()
    
    with open (filename,'r') as filehandle:
    
        textlist = filehandle.readlines()
        
        return textlist


def main():
    
    reference = readfile(sys.argv[1])
    system =  readfile(sys.argv[2])
  
    print( nltk.translate.bleu_score.sentence_bleu(reference[0], system[0]))
    print('Reference Sentence : '+ reference[0])
    print('System Sentence : '+ system[0] )
    #nltk.translate.bleu_score.sentence_bleu(references, hypothesis)

if __name__ == '__main__':
    main()
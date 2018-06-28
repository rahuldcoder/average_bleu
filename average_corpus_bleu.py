import nltk
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction
import sys
def readfile(filename):
    
    textlist = list()
    lines = list()

    with open (filename,'r') as filehandle:
    
        textlist = filehandle.readlines()
        for line in textlist:
            lines.append(line.split())
        
        return lines

def average_bleu(sen_bleu,num_of_sen):
    
    return (sum(sen_bleu)/num_of_sen)


def main():
    
    reference = readfile(sys.argv[1])
    system =  readfile(sys.argv[2])

  #  print(reference)

  #  print('____________________________________________________________________________________________________'+'\n\n\n\n\n\n')
  #  print(system)

    num_of_sen = len(reference)

    print(num_of_sen)

    sen_bleu = list()
      
    for i in range(num_of_sen):

        sen_bleu.append(nltk.translate.bleu_score.sentence_bleu([reference[i]], system[i],smoothing_function=SmoothingFunction().method5))
        print(sen_bleu[i] )
 

    print( average_bleu(sen_bleu,num_of_sen) )    
      

if __name__ == '__main__':
    main()
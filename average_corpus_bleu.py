import nltk
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction
import sys
def readfile(filename):
    
    textlist = list()
    lines = list()

    with open (filename,'r') as filehandle:
        
        lines =list()
        textlist = filehandle.readlines()
        for line in textlist:
            for word in line.split():
                lines.append(word)
        '''
        for line in textlist:
            lines.append(line.split())
        
        return lines
        '''    
        return lines
def average_bleu(sen_bleu,num_of_sen):
    
    return (sum(sen_bleu)/num_of_sen)

def calcBleu(ref,hyp):
    smoothing = SmoothingFunction()
    bleuScore = nltk.translate.bleu_score.corpus_bleu(ref,hyp,smoothing_function=smoothing.method5)
    return bleuScore 

def main():
    
    reference = readfile(sys.argv[1])
    system =  readfile(sys.argv[2])

  

    num_of_sen = len(reference)

  

    sen_bleu = list()
      
    for i in range(num_of_sen):

        sen_bleu.append(nltk.translate.bleu_score.sentence_bleu([reference[i]], system[i],smoothing_function=SmoothingFunction().method5))
       # print(sen_bleu[i] )
 

  #  print( 'Average Sentence Bleu '+ str(average_bleu(sen_bleu,num_of_sen) ) ) 

    print('Corpus Bleu')
    score = nltk.translate.bleu_score.corpus_bleu([[reference]],[system],smoothing_function=SmoothingFunction().method5) 

    print(score)  

if __name__ == '__main__':
    main()
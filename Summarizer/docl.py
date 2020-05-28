#importing the required libraries
import sumy
from sumy.parsers.plaintext import PlaintextParser #for parsing our text file
from sumy.nlp.tokenizers import Tokenizer # to tokenize into words for the para that we sent
from sumy.summarizers.lex_rank import  LexRankSummarizer #this is graph based summarizer
#reading the content i.e para from mldoc.txt in read mode

file1=open("mldoc.txt",'r')

doc=file1.readline()#reading every line...
#processing(i.e parsing) the text in a way that the alogorithm can understand by the function from_string
parser=PlaintextParser.from_string(doc,Tokenizer("english"))
'''
LEXRANK ALGORITHM:
It is an unsupervised approach to text summarization based on graph-based 
centrality scoring of sentences.
The main idea is that sentencse recommend other similar sentences to the
reader.
Thus if one sentence is very similar to many others,it will likely be a sentence of 
great importance.
'''
summarizer=LexRankSummarizer()

#The second argument in the summarizer constructor is the NUMBER OF SENTENCES REQUIRED in the summary.

summary=summarizer(parser.document,3)
#printing sentence by sentence of the summary
for sentence in summary:
    print(sentence)

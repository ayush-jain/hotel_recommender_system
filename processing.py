import re
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk

def preprocessing():

	lmtzr = WordNetLemmatizer()
	stop= stopwords.words('english')
	file = open('input')
	file1= open('preprocess1.txt','wb')
	a='.'

	while a != '':
		file.readline()
		file.readline()
		file.readline()
		a=file.readline().split(':')[1]

		b=re.findall(r'\w+', a,flags = re.UNICODE | re.LOCALE) #punctuation removal
		for i in b: 
			if i not in stop:  #stop word removal
				k=lmtzr.lemmatize(i) #stemming
				temp=nltk.pos_tag(nltk.word_tokenize(k))
				#print temp,k
				if(temp[0][1]!='CC' and temp[0][1]!='DT' and temp[0][1]!='MD' and temp[0][1]!='RB' and temp[0][1]!='PRP'and temp[0][1]!='EX'):
					#print temp
					file1.write(k)	
					file1.write(" ")	
		file1.write("\n")
		if(file.readline()==''):
			break
	#file1.write(a)
	file1.close()

#preprocessing()

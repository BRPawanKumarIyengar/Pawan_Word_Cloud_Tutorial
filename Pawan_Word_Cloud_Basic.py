#We import WordCloud and STOPWORDS
from wordcloud import WordCloud
from wordcloud import STOPWORDS


#We create a function to create a word Cloud
def Pawan_Word_Cloud(File_Path):

#We read from specified text file
	with open(File_Path,'r') as Read_File:
		File_Text = Read_File.read()

#We initialize the stop words
	STPWRD = set(STOPWORDS)
	
#We set the parameters to generate the Word Cloud	
	WrdCld = WordCloud(background_color = 'white',max_words = 50, stopwords=STPWRD)
	
#Finally we Generate the word Cloud
	WrdCld.generate(File_Text)

#we sabe the created file onto a picture file	
	WrdCld.to_file('mahan.png')
	
Pawan_Word_Cloud('C:/Users/brpaw/Desktop/txt files/ko.txt')

	




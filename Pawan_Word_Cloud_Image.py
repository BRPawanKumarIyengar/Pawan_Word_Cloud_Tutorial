#We import WordCloud and STOPWORDS
from wordcloud import WordCloud
from wordcloud import STOPWORDS

#Here we import pyplot to use a figure as a cloud
import matplotlib.pyplot as plt

#We import numpy  to create an array of images
import numpy as numpy_instance

#We import Image from PIL
from PIL import Image

#We create a function to create a word Cloud
def Pawan_Word_Cloud(File_Path):

#We read from specified text file
	with open(File_Path,'r') as Read_File:
		File_Text = Read_File.read()

#We initialize the stop words
	STPWRD = set(STOPWORDS)
	
	Pawan_Image_Show = numpy_instance.array(Image.open('Titli_the_Butterfly.PNG'))
	
#We set the parameters to generate the Word Cloud	
	WrdCld = WordCloud(max_font_size = 50, background_color = 'white', max_words = 100, mask = Pawan_Image_Show, stopwords=STPWRD)
	
#Finally we Generate the word Cloud
	WrdCld.generate(File_Text)
	
#We now use Pyplot to display the figure 
	plt.figure(figsize = (8, 12), facecolor = 'black') # we set figure size and background color
	plt.imshow(WrdCld) # uses image to show wordcloud
	plt.axis("off") 
	plt.tight_layout(pad = 0) 
	plt.show()
	
#we sabe the created file onto a picture file	
	WrdCld.to_file('mahaan.png')
	
Pawan_Word_Cloud('C:/Users/brpaw/Desktop/txt files/ko.txt')
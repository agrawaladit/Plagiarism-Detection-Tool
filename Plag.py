import nltk
from googlesearch import search
import os


# import urllib.request
from urllib.request import Request, urlopen
import urllib.parse
import re
nltk.download('stopwords')
from nltk.corpus import wordnet 

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")


import nltk.data
import io
from tkinter import * 
import tkinter.filedialog
import sys
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from bs4 import BeautifulSoup
from bs4.element import Comment

 



def master():
        a=[]
        global fname1
        global fname2
        fp1 = open(fname1)
        data1 = fp1.read()
        
        values={'s': 'basics','submit':'search'}
        data=urllib.parse.urlencode(values)
        data=data.encode('utf-8')
        # to search 
        query = (data1);
        for j in search(query, tld="co.in", num=10,stop=3, pause=2): 
                print(j)
                try:
                        req=urllib.request.Request(j,data,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
                        resp = urllib.request.urlopen(req)
                        html = resp.read()
                except:
                        print ("fail")
                        continue


                def tag_visible(element):
                        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]','header id']:
                                return False
                        if isinstance(element, Comment):
                                return False
                        return True

                def text_from_html(body):
                        global visible_texts
                        soup = BeautifulSoup(body, 'html.parser')
                        texts = soup.findAll(text=True)
                        visible_texts = filter(tag_visible,texts)  
                        return u" ".join(t.strip() for t in visible_texts)
                # print (text_from_html(html))
                # for eachP in (text_from_html(html)):
                fileout=open(fname2,"w",encoding="utf-8")
                
                fileout.write(text_from_html(html))
                fileout.close()


                def splitSen():
                        global a
                        global b
                        global fname1
                        global fname2
                        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
                        fp1 = open(fname1,encoding="utf-8")
                        fp2 = open(fname2,encoding="utf-8")
                        data1 = fp1.read()
                        data2 = fp2.read()
                        a=(tokenizer.tokenize(data1))
                        b=(tokenizer.tokenize(data2))
                        # print("Sentence 1: ")

                def compare():
                        global flag
                        global a
                        global b
                        global common
                        global common1
                        global notcommon
                        global notcommonU
                        global common_list
                        global synonyms
                        global fname3
                        global filtered_sentence1
                        global filtered_sentence2
                        global count
                        global count1

                        tokenizer = RegexpTokenizer(r'\w+')  
                        stop_words = set(stopwords.words('english'))

                        # print("\nCopied Sentences:\n")
                        fp3 = open(fname3,"a")
                        for i in range(len(a)):
                                word_tokens = tokenizer.tokenize(a[i])
                                for y in word_tokens:
                                        if y not in stop_words:
                                                count.append(y)

                                for j in range(len(b)):
                                        word_tokens1 = tokenizer.tokenize(a[i])
                                        word_tokens2 = tokenizer.tokenize(b[j])

                                        for w in word_tokens1:
                                                if w not in stop_words:
                                                        filtered_sentence1.append(w)

                                        for x in word_tokens2:
                                                if x not in stop_words:
                                                        filtered_sentence2.append(x)

                                        common = set(filtered_sentence1) & set(filtered_sentence2)
                                        common_words = ", ".join(common)
                                        if len(common)/len(filtered_sentence1) > 0.7 :
                                                for word in set(filtered_sentence1): 
                                                        count1[word] = count1.get(word, 0) + 1
                                                for word in set(filtered_sentence2): 
                                                        count1[word] = count1.get(word, 0) + 1

                                                for word in count1:
                                                        if count1[word] == 1 and word in filtered_sentence1:
                                                                notcommonU.append(word)

                                                # for word in set(filtered_sentence1) :         
                                                        # notcommonU.remove(word)


                                                for wordM in (notcommonU):
                                                	stemmedword=stemmer.stem(wordM)
                                                	for syn in wordnet.synsets(stemmedword): 
                                                		for l in syn.lemmas():
                                                			if l.name() not in synonyms: 
                                                				synonyms.append(l.name()) 
                                                	# print(set(synonyms)) 
                                                	for wordsP in filtered_sentence2 :
                                                		stemmedword2=stemmer.stem(wordsP)              
                                                		# print(stemmedword2)
                                                		if stemmedword2 in set(synonyms):
                                                			# print(wordsP)
                                                			if wordsP not in common1:
                                                				common1.append(wordsP)
                                                				common_list.append(wordM)

                                        if len(common)/len(filtered_sentence1) > 0.7:
                                                common_list.extend(common)
                                                fp3.write(",".join(common_list))
                                                fp3.write("//////")

                                        # print('****************************')
                                        # print("Sentence 1: "+ str(a[i]))
                                        # print("Sentence 2: "+ str(b[j]))
                                        # print('----------------------------')
                                        # print("Word Tokens 1: "+ str(word_tokens1))
                                        # print("Word Tokens 2: "+ str(word_tokens2))
                                        # print('----------------------------')
                                        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
                                        # print("Filtered Tokens 1: "+ str(filtered_sentence1).translate(non_bmp_map))
                                        # print("Filtered Tokens 2: "+ str(filtered_sentence2).translate(non_bmp_map))
                                        # print('----------------------------')
                                        # print("Common words are: " + str(common))
                                        # print('****************************')
                                        filtered_sentence1 = []
                                        filtered_sentence2 = []
                                        count1 = {}


                        
        # DISPLAY OF FINAL OUTPUT

                def perCal():
                        global count
                        print("common_list is :" + str(common_list))
                        print("notcommon list is : " + str(notcommonU))
                        print("replaced :" + str(common1))
                        # print("synonyms replaced are:",+ str(common1))
                        per = (float(len(common_list)/len(count)))*100.00
                        print("\nPercentage copied is",format(per, '.2f'))
                        

        #DISPLAY THE COPIED CONTENT 
                def display():
                    global fname1 
                    global common_list
                    file_path=fname1
                    while not os.path.exists(file_path):
                        file_path = input("The path does not exists, enter again the file path: ")
                    with open(file_path, mode='rt', encoding='utf-8') as f:
                        text = f.read()
                    # search_wordA = "database is oraganised collection of data"
                    for search_word in common_list:
                        if search_word in text:
                            # print()
                            print(text.replace(search_word, '\033[44;33m{}\033[m'.format(search_word)))

                        
                splitSen()
                compare()
                perCal()
                display()



def browse_file1():
        global fname1
        fname1 = tkinter.filedialog.askopenfilename(filetypes = (("Template files", "*.txt"), ("All files", "*")))

# def browse_file2():
        # global fname2
        # fname2 = tkinter.filedialog.askopenfilename(filetypes = (("Template files", "*.txt"), ("All files", "*")))

def browse_file3():
        global fname3
        fname3 = tkinter.filedialog.askopenfilename(filetypes = (("Template files", "*.txt"), ("All files", "*")))


#UI

fname1 = ""
fname2 = '/Users/nishigandhagawande/Desktop/FYPRO/text2.txt'
fname3 = ""
if sys.version_info[0] < 3:
   import tkinter as Tk
else:
   import tkinter as Tk

root = Tk.Tk()
root.wm_title("Browser")
broButton = Tk.Button(master = root, text = 'Select First File', width = 20, command=browse_file1)
broButton.pack(side=Tk.LEFT, padx = 2, pady=2)
# broButton = Tk.Button(master = root, text = 'Select Second File', width = 20, command=browse_file2)
# broButton.pack(side=Tk.LEFT, padx = 5, pady=5)
broButton = Tk.Button(master = root, text = 'Output File', width = 20, command=browse_file3)
broButton.pack(side=Tk.LEFT, padx = 8, pady=8)
broButton = Tk.Button(master = root, text = 'Close', width = 20, command=root.quit)
broButton.pack(side=Tk.BOTTOM, padx = 8, pady=100)
Tk.mainloop()



a = []
b = []
count = []
common = []
common1=[]
notcommon=[]
notcommonU=[]
common_list = []
filtered_sentence1 = []
filtered_sentence2 = []
synonyms = [] 

master()

from urllib.request import urlopen

def readFileURLString(ur1):
    data = urlopen(ur1)
    html_data = data.read()
    encoding = data.headers.get_content_charset('utf-8')
    decoded_html = html_data.decode(encoding)
    return decoded_html

data_str = readFileURLString('')
print(data_str)
'''
--> pick 5 books (gutenberg project, plain text)
---> read 4 of the 5 books (clean beg. and end)
-- wrute each of the four books into a separate file, automate this process as much as possible
--> the 5th book title keep in mind but dont read/write it

using try-except block to do the following:
--> read number of words of the story inly
--> find the frequence of each word in the file 
--> number of paragraphs 
--> number of sentences 
--> length of the smallest and longest woord, average length 
--> most common vowel 
--> average punction marks for every 100 sentences 
'''
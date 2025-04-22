# from urllib.request import urlopen

# def readFileURLString(ur1):
#     data = urlopen(ur1)
#     html_data = data.read()
#     encoding = data.headers.get_content_charset('utf-8')
#     decoded_html = html_data.decode(encoding)
#     return decoded_html

# data_str = readFileURLString('')
# print(data_str)
from urllib.request import urlopen

def readFileURLString(ur1):
    try:
        data = urlopen(ur1)
        html_data = data.read()
        encoding = data.headers.get_content_charset('utf-8')
        decoded_html = html_data.decode(encoding)
        return decoded_html
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# Example of a valid URL to a Project Gutenberg book
url = "http://www.gutenberg.org/files/75869/75869-0.txt"  # Replace with your desired URL
data_str = readFileURLString(url)
if data_str:
    print("Data successfully fetched")
else:
    print("Failed to fetch data")
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
# book1 = open('', 'r')
# book2 = open('', 'r')
# book3 = open('', 'r')
# book4 = open('', 'r')
# book5 = open('', 'r')
# try:
# def count(book):
try:
    book1 = open('75869.txt.utf-8', 'r')
    # book2 = open('', 'r')
    # book3 = open('', 'r')
    # book4 = open('', 'r')
    
    count_words = 0
    d_freq = {}
    d_vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'y': 0}
    count_sentec = 0
    count_parag = 0
    punct_marks = 0
    smallest = None
    longest = None
    words = []
    sum_w = 0
    max_count = 0

    for line in book1:
        line = line.strip()
    
        line_words = line.split()
        words.extend(line_words)
        count_words += len(line_words)
        
        for word in line_words:
            d_freq[word] = d_freq.get(word, 0) + 1
            

            if smallest is None or len(word) < len(smallest):
                smallest = word
            if longest is None or len(word) > len(longest):
                longest = word
            sum_w += len(word)

            for char in word.lower():
                if char in d_vowels:
                    d_vowels[char] += 1
                if char in ['.', ',', ':', ';', '?', '!']:
                    punct_marks += 1
        

            # for i in ['a', 'e', 'i', 'o', 'u', 'y']:
            #     if ['a', 'e', 'i', 'o', 'u', 'y'] in word:
            #         d_vowels[i] = d_vowels.get(i, 0) + 1
            

            # for i in ['a', 'e', 'i', 'o', 'u', 'y']:
            #     if ['a', 'e', 'i', 'o', 'u', 'y'] in word:
            #         d_vowels[i] = d_vowels.get(i, 0) + 1

        average = sum_w / len(words)
        for vowel, count in d_vowels.items():
            if count > max_count:
                most_common_vowel = vowel
                max_count = count

        if '.' in line or '?' in line or '!' in line:
            count_sentec += 1

        if not line:
            count_parag += 1 
        
        # if ['.', ',',':', ';', '?', '!'] in line:
        #     punct_marks += 1
        recc = count_sentec // 100
    if recc != 0:
        average_marks = round(punct_marks / recc, 2)
    else:
        average_marks = 0  

    # average word length
    average = sum(len(word) for word in words) / len(words) if words else 0
except FileNotFoundError:
    print('file not found')

except ZeroDivisionError:

    print('tried to divide by 0')

print(count_words)
print(average_marks)
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer 

ps = PorterStemmer() 

example_sent = "one of the most dangerous route had no lighting and illuminate illumination, terrible quality of roads, no light at all and full of holes"
  
stop_words = set(stopwords.words('english')) 
  
word_tokens = word_tokenize(example_sent) 
  
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
filtered_sentence = [] 
root_word = []
  
for w in word_tokens: 
    if w not in stop_words: 
        filtered_sentence.append(w) 
        
for w in filtered_sentence: 
    print(w, " : ", ps.stem(w)) 
    root_word.append(ps.stem(w))

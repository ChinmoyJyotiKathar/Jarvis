import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


#train_text = state_union.raw("2005-GWBush.txt")
#sample_text = state_union.raw("2006-GWBush.txt")
train_text = "Hello chinmoy, I am a robot. I am from the future. I drive vehicles."
sample_text = "Hello Humans! I am from the future.I drive rockets."
#custom_sent_tokenizer = PunktSentenceTokenizer(train_text) #A

tokenized = PunktSentenceTokenizer.tokenize(sample_text)   #B

def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))


process_content()
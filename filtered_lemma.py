from nltk import everygrams

def filtered_lemma_list(df, stopwords, ngram_len):
    
    filtered_lemmas = list(df.loc[df.xpos.isin(['JJ','JJR','JJS','NN', 
                                                  'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN','VBP',
                                                 'VBZ'])].lemma)
    
    filtered_lemmas = [word.lower() for word in filtered_lemmas if len(word)>2]

    filtered_lemma = [word for word in filtered_lemmas if word not in stopwords]
    n_gram = list(everygrams(filtered_lemma, max_len=ngram_len))
    
    return n_gram
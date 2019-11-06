def doc_list(df, stop):
    doc_list = list(df.loc[df.xpos.isin(['JJ','JJR','JJS','NN', 
                                        'NNS', 'NNP', 'NNPS', 
                                        'VB', 'VBD', 'VBG', 
                                        'VBN','VBP','VBZ'])].document)
    
    lemma_list = list(df.loc[df.xpos.isin(['JJ','JJR','JJS','NN', 
                                            'NNS', 'NNP', 'NNPS', 
                                            'VB', 'VBD', 'VBG', 
                                            'VBN','VBP','VBZ'])].lemma)
    docs = list(zip(doc_list,lemma_list))
    filtered = [(d,w.lower()) for d,w in docs if len(w)>2]
    filtered = [(d,w) for d,w in filtered if w not in stop]
    
    doc_dict = {}
    
    for d,l in filtered:
        if d not in doc_dict.keys():
            doc_dict[d] = [l]
        else:
            doc_dict[d].append(l)
            
    return(list(doc_dict.values()))

import stanfordnlp
import pandas as pd
nlp = stanfordnlp.Pipeline()

def word_feature_df(story_list):    

    name_vars = []
    for number in list(range(0,len(story_list))):
        name_vars.append("story_{}".format(number))

    vars_and_stories_dict = dict(zip(name_vars, story_list))

    for key,value in vars_and_stories_dict.items():
        vars_and_stories_dict[key]=nlp(vars_and_stories_dict[key])

    nlp_list = list(vars_and_stories_dict.values())

    df = pd.DataFrame(columns=['word', 'lemma', 'xpos', 'ind', 'gov', 'dependency', 'document'])
    
    for doc in nlp_list:
        word_list = [word.text for sent in doc.sentences for word in sent.words 
                     if word.dependency_relation != 'punct']
        
        lemma_list = [word.lemma for sent in doc.sentences for word in sent.words 
                      if word.dependency_relation != 'punct']
        
        xpos_list = [word.xpos for sent in doc.sentences for word in sent.words 
                     if word.dependency_relation != 'punct']
        
        ind_list = [word.index for sent in doc.sentences for word in sent.words 
                    if word.dependency_relation != 'punct']
        
        gov_list = [word.governor for sent in doc.sentences for word in sent.words 
                    if word.dependency_relation != 'punct']
        
        dep_list = [word.dependency_relation for sent in doc.sentences for word in sent.words 
                    if word.dependency_relation != 'punct']
        
        label_list = ["{}".format(nlp_list.index(doc))]*len(word_list)
        
        vals_list = [word_list, lemma_list, xpos_list, ind_list, gov_list, dep_list, label_list]
        
        col_labels = ['word', 'lemma', 'xpos', 'ind', 'gov', 'dependency', 'document']
        
        colval_dict = dict(zip(col_labels, vals_list))
        
        df_new = pd.DataFrame(colval_dict)
        
        df = pd.concat([df, df_new], ignore_index=True)
        
    df.ind = df.ind.astype(int)
    
    df["word_index"] = list(range(0,len(df)))
    
    df["gov_ind"] = df.word_index-df.ind+df.gov
    
    ind_list = list(df.loc[df.gov==0].index)
    
    gov_ind_dict = dict(enumerate(df.gov_ind))
    
    for k in gov_ind_dict.keys():
        if k in ind_list:
            gov_ind_dict[k] = k
        
    df.gov_ind = list(gov_ind_dict.values())
    
    gov_word = list(df.iloc[df.gov_ind].word)
    df['gov_word'] = gov_word

    gov_lemma = list(df.iloc[df.gov_ind].lemma)
    df['gov_lemma'] = gov_lemma
    return df
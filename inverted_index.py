# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 19:56:34 2019

@author: Akshay Jaryal
"""

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
import glob
import json

#------------------------------------------------------------------------------
def file_cleaning(lines):
    clean_lines = (re.sub("[^a-zA-Z0-9 @]", " ", lines))
    return clean_lines
#------------------------------------------------------------------------------
def tokenization(sentence):
    new_tokens=[]
    tokens = nltk.word_tokenize(sentence)
    for i in range(len(tokens)):
        if len(tokens[i]) > 1:            
            new_tokens.append(tokens[i])
    return new_tokens
#------------------------------------------------------------------------------
def stopword_removal(tokens):
    filtered_sentence = []
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in tokens if not w in stop_words]
    return filtered_sentence
#------------------------------------------------------------------------------   
def porter_stemming(filtred_tokens): 
    stemmed_tokens=[]
    ps = PorterStemmer()
    for word in filtred_tokens:
        stemmed_tokens.append(ps.stem(word).encode('utf8'))
    return stemmed_tokens
  #------------------------------------------------------------------------------
#def writeToJSONFile(path, fileName, data):
#    filePathNameWExt = './' + path + '/' + fileName + '.json'
#    with open(filePathNameWExt, 'w') as fp:
#        json.dump(data, fp)        
#------------------------------------------------------------------------------

if __name__ == '__main__':
    
    folders = ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian' ,'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']
    
    data_list = []    
    
    inverted_index = {}
    map_dict = {}
    postingslist = []
    document_no = 0
    
    vocab_file = open("Vocabulory_File_1.txt","w")
    
    for i in range(len(folders)):
        folders_path = '20_newsgroups/'+folders[i]+'/*'
#        folders_path = 'Test1/'+folders[i]+'/*'

        files = glob.glob(folders_path)
        print (folders_path)
        for file in files:

            f = open(file, 'r')  
            document_no += 1
            print ('------------------------------------------------------------')
            #writing mapping file
            key_1 = document_no
            value_1 = file
            map_dict[key_1] = value_1
            
            print (file,document_no)
            line = f.readlines()

            i=0
            for w in line:
                i=i+1
                if w.isspace():
                    break
#            print i
            f = open(file, 'r')
            lines = f.readlines()[i:]
            lines=''.join(lines)
            
            lines=lines.strip().lower()
            
            clean_lines = file_cleaning(lines)    
            
            tokens = tokenization(clean_lines)
            
            filtered_tokens = stopword_removal(tokens)    
            #------------------------------------------------------------------
            #prepare vocabulory
            for v in filtered_tokens:
                vocab_file.write('\n'+ v)
            #------------------------------------------------------------------
            stemmed_tokens = porter_stemming(filtered_tokens)
#            print 'length of Stemmed Tokens:', len(stemmed_tokens)
#            print 'Stemmed Tokens:', stemmed_tokens
            
            data_list = stemmed_tokens
            vocabulory = set(data_list)
            vocabulory = list(vocabulory)

            
            for i in range(len(vocabulory)):
                
                if vocabulory[i] in inverted_index:
                    old_value = inverted_index[vocabulory[i]]
                    old_value.append(document_no)
                    inverted_index[vocabulory[i]] = old_value
                else:
                    documents = []
                    documents.append(document_no)
                    inverted_index[vocabulory[i]] = documents
                
                
#==============================================================================
#writing mapping to a json file  
    with open('Mapping_1.json', 'w') as fp1:
        json.dump(map_dict, fp1, indent=2)
#============================================================================== 
#==============================================================================
#writing dictionary to a json file  
    with open('JSON_Data_1.json', 'w') as fp2:
        json.dump(inverted_index, fp2, indent=2)
#============================================================================== 
    vocab_file.close()                    
            
print ('========================================================================')

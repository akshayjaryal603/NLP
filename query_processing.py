# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:11:51 2019

@author: Akshay Jaryal
"""

import json
from pprint import pprint
from nltk.stem.porter import PorterStemmer
#import matplotlib.pyplot as plt

#------------------------------------------------------------------------------
def data_read_from_user():    
    str_1 = input('Enter the value of x: ')
    str_2 = input('Enter the value of y: ')
    
    return str_1, str_2
#------------------------------------------------------------------------------
def porter_stemming(word):     
    ps = PorterStemmer()
    stemmed_token = (ps.stem(word).encode('utf8'))
    
    return stemmed_token   
#------------------------------------------------------------------------------ 
def get_choice_from_user():
    print ('Available options: ')
    print ('1. x OR y')
    print ('2. x AND y')
    print ('3. x AND NOT y')
    print ('4. x OR NOT y')
    print ('5. Skip Pointers (x AND y)')
    selected_option = input('Choose option: ')
    
    return selected_option
#------------------------------------------------------------------------------
def  x_OR_y(x_list, y_list):
    i = 0
    j = 0
    xORy = []
    while i < len(x_list) and j < len(y_list):
        if x_list[i] < y_list[j]:
            xORy.append(x_list)
            i+=1
        elif x_list[i] > y_list[j]:
            xORy.append(y_list)
            j+=1
        else:
            xORy.append(x_list[i])
            i+=1
            j+=1
    while i < len(x_list):
        xORy.append(x_list[i])
        i+=1
    while j < len(y_list):
        xORy.append(y_list[j])
        j+=1
        
    return xORy
#------------------------------------------------------------------------------
def x_AND_y(x_list, y_list):
    i = 0
    j = 0
    xANDy = []
    while i < len(x_list) and j < len(y_list):
        if x_list[i] < y_list[j]:
            xANDy.append(x_list)
            i+=1
        elif y_list[j] < x_list[i]:
            xANDy.append(y_list)
            j+=1
        else:
            xANDy.append(x_list[i])
            j+=1
            i+=1
    while i < len(x_list):
        xANDy.append(x_list[i])
        i+=1
    while j < len(y_list):
        xANDy.append(y_list[j])
        j+=1
            
    return xANDy
#------------------------------------------------------------------------------
def x_AND_NOT_y(x_list, y_list):
    i = 0
    j = 0
    xANDNOTy = []
    while i < len(x_list) and j < len(y_list):
        if x_list[i] < y_list[j]:
            xANDNOTy.append(x_list[i])
            i+=1
        elif y_list[j] < x_list[i]:
            j+=1
        else:
            j+=1
            i+=1            
    while i < len(x_list):
        xANDNOTy.append(x_list[i])
        i+=1
            
    return xANDNOTy
#------------------------------------------------------------------------------
def x_OR_NOT_y(x_list, not_y_list):
    i = 0
    j = 0
    xORNOTy = []
    while i < len(x_list) and j < len(not_y_list):
        if x_list[i] < not_y_list[j]:
            xORNOTy.append(x_list[i])
            i+=1
        elif x_list[i] > not_y_list[j]:
            xORNOTy.append(not_y_list[j])
            j+=1
        else:
            xORNOTy.append(x_list[i])
            i+=1
            j+=1
    while i < len(x_list):
        xORNOTy.append(x_list[i])
        i+=1
    while j < len(not_y_list):
        xORNOTy.append(not_y_list[j])
        j+=1
        
    return xORNOTy
#------------------------------------------------------------------------------ 
def find_mapping(files, map_data):
    print ()
    # print (">>> ",map_data)
    path_with_name = []        
    for i in range(len(files)):
        file_path = map_data.get(str(files[i]))

        # print (file_path)
        name_path = str(files[i])+': '+str(file_path)
        path_with_name.append(name_path)
        
    return path_with_name          
#------------------------------------------------------------------------------
def skip_pointer_x_AND_y(x_list, y_list):
    skip_step = [1,2,3,4,5,6,7,8,9,10]

    dict = {}
    skip_x_list = []
    skip_y_list = []

    for ii in range(len(skip_step)):
        count_x = 0
    
        for ind in range(len(x_list)):
            count_x = count_x + 1
            if count_x%skip_step[ii] == 0:
                skip_x_list.append(x_list[ind])
            
        count_y = 0
        for ind in range(len(y_list)):
            count_y = count_y + 1
            if count_y%skip_step[ii] == 0:
                skip_y_list.append(y_list[ind])
        
        i = 0
        j = 0
    
    
        answer = []
        counter = 0
        while i < len(x_list) and j < len(y_list):
            if x_list[i] == y_list[j]:
                answer.append(x_list[i])
                counter = counter + 1
                i += 1
                j += 1
    
            elif x_list[i] < y_list[j]:
#                print ("i : ",i," skip_step[ii]: ",skip_step[ii],"j is : ",j," lenxlist : ",len(x_list)," lenylist",len(y_list)
                if x_list[i] in skip_x_list and (i+skip_step[ii] < len(x_list)) and x_list[i+skip_step[ii]] <= y_list[j] :
                    while x_list[i] in skip_x_list and (i+skip_step[ii] < len(x_list)) and x_list[i+skip_step[ii]] <= y_list[j] :
                        counter = counter + 1
                        i += skip_step[ii]
                else:
                    i += 1
                    counter = counter + 1
            else :
                if y_list[j] in skip_y_list and (j+skip_step[ii] < len(y_list)) and y_list[j+skip_step[ii]] <= x_list[i]:
                    while y_list[j] in skip_y_list and (j+skip_step[ii] < len(y_list)) and y_list[j+skip_step[ii]] <= x_list[i] :
                        counter = counter + 1
                        j += skip_step[ii]
                else:
                    j += 1
                    counter = counter + 1
             
        dict[skip_step[ii]] = counter
        if len(skip_step) == (ii + 1):
            print (('Number of relevant documents: ', len(answer)))
            res = find_mapping(answer, map_data)
            print ('Documents with the path are given below')
            print ('Format: <Document : Path>','\n')
            for i in res:
                print (i, '\n')
#
#     plt.plot(dict.keys(), dict.values())
#     plt.scatter(dict.keys(), dict.values())
#     plt.xlabel('Skip-Step')
#     plt.ylabel('No. of comparisions')
#     plt.title('Skip Pointer vs No of comparisions')
#     plt.grid(True)
# #    plt.savefig("SkipPointer_active_abort.png")
#     plt.show()
#
    
                
#------------------------------------------------------------------------------    
    #plotting graph    
#    plt.plot(skip_step, relevant_doc)
#    plt.scatter(skip_step, relevant_doc)
#    plt.xlabel('Skip-Step')
#    plt.ylabel('Relevant-Documents')
#    plt.title('Skip Pointer vs Relevant Documents')
#    plt.grid(True)
##    plt.savefig("SkipPointer_xANDy.png")
#    plt.show()
    
#------------------------------------------------------------------------------
if __name__ == '__main__':

    data = json.load(open('JSON_Data_1.json'))
#   print(data)
    map_data = json.load(open('Mapping_1.json'))
    # print (map_data)
    print ('--------------------------------------------------------------------')
    x, y = data_read_from_user()
#    print ('value entered by the user:',x+' ',y )

    x = porter_stemming(x)
    y = porter_stemming(y)

    x = x.decode('UTF-8')
    y = y.decode('UTF-8')

    x_list = data.get(x)
    y_list = data.get(y)    
#    print (len(x_list),len(y_list))
    all_docIDs = [n for n in range(1,19997)]
    not_y_list = [n for n in all_docIDs if not n in y_list]
        
#    print (len(x_list), ':len of x_list'
#    print (len(y_list), ':len of y_list'
#    print (len(not_y_list), ':len of not_y_list'
    print ('--------------------------------------------------------------------')
    choice = get_choice_from_user()
    print ('--------------------------------------------------------------------')
    
    if choice == '1':
        xORy = x_OR_y(x_list, y_list)
        print ('Documents in x OR y : ', len(xORy))
        files = find_mapping(xORy, map_data)
        print ('Documents with the path are given below')
        print ('Format: <Document : Path>','\n')
        for i in files:
            print (i, '\n')
    
    elif choice == '2':
        xANDy = x_AND_y(x_list, y_list)
        print ('Documents in x AND y : ', len(xANDy))
        files = find_mapping(xANDy, map_data)
        print ('Documents with the path are given below')
        print ('Format: <Document : Path>','\n')
        for i in files:
            print (i, '\n')
    
    elif choice == '3':
        xANDNOTy = x_AND_NOT_y(x_list, y_list)
        print ('Documents in x AND NOT y : ', len(xANDNOTy))
        files = find_mapping(xANDNOTy, map_data)
        print ('Documents with the path are given below')
        print ('Format: <Document : Path>','\n')
        for i in files:
            print (i, '\n')
        
    elif choice == '4':
        xORNOTy = x_OR_NOT_y(x_list, not_y_list)
        print ('Documents in x OR NOT y : ', len(xORNOTy))
        files = find_mapping(xORNOTy, map_data)
        print ('Documents with the path are given below')
        print ('Format: <Document : Path>','\n')
        for i in files:
            print (i, '\n')
    elif choice == '5':
        skip_pointer_x_AND_y(x_list, y_list)
        
        
    else:
        print ('Wrong choice.')
        
    
    
    
    
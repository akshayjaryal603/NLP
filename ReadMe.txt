Assignment 1
1] Making inverted index
Filename: inverted_index.py
All the documents are read one by one and the inverted index is stored in dictionary named ‘inverted_index’ in the format <key: value> where key is the vocabulary and the value is the postings list of the documents in which that key is present by performing the below preprocessing steps”
•	Normalization
•	Cleaning using regex
•	Tokenization
•	Stop word removal
•	Stemmming using Porter Stemmer
This dictionary is then stored in a json file named ‘JSON_Data_1.json’
The document number is given from 1 to 19997 successively and a separate Mapping_1.json file is prepared which is maintaining the document name along with its path.

2] Performing query processing
Filename: query_processing.py
For query processing, the below algorithms implemented
- Merge postings algorithm
- Skip pointers algorithm (only for x AND y)

The json file is read and then asking the user to input the value of x and y. After getting the value of x and y, stemming is performed using the Porter Stemmer.
Then, below options are given to the user:
Available options: 
1. x OR y
2. x AND y
3. x AND NOT y
4. x OR NOT y
5. Skip Pointers (x AND y)

Once the user select one of the option then the desired action is performed and result is shown to the user on console.

Note: I tried to install dependency for generating word cloud but it did not work out. So, I generate word cloud on linux system by using the Vocabulory file
which was generated on my system.



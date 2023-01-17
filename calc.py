# Program to measure the similarity between 2 arrays of phrases

import pandas as pd
from gensim.parsing.preprocessing import remove_stopwords

#function which computes the similarity value

def cosine_sim(X,Y):
  # removing stopwords
  X = remove_stopwords(X).lower()
  Y = remove_stopwords(Y).lower()

  # remove stop words from the string
  X_set = set(X.split())
  Y_set = set(Y.split())

  # form a set containing keywords of both strings
  rvector = X_set.union(Y_set)

  c=0
  for w in rvector:
    if w in X and w in Y:
      c+=1

  # cosine formula

  cosine = c /len(rvector)
  return(cosine)

#Reading the values from a .txt file

with open(r"<PATH.txt>", 'r') as f:      #CHANGE PATH HERE
    # Read the file and split it into lines
    arr1 = list(f.read().splitlines())
    arr2 = arr1
    #print(arr1)

# Matrix to store the similarity table
matrix=[]
size=len(arr1)

#Initializing matrix to random values (5) which will be replaced with similarity values later
matrix = [[5 for x in range(size)] for y in range(size)]

for i in range(len(arr1)):
    #print(i)
    for j in range(len(arr1)):
      res = cosine_sim(arr1[i],arr2[j])
        #print(res)
      matrix[i][j] = res

# Adding the row/column headers to the similarity matrix
for i in range(size):
  matrix[i].insert(0,arr1[i])
matrix.insert(0,[""]+arr1)

df = pd.DataFrame(matrix).T
#df.head()

# Exporting the matrix to an Excel workbook
df.to_excel(excel_writer = "<OUTPUT_FILE_PATH.xlsx")  #Change workbook name and path here

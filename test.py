import pandas as pd
import numpy as np
import csv


#for writing to csv file
#filepath = input("what is the filepath?: ")

#new_ciphertext = np.array([["amazon"],["abc123"]])
new_ciphertext = {
    'hulu': 'abc124'
}
#header = ['Keyword', 'ciphertext']
#df = pd.DataFrame(new_ciphertext, orient='index')
      
#df.to_csv('/Users/thomasedgemon/Desktop/testing.py', mode='a')
#df.columns = ["keyword", "ciphertext"]
#print(df)

#new_ciphertext = np.array(['keyword', 'ciphertext'])



with open('/Users/thomasedgemon/Desktop/testing.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in new_ciphertext.items():
        writer.writerow([key, value])




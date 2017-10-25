import pandas as pd
import csv

def write(df):
    fileout = open('/Users/sakamotoryuuji/syuron/Ciao/doc/dataset/rating_doc.txt', 'wt')
    for index, row in df.iterrows():
        if str(row['review']).strip():
            fileout.write("<DOC>" + "\n")
            fileout.write(row['review'] + "\n")
            fileout.write("</DOC>" + "\n")

if __name__ == '__main__':
    df = pd.read_csv("/Users/sakamotoryuuji/syuron/Ciao/dataset/rating.txt", delimiter='::::', engine='python' )
    #df = pd.read_csv("/Users/sakamotoryuuji/syuron/Ciao/doc/dataset/rating_doc.txt")
    #print df[df['review'].isnull].size

    write(df)

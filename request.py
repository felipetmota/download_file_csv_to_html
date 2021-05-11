import requests
import pandas as pd


def save_file (url, path_file):
    #request 
    response = requests.get(url)
    #open file
    with open(path_file, 'wb') as newfile:
        #write file
        newfile.write(response.content)
        

def trans_file_html (data):

    #read csv
    data = pd.read_csv(data, sep=';')
    #transform csv to html
    data.to_html('data.html')
    
    
if __name__ == "__main__":
     BASE_URL = "link"
     save_file(BASE_URL, 'data.csv')
     trans_file_html('data.csv')

    
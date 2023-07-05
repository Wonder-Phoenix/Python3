import requests
from bs4 import BeautifulSoup

sitecrypto= 'https://www.courscrypto.com/monnaie/'
sample_csv = "crypto.csv"

crypto = {'USDT': ('Tether', '96.92'), 
          'AVAX': ('Avalanche-2', '3.01'), 
          'DOT': ('Polkadot', '7.26'), 
          'XRP': ('Ripple', '81.88'), 
          'BNX': ('binaryX', '0.62'), 
          'BNB': ('binancecoin', '0.02'), 
          'SOLO': ('solo-coin','0.22')}
cryptoprix = 0
nbrecrypto = 0
total = 0

fichier=open(sample_csv,"w")
fichier.write('"acronyme"\t"monnaie"\t"prix"\t"quantité"\t"somme"\n')
for i in crypto.items():
    url=(sitecrypto+i[0]+"/"+i[1][0]+"/")
    r = requests.get(url)
    html_soup = BeautifulSoup(r.text, features="html.parser")
    prix=str(html_soup.find('title'))
    prix=prix[prix.find("€")+1:prix.find("</")]
    prix=prix.replace(",","")
    cryptoprix=float(prix)
    nbrecrypto=float(i[1][1])
    total=cryptoprix*nbrecrypto
    fichier.write('"'+i[0]+'"\t"'+i[1][0]+'"\t"'+str(prix)+'"\t"'+str(nbrecrypto)+'"\t"'+str(total)+'"\n')
fichier.close()

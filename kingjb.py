from bs4 import BeautifulSoup
import requests
import os

agent = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0"}
url = 'https://thekingsbible.com/Bible/%d/%d'

start = int(input('Where do you went to start: '))
#start = 1
for b1 in range(start, 67):
    url1 = url %(b1, 1)
    r1 = requests.get(url1, headers=agent)

    if r1.status_code == 200:
        print('[x] GOT: book: %d' %(b1))
        os.mkdir(str(b1))
    s1 = BeautifulSoup(r1.text, features='html.parser')
    col7 = s1.findAll('div', {'class': 'col-md-7'})

    ref = col7[0].findAll('div', {'class': 'chapterref'})
    a = ref[0].findAll('a')
    print('[**] GOT: %d Chapters' %(len(a)))

    for chap in range(1, len(a)+1):
        url2 = url %(b1, chap)
        r2 = requests.get(url2, headers=agent)

        if r2.status_code == 200:
            print('[x] GOT: book %d: chapter: %d' %(b1, chap))
            f = open('%d/%d.csv' %(b1, chap), 'w')

        s = BeautifulSoup(r2.text, features='html.parser')
        col7 = s.findAll('div', {'class': 'col-md-7'})
        tabl = col7[0].findAll('table', {'class':'bibletable'})

        tr = tabl[0].findAll('tr')

        for i in range(len(tr)):

            f.write(tr[i].findChild().text+'::')
            f.write(tr[i].findChild().findNext().text)
            f.write('\n')
        f.close()

    cont = input('Continue [y/n]: ')
    if cont != 'y':
        break

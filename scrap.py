# coding: utf-8

from bs4 import BeautifulSoup

from jobobject import *

import csv
import urllib.request

def recherchedescrap(URLderecherche, filesnames) :
    with urllib.request.urlopen(URLderecherche) as url:
        s = url.read()

    soup = BeautifulSoup( s , 'html.parser')

    jobs= []
        
    for div in soup.find_all('div', {'class': 'jobsearch-SerpJobCard'}):
        jobs.append(div)
        nbr = len(jobs)

    nbrdejobpercu = "il y a " + str(nbr) + " jobs"
    print( nbrdejobpercu)

    reclames = []

    for data in jobs : 
        jobtitle = data.find_all('a', {'class': 'jobtitle'})
        joblocation = data.find_all('div', {'class': 'location'})
        jobcompany = data.find_all('span', {'class': 'company'})
        jobdesc = data.find_all('div', {'class': 'summary'})
        jobdate = data.find_all('span', {'class': 'date'})
        jobsponso = data.find_all('span', {'class': 'sponsoredGray'})

        for data in jobtitle :
            onejob = data.getText()
            onelink = data.get_attribute_list('href')[0]
        if joblocation:
            for data in joblocation:
                onelocation = data.getText()
        else:
            onelocation = "notfound"
        for data in jobcompany:
            onecompany = data.getText()
        for data in jobdesc:
            onedesc = data.getText()
        if jobdate :
            for data in jobdate:
                onedate = data.getText()
        else:
            onedate = "notfound"
        if jobsponso:
            for data in jobsponso:
                onesponso = True
        else:
            onesponso = False
        
        unereclame = Job()
        unereclame.poste = onejob.strip("\n")
        unereclame.url = onelink.strip("\n")
        unereclame.lieu = onelocation.strip("\n")
        unereclame.entreprise = onecompany.strip("\n")
        unereclame.desc = onedesc.strip("\n")
        unereclame.depuis = onedate.strip("\n")
        unereclame.sponso = onesponso

        reclames.append(unereclame)

        namefich = filesnames
        nameexcel = namefich + ".csv"
    with open(nameexcel, 'a', newline='') as csvfile:
        fields = ['entreprise', 'poste', 'desc', 'lieu', 'depuis', 'sponso', 'url']
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        lolilol = []
        writer.writeheader()
        for reclame in reclames:
            writer.writerow({'entreprise': reclame.entreprise.strip() , 'poste': reclame.poste.strip() , 'desc': reclame.desc.strip() , 'lieu': reclame.lieu.strip() , 'depuis': reclame.depuis.strip() , 'sponso': reclame.sponso , 'url': reclame.url.strip() })
    
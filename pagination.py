URLderecherche = "https://www.indeed.fr/emplois?l=Nancy&start=60"
#Fonctionne sans conditions, avec 1, 2 mais pas 3 
URLderecherche = URLderecherche.split("&")
pagination = 0 
while pagination <=10:
    increm = pagination * 10 
    matchstart = [xs for xs in URLderecherche if "start=" in xs ]
    if "sort=date" not in URLderecherche :
        if matchstart :
            del URLderecherche[-1]
        URLderecherche.append("sort=date") 
        print(URLderecherche)
    matchsort = [s for s in URLderecherche if "sort=" in s ]

    # ajout de la variable GET 'start' pour traiter les 10 pages les plus récentes
    if matchsort :
        paginurl= "start=" + str(increm)
        URLderecherche.append(paginurl)
    #j'enregistre l'url dont j'ai besoin
    urlcomplete= "&".join(URLderecherche)
    # je vide la derniere partie qui contient la pagination pour la remplacer dans le prochain
    if len(URLderecherche) > 2 :
        del URLderecherche[-1]
    print(urlcomplete)

    pagination +=1




# coding: utf-8

class Job(object):
    def __init__(self):
        self.poste :poste
        self.url : url
        self.lieu : lieu
        self.entreprise : entreprise
        self.desc : desc
        self.depuis: depuis
        self.sponso : False

    def __del__(self):
        print("deleted")

    def getPoste(self):
        return self.poste
    
    def setPoste(self, poste):
        self.poste = poste

    def getUrl(self):
        return self.url
    
    def setUrl(self, url):
        self.url = url

    def getLieu(self):
        return self.lieu
    
    def setLieu(self, lieu):
        self.lieu = lieu

    def getEntreprise(self):
        return self.entreprise
    
    def setEntreprise(self, entreprise):
        self.entreprise = entreprise

    def getDesc(self):
        return self.desc
    
    def setDesc(self, desc):
        self.desc = desc

    def getDepuis(self):
        return self.depuis
    
    def setDepuis(self, depuis):
        self.depuis = depuis

    def getSponso(self):
        return self.sponso
    
    def setSponso(self, sponso):
        self.sponso = sponso

    
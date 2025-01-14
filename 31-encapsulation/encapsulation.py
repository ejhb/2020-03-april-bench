# Exercice
# 1. Modifier _get_naissance() de sorte qu’il provoque un affichage dans la console avant de renvoyer la valeur. L’appel au calcul de l’âge provoque-t-il un affichage supplémentaire ? Pourquoi ?



class formulaire:
    def __init__(self, nom, prenom, naissance):
        self.nom = str(nom).upper()
        self.prenom = str(prenom).upper()
        self.naissance = naissance
    def _set_naissance(self, naissance):
        na = str(naissance)
        if na.isnumeric():
            self._naissance = int(na)
        else:
            self._naissance = 1900
    def _get_naissance(self):        
        print("Année de naissance :" , self._naissance)
        return   self._naissance 
    naissance = property(_get_naissance, _set_naissance)
    def age(self):
        return 2020 - self._naissance
    def majeur(self):
        return self.age() >= 18
    def memeFamille(self, formulaire):
        return self.nom == fromulaire.nom
    
ad = formulaire('John', 'Doe', '1996')
ad.naissance = '1996'
print(ad.age())
print(ad.naissance)



# 2. Modifier _set_naissance() de sorte qu’il gère aussi le cas ou la date de naissance est donnée comme une liste.



class formulaire:
    def __init__(self, nom, prenom, naissance):
        self.nom = str(nom).upper()
        self.prenom = str(prenom).upper()
        self.naissance = naissance
    def _set_naissance(self, naissance):
        if str(type(naissance)) == "<class 'list'>":
            naissance = ''.join(naissance)
        if str(type(naissance)) == "<class 'str'>" and naissance.isnumeric():
            naissance = int(naissance)
        if str(type(naissance)) == "<class 'int'>":
            self._naissance = naissance
        else:
            self._naissance = 1900
    def _get_naissance(self):        
        print("Année de naissance :" , self._naissance)
        return   self._naissance 
    naissance = property(_get_naissance, _set_naissance)
    def age(self):
        return 2020 - self._naissance
    def majeur(self):
        return self.age() >= 18
    def memeFamille(self, formulaire):
        return self.nom == fromulaire.nom
    
ad = formulaire('John', 'Doe', ['1','9','9','6'])
print(ad.age())
print(ad.naissance)




# 3. Utiliser des propriété similaire pour encapsuler le nom et le prénom.


class formulaire:
    def __init__(self, nom, prenom, naissance):
        self.nom = str(nom)
        self.prenom = str(prenom)
        self.naissance = naissance
    def _set_naissance(self, naissance):
        if str(type(naissance)) == "<class 'list'>":
            naissance = ''.join(naissance)
        if str(type(naissance)) == "<class 'str'>" and naissance.isnumeric():
            naissance = int(naissance)
        if str(type(naissance)) == "<class 'int'>":
            self._naissance = naissance
        #else:
        #    self._naissance = 1900
    def _get_naissance(self):        
        print("Année de naissance :" , self._naissance)
        return   self._naissance 
    naissance = property(_get_naissance, _set_naissance)
    def _set_nom(self, nom):
        if str(type(nom)) == "<class 'str'>":
            nom = str(nom)
            self._nom = nom
    def _get_nom(self):
        return   self._nom
    nom = property(_get_nom, _set_nom)
    def _set_prenom(self, prenom):
        if str(type(prenom)) == "<class 'str'>":
            prenom = str(prenom)
            self._prenom = prenom
    def _get_prenom(self):
        return   self._prenom
    prenom = property(_get_prenom, _set_prenom)
    def age(self):
        return 2020 - self._naissance
    def majeur(self):
        return self.age() >= 18
    def memeFamille(self, formulaire):
        return self.nom == fromulaire.nom
    
ad = formulaire('John', 'Doe', ['1','9','9','6'])
print(ad.age())
print(ad.naissance) 
print(ad.nom)
print(ad.prenom)
from utils import pluralize
import utils
class SportTeam:
    prix_amande = 50_000
    n_equipe = 0

    def __init__(self,nom,vic,deff): #le constructeur
        self.nom = nom
        self.vic = vic
        self.deff = deff
        self.totalAmande = 0

        self.__class__.n_equipe += 1
        SportTeam.n_equipe += 1

##        # isinstance déterminer la classe de l'objet
##        if isinstance(self,Basketball):
##            Basketball.n_equipe += 1
##        elif isinstance(self,Football):
##            Football.n_equipe += 1
##        elif isinstance(self,Handball):
##            Handball.n_equipe += 1
##
##        SportTeam.n_equipe += 1

    @classmethod
    def chaine(cls,states_chaine):
        nom,vic,deff = states_chaine.split('-')
        return cls(nom,vic,deff)

    @classmethod
    def fiche(cls,states_fiche):
        with open(states_fiche) as file:
            nom,vic,deff = file.readline().strip().split('-')
            return cls(nom,int(vic),int(deff))

    def getAmande(self):
        self.totalAmande += Basketball.prix_amande
        #self.totalAmande += Football.prix_amande "accéder à un attribut de la claase avec self "

    @classmethod # methode de classe //constructeur alternative
    def fixe_montant_amande(cls,amande):
        cls.prix_amande = amande

    def states(self):
        return f"{self.nom} à {utils.pluralize(self.vic, ' vicoire')} et {utils.pluralize(self.deff, ' défaite')}."


# Basketball
class Basketball(SportTeam):
    n_equipe = 0
    def states(self):
        return "[Basketball] STATIQUES:" + super().states()
        # super() permet d'appeler une methode de la classe parent

team1 =  Basketball("Golden state",12,1)
team2 = Basketball("Linkers",5,5)

print(team1.states())
print(team2.states())

print("--------------------------------------------------------")
#Football
class Football(SportTeam):
   n_equipe = 0

   def states(self):
        return "[Football] STATIQUES:" + super().states()

equipe1 =  Football("Barcelone",42,6)
equipe2 = Football("Real",32,5)

print(equipe1.states())
print(equipe2.states())

print("--------------------------------------------------------")
#Handball
class Handball(SportTeam):
   n_equipe = 0

   def states(self):
        return "[Handballl] STATIQUES:" + super().states()

handball1 =  Handball("Monaco",8,2)
handball2 = Handball("Le Havre",6,3)
handball3 = Handball("Dijon",9,3)

print(handball1.states())
print(handball2.states())

print(SportTeam.n_equipe)
print(Football.n_equipe)
print(Basketball.n_equipe)
print(Handball.n_equipe)

#print(help(Basketball))
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

    @classmethod
    def chaine(cls,states_chaine):
        nom,vic,deff = states_chaine.split('-')
        return cls(nom,int(vic),int(deff))

    @classmethod
    def fiche(cls,states_fiche):
        try:
            with open(states_fiche) as file:
                return cls.chaine(file.readline().strip())
        except:
            print("Fichier non trouvé")
            # raise ValueError("Fichier non trouvé")


    def getAmande(self):
        self.totalAmande += SportTeam.prix_amande
        #self.totalAmande += Football.prix_amande "accéder à un attribut de la claase avec self "

    @classmethod # methode de classe //constructeur alternative
    def fixe_montant_amande(cls,amande):
        cls.prix_amande = amande

    def states(self):
        return f"{self.nom} à {utils.pluralize(self.vic, ' vicoire')} et {utils.pluralize(self.deff, ' défaite')}."


# Basketball
class Basketball(SportTeam):
    prix_amande = 60000
    n_equipe = 0
    def states(self):
        return "[Basketball] STATIQUES:" + super().states()
        # super() permet d'appeler une methode ou attribut de la classe parent

team1 =  Basketball("Golden state",12,1)
team2 = Basketball("Linkers",5,5)

print(team1.states())
print(team2.states())




print("--------------------------------------------------------")
#Football
class Football(SportTeam):
   n_equipe = 0

   def __init__(self,nom,vic,deff,nul): #le constructeur redefini
        super().__init__(nom,vic,deff)
        self.nul = nul


   @classmethod
   def chaine(cls,states_chaine):
        nom,vic,deff,nul = states_chaine.split('-')
        return cls(nom,int(vic),int(deff),int(nul))

   def states(self):
        return f"[Football] STATIQUES: {self.nom} à {utils.pluralize(self.vic, ' vicoire')} et {utils.pluralize(self.deff, ' défaite')}, et {utils.pluralize(self.nul, ' Nul')}"

equipe1 =  Football("Barcelone",42,6,1)
equipe2 = Football("Real",32,5,3)
#equipe3 = Football.fiche('djime.txt')

print(equipe1.states())
print(equipe2.states())
#print(equipe3.states())


#print(help(Basketball))
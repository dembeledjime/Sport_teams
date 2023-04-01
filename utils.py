@staticmethod
def pluralize(total,singular,plural=None):
        assert isinstance(total,int) and total >= 0, 'Le total doit etre une valeur positive.'

        if plural is None:
            plural = singular + "s";
        string = singular if total <= 1 else plural
        return f'{total}{string}'

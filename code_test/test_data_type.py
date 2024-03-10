from collections import defaultdict

TYPES = ('single', 'multi')

class Share:

    def __init__(self) -> None:
        self.args = dict()
        self.single = defaultdict(dict)

    def keys(self, typ, fn=None):

        if typ.lower() not in TYPES:
            raise KeyError(f"Given type must be one of {TYPES}, not '{typ}'.")
        
        dic = 

if __name__ == '__main__':

    share = Share()

    share.keys('singlemulti','함수1')
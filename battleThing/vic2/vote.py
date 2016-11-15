# this is about total voting sys.
# basically follows victoria 2 rule, but POPs' voting pattern is based on vic1(i guess)
# right now there's technically nothing done. and all is just for tests.

vicpop = ['farmers', 'laborers', 'craftsmen', 'slaves', 'soldiers', 'artisans', 'breaucrats', 'clerks', 'clergymen',
       'officers', 'aristocrats', 'capitalists']

class pops:
    def __init__(self, pop, loc):
        pppp = True
        while pppp:
            if pop not in vicpop:
                pop = input('put correct name of pop')
            if pop in vicpop:
                pppp = False
        self.pop = pop



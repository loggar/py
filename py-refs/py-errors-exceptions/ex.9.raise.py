# So, we can catch exections with try...except. But what if we actually want to throw one?

# In Python terminology, we say we raise an exception, and like most things in this language, accomplishing that is obvious: just use the raise keyword:


class Tardis:

    def __init__(self):
        pass

    def camouflage(self):
        raise NotImplementedError('Chameleon circuits are stuck.')


tardis = Tardis()
tardis.camouflage()

class Tardis:

    def __init__(self):
        pass

    def camouflage(self):
        raise NotImplementedError('Chameleon circuits are stuck.')


tardis = Tardis()

try:
    tardis.camouflage()
except NotImplementedError as e:
    print(e)

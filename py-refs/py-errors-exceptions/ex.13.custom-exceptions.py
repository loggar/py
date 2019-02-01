class SpacetimeError(Exception):
    def __init__(self, message):
        super().__init__(self, message)


class Tardis():

    def __init__(self):
        self._destination = ""
        self._timestream = []

    def cloister_bell(self):
        print("(Ominous bell tolling)")

    def dematerialize(self):
        self._timestream.append(self._destination)
        print("(Nifty whirring sound)")

    def set_destination(self, dest):
        if dest in self._timestream:
            self.cloister_bell()
        self._destination = dest

    def engage(self):
        if self._destination in self._timestream:
            raise SpacetimeError("You should not cross your own timestream!")
        else:
            self.dematerialize()


tardis = Tardis()

# Should be fine
tardis.set_destination("7775/349x10,012/acorn")
tardis.engage()

# Also fine
tardis.set_destination("5136/161x298,58/delta")
tardis.engage()

# The TARDIS is not going to like this...
tardis.set_destination("7775/349x10,012/acorn")
tardis.engage()

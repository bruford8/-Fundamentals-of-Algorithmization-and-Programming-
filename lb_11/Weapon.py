class ColdSteel:
    pass

class Bladed(ColdSteel):
    pass

class NotBladed(ColdSteel):
    pass

class Combined(ColdSteel):
    pass

class Stabbing(Bladed):
    pass

class Chopping(Bladed):
    pass

class StabbingChopping(Bladed):
    pass

class StabbingCutting(Bladed):
    pass

class ImpactCrushing(NotBladed):
    pass

class PiercingAndChopping(Combined):
    pass
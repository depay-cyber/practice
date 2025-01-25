print('Hey, you wanna take a tour on my dogs lets go')
class Dogs:
    def __init__(self,name, breed, colour, personality):
        self.name=name
        self.breed= breed
        self.colour=colour
        self.personality=personality
    def breeds(self):
        print('This dog is called', self.name, 'Its  a ', self.breed, 'its ', self.colour,'its',self.personality)
Blackman= Dogs('Blackman','Roweiler','black', ' aggresive and playfull') 
ray=Dogs('Ray', 'PitBull', 'brown', 'Deadly and aggressive')
dom=Dogs('Dirty Dom', 'mastif','white', 'friendly and annoying')
Blackman.breeds()
ray.breeds()
dom.breeds()
          
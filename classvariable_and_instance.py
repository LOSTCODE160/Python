class pokemon:
    pokemon_type="fire"
    def __init__(self,name):
        self.name=name
    
c=pokemon('charizad')
a=pokemon('charmender')
print(c.pokemon_type)
print(c.name)
print(a.pokemon_type)
print(a.name)
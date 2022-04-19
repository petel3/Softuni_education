from project.pokemon import Pokemon


class Trainer:
    def __init__(self,name):
        self.name = name
        self.pokemons = []
    def add_pokemon(self,pokemon:Pokemon):
        for pokemons in self.pokemons:
            if pokemon == pokemons:
               return f"This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {Pokemon.pokemon_details(pokemon)}"
    def release_pokemon(self,pokemon_name):
        for pokemons in self.pokemons:
            if pokemons.name == pokemon_name:
                self.pokemons.remove(pokemons)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"
    def trainer_data(self):
        result=f"Pokemon Trainer {self.name}" + '\n' + f"Pokemon count {len(self.pokemons)}"
        for pokemon in self.pokemons:
            result+='\n'
            result+=f'- {pokemon.pokemon_details()}'
        return result

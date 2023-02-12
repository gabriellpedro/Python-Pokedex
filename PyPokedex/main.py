import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

#Projeto simples, criando uma Pokédex que apresenta o nome e tipo do Pokémon, com base em seu ID na Pokédex.

window = tk.Tk()
window.geometry("600x700")
window.title("GPyPokedex")
window.config(padx=10, pady=10)

title_label = tk.Label(window, text="GPyPokedex")
title_label.config(font=("Arial", 30))
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 20))
pokemon_types.pack(padx=10, pady=10)

pokemon_text_moves = tk.Label(window)
pokemon_text_moves.config(font=("Arial", 12))
pokemon_text_moves.pack(padx=10, pady=10)

pokemon_abilities = tk.Label(window)
pokemon_abilities.config(font=("Arial", 20))
pokemon_abilities.pack(padx=10, pady=10)


def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))

    image = PIL.Image.open(BytesIO(response.data))
    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"ID: {pokemon.dex} \n Name: {pokemon.name} \n Height: {pokemon.height}".title())
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())
    #pokemon_text_moves.config(text="Moves of this Pokémon:")
    #pokemon_abilities.config(text=pokemon.abilities)

label_id_pokemon = tk.Label(window, text="ID ou Nome")
label_id_pokemon.config(font=("Arial", 16))
label_id_pokemon.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 16))
text_id_name.pack(pady=10, padx=10)

btn_load = tk.Button(window, text="Load Pokémon", command=load_pokemon)
btn_load.config(font=("Arial", 16))
btn_load.pack(padx=10, pady=10)

window.mainloop()
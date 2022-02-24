from tkinter import *
import webbrowser


def open_pokepedia():
    webbrowser.open_new_tab("https://www.pokepedia.fr/" + saisie_fr.get())

def open_bulbapedia():
    webbrowser.open_new_tab("https://bulbapedia.bulbagarden.net/wiki/" + saisie_en.get())

def open_pokemon_pp():
    webbrowser.open_new_tab("https://www.pokepedia.fr/Liste_des_Pok%C3%A9mon_dans_l%27ordre_du_Pok%C3%A9dex_National")

def open_atk_pp():
    webbrowser.open_new_tab("https://www.pokepedia.fr/Liste_des_capacit%C3%A9s")

def open_types_pp():
    webbrowser.open_new_tab("https://www.pokepedia.fr/Cat%C3%A9gorie:Pok%C3%A9mon_par_type")

def open_pokemon_bb():
    webbrowser.open_new_tab("https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number")

def open_atk_bb():
    webbrowser.open_new_tab("https://bulbapedia.bulbagarden.net/wiki/Category:Moves")

def open_types_bb():
    webbrowser.open_new_tab("https://bulbapedia.bulbagarden.net/wiki/Type")


window = Tk()

window.title("Recherche page Pokémon")
window.geometry("720x600")
window.minsize(600, 600)
window.iconbitmap("logo.ico")
window.config(background='brown')

frame = Frame(
    window,
    bg='brown'
)

search = Frame(
    window,
    bg='brown'
)

text = Label(
    window,
    text="Recherche de Pokémon sur Internet",
    font=("Calibri", 20),
    bg='brown'
)

button_fr = Button(
    search,
    text="Pokepedia",
    font=("Arial", 20),
    bg='red',
    command=open_pokepedia
)

saisie_fr = Entry(
    search,
    font=("Arial", 20)
)

button_en = Button(
    frame,
    text="Bulbapedia",
    font=("Arial", 20),
    bg='red',
    command=open_bulbapedia
)

saisie_en = Entry(
    frame,
    font=("Arial", 20)
)

text.pack(side=TOP, pady=50)
button_fr.pack(side=RIGHT)
saisie_fr.pack(side=LEFT)
button_en.pack(side=RIGHT)
saisie_en.pack(side=LEFT)
search.pack(expand=YES, fill=Y)
frame.pack(expand=YES, fill=Y)

menu_bar = Menu(window)
pp = Menu(menu_bar, tearoff=0)
bb = Menu(menu_bar, tearoff=1)
quit = Menu(menu_bar, tearoff=2)
pp.add_command(label="Pokemon", command=open_pokemon_pp)
pp.add_command(label="Attaques", command=open_atk_pp)
pp.add_command(label="Types", command=open_types_pp)
bb.add_command(label="Pokemon", command=open_pokemon_bb)
bb.add_command(label="Attaques", command=open_atk_bb)
bb.add_command(label="Types", command=open_types_bb)
menu_bar.add_cascade(label="Poképedia", menu=pp)
menu_bar.add_cascade(label="Bulbapedia", menu=bb)
menu_bar.add_cascade(label="Quitter", command=window.quit)

window.config(menu=menu_bar)
window.mainloop()

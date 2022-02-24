from tkinter import *
import webbrowser

#-----------------------------------------------
#------------------Fonction---------------------

def open_pokepedia_enter(event):
    webbrowser.open_new_tab("https://www.pokepedia.fr/" + saisie_fr.get())

def open_pokepedia():
    webbrowser.open_new_tab("https://www.pokepedia.fr/" + saisie_fr.get())

def open_bulbapedia():
    webbrowser.open_new_tab("https://bulbapedia.bulbagarden.net/wiki/" + saisie_en.get())

def open_bulbapedia_enter(event):
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
    

#-----------------------------------------------
#------------------Var Tk-----------------------

window = Tk()

#-----------------------------------------------
#------------------Perso Window-----------------

window.title("Recherche page Pokémon V3")
window.geometry("720x600")
window.minsize(720, 600)
window.maxsize(720, 600)
window.iconbitmap("img/logo.ico")
window.config(background='brown')

#-----------------------------------------------
#------------------Frame------------------------

frame = Frame(
    window,
)


#-----------------------------------------------
#------------------Variable---------------------

quit = PhotoImage(file='img/deconnexion.png')
search = PhotoImage(file='img/search.png')
bar_blue = PhotoImage(file='img/bar_blue.png')
box_grey = PhotoImage(file='img/box_grey.png')
pokemon = PhotoImage(file='img/pokemon.png')
ball = PhotoImage(file='img/ball.png')

#-----------------------------------------------
#------------------Canvas-----------------------

canvas1 = Canvas(
    window,
    width=720,
    height=600,
    highlightthickness=0,
    bg='brown'
)

#-----------------------------------------------
#------------------Entity-----------------------

canvas1.create_image(
    100,
    20,
    image=ball,
    anchor=NW
)

canvas1.create_image(
    30,
    0,
    image=pokemon,
    anchor=NW
)

canvas1.create_image(
    0,
    0,
    anchor=NW,
    image=bar_blue
)

canvas1.create_image(
    30,
    0,
    anchor=NW,
    image=box_grey    
)

#-----------------------------------------------
#-----------------Objets------------------------

btn_quit = Button(
    window,
    image=quit,
    bg='#06dee5',
    borderwidth=0,
    command=window.quit
)

button_fr = Button(
    window,
    image=search,
    bg='white',
    activebackground='#8f8f8f',
    fg='brown',
    borderwidth=0,
    command=open_pokepedia
    )

saisie_fr = Entry(
    window,
    font=("Arial", 20),
    borderwidth=0,
    justify=CENTER
)
saisie_fr.bind('<KeyPress-Return>', open_pokepedia_enter)

button_en = Button(
    window,
    image=search,
    bg='white',
    fg='brown',
    borderwidth=0,
    command=open_bulbapedia
)

saisie_en = Entry(
    window,
    font=("Arial", 20),
    borderwidth=0,
    justify=CENTER
)
saisie_en.bind('<KeyPress-Return>', open_bulbapedia_enter)

#-----------------------------------------------
#-----------------------------------------------

canvas1.create_window(
    494,
    205,
    anchor=NW,
    window=button_fr
)

canvas1.create_window(
    180,
    202,
    anchor=NW,
    window=saisie_fr
)

canvas1.create_window(
    494,
    355,
    anchor=NW,
    window=button_en
)

canvas1.create_window(
    180,
    352,
    anchor=NW,
    window=saisie_en
)

canvas1.create_window(
    640,
    525,
    anchor=NW,
    window=btn_quit
)
#-----------------------------------------------
#--------------------.pack----------------------

canvas1.pack(fill=BOTH, expand=YES)
frame.pack(expand=YES)

#-----------------------------------------------
#------------------menu_bar---------------------

menu_bar = Menu(window)
pp = Menu(menu_bar, tearoff=0)
bb = Menu(menu_bar, tearoff=0)
pp.add_command(label="Pokemon", command=open_pokemon_pp)
pp.add_command(label="Attaques", command=open_atk_pp)
pp.add_command(label="Types", command=open_types_pp)
bb.add_command(label="Pokemon", command=open_pokemon_bb)
bb.add_command(label="Attaques", command=open_atk_bb)
bb.add_command(label="Types", command=open_types_bb)
menu_bar.add_cascade(label="Poképedia", menu=pp)
menu_bar.add_cascade(label="Bulbapedia", menu=bb)

#-----------------------------------------------
#------------------Launch-----------------------

window.config(menu=menu_bar)
window.mainloop()


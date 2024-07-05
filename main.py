import random
from tkinter import *
from PIL import Image, ImageTk

quote = {
    'quote1':'Es el vecino el que elige al alcalde y es el alcalde el que quiere que sean los vecinos el alcalde.',
    'quote2': 'Lo más importante que se puede hacer por los demás es exactamente lo que los demás pueden hacer por uno.',
    'quote3': 'Cuanto peor, mejor para todos; y cuanto peor para todos, mejor, mejor para mí el suyo, beneficio político.',
    'quote4': 'Somos sentimientos y tenemos seres humanos.',
    'quote5': 'Me gustan los catalanes porque hacen cosas.',
    'quote6': 'Una cosa es ser solidario, y otra es ser solidario a cambio de nada.',
    'quote7': 'Yo no quiero bajar impuestos, lo que quiero es subirlos.',
    'quote8': 'ETA es una gran nación.',
    'quote9': 'Fin de la cita.',
    'quote10': '¡Viva el vino!',
    'quote11': 'Un vaso es un vaso y un plato es un plato.',
    'quote12': 'Its very difficult todo esto.',
    'quote13': 'España es una gran nación y los españoles muy españoles y mucho españoles.',
    'quote14': 'Haremos lo que podamos y dejaremos hacer a los demás lo que no podemos hacer nosotros.',
    'quote15': 'A veces la mejor decisión es no tomar ninguna decisión, que también es tomar una decisión.',
    'quote16': 'Vamos a ver, el tráfico, ya, ya, ya. Estamos trabajando en ello.',
    'quote17': 'Todo lo que se ha publicado es falso, salvo alguna cosa que es lo que han publicado los diarios.',
    'quote18': 'Una nación es un país que tiene... nación.',
    'quote19': 'Me he emocionado, no lo voy a negar.',
    'quote20': 'Esto no es como el agua, que cae del cielo sin que se sepa exactamente por qué.',
    'quote21': 'No es que no me haya olvidado, es que me voy a seguir acordando.',
    'quote22': 'Yo creo que estamos donde estamos.',
    'quote23': 'Lo que nosotros hemos hecho, cosa que no hizo usted, es engañar a la gente.',
    'quote24': 'Los españoles hacen cosas.',
    'quote25': 'A veces la mejor manera de solucionar los problemas es no creándolos.'
}


def get_quote ():
    claves = list(quote.keys())
    clave_aleatoria = random.choice(claves)
    new_quote = quote[clave_aleatoria]
    canvas.itemconfig(quote_text, text= new_quote)

#print(random_quote(quote))



window = Tk()
window.title("Rajoy dice...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="C:/Users/jenni/OneDrive/Escritorio/DOP/Proyecto_15/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 14, "bold"), fill="black")
canvas.grid(row=0, column=0)

rajoy_img = Image.open("C:/Users/jenni/OneDrive/Escritorio/DOP/Proyecto_15/rajoy.png")
rajoy_img = rajoy_img.resize((100, 100), Image.Resampling.LANCZOS)  #Redimensionar la imagen
rajoy_img = ImageTk.PhotoImage(rajoy_img)
rajoy_button = Button(image=rajoy_img, highlightthickness=0, command=get_quote)
rajoy_button.grid(row=1, column=0)



window.mainloop()
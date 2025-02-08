import requests
from tkinter import Tk, Label, Listbox, Scrollbar, Frame, StringVar
from tkinter.ttk import Style, Combobox
from tkcalendar import Calendar
from datetime import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Deshabilitar advertencias SSL
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Mapeo de circuitos y rutas
CIRCUITOS = {
    "Circuito 1 - Panorámico": {
        "Ruta 1-A: Ruta Montaña Machupicchu": 7,
        "Ruta 1-B: Ruta terraza superior": 8,
        "Ruta 1-C: Ruta Portada Intipunku (disponible solo en temporada alta)": 9,
        "Ruta 1-D: Ruta Puente Inka (disponible solo en temporada alta)": 10
    },
    "Circuito 2 - Circuito clásico": {
        "Ruta 2-A: Ruta clásico diseñada": 11,
        "Ruta 2-B: Ruta terraza inferior": 12
    },
    "Circuito 3 - Machupicchu realeza": {
        "Ruta 3-A: Ruta Montaña Waynapicchu": 13,
        "Ruta 3-B: Ruta realeza diseñada": 14,
        "Ruta 3-C: Ruta Gran Caverna (solo disponible en temporada alta)": 15,
        "Ruta 3-D: Ruta Huchuypicchu (solo disponible en temporada alta)": 16
    }
}

# Obtener fechas disponibles
def get_fechas_disponibles(nidruta):
    try:
        response = requests.get(
            f"https://api-tuboleto.cultura.pe/reserva/consulta-fechas-disponibles?nidruta={nidruta}",
            headers={"Accept": "application/json"},
            verify=False
        )
        return [fecha["dfecha"] for fecha in response.json()] if response.status_code == 200 else []
    except:
        return []

# Obtener horarios disponibles
def get_horarios_disponibles(nidruta, nidcircuito, fecha):
    try:
        response = requests.get(
            f"https://api-tuboleto.cultura.pe/reserva/consulta-horarios?nidruta={nidruta}&nidcircuito={nidcircuito}&nidlugar=llaqta_machupicchu&df_inicio={fecha}",
            headers={"Accept": "application/json"},
            verify=False
        )
        return [
            f"{h['dhora_ini']} - {h['dhora_fin']} | Cupos: {h['ncupo_actual']}/{h['ncupo']}"
            for h in response.json().get("data", [])
        ] if response.status_code == 200 else []
    except:
        return []

# Cargar fechas en el calendario
def cargar_calendario():
    calendar.calevent_remove("all")
    horarios_listbox.delete(0, "end")
    circuito, ruta = circuito_var.get(), ruta_var.get()
    if circuito and ruta:
        nidruta = CIRCUITOS[circuito][ruta]
        fechas = get_fechas_disponibles(nidruta)
        for fecha in fechas:
            day, month, year = map(int, fecha.split("-"))
            calendar.calevent_create(datetime(year, month, day).date(), "Disponible", "available")

# Mostrar horarios disponibles
def on_date_selected(event):
    horarios_listbox.delete(0, "end")
    circuito, ruta = circuito_var.get(), ruta_var.get()
    if circuito and ruta:
        nidruta = CIRCUITOS[circuito][ruta]
        horarios = get_horarios_disponibles(nidruta, list(CIRCUITOS.keys()).index(circuito) + 1, calendar.get_date())
        for horario in horarios:
            horarios_listbox.insert("end", horario)
        if not horarios:
            horarios_listbox.insert("end", "No hay horarios disponibles.")

# Actualizar rutas disponibles
def actualizar_rutas(*args):
    rutas = CIRCUITOS.get(circuito_var.get(), {}).keys()
    ruta_var.set("")
    ruta_menu["values"] = list(rutas)
    cargar_calendario()

def on_ruta_changed(*args):
    cargar_calendario()

# Crear ventana principal
root = Tk()
root.title("Adquiere tu boleto")
root.geometry("600x500")
root.configure(bg="white")

# Estilo
style = Style()
style.configure("TLabel", background="white", font=("Arial", 12))
style.configure("TCombobox", font=("Arial", 12))

# Encabezado
Label(root, text="🎟️ Adquiere tu boleto", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

# Selección de circuito
frame_seleccion = Frame(root, bg="white")
frame_seleccion.pack(pady=10)

Label(frame_seleccion, text="Selecciona el circuito que deseas visitar", bg="white").grid(row=0, column=0, padx=5, sticky="w")
circuito_var = StringVar()
circuito_menu = Combobox(frame_seleccion, textvariable=circuito_var, state="readonly", width=30)
circuito_menu["values"] = list(CIRCUITOS.keys())
circuito_menu.grid(row=1, column=0, padx=5, pady=5)

# Selección de ruta
Label(frame_seleccion, text="Seleccionar la ruta de tu recorrido", bg="white").grid(row=2, column=0, padx=5, sticky="w")
ruta_var = StringVar()
ruta_menu = Combobox(frame_seleccion, textvariable=ruta_var, state="readonly", width=30)
ruta_menu.grid(row=3, column=0, padx=5, pady=5)

# Calendario para selección de fecha
Label(frame_seleccion, text="Selecciona la fecha de tu visita", bg="white").grid(row=4, column=0, padx=5, sticky="w")
calendar = Calendar(frame_seleccion, selectmode="day", date_pattern="dd-mm-yyyy", background="#f0f0f0")
calendar.grid(row=5, column=0, padx=5, pady=5)
calendar.tag_config("available", background="green", foreground="white")
calendar.bind("<<CalendarSelected>>", on_date_selected)

# Lista de horarios disponibles
Label(frame_seleccion, text="Selecciona el horario de ingreso", bg="white").grid(row=6, column=0, padx=5, sticky="w")
horarios_listbox = Listbox(frame_seleccion, width=40, height=5, font=("Arial", 10))
horarios_listbox.grid(row=7, column=0, padx=5, pady=5)
scrollbar = Scrollbar(frame_seleccion, orient="vertical", command=horarios_listbox.yview)
scrollbar.grid(row=7, column=1, sticky="ns")
horarios_listbox.config(yscrollcommand=scrollbar.set)

# Vincular eventos
circuito_var.trace("w", actualizar_rutas)
ruta_var.trace("w", on_ruta_changed)

# Ejecutar aplicación
root.mainloop()

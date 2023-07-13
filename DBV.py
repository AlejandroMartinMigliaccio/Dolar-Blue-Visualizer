import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import font

# Ventana principal

ventana = tk.Tk()
ventana.title('Precios')
ventana.geometry('1040x700')
ventana.resizable(False, False)
ventana.configure(bg='white')

# Conseguir información del dolar blue desde Bluelytics

historicoBlue = pd.read_json('https://api.bluelytics.com.ar/v2/evolution.json')
historicoDolarBlue = historicoBlue.loc[historicoBlue['source'] == 'Blue', ['value_sell','value_buy']] #Devuelve los valores historicos del Dolar Blue para la compra y venta
historicoDolarBlue['date'] = pd.to_datetime(historicoBlue['date'])
historicoDolarBlue.set_index('date', inplace=True)

# Conseguir ultimo precio compra y venta

ultimoPrecioCompra = historicoBlue['value_buy'].iloc[1]
ultimoPrecioVenta = historicoBlue['value_sell'].iloc[1]

# GRAFICO MATPLOT

fig, ax = plt.subplots()
ax.plot(historicoDolarBlue.index, historicoDolarBlue['value_sell'], label='Venta')
ax.plot(historicoDolarBlue.index, historicoDolarBlue['value_buy'], label='Compra')
ax.set_title('Valores Blue')
ax.set_xlabel('Fecha')
ax.set_ylabel('Valor')
ax.legend()

# Widget FigureCanvasTkAgg

canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.draw()
canvas.get_tk_widget().grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Ajustar el tamaño del gráfico al tamaño del widget FigureCanvasTkAgg

fig.tight_layout()
canvas.get_tk_widget().configure(width=1020, height=540)



label_font = font.Font(size=30) # Aumentar tamaño de las etiquetas de compra y venta

# Mostrar precios de compra y venta

labelCompra = tk.Label(ventana, text=f'Último precio de compra:\n\n{ultimoPrecioCompra}', font=label_font, bg='white', justify='center', width=20)
labelCompra.grid(row=0, column=0, padx=10, pady=10)

labelVenta = tk.Label(ventana, text=f'Último precio de venta:\n\n{ultimoPrecioVenta}', font=label_font, bg='white', justify='center', width=20)
labelVenta.grid(row=0, column=1, padx=10, pady=10)

ventana.mainloop()





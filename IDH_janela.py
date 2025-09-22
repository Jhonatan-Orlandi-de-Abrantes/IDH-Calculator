# Imports/Frameworks
import tkinter as tk, math
from tkinter import ttk, messagebox

# Funções
def calcular_idh():
    try:
        expect_de_vida = float(entry_expect_vida.get().replace(',', '.').strip())
        rnb = float(entry_rnb.get().replace(',', '.').strip())
        escolha = var_estudo.get()
        media_anos = entry_media_anos.get().replace(',', '.').strip()
        expect_anos = entry_expect_anos.get().replace(',', '.').strip()
        media_anos_de_estudo = float(media_anos) if media_anos else 0
        expect_anos_estudo = float(expect_anos) if expect_anos else 0

        IL = (expect_de_vida - 20) / (85 - 20)
        IE_media = (media_anos_de_estudo / 15)
        IE_expectativa = (expect_anos_estudo / 18)
        IR = ((math.log(rnb) - 4.60) / 6.62)

        if escolha == 1:
            multiplicacao = (IL * IE_media * IR)
        else:
            multiplicacao = (IL * IE_expectativa * IR)

        IDH = (multiplicacao ** (1/3))
        IDH = round(IDH, 3)
        IDH_str = str(IDH).replace('.', ',')
        label_resultado.config(text=f'O IDH desse país é:')
        label_resultado_num.config(text=f'{IDH_str}')
    
    except Exception as e:
        messagebox.showerror('Erro', 'Verifique se todos os campos estão preenchidos corretamente!')

def alternar_campos():
    if var_estudo.get() == 1:
        entry_media_anos.config(state='normal')
        entry_expect_anos.delete(0, tk.END)
        entry_expect_anos.config(state='disabled')
    else:
        entry_expect_anos.config(state='normal')
        entry_media_anos.delete(0, tk.END)
        entry_media_anos.config(state='disabled')

# Janela gráfica
win = tk.Tk()
win.title('Calculadora de IDH')
win.geometry('400x400')
win.resizable(False, False)

ttk.Label(win, text='Bem-vindo ao calculador de IDH!', font=('Arial', 14)).pack(pady=10)

frame = ttk.Frame(win)
frame.pack(pady=10)

ttk.Label(frame, text='Expectativa de vida:').grid(row=0, column=0, sticky='w')
entry_expect_vida = ttk.Entry(frame)
entry_expect_vida.grid(row=0, column=1)

ttk.Label(frame, text='Forma de medida de estudo:').grid(row=1, column=0, sticky='w')
var_estudo = tk.IntVar(value=1)
radio_media = ttk.Radiobutton(frame, text='Média de anos de estudo', variable=var_estudo, value=1, command=alternar_campos)
radio_media.grid(row=1, column=1, sticky='w')
radio_expect = ttk.Radiobutton(frame, text='Expectativa de anos de estudo', variable=var_estudo, value=2, command=alternar_campos)
radio_expect.grid(row=2, column=1, sticky='w')

ttk.Label(frame, text='Média de anos de estudo:').grid(row=3, column=0, sticky='w')
entry_media_anos = ttk.Entry(frame)
entry_media_anos.grid(row=3, column=1)

ttk.Label(frame, text='Expectativa de anos de estudo:').grid(row=4, column=0, sticky='w')
entry_expect_anos = ttk.Entry(frame, state='disabled')
entry_expect_anos.grid(row=4, column=1)

ttk.Label(frame, text='PIB per capita Ppp:').grid(row=5, column=0, sticky='w')
entry_rnb = ttk.Entry(frame)
entry_rnb.grid(row=5, column=1)

btn_calcular = ttk.Button(win, text='Calcular IDH', command=calcular_idh)
btn_calcular.pack(pady=15)

label_resultado = ttk.Label(win, text='', font=('Arial', 12))
label_resultado.pack(pady=10)

label_resultado_num = ttk.Label(win, text='', foreground='blue', font=('Arial', 16))
label_resultado_num.pack(pady=10)

ttk.Button(win, text='Fechar', command=win.destroy).pack(pady=5)

alternar_campos()

# Manter a janela aberta
win.mainloop()
from gerasenha import gerasenha, substituicao
import tkinter as tk

def mostrarsenha():
    senha = gerasenha()
    if acrescentar_leetspeak.get():
        senha = substituicao(senha)
    mensagem2.config(text=f"{senha}")


    mensagem2.config(state="normal", width=len(senha))
    mensagem2.delete(0, tk.END)
    mensagem2.insert(0, senha)
    mensagem2.config(state="readonly")
    mensagem2.grid(row=3, column=0, pady=10)


# Janela Principal
janela = tk.Tk()
janela.geometry("400x300")
janela.title("Diceware Password Generator")
janela.configure(bg='#A9A9A9')
janela.grid_columnconfigure(0, weight=1)


mensagem = tk.Label(janela, text="DICEWARE PASSWORD GENERATOR", font=("Arial", 12), fg="black", bg = "#A9A9A9",)
mensagem.grid(row= 0, column=0, pady=20)

acrescentar_leetspeak = tk.BooleanVar()
botao_opcao = tk.Checkbutton(janela, text="    Acrescentar Leetspeak (Substituição)", bg="#A9A9A9",
                             font=("Arial", 10), variable=acrescentar_leetspeak, fg="black", activebackground="#A9A9A9")
botao_opcao.grid(row=1, column=0, pady=15)

botao = tk.Button(janela, text="Criar senha", command=mostrarsenha, width= 40, height=2, bg="white", fg="black", activebackground="white", activeforeground="black")
botao.grid(row=2, column=0, pady=15)

mensagem2 = tk.Entry(janela, text="", font=("Arial", 12), fg="black", relief="raised", bg="white", justify="center")

janela.mainloop()

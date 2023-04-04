#Importando biblioteca necessária
import customtkinter

#criando tela principal com o modo escuro
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#criando variável janela para visualizar a tela
janela = customtkinter.CTk()
#tamanho da janela
janela.geometry("500x300")

#Função clique
def clique():
    print("Login concluído")

#Elementos da tela
texto = customtkinter.CTkLabel(janela,text="Fazer login")

email = customtkinter.CTkEntry(janela,placeholder_text="E-mail")

senha = customtkinter.CTkEntry(janela,placeholder_text="Senha",show="*")

botao = customtkinter.CTkButton(janela,text="Login",command=clique)

#Organizando cada elemento da tela
texto.pack(padx=10,pady=10)
email.pack(padx=10,pady=10)
senha.pack(padx=10,pady=10)
botao.pack(padx=10,pady=10)

#Vizualisando
janela.mainloop()

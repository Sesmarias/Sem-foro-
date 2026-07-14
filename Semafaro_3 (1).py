from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
import math
import numpy as np
import tkinter.messagebox
import os
import random
from PIL import ImageTk, Image
import winsound
 

Semafaro = Tk()
Semafaro.title("Jogo do Semáfaro (Programado por Nilson Moreira e Vánia Moreira)")
Semafaro.geometry("800x570")
Semafaro.wm_resizable(False, False) # impede de redimensionar a janela
Semafaro.configure(bg="white")  # define a cor de fundo da janela
Semafaro.iconbitmap('semafaro.ico')

matriz = np.zeros((4, 4))

def bar1():
    import time
    for i in range(10, 101, 1):
        progress_bar_jog1['value'] = i
        Semafaro.update_idletasks()
        time.sleep(0.001)

def bar2():
    import time
    for i in range(10, 101, 1):
        progress_bar_jog2['value'] = i
        Semafaro.update_idletasks()
        time.sleep(0.001)

def fazer_nada(event):
    pass


M = np.ndarray([1,4,4], dtype=int)
M[0] = matriz 

vez_do_comp_ou_jog2 = 1
control_bar = 0
jj = 1
def mudar_cor(i, j):
    # toca beep sempre que clica
    if som_ligado == 1:
        winsound.Beep(500, 150)  # 500Hz por 150ms

    global M, matriz, a, control_bar, vez_do_comp_ou_jog2, comput, jj, ind_ret_ava

    if control_bar == 0:
        check_1.configure(image=image6)
        check_2.configure(image=image5)
        bar1()
        control_bar = 1
    else:
        check_1.configure(image=image5)
        check_2.configure(image=image6)
        bar2()
        control_bar = 0

    if matriz[i, j] == 0:
        a[4*j+i].config(bg="green")
        matriz[i, j] = 1
    elif matriz[i, j] == 1:
        a[4*j+i].config(bg="yellow")
        matriz[i, j] = 2
    elif matriz[i, j] == 2:
        a[4*j+i].config(bg="red")
        matriz[i, j] = 3
        a[4*j+i].config(state="disabled", bg="red", activebackground="red")
        a[4*j+i].bind("<Button-1>", fazer_nada)

    M.resize([jj+1, 4, 4], refcheck=False)
    M[jj] = matriz   
    jj += 1      
    ind_ret_ava = jj - 2
    retroc.config(state="normal")
    retroc.bind("<Button-1>", retroceder)
    verificar_vencedor(i, j)
    if comput == 1:
        if vez_do_comp_ou_jog2 == 1:
            movimento_computador()
        else:
            vez_do_comp_ou_jog2 = 1
    else:
        if vez_do_comp_ou_jog2 == 1:
            vez_do_comp_ou_jog2 = 0
        else:
            vez_do_comp_ou_jog2 = 1

def reiniciar_fechar():   
    global M, jj, control_bar

    novo_jogo = tkinter.messagebox.askyesno("Jogar/Fechar", "Quer jogar novamente?")
    if novo_jogo == True:
        pass
    else:
        Semafaro.quit()
    for i in range(16):
        a[i].config(bg="gray")
        a[i].config(state="normal")
    matriz[:,:] = 0    
    vez_do_comp_ou_jog2 == 1
    atual.config(state="disabled")
    atual.bind("<Button-1>", fazer_nada) 
    avanc.config(state="disabled")
    avanc.bind("<Button-1>", fazer_nada) 
    retroc.config(state="disabled")
    retroc.bind("<Button-1>", fazer_nada)
    M = None
    M = np.ndarray([1,4,4], dtype=int)
    M[0] = matriz 
    jj = 1
    #control_bar = 0

def verificar_vencedor(i, j):
    global matriz, pontos_jog1, pontos_jog2
    # Verificar sequência à direita da ficha selecionada
    if 3-j >= 2:
        if matriz[i, j] == matriz[i, j+1] and matriz[i, j+1] == matriz[i, j+2]:
            if vez_do_comp_ou_jog2 == 1: # último a jogar foi o jogador 1
                vencedor = 'Vencedor: '+jog1['text']
                pontos_jog1 += 1
                pontos_label_jog1.config(text=pontos_jog1)
                if comput == 1:
                    control_bar = 1 
                    check_1.configure(image=image5)
                    check_2.configure(image=image6)
            else:
                vencedor = 'Vencedor: '+jog2['text']
                pontos_jog2 += 1
                pontos_label_jog2.config(text=pontos_jog2)                
            tkinter.messagebox.showinfo("FIM do JOGO!", vencedor, default='ok')   
            reiniciar_fechar()         
            return    
    # Verificar sequência à esquerda
    if j > 1:
        if matriz[i, j] == matriz[i, j-1] and matriz[i, j-1] == matriz[i, j-2]:
            if vez_do_comp_ou_jog2 == 1:
                vencedor = 'Vencedor: '+jog1['text']
                pontos_jog1 += 1
                pontos_label_jog1.config(text=pontos_jog1)
                if comput == 1:
                    control_bar = 1 
                    check_1.configure(image=image5)
                    check_2.configure(image=image6)
            else:
                vencedor = 'Vencedor: '+jog2['text']
                pontos_jog2 += 1
                pontos_label_jog2.config(text=pontos_jog2)                 
            tkinter.messagebox.showinfo("FIM do JOGO!", vencedor, default='ok')  
            reiniciar_fechar()         
            return
    # Verificar sequência abaixo
    if 3-i >= 2:
        if matriz[i, j] == matriz[i+1, j] and matriz[i+1, j] == matriz[i+2, j]:
            if vez_do_comp_ou_jog2 == 1:
                vencedor = 'Vencedor: '+jog1['text']
                pontos_jog1 += 1
                pontos_label_jog1.config(text=pontos_jog1)
                if comput == 1:
                    control_bar = 1 
                    check_1.configure(image=image5)
                    check_2.configure(image=image6)
            else:
                vencedor = 'Vencedor: '+jog2['text']
                pontos_jog2 += 1
                pontos_label_jog2.config(text=pontos_jog2)                 
            tkinter.messagebox.showinfo("FIM do JOGO!", vencedor, default='ok')  
            reiniciar_fechar()         
            return
    # Verificar sequência acima
    if i > 1:
        if matriz[i, j] == matriz[i-1, j] and matriz[i-1, j] == matriz[i-2, j]:
            if vez_do_comp_ou_jog2 == 1:
                vencedor = 'Vencedor: '+jog1['text']
                pontos_jog1 += 1
                pontos_label_jog1.config(text=pontos_jog1)
                if comput == 1:
                    control_bar = 1 
                    check_1.configure(image=image5)
                    check_2.configure(image=image6)
            else:
                vencedor = 'Vencedor: '+jog2['text']
                pontos_jog2 += 1
                pontos_label_jog2.config(text=pontos_jog2)                 
            tkinter.messagebox.showinfo("FIM do JOGO!", vencedor, default='ok')  
            reiniciar_fechar()         
            return
    # Verificar sequência onde a ficha selecionada é o centro
    # Caso 1: A ficha está na primeira ou última linhas, a partir da segunda coluna até a penúltima
    if (i == 0 or i == 3) and (j >= 1 and j < 3):
        if matriz[i, j-1] == matriz[i, j] and matriz[i, j] == matriz[i, j+1]:
            if vez_do_comp_ou_jog2 == 1:
                vencedor = 'Vencedor: '+jog1['text']
                pontos_jog1 += 1
                pontos_label_jog1.config(text=pontos_jog1)
                if comput == 1:
                    control_bar = 1 
                    check_1.configure(image=image5)
                    check_2.configure(image=image6)
            else:
                vencedor = 'Vencedor: '+jog2['text']
                pontos_jog2 += 1
                pontos_label_jog2.config(text=pontos_jog2)                 
            tkinter.messagebox.showinfo("FIM do JOGO!", vencedor, default='ok')  
            reiniciar_fechar()         
            return
    # Caso 2: A ficha está na primeira ou última colunas, a partir da segunda linha até a penúltima
    if (i >= 1 and i < 3) and (j == 0 or j == 3):
        if matriz[i-1, j] == matriz[i, j] and matriz[i, j] == matriz[i+1, j]:
            if vez_do_comp_ou_jog2 == 1:
                vencedor = 'Vencedor: '+jog1['text']
                pontos_jog1 += 1
                pontos_label_jog1.config(text=pontos_jog1)
                if comput == 1:
                    control_bar = 1 
                    check_1.configure(image=image5)
                    check_2.configure(image=image6)
            else:
                vencedor = 'Vencedor: '+jog2['text']
                pontos_jog2 += 1
                pontos_label_jog2.config(text=pontos_jog2)                 
            tkinter.messagebox.showinfo("FIM do JOGO!", vencedor, default='ok')  
            reiniciar_fechar()         
            return
    # Caso 3: A ficha não está nem na primeira e última colunas, nem na primeira e última linhas
    if i >= 1 and i < 3 and j >=1 and j < 3:
        if matriz[i-1, j] == matriz[i, j] and matriz[i, j] == matriz[i+1, j]:
            if vez_do_comp_ou_jog2 == 1:
                vencedor = 'Vencedor: '+jog1['text']
                pontos_jog1 += 1
                pontos_label_jog1.config(text=pontos_jog1)
                if comput == 1:
                    control_bar = 1 
                    check_1.configure(image=image5)
                    check_2.configure(image=image6)
            else:
                vencedor = 'Vencedor: '+jog2['text']
                pontos_jog2 += 1
                pontos_label_jog2.config(text=pontos_jog2)                 
            tkinter.messagebox.showinfo("FIM do JOGO!", vencedor, default='ok')  
            reiniciar_fechar()         
            return
        if matriz[i, j-1] == matriz[i, j] and matriz[i, j] == matriz[i, j+1]:
            if vez_do_comp_ou_jog2 == 1:
                vencedor = 'Vencedor: '+jog1['text']
                pontos_jog1 += 1
                pontos_label_jog1.config(text=pontos_jog1)
                if comput == 1:
                    control_bar = 1 
                    check_1.configure(image=image5)
                    check_2.configure(image=image6)
            else:
                vencedor = 'Vencedor: '+jog2['text']
                pontos_jog2 += 1
                pontos_label_jog2.config(text=pontos_jog2)                 
            tkinter.messagebox.showinfo("FIM do JOGO!", vencedor, default='ok')  
            reiniciar_fechar()         
            return
    # Verificação nas diagonais
    # Diagonal principal, a partir da linha 1 
    if i == j and i <= 3-2:
        if matriz[i+1, j+1] == matriz[i, j] and matriz[i, j] == matriz[i+2, j+2]:
            if vez_do_comp_ou_jog2 == 1:
                vencedor = 'Vencedor: '+jog1['text']
                pontos_jog1 += 1
                pontos_label_jog1.config(text=pontos_jog1)
                if comput == 1:
                    control_bar = 1 
                    check_1.configure(image=image5)
                    check_2.configure(image=image6)
            else:
                vencedor = 'Vencedor: '+jog2['text']
                pontos_jog2 += 1
                pontos_label_jog2.config(text=pontos_jog2)                 
            tkinter.messagebox.showinfo("FIM do JOGO!", vencedor, default='ok')  
            reiniciar_fechar()         
            return
    # Diagonal principal, da última linha à terceira 
    if i == j and i >= 2:
        if matriz[i-1, j-1] == matriz[i, j] and matriz[i, j] == matriz[i-2, j-2]:
            if vez_do_comp_ou_jog2 == 1:
                vencedor = 'Vencedor: '+jog1['text']
                pontos_jog1 += 1
                pontos_label_jog1.config(text=pontos_jog1)
                if comput == 1:
                    control_bar = 1 
                    check_1.configure(image=image5)
                    check_2.configure(image=image6)
            else:
                vencedor = 'Vencedor: '+jog2['text']
                pontos_jog2 += 1
                pontos_label_jog2.config(text=pontos_jog2)                 
            tkinter.messagebox.showinfo("FIM do JOGO!", vencedor, default='ok')  
            reiniciar_fechar()         
            return
    # Verificar sequência da diagonal principal, onde a ficha selecionada é o centro
    if i == j and i >= 1 and i < 3:
        if matriz[i-1, j-1] == matriz[i, j] and matriz[i, j] == matriz[i+1, j+1]:
            if vez_do_comp_ou_jog2 == 1:
                vencedor = 'Vencedor: '+jog1['text']
                pontos_jog1 += 1
                pontos_label_jog1.config(text=pontos_jog1)
                if comput == 1:
                    control_bar = 1 
                    check_1.configure(image=image5)
                    check_2.configure(image=image6)
            else:
                vencedor = 'Vencedor: '+jog2['text']
                pontos_jog2 += 1
                pontos_label_jog2.config(text=pontos_jog2)                 
            tkinter.messagebox.showinfo("FIM do JOGO!", vencedor, default='ok')  
            reiniciar_fechar()         
            return
    # 1ª Super Diagonal 
    if j - i == 1:
        if matriz[0, 1] == matriz[1, 2] and matriz[1, 2] == matriz[2, 3]:
            if vez_do_comp_ou_jog2 == 1:
                vencedor = 'Vencedor: '+jog1['text']
                pontos_jog1 += 1
                pontos_label_jog1.config(text=pontos_jog1)
                if comput == 1:
                    control_bar = 1 
                    check_1.configure(image=image5)
                    check_2.configure(image=image6)
            else:
                vencedor = 'Vencedor: '+jog2['text']
                pontos_jog2 += 1
                pontos_label_jog2.config(text=pontos_jog2)                 
            tkinter.messagebox.showinfo("FIM do JOGO!", vencedor, default='ok')  
            reiniciar_fechar()         
            return
    # 1ª Sub Diagonal 
    if i - j == 1:
        if matriz[1, 0] == matriz[2, 1] and matriz[2, 1] == matriz[3, 2]:
            if vez_do_comp_ou_jog2 == 1:
                vencedor = 'Vencedor: '+jog1['text']
                pontos_jog1 += 1
                pontos_label_jog1.config(text=pontos_jog1)
                if comput == 1:
                    control_bar = 1 
                    check_1.configure(image=image5)
                    check_2.configure(image=image6)
            else:
                vencedor = 'Vencedor: '+jog2['text']
                pontos_jog2 += 1
                pontos_label_jog2.config(text=pontos_jog2)                 
            tkinter.messagebox.showinfo("FIM do JOGO!", vencedor, default='ok')  
            reiniciar_fechar()         
            return
    # Diagonal secundária (da direita para esquerda)
    if i + j == 3 and i <= 3-2:
        if matriz[i+1, j-1] == matriz[i, j] and matriz[i, j] == matriz[i+2, j-2]:
            if vez_do_comp_ou_jog2 == 1:
                vencedor = 'Vencedor: '+jog1['text']
                pontos_jog1 += 1
                pontos_label_jog1.config(text=pontos_jog1)
                if comput == 1:
                    control_bar = 1 
                    check_1.configure(image=image5)
                    check_2.configure(image=image6)
            else:
                vencedor = 'Vencedor: '+jog2['text']
                pontos_jog2 += 1
                pontos_label_jog2.config(text=pontos_jog2)                 
            tkinter.messagebox.showinfo("FIM do JOGO!", vencedor, default='ok')  
            reiniciar_fechar()         
            return
    # Diagonal secundária (da esquerda para direita)
    if i + j == 3 and i > 3-2:
        if matriz[i-1, j+1] == matriz[i, j] and matriz[i, j] == matriz[i-2, j+2]:
            if vez_do_comp_ou_jog2 == 1:
                vencedor = 'Vencedor: '+jog1['text']
                pontos_jog1 += 1
                pontos_label_jog1.config(text=pontos_jog1)
                if comput == 1:
                    control_bar = 1 
                    check_1.configure(image=image5)
                    check_2.configure(image=image6)
            else:
                vencedor = 'Vencedor: '+jog2['text']
                pontos_jog2 += 1
                pontos_label_jog2.config(text=pontos_jog2)                 
            tkinter.messagebox.showinfo("FIM do JOGO!", vencedor, default='ok')  
            reiniciar_fechar()         
            return
    # Diagonal secundária (verificar os centros)
    if i + j == 3 and i < 3 and i > 0:
        if matriz[i-1, j+1] == matriz[i, j] and matriz[i, j] == matriz[i+1, j-1]:
            if vez_do_comp_ou_jog2 == 1:
                vencedor = 'Vencedor: '+jog1['text']
                pontos_jog1 += 1
                pontos_label_jog1.config(text=pontos_jog1)
                if comput == 1:
                    control_bar = 1 
                    check_1.configure(image=image5)
                    check_2.configure(image=image6)
            else:
                vencedor = 'Vencedor: '+jog2['text']
                pontos_jog2 += 1
                pontos_label_jog2.config(text=pontos_jog2)                 
            tkinter.messagebox.showinfo("FIM do JOGO!", vencedor, default='ok')  
            reiniciar_fechar()         
            return
    # 1ª Super Diagonal secundária
    if j + i == 2:
        if matriz[0, 2] == matriz[1, 1] and matriz[1, 1] == matriz[2, 0]:
            if vez_do_comp_ou_jog2 == 1:
                vencedor = 'Vencedor: '+jog1['text']
                pontos_jog1 += 1
                pontos_label_jog1.config(text=pontos_jog1)
                if comput == 1:
                    control_bar = 1 
                    check_1.configure(image=image5)
                    check_2.configure(image=image6)
            else:
                vencedor = 'Vencedor: '+jog2['text']
                pontos_jog2 += 1
                pontos_label_jog2.config(text=pontos_jog2)                 
            tkinter.messagebox.showinfo("FIM do JOGO!", vencedor, default='ok')  
            reiniciar_fechar()         
            return
    # 1ª Sub Diagonal secundária 
    if i + j == 4:
        if matriz[1, 3] == matriz[2, 2] and matriz[2, 2] == matriz[3, 1]:
            if vez_do_comp_ou_jog2 == 1:
                vencedor = 'Vencedor: '+jog1['text']
                pontos_jog1 += 1
                pontos_label_jog1.config(text=pontos_jog1)
                if comput == 1:
                    control_bar = 1 
                    check_1.configure(image=image5)
                    check_2.configure(image=image6)
            else:
                vencedor = 'Vencedor: '+jog2['text']
                pontos_jog2 += 1
                pontos_label_jog2.config(text=pontos_jog2)                 
            tkinter.messagebox.showinfo("FIM do JOGO!", vencedor, default='ok')  
            reiniciar_fechar()         
            return

comput = 0

def comp_jog2(event):
    global comput, nome_jog_2, a, control_bar, pontos_jog1, pontos_jog2, vez_do_comp_ou_jog2    
    #Iniciar()    
    if comput == 0:
        jog2.config(text="Computador")  
        control_bar = 0    
        vez_do_comp_ou_jog2 = 1  
        check_1.configure(image=image5)
        check_2.configure(image=image6)
        pontos_jog1 = 0
        pontos_jog2 = 0    
        pontos_label_jog1.config(text=pontos_jog1)
        pontos_label_jog2.config(text=pontos_jog2)
        # Fonte de imagem: https://www.visualpharm.com/free-icons/person-595b40b75ba036ed117da139
        image0 = Image.open("person.png")
        image0 = image0.resize((70, 70), Image.Resampling.LANCZOS)
        image0 = ImageTk.PhotoImage(image0)     
        imagem_comp_jog2.configure(image=image0) 
        imagem_comp_jog2.image=image0
        comput = 1        
        for i in range(16):
            a[i].config(bg="gray")
            matriz[:,:] = 0    
    else:
        nome_jog_2 = pedir_nome_jogador("Nome do Jogador 2", "Digite o nome do jogador 2:")
        if nome_jog_2 and nome_jog_2.strip():
            jog2.config(text=nome_jog_2.strip())
        else:
            jog2.config(text="Jogador 2")
        try:
            if len(nome_jog_2.strip()) != 0:
                jog2.config(text=nome_jog_2.strip())
        except:
            pass
        pontos_jog1 = 0
        pontos_jog2 = 0  
        pontos_label_jog1.config(text=pontos_jog1)
        pontos_label_jog2.config(text=pontos_jog2)
        image0 = Image.open("computer.png")
        image0 = image0.resize((70, 70), Image.Resampling.LANCZOS)
        image0 = ImageTk.PhotoImage(image0) 
        imagem_comp_jog2.configure(image=image0) 
        imagem_comp_jog2.image=image0
        comput = 0 
        for i in range(16):
            a[i].config(bg="gray")
            matriz[:,:] = 0 

def mov_vitoria(matriz):
    lista = []
    for i in range(4):
        for j in range(4):
            if i > 0 and i < 3 and j > 0 and j < 3 and matriz[i, j] != 0:
                if matriz[i, j] == matriz[i, j+1] and matriz[i, j] - matriz[i, j-1] == 1:
                    lista.append((i, j-1))
                if matriz[i, j] == matriz[i, j-1] and matriz[i, j] - matriz[i, j+1] == 1:
                    lista.append((i, j+1))
                if matriz[i, j] == matriz[i-1, j] and matriz[i, j] - matriz[i+1, j] == 1:
                    lista.append((i+1, j))
                if matriz[i, j] == matriz[i+1, j] and matriz[i, j] - matriz[i-1, j] == 1:
                    lista.append((i-1, j))
                if matriz[i, j] == matriz[i+1, j+1] and matriz[i, j] - matriz[i-1, j-1] == 1:
                    lista.append((i-1, j-1))
                if matriz[i, j] == matriz[i-1, j+1] and matriz[i, j] - matriz[i+1, j-1] == 1:
                    lista.append((i+1, j-1))
                if matriz[i, j] == matriz[i-1, j-1] and matriz[i, j] - matriz[i+1, j+1] == 1:
                    lista.append((i+1, j+1))
                if matriz[i, j] == matriz[i+1, j-1] and matriz[i, j] - matriz[i-1, j+1] == 1:
                    lista.append((i-1, j+1))
            #------------- Linhas 1 e 4 --------------------------------------------------
            if (j == 1 or j == 2) and matriz[3, j] != 0: 
                if matriz[3, j] == matriz[3, j-1] and matriz[3, j] - matriz[3, j+1] == 1:
                    lista.append((3, j+1))
            if (j == 1 or j == 2) and matriz[3, j+1] != 0: 
                if matriz[3, j+1] == matriz[3, j] and matriz[3, j+1] - matriz[3, j-1] == 1:
                    lista.append((3, j-1))
            if (j == 1 or j == 2) and matriz[0, j] != 0: 
                if matriz[0, j] == matriz[0, j-1] and matriz[0, j] - matriz[0, j+1] == 1:
                    lista.append((0, j+1))
            if (j == 1 or j == 2) and matriz[0, j+1] != 0: 
                if matriz[0, j+1] == matriz[0, j] and matriz[0, j+1] - matriz[0, j-1] == 1:
                    lista.append((0, j-1))      
            #-------------------------------------------------------------------------------
            #------------- Colunas 1 e 4 ---------------------------------------------------
            if (i == 1 or i == 2) and matriz[i, 3] != 0: 
                if matriz[i, 3] == matriz[i-1, 3] and matriz[i, 3] - matriz[i+1, 3] == 1:
                    lista.append((i+1, 3))
            if (i == 1 or i == 2) and matriz[i+1, 3] != 0: 
                if matriz[i+1, 3] == matriz[i, 3] and matriz[i+1, 3] - matriz[i-1, 3] == 1:
                    lista.append((i-1, 3))
            if (i == 1 or i == 2) and matriz[i, 0] != 0: 
                if matriz[i, 0] == matriz[i-1, 0] and matriz[i, 0] - matriz[i+1, 0] == 1:
                    lista.append((i+1, 0))
            if (i == 1 or i == 2) and matriz[i+1, 0] != 0: 
                if matriz[i+1, 0] == matriz[i, 0] and matriz[i+1, 0] - matriz[i-1, 0] == 1:
                    lista.append((i-1, 0))      
            #-------------------------------------------------------------------------------  
            #----------------- Diagonais (pricipal e secundária) ---------------------------        
            if (i == 0 or i == 1) and matriz[i, j] != 0:
                if matriz[i, j] == matriz[i+2, j] and matriz[i, j] - matriz[i+1, j] == 1:
                    lista.append((i+1, j))
            if (j == 0 or j == 1) and matriz[i, j] != 0:
                if matriz[i, j] == matriz[i, j+2] and matriz[i, j] - matriz[i, j+1] == 1:
                    lista.append((i, j+1))
            if (i == 0 or i == 1) and matriz[i, i] != 0:
                if matriz[i, i] == matriz[i+2, i+2] and matriz[i, i] - matriz[i+1, i+1] == 1:
                    lista.append((i+1, i+1))
    #--------------------------------------------------------------------------------------------
    #----------- Sub e super diagonais ----------------------------------------------------------
    if matriz[1, 0] == matriz[3, 2] and matriz[1, 0] - matriz[2, 1] == 1 and matriz[1, 0] != 0:
        lista.append((2, 1))
    if matriz[0, 1] == matriz[2, 3] and matriz[0, 1] - matriz[1, 2] == 1 and matriz[0, 1] != 0:
        lista.append((1, 2))
    if matriz[2, 0] == matriz[0, 2] and matriz[2, 0] - matriz[1, 1] == 1 and matriz[2, 0] != 0:
        lista.append((1, 1))
    if matriz[3, 1] == matriz[1, 3] and matriz[3, 1] - matriz[2, 2] == 1 and matriz[3, 1] != 0:
        lista.append((2, 2))
    if matriz[0, 3] == matriz[2, 1] and matriz[0, 3] - matriz[1, 2] == 1 and matriz[0, 3] != 0:
        lista.append((1, 2))
    if matriz[3, 0] == matriz[1, 2] and matriz[3, 0] - matriz[2, 1] == 1 and matriz[3, 0] != 0:
        lista.append((2, 1))
    #----------------------------------------------------------------------------------------------
    return list(set(lista)) 

v = [(i, j) for i in range(4) for j in range(4)]
def movimento_computador():
    global matriz, a, vez_do_comp_ou_jog2, v, M, jj, ind_ret_ava 
    lista = []
    lista = mov_vitoria(matriz)
    if len(lista) != 0:
        vez_do_comp_ou_jog2 = 0
        mudar_cor(lista[0][0], lista[0][1])        
    else:
        w = v.copy()        
        while True:  
            if len(w) != 0:    
                aux = random.sample(w, 1)
                pos_i_j = aux[0]
                i = pos_i_j[0]
                j = pos_i_j[1]
                if matriz[i, j] != 3:
                    matriz_teste = matriz.copy()
                    matriz_teste[i, j] = matriz_teste[i, j] + 1 
                    lista_teste = [] 
                    lista_teste = mov_vitoria(matriz_teste) 
                    if len(lista_teste) == 0:
                        vez_do_comp_ou_jog2 = 0
                        mudar_cor(i, j)
                        #M.resize([jj+1, 4, 4], refcheck=False)
                        #M[jj] = matriz   
                        #jj += 1
                        #ind_ret_ava = jj - 2
                        break
                    else:
                        i_derrota = i
                        j_derrota = j
                        w.remove((i, j))
                else:
                    w.remove((i, j))
            else:
                vez_do_comp_ou_jog2 = 0
                mudar_cor(i_derrota, j_derrota)
                #M.resize([jj+1, 4, 4], refcheck=False)
                #M[jj] = matriz   
                #jj += 1
                #ind_ret_ava = jj - 2
                break

#def som():
    #import winsound as ws
    #ws.Beep(440, 500) # Toca um beep de 440Hz durante 500ms
    #ws.MessageBeep(type=-1) # Toca um som padrão do Windows

    #import beepy as bp
    #bp.beep(sound=4) # Toca um som predefinido (0 a 6)


def retroceder(event):
    global M, a, matriz_ret_avanc, ind_ret_ava 

    matriz_ret_avanc = M[ind_ret_ava]
    for i in range(4):
        for j in range(4):
            if matriz_ret_avanc[i, j] == 1:
                a[4*j+i].config(bg="green")
            elif matriz_ret_avanc[i, j] == 2:
                a[4*j+i].config(bg="yellow")
            elif matriz_ret_avanc[i, j] == 3:
                a[4*j+i].config(bg="red")
            elif matriz_ret_avanc[i, j] == 0:
                a[4*j+i].config(bg="gray")
    vez = divmod(ind_ret_ava, 2)
    if vez[1] == 1:
        check_1.configure(image=image6)
        check_2.configure(image=image5)
    else:
        check_1.configure(image=image5)
        check_2.configure(image=image6)
    ind_ret_ava -= 1
    if ind_ret_ava < 0:
        retroc.config(state="disabled")
        retroc.bind("<Button-1>", fazer_nada)
    avanc.config(state="normal")
    avanc.bind("<Button-1>", avancar) 
    atual.config(state="normal") 
    atual.bind("<Button-1>", atualizar)
    bloq() 

def avancar(event):
    global M, a, ind_ret_ava, matriz_ret_avanc 

    ind_ret_ava += 1
    matriz_ret_avanc = M[ind_ret_ava + 1]
    for i in range(4):
        for j in range(4):
            if matriz_ret_avanc[i, j] == 1:
                a[4*j+i].config(bg="green")
            elif matriz_ret_avanc[i, j] == 2:
                a[4*j+i].config(bg="yellow")
            elif matriz_ret_avanc[i, j] == 3:
                a[4*j+i].config(bg="red")
            elif matriz_ret_avanc[i, j] == 0:
                a[4*j+i].config(bg="gray")
    vez = divmod(ind_ret_ava, 2)
    if vez[1] == 0:
        check_1.configure(image=image6)
        check_2.configure(image=image5)
    else:
        check_1.configure(image=image5)
        check_2.configure(image=image6)     
    if ind_ret_ava > jj - 3:
        avanc.config(state="disabled")
        avanc.bind("<Button-1>", fazer_nada)
    retroc.config(state="normal")
    retroc.bind("<Button-1>", retroceder)
    atual.config(state="normal")
    atual.bind("<Button-1>", atualizar)
    bloq()

def atualizar(event):
    global matriz, jj, ind_ret_ava

    ind_ret_ava = jj - 2

    for i in range(4):
        for j in range(4):
            if matriz[i, j] == 1:
                a[4*j+i].config(bg="green")
            elif matriz[i, j] == 2:
                a[4*j+i].config(bg="yellow")
            elif matriz[i, j] == 3:
                a[4*j+i].config(bg="red")
            elif matriz[i, j] == 0:
                a[4*j+i].config(bg="gray")

    retroc.config(state="normal")
    retroc.bind("<Button-1>", retroceder)

    avanc.config(state="disabled")
    avanc.bind("<Button-1>", fazer_nada)

    atual.config(state="disabled")
    atual.bind("<Button-1>", fazer_nada)    
    desbloq()

def bloq():
    for i in range(16):
        a[i].config(state="disabled")
        a[i].bind("<Button-1>", fazer_nada)

def desbloq():
    for i in range(16):
        a[i].config(state="normal")


progress_bar_jog2 = ttk.Progressbar(Semafaro, orient="horizontal", mode="determinate", length=325)
progress_bar_jog2.place(x=140, y=20)

progress_bar_jog1 = ttk.Progressbar(Semafaro, orient="horizontal", mode="determinate", length=325)
progress_bar_jog1.place(x=140, y=455)

frame_semafaro = LabelFrame(Semafaro, text="", fg="purple", font="lucida 25 bold")
frame_semafaro.place(x=100, y=120)

b11 = Button(frame_semafaro, height=3, width=9, text="", bd=0, bg="gray", fg="white", font="lucida 12 bold", command=lambda : mudar_cor(0, 0))
#b11.bind("<Button-1>", mudar_cor)
b11.grid(row=0, column=0, padx=6, pady=6)

b12 = Button(frame_semafaro, height=3, width=9, text="", bd=0, bg="gray", fg="white", font="lucida 12 bold", command=lambda : mudar_cor(0, 1))
#b12.bind("<Button-1>", mudar_cor)
b12.grid(row=0, column=1, padx=6, pady=6)

b13 = Button(frame_semafaro, height=3, width=9, text="", bd=0, bg="gray", fg="white", font="lucida 12 bold", command=lambda : mudar_cor(0, 2))
#b13.bind("<Button-1>", mudar_cor)
b13.grid(row=0, column=2, padx=6, pady=6)

b14 = Button(frame_semafaro, height=3, width=9, text="", bd=0, bg="gray", fg="white", font="lucida 12 bold", command=lambda : mudar_cor(0, 3))
#b14.bind("<Button-1>", mudar_cor)
b14.grid(row=0, column=3, padx=6, pady=6)

b21 = Button(frame_semafaro, height=3, width=9, text="", bd=0, bg="gray", fg="white", font="lucida 12 bold", command=lambda : mudar_cor(1, 0))
#b21.bind("<Button-1>", mudar_cor)
b21.grid(row=1, column=0, padx=6, pady=6)

b22 = Button(frame_semafaro, height=3, width=9, text="", bd=0, bg="gray", fg="white", font="lucida 12 bold", command=lambda : mudar_cor(1, 1))
#b22.bind("<Button-1>", mudar_cor)
b22.grid(row=1, column=1, padx=6, pady=6)

b23 = Button(frame_semafaro, height=3, width=9, text="", bd=0, bg="gray", fg="white", font="lucida 12 bold", command=lambda : mudar_cor(1, 2))
#b23.bind("<Button-1>", mudar_cor)
b23.grid(row=1, column=2, padx=6, pady=6)

b24 = Button(frame_semafaro, height=3, width=9, text="", bd=0, bg="gray", fg="white", font="lucida 12 bold", command=lambda : mudar_cor(1, 3))
#b24.bind("<Button-1>", mudar_cor)
b24.grid(row=1, column=3, padx=6, pady=6)

b31 = Button(frame_semafaro, height=3, width=9, text="", bd=0, bg="gray", fg="white", font="lucida 12 bold", command=lambda : mudar_cor(2, 0))
#b31.bind("<Button-1>", mudar_cor)
b31.grid(row=2, column=0, padx=6, pady=6)

b32 = Button(frame_semafaro, height=3, width=9, text="", bd=0, bg="gray", fg="white", font="lucida 12 bold", command=lambda : mudar_cor(2, 1))
#b32.bind("<Button-1>", mudar_cor)
b32.grid(row=2, column=1, padx=6, pady=6)

b33 = Button(frame_semafaro, height=3, width=9, text="", bd=0, bg="gray", fg="white", font="lucida 12 bold", command=lambda : mudar_cor(2, 2))
#b33.bind("<Button-1>", mudar_cor)
b33.grid(row=2, column=2, padx=6, pady=6)

b34 = Button(frame_semafaro, height=3, width=9, text="", bd=0, bg="gray", fg="white", font="lucida 12 bold", command=lambda : mudar_cor(2, 3))
#b34.bind("<Button-1>", mudar_cor)
b34.grid(row=2, column=3, padx=6, pady=6)

b41 = Button(frame_semafaro, height=3, width=9, text="", bd=0, bg="gray", fg="white", font="lucida 12 bold", command=lambda : mudar_cor(3, 0))
#b41.bind("<Button-1>", mudar_cor)
b41.grid(row=3, column=0, padx=6, pady=6)

b42 = Button(frame_semafaro, height=3, width=9, text="", bd=0, bg="gray", fg="white", font="lucida 12 bold", command=lambda : mudar_cor(3, 1))
#b42.bind("<Button-1>", mudar_cor)
b42.grid(row=3, column=1, padx=6, pady=6)

b43 = Button(frame_semafaro, height=3, width=9, text="", bd=0, bg="gray", fg="white", font="lucida 12 bold", command=lambda : mudar_cor(3, 2))
#b43.bind("<Button-1>", mudar_cor)
b43.grid(row=3, column=2, padx=6, pady=6)

b44 = Button(frame_semafaro, height=3, width=9, text="", bd=0, bg="gray", fg="white", font="lucida 12 bold", command=lambda : mudar_cor(3, 3))
#b44.bind("<Button-1>", mudar_cor)
b44.grid(row=3, column=3, padx=6, pady=6)


a = (b11, b21, b31, b41, b12, b22, b32, b42, b13, b23, b33, b43, b14, b24, b34, b44)

# Fonte de imagem: https://commons.wikimedia.org/wiki/File:Gnome-computer.svg
nome_image = "computer.png"
image0 = Image.open(nome_image)
image0 = image0.resize((70, 70), Image.Resampling.LANCZOS)
image0 = ImageTk.PhotoImage(image0)
imagem_comp_jog2 = Button(Semafaro, text="",  image=image0, bd=0, bg="white", font="lucida 12 bold", compound=RIGHT)
imagem_comp_jog2.place(x=595, y=120)
imagem_comp_jog2.bind("<Button-1>", comp_jog2)

# Fonte de imagem: https://play.google.com/store/apps/details?id=com.stedi.poweroffclick&hl=en&gl=US
image1 = Image.open('btn_off.png')
image1 = image1.resize((70, 70), Image.Resampling.LANCZOS)
image1 = ImageTk.PhotoImage(image1)
reiniciar = Button(Semafaro, image=image1, bg="white", bd=0, command=lambda : reiniciar_fechar())
reiniciar.place(x=685, y=120)
#reiniciar.bind("<Button-1>", reiniciar_fechar)

# Fonte de Imagem: https://br.vexels.com/png-svg/previsualizar/135197/icone-plano-do-botao-retroceder-02
image2 = Image.open('retroceder.png')
image2 = image2.resize((75, 70), Image.Resampling.LANCZOS)
image2 = ImageTk.PhotoImage(image2)
retroc = Button(Semafaro, image=image2, bg="white", bd=0)
retroc.place(x=595, y=210)
retroc.bind("<Button-1>", retroceder)


image3 = Image.open('play.png')
image3 = image3.resize((160, 80), Image.Resampling.LANCZOS)
image3 = ImageTk.PhotoImage(image3)
atual = Button(Semafaro, image=image3, bg="white", bd=0)
atual.place(x=595, y=300)
atual.bind("<Button-1>", atualizar)

image4 = Image.open('avancar.png')
image4 = image4.resize((70, 70), Image.Resampling.LANCZOS)
image4 = ImageTk.PhotoImage(image4)
avanc = Button(Semafaro, image=image4, bg="white", bd=0)
avanc.place(x=685, y=210)
avanc.bind("<Button-1>", avancar)

atual.config(state="disabled")
atual.bind("<Button-1>", fazer_nada) 
avanc.config(state="disabled")
avanc.bind("<Button-1>", fazer_nada) 
retroc.config(state="disabled")
retroc.bind("<Button-1>", fazer_nada)

image5 = Image.open('not.png')
image5 = image5.resize((70, 76), Image.Resampling.LANCZOS)
image5 = ImageTk.PhotoImage(image5)
check_1 = Label(Semafaro, image=image5, bg="white", bd=0)
check_1.place(x=475, y=25)


image6 = Image.open('check.png')
image6 = image6.resize((70, 76), Image.Resampling.LANCZOS)
image6 = ImageTk.PhotoImage(image6)
check_2 = Label(Semafaro, image=image6, bg="white", bd=0)
check_2.place(x=475, y=460)

# Placar
pontos_jog1 = tkinter.IntVar()
pontos_jog1 = 0
pontos_label_jog1 = Label(Semafaro, text=pontos_jog1, height=2, width=3, bg="white", fg="blue", font="lucida 30 bold")
pontos_label_jog1.place(x=50, y=450)

pontos_jog2 = tkinter.IntVar()
pontos_jog2 = 0
pontos_label_jog2 = Label(Semafaro, text=pontos_jog2, height=2, width=3, bg="white", fg="blue", font="lucida 30 bold")
pontos_label_jog2.place(x=50, y=15)

nome_jog_1 = tkinter.StringVar()
jog1 = Label(Semafaro, text=nome_jog_1, fg="blue", font="lucida 25 bold")
jog1.config(text="Jogador 1")
jog1.configure(bg="white")
jog1.place(x=230, y=480)

nome_jog_2 = tkinter.StringVar()
jog2 = Label(Semafaro, text=nome_jog_2, fg="blue", font="lucida 25 bold")
jog2.config(text="Jogador 2")
jog2.configure(bg="white")
jog2.place(x=230, y=45)

#Semafaro.withdraw()  # esconde a janela principal temporariamente


def escolher_opcao():
    top = Toplevel(Semafaro)
    top.title("Escolha o modo de jogo")
    top.geometry("300x150")
    top.configure(bg="white")
    top.wm_resizable(False, False) # impede de redimensionar a janela
    top.iconbitmap('semafaro.ico')

    escolha = []

    def contra_computador():
        escolha.append("computador")
        top.destroy()

    def contra_jogador():
        escolha.append("jogador")
        top.destroy()

    Label(top, text="Deseja jogar contra o computador?", font=("Arial", 12), bg="white").pack(pady=10)
    Button(top, text="Sim", width=10, command=contra_computador, bg="white").pack(pady=5)
    Button(top, text="Não", width=10, command=contra_jogador, bg="white").pack(pady=5)

    top.grab_set()
    Semafaro.wait_window(top)

    return escolha[0] if escolha else None


def pedir_nome_jogador(titulo, prompt):
    top = Toplevel(Semafaro)
    top.title(titulo)
    top.geometry("300x150")
    top.configure(bg="white")
    top.resizable(False, False)
    top.iconbitmap('semafaro.ico')

    # Label com fundo branco
    Label(top, text=prompt, font=("Arial", 12), bg="white").pack(pady=10)

    # Entry com fundo branco
    entry = Entry(top, font=("Arial", 12), bg="white", fg="black", insertbackground="black")
    entry.pack(pady=5)
    entry.focus()

    nome = []

    def confirmar():
        if entry.get().strip():
            nome.append(entry.get().strip())
        top.destroy()

    Button(top, text="OK", command=confirmar, bg="white").pack(pady=10)
    top.grab_set()
    Semafaro.wait_window(top)

    return nome[0] if nome else None


# Escolher modo de jogo
modo = escolher_opcao()

# Pedir nomes
if modo == "computador":
    nome_jog_1 = pedir_nome_jogador("Nome do Jogador", "Digite seu nome:")
    if nome_jog_1 and nome_jog_1.strip():
        jog1.config(text=nome_jog_1.strip())
    else:
        jog1.config(text="Jogador 1")
    nome_jog_2 = "Computador"
    jog2.config(text=nome_jog_2.strip())
    image0 = Image.open("person.png")
    image0 = image0.resize((70, 70), Image.Resampling.LANCZOS)
    image0 = ImageTk.PhotoImage(image0)
    imagem_comp_jog2.configure(image=image0)
    imagem_comp_jog2.image = image0
    comput=1
else:
    nome_jog_1 = pedir_nome_jogador("Nome do Jogador 1", "Digite o nome do jogador 1:")
    if nome_jog_1 and nome_jog_1.strip():
        jog1.config(text=nome_jog_1.strip())
    else:
        jog1.config(text="Jogador 1")
    nome_jog_2 = pedir_nome_jogador("Nome do Jogador 2", "Digite o nome do jogador 2:")
    if nome_jog_2 and nome_jog_2.strip():
        jog2.config(text=nome_jog_2.strip())
    else:
        jog2.config(text="Jogador 2")

#Semafaro.deiconify()  # mostra a janela principal novamente

som_ligado = 1

def alternar_som():
    global som_ligado  # necessário para alterar a variável global
    if som_ligado == 0:
        image7 = Image.open('comsom.png')
        image7 = image7.resize((70, 70), Image.Resampling.LANCZOS)
        image7 = ImageTk.PhotoImage(image7)
        btn_som.config(image=image7)
        btn_som.image=image7
        som_ligado = 1
        winsound.Beep(500, 150)  # 500Hz por 150ms  # toca imediatamente quando liga
    else:
        image7 = Image.open('semsom.png')
        image7 = image7.resize((70, 70), Image.Resampling.LANCZOS)
        image7 = ImageTk.PhotoImage(image7)
        btn_som.config(image=image7)
        btn_som.image=image7
        som_ligado = 0


image7 = Image.open('comsom.png')
image7 = image7.resize((70, 70), Image.Resampling.LANCZOS)
image7 = ImageTk.PhotoImage(image7)
btn_som = Button(Semafaro, image=image7, bg="white", bd=0, command=alternar_som)
btn_som.pack(pady=20)
btn_som.place(x=725, y=5)

#check_1 = Label(Semafaro, image=image5, bg="white", bd=0)

Semafaro.mainloop()
# Tkinter

---
## Definição
Uma biblioteca nativa do [[Python]] para criar [[Graphic User Interface|GUI]]. A referência para instanciar sua [[Classe]] principal é `Tk()`.

---
## Widgets
No Tkinter, todo widget precisa saber quem é seu pai, pois ele funciona como uma árvore de widgets. Para isso, basta passar um "parent" como argumento de qualquer widget — todo primeiro [[Função#Argumento|argumento]] de um widget é sua referência de "parent".

Todo widget deve chamar o [[Classe#Método|método]] "pack" para poder renderizar — `widget.pack()`.

---
## Ver uma demo
`py -m tkinter`
	
---
## Como importar em diferentes versões
* python2 — `import Tkinter as tk`
* python3 — `import tkinter as tk`

---
## [[Função#Parâmetro|Parâmetros]] — Tk()
* `className` — Definir o nome da janela
	* obs: `className` não aparece dependendo do SO
	* obs: o primeiro caractere é sempre minúsculo

---
## [[Classe#Método|Métodos]] — Tk()

Configurar a resolução da janela — string entre aspas duplas
`geometry(<resolution-width>x<resolution-height)`

Abrir uma janela
`mainloop()`

Colocar título na janela — string entre aspas duplas
`title.(<window-title>)`

`configure.()` — estilização da janela
* `bg=<hexcolor>` — cor de fundo

---
## tk.Text()

### [[Classe#Método|Métodos]]
`insert()`
* O primeiro argumento é o onde posicionar (utilizando números float entre strings)
* O segundo é o texto a ser inserido

---
## Referências
1. [DEVMEDIA — Tkinter: Interfaces gráficas em Python](https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956)
2. [Stack Overflow — TypeError: insert() missing 1 required positional argument: 'chars' duplicate](https://stackoverflow.com/questions/43436404/typeerror-insert-missing-1-required-positional-argument-chars)
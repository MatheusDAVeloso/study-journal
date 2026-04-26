# Tkinter

---
## Definição
Uma biblioteca nativa do [[python]] para criar [[Graphic User Interface|GUI]]. A referência para instanciar sua classe principal é `Tk()` que se buscar através de `tk.Tk()`.

No Tkinter, todo widget precisa saber que é seu pai, criando uma árvore de widgets. Para isso, basta passar um "parent" como argumento de qualquer widget.

---
## Ver uma demo
`py -m tkinter`
	
---
## Como importar em diferentes versões
* python2 — `import Tkinter as tk`
* python3 — `import tkinter as tk`

---
## Parâmetros — Tk()
* `className` — Definir o nome da janela
	* obs: `className` não aparece dependendo do SO
	* obs: o primeiro caractere é sempre minúsculo

---
## Métodos — Tk()

Configurar a resolução da janela — string entre aspas duplas
`geometry(<resolution-width>x<resolution-height)`

Abrir uma janela
`mainloop()`

Colocar título na janela — string entre aspas duplas
`title.(<window-title>)`

`configure.()` — estilização da janela
* `bg=<hexcolor>` — cor de fundo

---
## Referências
1. [DEVMEDIA — Tkinter: Interfaces gráficas em Python](https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956)
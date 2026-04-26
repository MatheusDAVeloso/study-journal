# Python

---
## Rodar um script
- `py <binary-path>`

---
## Importar bibliotecas

* `from <library> import <filter>` — especifica o que quer importar
	* se `<filter>` for `*`, importa tudo
* `import <library> as <alias>` — importando dando um apelido a biblioteca

---
## Erros de compilação

**`TypeError: 'module' object is not callable`**
	Quando se vai importar uma biblioteca como : `import <libraby> as <alias>`, `<alias>` será a biblioteca, não a classe dessa biblioteca. Para pode instanciar a classe, deve-se buscar a classe — `val a = <alias>.Alias()`

---
## Referências
1. [DEVMEDIA — Tkinter: Interfaces gráficas em Python](https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956)
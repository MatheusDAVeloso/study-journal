# Python

---
## Rodar um script
- `py <binary-path>`

---
## [[Construtor]]
* O [[construtor]] do python é declarado da seguinte forma: `__init()__`.
* O primeiro argumente deve ser `self`
* Não tem retorno

---
## Escopo de [[Variável na Informática|Variável]]
* Para acessar [[Variável na Informática|variável]] em qualquer lugar em uma [[Classe]], deve utilizar `self`.
* Não precisa declarar uma [[Variável na Informática|variável]] para poder usar, já pode usar direto.
	* Ex: `self.text = 'Hello, World!'`

---
## Importes

**Arquivo Local** — `from <path> import <file>`
Dessa forma, importamos o arquivo em si, não algo dentro dele.

**Biblioteca Nativa** — `from <library> import <filter>`
Especifica o que quer importar de uma biblioteca.  Se `<filter>` for `*`, importa tudo

**Alias** — após um `import <file/filter>`
`as <alias>` — importando dando um apelido

---
## Erros de compilação

**`TypeError: 'module' object is not callable`**
	Quando se vai importar um arquivo local ou biblioteca nativa como : `import <libraby> as <alias>`, `<alias>` será a biblioteca, não a [[Classe]] dessa biblioteca. Para pode instanciar a [[Classe]], deve-se buscar a [[Classe]] — `val a = <alias>.Alias()`

---
## Referências
1. [DEVMEDIA — Tkinter: Interfaces gráficas em Python](https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956)
2. [Python Academy — Classes e Objetos no Python](https://pythonacademy.com.br/blog/classes-e-objetos-no-python)
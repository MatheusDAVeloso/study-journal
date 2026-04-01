# Terminal Linux
Antigamente em sistemas Unix-like como Linux, o [[Shell]] era a única interface para o usuário. Na maioria dos sistema Linux, utiliza-se o [[Bash]]. Para podermos interagir com o [[Shell]], utilizamos o [[Terminal]].

---
## **Identificadores**
Se aparecer '#' no Terminal do Linux ao invés de '$', quer dizer que é um superuser (root), ou seja, você pode reescrever ou deletar qualquer arquivo do sistema, dado que o Linux entende que todos seus usuários root são donos do sistema e sabem o que estão fazendo.

---
## **Organização de diretórios**
Toda navegação de sistema Unix-like começa na pasta root. Que é a primeira pasta. Uma diferença importante para sistema Unix-like do Windows, é que o Windows armazena os diretórios em várias árvores, um para cada dispositivo, o Linux tem apenas um.

### **Comandos**
`pwd` — print work directory — mostra o caminho completo até o diretório atual

`cd` — change directory
-  `~` ou `~<user-name>`  — home
- `..` — subir um nível — caminho relativo
-  `<folder-name>` ou `./<folder-name>` — caminho relativo
- `/<folder-name>` — caminho absoluto — começa da raiz

`ls` — list
* `-l` — long — forma detalhada
- Se um arquivo aparecer verde ou com um "`*`" significa que é executável

`mkdir <directory-name>` — make directory

---
## Execução de [[Programa]]

### Comandos
`<program-name> .` — do sistema ou integrado a ele 
`./<file-name>` — criado por um usuário

---
## Limpeza

### Comandos
`ctrl + l` ou `clear`

---

## Filtros
Utilizar após um comando que traz uma lista.

### Comandos
`| grep 'name'` — filtra pela nomenclatura entre aspas simples


---
## Referências
1. Claude (Anthropic) utilizado para verificação e validação de respostas
2. https://linuxcommand.org/lc3_lts0010.php
3. https://linuxcommand.org/lc3_lts0020.php
# Terminal Linux

---
## Definição
O Linux é um sistema [[Unix-like]]. Por isso, na maioria dos sistema Linux, utiliza-se o [[Bash]]. Para podermos interagir com o [[Shell]], utilizamos o [[Terminal]].

---
## **Identificadores**
Se aparecer '#' no Terminal do Linux ao invés de '$', quer dizer que é um superuser (root), ou seja, você pode reescrever ou deletar qualquer arquivo do sistema, dado que o Linux entende que todos seus usuários root são donos do sistema e sabem o que estão fazendo.

---
## **Comandos**
1. Navegação de diretório
2. Execução de [[Programa]]
3. Limpeza do [[Terminal]]
4. Filtragem

### 1. Navegação de diretório

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

### 2. Execução de [[Programa]]

`<program-name> .` — do sistema ou integrado a ele 
`./<file-name>` — criado por um usuário

### 3. Limpeza do [[Terminal]]

`ctrl + l` ou `clear`

### 4. Filtragem

Utilizar após um comando que traz uma lista.

`| grep 'name'` — filtra pela nomenclatura entre aspas simples


---
## Referências
1. [LinuxCommand.org — What is "the Shell"?](https://linuxcommand.org/lc3_lts0010.php)
2. [LinuxCommand.org — Navigation](https://linuxcommand.org/lc3_lts0020.php)
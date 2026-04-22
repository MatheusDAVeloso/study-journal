# Cache de CPU

---
## Definição
É uma memória rápida, utilizada pela CPU para acessar dados e instruções frequentes em velocidade extrema.

---
## Tipos
Existem 3 níveis de cache, por isso o "L" — de "Level"

### L1 — Cache de nível 1
- É o menor cache, porém o mais rápido. Localizado próximo aos núcleos da CPU. Por isso possui baixa latência (tempo necessário para acessar dados).
- O objetivo dele é guardar dados e instruções mais frequentes, acelerando as operações da CPU. 
- Cada núcleo possui acesso ao seu próprio L1.
### L2 — Cache de nível 2
- O cache L2 é maior que o cache L1, porém ligeiramente mais lento. Contudo, mais rápido que acessar a memória RAM (memória principal).
- É utilizado para alocar dados e instruções adicionais que não couberam no cache L1.
- É compartilhado entre os núcleos em processadores multi-core.

### L3 — Cache de nível 3
- As vezes não está disponível em alguns processadores.

---
## Referências
1. [Dev Community — CPU Cache Basics](https://dev.to/larapulse/cpu-cache-basics-57ej)
# Observer

---
## Definição
Um design pattern que define uma relação de **1 para n** entre objetos, onde um Publisher notifica automaticamente seus Subscribers quando seu estado muda.

---
## Problema em que se propõe resolver — Analogia
Um leitor precisa saber se há uma nova matéria em um Jornal local. Ao invés do leitor ficar perguntando várias vezes se há uma nova matéria, o Jornal agora possui um sistema de notificação que vai de casa em casa avisar quando há uma nova matéria, já que ele é o dono daquele objeto.

Porém se o Jornal começar a notificar qualquer casa, gastará seus recursos a toa. A solução é o Jornal possuir opções de se inscrever e desinscrever para dar opção a quem quer receber aquele objeto ou não. 

---
## Referências
1. [Refactoring Guru — Observer](https://refactoring.guru/design-patterns/observer)
# Observer

---
## Definição
Um design pattern que define uma relação de **1 para n** entre objetos, onde um Publisher notifica automaticamente seus Subscribers quando seu estado muda.

---
## Problema em que se propõe resolver
Uma classe Leitor precisa verificar em uma classe Jornal se uma flag "Nova Matéria" foi adicionada. Ao invés da Leitor ficar perguntando várias vezes se esta flag mudou, a classe que guarda essa variável poderia enviar uma notificação para a que quer receber quando "Nova Matéria" for verdadeira.

Porém se Jornal começar a notificar qualquer classe, gastará recursos a toa. A solução é criar funções de "subscribe" e "unsubscribe" para dar escolhar a quem quiser ouvir ou não.

---
## Referências
1. [Refactoring Guru — Observer](https://refactoring.guru/design-patterns/observer)
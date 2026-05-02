# Member Initializer List

---
## Definição
Irá listar quem vai inicializar

---
## Modo de uso
Após os parênteses de um construtor, utilizar ":" antes das chaves — { }.

---
## Diferença
Por que utilizar assim:
```c++
PublisherController() : _state(nullptr) {}
```

e não assim:
```c++
PublisherController() {
	_state = nullptr;
}
```

Simples, porque dentro das chaves, a linguagem cria o \_state com um valor lixo aleatório e depois executa a linha que troca o lixo por `nullptr`.
Com **Member Initializer List**, \_state já nasce sendo `nullptr`. Não existe um millisegundo em que ele contém lixo. É mais rápido e seguro.
# Construtor

Um construtor é uma [[função]] especial invocado no momento da criação (instanciação) de um objeto a partir de uma classe ou estrutura. Seu objetivo principal é inicializar o estado do objeto e alocar os recursos necessários para que ele exista na memória de forma válida.

---
## Member Initializer List

O *Member Initializer List* é uma sintaxe específica usada para inicializar os atributos da classe **antes** que o corpo do construtor seja executado.

**Modo de uso:**
Após a [[Função#Assinatura de Função|assinatura de função]] do construtor, utiliza-se o caractere `:` seguido da inicialização das variáveis, antes da abertura das chaves `{ }`.

**Por que utilizar?**
Considere a diferença de performance:

```cpp
// Forma TRADICIONAL (Mais lenta)
PublisherController() {
	_state = nullptr;
}
```
Na forma tradicional, a linguagem primeiro aloca a variável `_state` com um valor "lixo" aleatório na memória, e só depois (dentro das chaves) atribui `nullptr` a ela.

```cpp
// Usando MEMBER INITIALIZER LIST (Mais rápida e segura)
PublisherController() : _state(nullptr) {}
```
Com o *Member Initializer List*, `_state` já nasce na memória contendo `nullptr`. Não existe sequer um milissegundo em que a variável contenha dados inválidos.


# Guard clause

---
## Definição
Técnica de se fazer verificações em um código, tratando casos de erro primeiro, evitando aninhamento de condicionais.

---
## Utilidade
Mais fácil de encontrar qual "if" deu qual erro

---
## Forma de se utilizar
Ao invés de
```c++
if (!erro1) {
    if (!erro2) {
        if (!erro3) {
	        std::cout << "Hello" << std::endl;
        } else {
	        std::cout << "erro 3" << std::endl;
        }
    } else {
	    std::cout << "erro 2" << std::endl;
    }
} else {
	std::cout << "erro 1" << std::endl;
}
```

ficaria assim:
```c++
if (erro1) {
	std::cout << "erro 1" << std::endl;
	return;
}

if (erro2) {
	std::cout << "erro 2" << std::endl;
	return;
}

if (erro3) {
	std::cout << "erro 3" << std::endl;
	return;
}

std::cout << "Hello" << std::endl;
```
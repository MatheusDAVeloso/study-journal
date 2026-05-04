# raylib

> [!INFO] Resumo
> No raylib, a tela é como um canvas. A cada frame você redesenha tudo do zero — não existe manter o estado do frame anterior automaticamente.

---
## 1. Ciclo de Vida da Janela

Para criar qualquer aplicação em raylib, você precisa inicializar a janela, manter um loop de execução (Game Loop) e fechar a janela ao final para liberar a memória e os recursos da GPU.

```cpp
// 1. Inicialização
// [[Parâmetros]]: Largura, Altura, Título
InitWindow(800, 600, "CPlusPlusTheGame"); 

// 2. Game Loop
// A [[Função]] WindowShouldClose() retorna true quando o usuário clica no 'X' ou aperta ESC.
while (!WindowShouldClose()) {
	// Lógica de atualização e desenho acontecem aqui dentro
}

// 3. Limpeza de memória e liberação de recursos
CloseWindow();
```

---
## 2. Desenhando um Frame

Tudo que for ser desenhado na tela **deve** estar entre o `BeginDrawing()` e o `EndDrawing()`.

```cpp
BeginDrawing();

	// Limpa a tela inteira com uma cor. 
	// Sem isso, o frame anterior não é apagado e deixa um "rastro".
	ClearBackground(RAYWHITE); 
	
	// DrawText(), DrawCircle(), etc...
	
EndDrawing();
```

---
## 3. Desenhando um Cubo
```cpp
// Parâmetros:
// Posição do mundo
// Largura
// Altura
// Profundidade
// Cor
DrawCube({0.0f, 0.0f, 0.0f}, 2.0f, 2.0f, 2.0f, RED)
```

---
## 4. Câmera e Modo 3D

Para ver qualquer coisa 3D aparecer no jogo, é obrigatório instanciar e configurar uma Câmera, além de colocar os comandos de desenho dentro do modo 3D.

### Configurando a struct Câmera
Para declarar uma câmera com todos os atributos zerados, utiliza-se `Camera3D camera = {0};`. A câmera é uma *struct* do raylib com várias [[Classe#Propriedade|propriedades]]:

| Propriedade    | Exemplo de Valor                 | Descrição                                                   |
| :------------- | :------------------------------- | :---------------------------------------------------------- |
| **position**   | `(Vector3){10.0f, 10.0f, 10.0f}` | A posição da câmera no mundo 3D                             |
| **target**     | `(Vector3){0.0f, 0.0f, 0.0f}`    | O ponto fixo (alvo) para onde a câmera está olhando         |
| **up**         | `(Vector3){0.0f, 1.0f, 0.0f}`    | O vetor que define qual direção é "para cima"               |
| **fovy**       | `45.0f`                          | Campo de visão (Field of View) no eixo Y                    |
| **projection** | `CAMERA_ORTHOGRAPHIC`            | Perspectiva da lente (Pode ser também `CAMERA_PERSPECTIVE`) |

### Utilizando a Câmera
```cpp
BeginMode3D(camera);
	// DrawCube(), DrawSphere(), etc...
EndMode3D();
```

---
## 5. Solução de Problemas

> [!BUG] O VsCode não encontra o raylib.h
> **Erro:** `#include errors detected. Please update your includePath.`
> 
> **Causa:** O IntelliSense do VsCode está reclamando que não acha a biblioteca, pois ela só é baixada na máquina quando você roda o CMake pela primeira vez.
> 
> **Solução:** Rode o comando `cmake -B build` no terminal. Isso forçará o CMake a fazer o download dos arquivos externos, resolvendo o caminho para o VsCode.

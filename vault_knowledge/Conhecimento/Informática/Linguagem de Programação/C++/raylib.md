# raylib

---
## Introdução
No raylib, a tela é como um canvas, a cada frame você redesenha tudo do zero — não existe manter o estado que estava antes.

---
## Janela
**Iniciar uma janela**
`InitWindow(800, 600, "CPlusPlusTheGame");`
- O primeiro parâmetro é a altura
- O segundo parâmetro é a largura
- O terceiro parâmetro é o nome da janela

Após isso, é necessário um gameloop, se não a janela fecha.
Para se ter um, basta utilizar a função `WindowShouldClose()` da seguinte maneira:

```
while (!WindowShouldClose()) {

}
```

`WindowShouldClose()` retorna "true" quando o usuário clica no X, fechando o loop, porém para isso funcionar, deve ter algum conteúdo dentro do loop

**Liberar recursos**
`CloseWindow();`

---
## **Fazer um frame**
`BeginDrawing()` — inicializa o frame
`EndDrawing()` — finaliza o frame

`ClearBackground(RAYWHITE)` — Limpa a tela inteira com uma cor
Se não utilizar isso a cada frame, o frame anterior ainda aparece e vai deixando um "rastro"

---
## Modo 3D
Dentro de um frame:
`BeginMode3D(camera.camera);`
`EndMode3D();`

## Câmera
Para ver qualquer coisa 3D aparecer no jogo, é necessário uma câmera.

**Inicializar uma câmera**
Para declarar uma câmera com todos os atributos zerados é assim `Camera3D camera = {0}` — uma câmera é uma struct do raylib com várias propriedades.

Campo a campo:
**Posição** no mundo — `camera.position = (Vector3){10.0f, 10.0f, 10.0f};`
Para onde olha — `camera.target = (Vector3){0.0f, 0.0f, 0.0f};`
Definir que direção é para cima — `camera.up = (Vector3){0.0f, 1.0f, 0.0f};`
Fov — `camera.fovy = 45.0f;`
Perspectiva — `camera.projection = CAMERA_ORTHOGRAPHIC;` — ou `CAMERA_ORTHOGRAPHIC`
 
---
## Erro comum ao importar
`#include errors detected. Please update your includePath. Squiggles are disabled for this translation unit`

Esse é um erro do **IntelliSense** do VsCode reclamando que ele não sabe onde está o `raylib.h`. Ele só é baixado quando você rodaro CMake pela primeira vez

**Uma forma de se resolver**
Primeiro, tentar rodar no terminal `cmake -B build`. Esse comando vai baixar o CMake e gerar os arquivos de build.

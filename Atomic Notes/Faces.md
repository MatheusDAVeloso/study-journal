# Faces

---
## Criador/Descobridor

---
## Definição
Junção de 3 ou mais [[Aresta]], sendo visíveis na renderização.

---
## Tipos
Dependendo da quantidade de arestas utilizadas para se formar uma face, temos:

- Triângulo — ou tris — junção de 3 [[Aresta]], sendo mais fácil de calcular
- Quadrado — ou quads — junção de 4 [[Aresta]], sendo mais fácil de deformar
- N-gons — mais de 4 [[Aresta]]

---
## Normais
É a direção ou linha perpendicular em relação aquela face.

---
## **Quando usar N-gons**
Há uma questão bastante discutida sobre a sua utilização.

**Quando se utilizar**
Enquanto estiver dentro do ambiente Blender e apenas você for mexer nessa modelagem. São bons já que reduzem a contagem de polígonos e te dá mais liberdade.

**Quando não se utilizar**
1. Quando exportar para uma Engine, onde tudo vira triângulo e você perde a precisão do modelo. Com quads e tris você tem mais controle de como vai ficar.
2. Ao mandar para outro artista, visto que alguns [[Programa]] não suportam, é mais fácil de quebrar o visual e não são bons para animação.

---
## Referências
1. https://docs.blender.org/manual/en/latest/modeling/meshes/structure.html
2. https://blender.stackexchange.com/questions/89/when-should-n-gons-be-used-and-when-shouldnt-they
3. Claude (Anthropic) utilizado para verificação e validação de respostas
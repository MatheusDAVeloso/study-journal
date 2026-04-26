# Atomic Notes 2.0: Governança Estrutural do Conhecimento

---

## O Problema

Filósofos, bibliotecários e cientistas debatem há séculos como classificar o conhecimento humano. Aristóteles tentou com suas categorias. Lineu resolveu para a biologia. A CDD resolve para bibliotecas. Nenhum sistema é perfeito — porque o conhecimento é uma **rede**, mas pastas são uma **árvore**.

Este vault não pretende encerrar esse debate. Pretende aplicá-lo de forma rigorosa e consistente a um conjunto pessoal de notas, testando se uma taxonomia ontológica — classificar conceitos pela sua **natureza primária**, não pelo seu **contexto de uso** — melhora a qualidade do conhecimento armazenado e recuperado.

A tensão central: o Princípio MECE exige um lar único para cada nota, mas alguns conceitos são genuinamente transdisciplinares. Toda decisão de classificação aqui é uma decisão filosófica real.

---

## Filosofia Central

### 1. Princípio MECE
*Mutually Exclusive, Collectively Exhaustive* — cada nota tem um, e apenas um, lar lógico. As categorias não se sobrepõem. Se um conceito parece pertencer a dois lugares, isso indica que a taxonomia precisa ser resolvida, não que o conceito vai para os dois.

### 2. Atomicidade
Cada nota representa um único conceito granular. Se uma nota cobre dois assuntos distintos, ela deve ser dividida. O critério: um subtipo vira nota própria quando tem **comportamento, decisão ou contexto de uso independente**.

### 3. Taxonomia Acadêmica
Não usamos divisões arbitrárias. Seguimos a hierarquia científica real. Computação Gráfica e IHC são subáreas da Ciência da Computação. Lógica é subárea da Filosofia. O uso prático não define a natureza do conceito.

> `Buffer` é usado em vídeos, em redes, em jogos. Mas sua natureza primária é Arquitetura de Computadores. Ele mora lá.

### 4. Hierarquia de Fundamentos
Organizamos do abstrato ao aplicado. `Algoritmo` em sua forma universal mora em `Filosofia/` — não em `Informática/`. `Design de Algoritmos` mora em `Informática/` — porque é a aplicação prática do conceito.

### 5. Regra 10-15
Pastas devem ter idealmente entre 10 e 15 arquivos. Se passar disso, a categoria deve ser subdividida. Se ficar abaixo, a subpasta pode não estar justificada ainda.

> A subdivisão acontece quando um **padrão real emerge** — não por antecipação. A taxonomia emerge dos dados, não é imposta antes deles.

---

## Regras de Manutenção

**Nomenclatura:** nomes descritivos em português, separados por espaço, com acentuação correta. Ex: `Estrutura de Dados.md`.

**Sufixos de disambiguação:** quando um conceito existe em múltiplos domínios e a nota é específica de um, usar sufixo. Ex: `Aresta (Blender).md`. Quando o conteúdo é geral, sem sufixo.

**Links:** sempre utilizar links internos (`[[Link]]`) para conectar conceitos entre domínios. A pasta é o lar principal; os links capturam a rede. Uma nota pode morar em `Arquitetura de Computadores/` e linkar para `Segurança da Informação/` — a conexão não se perde.

**Referências:** registrar a fonte de cada nota. Notas com fontes de hobby ou secundárias podem precisar de referências acadêmicas no futuro.

**Pastas soltas:** notas sem subpasta definida ficam soltas na pasta pai até o volume revelar o padrão. Nota solta não é problema — é o vault respirando.

---

## Estrutura Atual

```
Conhecimento/
  Artes/
  Filosofia/
  Matemática/
  Teoria das Cores/
  Informática/
    Ciência da Computação/
      Algoritmo/
      Arquitetura de Computadores/
      Computação Gráfica/
      Engenharia de Software/
        Architectural Patterns/
        Design Patterns/
        Processos/
        Programação/
      Estrutura de Dados/
      Interação Humano-Computador/
      Redes de Computadores/
      Segurança da Informação/
      Sistemas Operacionais/
    Ferramentas/
    Linguagens de Programação/
      Python/
    Técnicas de Hardware/
```

---

> *"Definir de que área nasceu um conhecimento ou informação é uma das maneiras mais intrigantes de conhecer a história perdida do ser humano. Juntando conhecimento desde cursos gratuitos de Harvard, a cursos com diplomas de outros países e chegando até vídeos e blogs com poucas visualizações, vemos uma herança de conhecimento, carregada como uma metamorfose assim como a genética é. Ao olharmos e vermos que cada pessoa carrega consigo um significado diferente para uma coisa só, poderíamos pensar: onde que aconteceu a ramificação? E porque alguns interpretam a mesma coisa de forma diferente? O que é a verdade se não um pedaço da história dividida em pequenos pedacinhos entre povos e espalhados por toda a longa história da humanidade."* — Matheus A. Veloso, 2026 — Sem IA.
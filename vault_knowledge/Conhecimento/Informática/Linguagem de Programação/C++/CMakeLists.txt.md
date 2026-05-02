# CMakeLists.txt

---
## Definição
É um arquivo de configuração do build de um projeto em [[C++]] — precisa ter exatamente esse nome, incluindo o "list" no plural e em ".txt", pois o CMake procura por esse nome exato. É ele quem informa ao compilador quais arquivos compilar, quais bibliotecas linkar e qual versão do [[C++]] utilizar, por exemplo.

---
## O que ele resolve
Em projetos pequenos, um simples comando de compilação resolve como `g++ main.cpp -o example`. Porém em projetos grandes, seria necessário incluir os path de arquivos que foram importados no main.cpp, incluir bibliotecas externas, etc.

---
## Configurações

### **Nome do projeto**
- `project(ProjectName)`
- O CMake utiliza isso para várias coisas internamente — nome do executável gerado, nome da solução no VSCode se utilizar
- A convenção é PascalCase
- Deve vir antes de `cmake_minimum_required(VERSION 3.16)`

### **Dizer a versão mínima do CMake que o projeto precisa para funcionar.**
- `cmake_minimum_required(VERSION 3.16)`
-  Se alguém tentar buildar com uma versão anterior antiga, o CMake avisa e para

### **Definir a versão do [[C++]] a ser utilizada**
- `set(CMAKE_CXX_STANDARD 20)`

### **Baixar bibliotecas externas**
Primeiro precisa incluir um módulo que não vem ativo por padrão, mas é build-in do CMake: o `include(FetchContent)`

**Após isso, precisa declarar de onde vem a biblioteca**
"raylib" será usado como exemplo. Primeiro chamar a função — isso apenas está registrando onde será feito a consulta, não está baixando ainda.
```CMake
FetchContent_Declare(
	raylib <- aqui é onde você vai dar um apelido para a biblioteca
	GIT_REPOSITORY https://github.com/raysan5/raylib.git <- onde deve buscar
	GIT_TAG 5.5 <- Versão específica.
)
```
Sempre trave em uma versão específica, pois se deixar sem pega a versão mais recente pode quebrar o projeto com uma atualização imprevista.

**Agora precisa baixar a biblioteca**
O nome utilizado para identificar a biblioteca no passo anterior será passado para a seguinte função fazer o download: `FetchContent_MakeAvailable(raylib)`

**E agora precisa linkar a biblioteca externa**
`target_link_libraries(ProjectName raylib)`
- Deve vir depois de `add_executable(ProjectName main.cpp)`, pois você precisa criar o executável primeiro antes de linkar

### **Criar executável**
`add_executable(ProjectName main.cpp)`
O primeiro parâmetro deve ser o mesmo em `project(ProjectName)`

O primeiro parâmetro deve ser o mesmo declarado em `project(ProjectName)` e o segundo é o caminho do arquivo main.cpp
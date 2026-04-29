# Android Debug Bridge

---
## Definição
Ferramente de debug para [[Host]] Android.

---
## Entrada para sua command-line interface

`adb`

---
## Comandos de servidores internos
ADB faz seus comandos através de um servidor que serve de canal de comunicação entre os comandos e o dispositivos.

`adb kill-server` — desliga o servidor
`adb start-server` — inicializa o servidor

---
## Comandos de conexão
Para se conectar com um dispositivo e mandar comandos

`adb connect <ip-device>` — fazer uma conexão com um dispositivo
`adb disconnect <ip-device>` — desfazer uma conexão com um dispositivo

### ADB Devices
`adb devices` — listar os aparelhos que o adb fez conexão

Mensagens de erros comuns e soluções:
- Erro: `failed to authenticate to <ip-device>`
- Solução: ir em "Opção de Desenvolvedores" e desligar e ligar o "USB debbuging"

---
## [[Shell]] package manager
Gerenciador de pacotes através de [[shell]]

Listar **package names**
`adb shell pm list packages`

---
## Limpar cache de um app
Primeiro precisa pegar o nome do "package name" e então rodar algum dos seguintes comando:
* `adb shell pm clear <package-name>` — limpa todos os dados, como se fosse inicialização nova
* `adb shell pm clear --cache-only <package-name>` — limpa apenas o cache

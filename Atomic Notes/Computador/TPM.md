# TPM
#root_of_trust

---
# Definição
Sigla para **Trusted Platform Module** — Módulo de Segurança da Placa-mãe  —  é um chip físico integrado a placa-mãe que tem um papel de [[Root of trust]].

---
## Utilidade
Gera, armazena e evita exposição de chaves criptográficas — a chave fica dentro de seu chip e é exposta e lida apenas no momento do boot, após isso volta a guardar novamente.

Valida e garante a integridade de um sistema de hardware de computador — sem alteração no boot de um disco, [[Bios]] ou em algum chip da placa-mãe, incluindo a si mesmo — em sua inicialização, se estiver tudo certo, libera o sistema operacional.

Serve como proteção de dados contra [[Furto de informação#Por software|furto de informação por software]] e [[Furto de informação#Por hardware|furto de informação por hardware]] em usuários comuns.

---
## Cenários de eficácia
### 1. **Contra tecnologia militar**
Em um equipamento de guerra israelense — licenciado pela ONU e que o exército brasileiro tem  — é possível apontar para um dispositivo a fim de obter dados que estão em tempo real no hardware. Então tentaram pegar na hora em que o chip abre para leitura do boot, contudo mesmo assim, o TPM conseguiu proteger.

---
## Pontos de atenção

> [!CAUTION] **TPM** para empresas
> 
> Como ele vê que se o hardware for alterado não, deixa o sistema operacional prosseguir, em sistemas empresariais com informação pessoal sigilosa, é utilizado essa tecnologia. Então ficar trocando de hardware como placa de vídeo, memória, dentre outras peças, pode ser visto como uma ameaça e bloquear o computador.

---
## Informações adicionais
- Quando se vai comprar uma placa-mãe, normalmente não vem com TPM em lojas normais.
- Placas-mãe com TPM tendem custar em média, R$300 a mais

---
## Referências
1. Aula de Segurança da Informação — Faculdade UniGoiás, abril de 2026.

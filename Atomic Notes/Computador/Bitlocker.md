# Bitlocker

---
## Criador/Descobridor
Microsoft

---
## Definição
[[Software]] que atua como uma solução de [[Criptografia]] nativa no Windows em um arquivo, pasta e até volume (partição/disco) inteiro, onde apenas seus usuários possuem acesso.

---
## Utilidade
Serve como proteção de dados contra [[Furto de informação]] — exceto seção [[Furto de informação#2. Ação externa|2. Ação Externa em Furto de Informação — Deixar o computador aberto sem senha]] — em usuários comuns. 

---
## Desbloqueio
A [[Criptografia]] pode ser desbloqueada através de pin, porém se esquecer ainda sim pode-se utilizar uma chave de recuperação.

---
## Cenários de eficácia
### 1. Contra vírus keykogger
- Este vírus por estar apenas no sistema operacional, não consegue pegar o PIN do bitlocker — já que o lugar onde é digitado é numa janela própria do [[software]], que é inicializado antes do sistema operacional.

---
### Integração com [[TPM]]
Em placas-mãe que possuem esse chip, se o mesmo não indicar alteração, o Bitlocker apenas deixa prosseguir. Em caso de alteração, o Bitlocker solicita uma chave de recuperação. 

Ele armazena a metade da chave em seu disco rígido e a outra metade da chave no chip. Ou seja, aquele disco rígido só funciona naquele computador. E somente com essa junção que o Bitlocker irá liberar os seus dados — sendo muito difícil de quebrar essa [[Criptografia]] justamente por estar dividido.

Essas duas tecnologias juntas garantem a confidencialidade, integridade e autenticidade dos dados — [[Segurança da Informação#Pilares|pilares da Segurança da Informação]].

>[!EXAMPLE] Cenários em que a junção dessas tecnologias se mostrou poderosa
>
>A polícia federal — mesmo utilizando um computador potente ligado a mais de dois anos — não conseguiu quebrar essa [[Criptografia]] que possuía informações sigilosas e relevantes de um faccionados.

---
## Pontos de atenção

>[!CAUTION] Bitlocker com dual boot
>
>Segundo relato de um professor de Segurança da Informação na UniGoiás em abril/2026, ao usar bitlocker com dual boot de Windows com [[Linux]] corrompe tudo, e nenhuma chave volta — ou é tudo [[Linux]] ou tudo Windows.

>[!CAUTION] Bitlocker após autenticação
>Após a autenticação do usuário, não há diferença nenhuma se tiver esta ferramenta.

---
## Referências
1. Aula de Segurança da Informação — Faculdade UniGoiás, abril de 2026.

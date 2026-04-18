# Segurança da Informação
#si_pilar_da_autenticidade #si_pilar_da_confidencialidade #si_pilar_da_integridade 

---
## Proteção contra cheat em jogos
Toda vez que um pacote de jogo vai sair da máquina de um usuário para ser enviado com um processo de [[Criptografia]] para um servidor, ele manda uma parte através de hash — e como um input de uma assinatura hash produz sempre o mesmo output — é possível saber se tem um hardware extra para cheat, já que este alteraria o output do hash feito inicialmente quando não tinha algo extra. Tudo isso é feito individualmente de máquina para máquina, validando tanto hardware quanto software. Utilizando extração de chave.

>[!EXAMPLE] Exemplo
>O servidor faz parte de uma empresa, portanto conhece seu próprio [[software]]. O servidor então já sabe que a assinatura do [[software]] é "A". Com a assinatura do usuário sendo "B", produz uma assinatura que o servidor espera, que é "C".
>
>Com um cheat no jogo — ao enviar o pacote — os dados não serão mais "A", mas sim "Azão". E ao juntar com a assinatura "B", não vai chegar "C" que o servidor espera, mas sim, "Cezin". E aí o dispositivo é bloqueado na hora.

---
## Pilares
Utilizados para dar segurança em [[Host]] de diversas formas.

### 1. Pilar da confidencialidade
### 2. Pilar da integridade
### 3. Autenticidade

---
## Referências
1. Aula de Segurança da Informação — Faculdade UniGoiás, abril de 2026.
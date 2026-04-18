## Técnica segurança de host
Tem como objetivo garantir confidencialidade, integridade e autenticidade dos dados - 3 pilares da Segurança da Informação

## Conceito Importante do TMP
Root of Trust -> É ele que garante as próximas camadas de segurança. Se tem um TPM tem um Bitlocker seguro. Ou seja, causa primária de toda a cadeia de segurança. Segurança de host/usuário

## Chip Off
Extrair o chip da placa mãe e coloca na outra placa mãe. Mas tem que ser outra placa-mae da mesma marca, modelo e até do mesmo lote, para que as "perninhas" do chip encaixe de forma segurança -> pessoal que trabalha muito com conserto de celular.

## Utilização de tpm em jogos

apenas seu usuário vai enviar essa chave para o servidor. Ele vai validar o hardware + tpm.

Ele manda uma parte criptografada através de hash, e com o hash é possível saber se tem um hardware extra para cheat.

Outra técnica -> toda vez que o pacote do jogo vai sair da sua máquina e é enviado com um processo de criptografia para o servidor, ele envia de uma forma . O servidor então sabe que o assinatura do software é A. com a assinatura do usuário é B, e envia C.

com um cheat no jogo, ao conectar, os dados não será mais o "a" serão o "azão" + b , não vai chegar C, vai chegar "celin"

valida tanto hardware quanto software. Utilizando extração de chave.

---

## Equipamento de guerra israelense - licenciado pela ONU - exercito BR tem

Você consegue pegar dados que estão em tempo real apontando para um dispositivo, pegando dados no chip.

Porém, o TPM consegue proteger. Na hora que ele abre para leitura para o boot, o equipamento de guerra nao consegue pegar.

---

Outra técnica de invasão é alteração do boot -> é quando altero as configurações da bios do computado para que o boot seja feito sem o segure boot ou que seja feito carregando dados de um pen-drive.

Com um simples pen-drive ele coloca atrás do pc e o usuário não vê, e por não ter criptografia, é roubado as informações.

Porém com um Trust se ele ver que o hardware foi alterado não deixa. Por isso que em sistema empresariais com informação pessoal sigilosa, ficar trocando hardware como placa de vídeo, memória, pode ser visto pelo TPM como um ataque e pode bloquear o computador.

---

## Vírus KeyLogger
Não consegue pegar a senha do bitlocker, pq a senha do bitlocker não é digitado pq a senha é salvo em um lugar externo. Pq você digita apenas o PIN, não a chave.

---

Quando vai comprar placa-mae para computador, as placa-maes não veem normalmente com TPM em lojas normais. Placas com TPM custam em média R$300 a mais

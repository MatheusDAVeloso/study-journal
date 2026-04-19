# OR Bitwise

---
## Operador
|=

---
## Forma de se utilizar

```cpp
state |= 0b00000001
state = state | 0b00000001
```

---
## Definição
Operador que compara cada bit individualmente e devolve o resultado utilizando a lógica OR.

>[!EXAMPLE] Exemplo bit a bit
>```cpp
>
>state: 00000000
>INPUT_FRONT: 00000001
>
>Bit a bit:
>0 | 0 = 0
>0 | 0 = 0
>0 | 0 = 0
>0 | 0 = 0
>0 | 0 = 0
>0 | 0 = 0
>0 | 0 = 0
>0 | 1 = 1 ← esse bit, se um dos dois for 1, o resultado é 1
>```

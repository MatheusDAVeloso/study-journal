# SharedPreferences

---
## Como utilizar
Primeiro deve-se ter a instância do SharedPreferences guardada em uma variável — `final prefs = await SharedPreferences.getInstance()`.

**Pegar um booleano em cache**
`prefs.getBool('bool_variable_name') ?? false`

**Colocar um booleano em cache**
`prefs.setBool('bool_variable_name', bool-value)`
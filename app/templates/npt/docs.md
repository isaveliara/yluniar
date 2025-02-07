# Npt Documentation

Npt é uma linguagem interpretada na Suni, para programação de instruções, executada internamente em si mesma, podendo automatizar tarefas, intermediar processos, etc.
---

## 📚 Introdução

**NPT** é uma linguagem interpretada e tipada estaticamente, projetada para:
- Interação tanto quanto para a API do Discord quanto para a API da própria Suni.
- Controle de fluxo simples e amigável
- Manipulação básica de dados
- Execução de scripts com substituição dinâmica de valores

---

## 🚀 Primeiros Passos

### Tipos de Dados
| Tipo      | Descrição                          | Exemplo                   |
|-----------|------------------------------------|---------------------------|
| `Int`     | Números inteiros                   | `40028922`                |
| `Float`   | Números decimais                   | `3,1415`                  |
| `Bool`    | Valores lógicos                    | `&true` ou `&false`       |
| `Char`    | Caractere único                    | `c'A'`                    |
| `Str`     | Cadeia de caracteres               | `s'BOM DIA PIRANHA'`      |
| `List`    | Coleção de valores                 | `{3,14, s'bem vindo'}`    |
| `Dict`    | Dicionário (chave Str)             | `{s'joao': s'admin'}`     |
| `Nil`     | Valor nulo                         | `nil`                     |

---

## 🔍 Variáveis e Placeholders

### Placeholders Dinâmicos
Valores pré-definidos que são substituídos durante a execução:
```
&{username}       &{userId}         &{userAvatarUrl}
&{guildId}        &{guildName}      &{guildAvatarUrl} 
&{channelName}    &{channelId}      &{runnerId}
```

### Declaração de Variáveis
Sintaxe básica:
```
~<TIPO> &set <NOME> <VALOR>
```
Exemplos:
```
~Int &set phone 40028922
~Str &set message s'Hello' + s' World'
~List &set options {s'hi', 123, &true}::randomOf::toStr
```

### Uso em Strings
```
std::nout() -> s'Seu número: ${phone}'
std::nout() -> s'Mensagem: ${message}'
```

---

## 🎮 Controle de Fluxo

### Estrutura Condicional (`&if`)
```
&if (&{runnerName} == s'lan') &do{
    std::nout() -> s'Olá Lan!'
    &kit  # Encerra execução
&}
```

**Regras:**
- A expressão deve retornar `&true`
- Bloco delimitado por `&do{ ... &}`
- `&kit` para interromper execução

---

## 🔧 Operadores

### Lógicos
| Operador | Descrição       | Exemplo          |
|----------|-----------------|------------------|
| `&&`     | E lógico        | `a && b`         |
| `||`     | OU lógico       | `a || b`         |
| `!`      | Negação         | `!&true`         |

### Booleanos
| Operador | Descrição       | Exemplo          |
|----------|-----------------|------------------|
| `==`     | Igualdade       | `a == b`         |
| `~=`     | Diferença       | `a ~= b`         |
| `>`      | Maior que       | `a > b`          |
| `<`      | Menor que       | `a < b`          |
| `<`      | Está em         | `a ? b`          |

### Matemáticos
```
3 + 2   # Soma
5 / 2   # Divisão
4 * 1.5 # Multiplicação
```

### Precedência
1. `[]`, `{}`, `::`
2. `!`
3. `*`, `/`
4. `+`, `-`
5. `?`, `#`
6. `&&`
7. `||`


# 🐾 Projeto: Hierarquia de Animais em Python

Este projeto demonstra conceitos básicos de **Programação Orientada a Objetos (POO)** em Python, como **herança**, **construtores**, e **sobrescrita de métodos**, através de uma estrutura simples de classes representando animais.

## 📁 Estrutura do Código

O código define uma classe base `Animals` e duas subclasses `Dog` (Cachorro) e `Cat` (Gato), cada uma com atributos e métodos próprios.

### 🧩 Classes

#### `Animals`
Classe base para representar um animal genérico.

**Atributos:**
- `name` (str): Nome do animal
- `age` (int): Idade do animal
- `legs` (int): Número de pernas (padrão: 4)

**Métodos:**
- `info()`: Imprime os atributos do animal (nome, idade e pernas)

#### `Dog` (herda de `Animals`)
Classe que representa um cachorro.

**Métodos:**
- `info()`: Sobrescreve o método da classe base para imprimir informações do cachorro

#### `Cat` (herda de `Animals`)
Classe que representa um gato.

**Métodos:**
- `info()`: Sobrescreve o método da classe base para imprimir informações do gato

---

## ▶️ Como executar

Execute o script Python para ver o comportamento das classes:

```bash
python nome_do_arquivo.py
```
Saída esperada:
Dog 2 4
Cat 4 4
💡 Conceitos Demonstrados
Herança: Dog e Cat herdam de Animals

Sobrescrita de métodos: cada subclasse redefine o método info()

Construtores com super(): reutilização do construtor da classe base

### 📌 Requisitos
Python 3.x

### 📄 Licença
Este projeto é de uso livre para fins educacionais.


Se quiser que eu salve isso como arquivo e envie diretamente, você pode ativar o **ChatGPT Canvas** ao fazer login.

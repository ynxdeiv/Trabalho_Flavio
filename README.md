Com certeza! Aqui está o código Markdown exato que você pode copiar e colar no seu arquivo README.md no GitHub. Ele já está formatado com todos os títulos, tabelas e listas que conversamos.

Markdown

# 📚 Trabalhos de Estruturas de Dados

## 🔹 Trabalho 1 – Gerenciador de Palavras com Listas Encadeadas

### 📖 Descrição

Este programa gerencia palavras, organizando-as em três listas simplesmente encadeadas de acordo com o tamanho:

* **Lista 1:** Palavras com até 5 letras.
* **Lista 2:** Palavras de 6 a 10 letras.
* **Lista 3:** Palavras com mais de 10 letras.

Além disso, cada palavra está vinculada a listas encadeadas pelas classes morfológicas (`adjetivo`, `substantivo`, `verbo`). Todas as palavras são mantidas em ordem alfabética dentro de suas respectivas listas.

### 🛠️ Comandos

| Comando                       | Descrição                                                                                             |
| :---------------------------- | :---------------------------------------------------------------------------------------------------- |
| `i <palavra> <classe>`        | Insere uma palavra nova (classes: `adj`, `subst`, `verbo`). Se a palavra já existir, um erro é exibido.  |
| `l <número>`                  | Lista as palavras da lista básica correspondente (1 a 3).                                             |
| `m <classe>`                  | Lista as palavras da classe morfológica especificada.                                                 |
| `x <número> <classe>`         | Lista as palavras de uma classe morfológica que estão em uma lista de tamanho exata.                  |
| `o`                           | Lista todas as palavras em ordem alfabética.                                                          |
| `c <número1> <número2>`       | Intercala duas listas básicas (1 a 3) e imprime as palavras alternadamente.                             |
| `r <palavra>`                 | Remove uma palavra. Se a palavra não existir, exibe um aviso.                                         |
| `e`                           | Encerra o programa.                                                                                   |

### 📥 Entrada e 📤 Saída

* **Entrada:** Comandos com palavras em minúsculas e sem acentos.
* **Saída:** Mensagens e listagens de acordo com o comando executado.

---

## 🔹 Trabalho 2 – Dicionário Bilíngue com Árvore Binária de Busca

### 📖 Descrição Geral

Este programa implementa um dicionário bilíngue que usa uma **Árvore Binária de Busca (ABB)** para armazenar palavras do idioma de origem. Cada palavra na árvore inclui:

* Traduções para o idioma de destino.
* Classe morfológica (`substantivo`, `adjetivo` ou `verbo`).

### 🛠️ Comandos

| Comando                   | Descrição                                                                                               |
| :------------------------ | :------------------------------------------------------------------------------------------------------ |
| `i`                       | Insere uma palavra, sua classe (s=substantivo, a=adjetivo, v=verbo) e até 10 traduções. Exibe erro se já existir. |
| `l`                       | Lista todas as palavras do idioma de origem em ordem alfabética.                                        |
| `t <palavra>`             | Lista as traduções de uma palavra. Exibe erro se a palavra não existir.                                     |
| `c <palavra>`             | Consulta a classe morfológica da palavra. Exibe erro se a palavra não existir.                            |
| `r <palavra>`             | Remove uma palavra do dicionário. Exibe erro se a palavra não existir.                                      |
| `p`                       | Imprime a árvore em pré-ordem, mostrando a chave e seus filhos. Usa `nil` para filhos ausentes.              |
| `e`                       | Encerra o programa.                                                                                     |

**Observação:** Os comandos `a + letra` e `s + letra + número` parecem estar incompletos. Você pode me dizer qual a função deles para que eu possa adicioná-los corretamente?

### 📥 Entrada e 📤 Saída

* **Entrada:** Comandos com palavras em minúsculas e sem acento.
* **Saída:** Mensagens e listagens de acordo com o comando executado.

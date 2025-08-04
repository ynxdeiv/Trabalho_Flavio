📚 Trabalhos de Estruturas de Dados
🔹 Trabalho 1 – Gerenciador de Palavras com Listas Encadeadas
📖 Descrição
Programa que gerencia palavras organizadas em três listas simplesmente encadeadas conforme o tamanho das palavras:

Lista 1: Palavras com até 5 letras

Lista 2: Palavras de 6 a 10 letras

Lista 3: Palavras com mais de 10 letras

Além disso, cada palavra está ligada a listas encadeadas pelas classes morfológicas:
adjetivo (adj), substantivo (subst), verbo (verbo). Todas as listas mantêm as palavras em ordem alfabética.

🛠️ Comandos
Comando	Descrição
i + palavra + classe	Insere palavra na lista básica e classe morfológica (adj, subst, verbo). Se existir, mostra erro.
l + número (1 a 3)	Lista palavras da lista básica correspondente.
m + classe	Lista palavras da classe morfológica.
x + número + classe	Lista palavras da classe morfológica com tamanho exato.
o	Lista todas as palavras em ordem alfabética.
c + dois números (1 a 3)	Intercala duas listas básicas e imprime palavras alternadas.
r + palavra	Remove palavra, ou avisa se não existir.
e	Encerra o programa.

📥 Entrada e 📤 Saída
Entrada: comandos com palavras minúsculas e sem acentos.

Saída: mensagens e listagens conforme comandos.

🔹 Trabalho 2 – Dicionário Bilíngue com Árvore Binária de Busca
📖 Descrição Geral
Implementa um dicionário bilíngue com palavras no idioma origem organizadas numa árvore binária de busca. Cada palavra possui:

Traduções para o idioma destino

Classe morfológica: substantivo, adjetivo ou verbo

🛠️ Comandos
Comando	Descrição
i	Insere palavra no idioma origem, classe (s=substantivo, a=adjetivo, v=verbo) e até 10 traduções. Mensagem de erro se palavra já existe.
l	Lista todas as palavras do idioma origem em ordem alfabética.
t + palavra	Lista traduções da palavra. Mensagem de erro se não existir.
a + letra (s	a
s + letra + número	Lista palavras da classe e tamanho exato.
c + palavra	Consulta classe morfológica da palavra. Mensagem de erro se não existir.
r + palavra	Remove palavra do dicionário. Mensagem de erro se não existir.
p	Imprime a árvore binária em pré-ordem, mostrando chave e filhos (usa nil para filhos ausentes).
e	Encerra o programa.

📥 Entrada e 📤 Saída
Entrada: comandos conforme descritos, todas palavras minúsculas e sem acento.

Saída: mensagens e listagens conforme cada comando.

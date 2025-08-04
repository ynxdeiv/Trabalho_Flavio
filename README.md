Trabalho 1 – Gerenciador de Palavras com Listas Encadeadas
Descrição
Programa que armazena palavras em três listas simplesmente encadeadas, divididas por tamanho:

Lista 1: palavras com até 5 letras

Lista 2: palavras de 6 a 10 letras

Lista 3: palavras com mais de 10 letras

Além disso, as palavras estão ligadas a listas encadeadas pelas classes morfológicas: adjetivo (adj), substantivo (subst) e verbo (verbo). Todas as listas mantêm as palavras em ordem alfabética.

Comandos
Comando	Descrição
i + palavra + classe	Insere palavra (classes: adj, subst ou verbo). Se existir, exibe mensagem de erro.
l + número (1 a 3)	Lista palavras da lista básica correspondente.
m + classe	Lista palavras da classe morfológica.
x + número + classe	Lista palavras da classe com tamanho exato.
o	Lista todas as palavras em ordem alfabética.
c + dois números (1 a 3)	Intercala duas listas básicas e imprime palavras alternadas.
r + palavra	Remove palavra, ou avisa se não existir.
e	Encerra o programa.

Entrada e Saída
Entrada: comandos conforme descritos acima, com palavras sem acentos e todas em minúsculas.

Saída: mensagens e listagens conforme cada comando.

Trabalho 2 – Dicionário Bilíngue com Árvore Binária de Busca
1. Descrição Geral
Programa que armazena palavras em um idioma origem, suas traduções em um idioma destino e a classe morfológica (substantivo, adjetivo ou verbo). As palavras do idioma origem são organizadas em uma árvore binária de busca, onde as chaves são as palavras do idioma origem.

2. Entrada e Saída
O programa lê comandos da entrada padrão e gera saídas conforme descrito:

Comandos principais
Comando	Descrição
i	Insere palavra no idioma origem, sua classe (s=substantivo, a=adjetivo, v=verbo) e traduções (até 10). Se existir, exibe palavra ja existente: <palavra>. Se inserir, exibe palavra inserida no dicionario: <palavra>.
l	Lista todas as palavras do idioma origem em ordem alfabética (uma por linha).
t + palavra	Lista traduções da palavra. Se não existir, exibe palavra inexistente: <palavra>. Se existir, mostra traducoes da palavra: <palavra>, seguido das traduções.
a + letra (s	a
s + letra (s	a
c + palavra	Consulta a classe morfológica da palavra. Se não existir, exibe palavra inexistente no dicionario: <palavra>. Se existir, exibe classe da palavra: <palavra>: <classe>.
r + palavra	Remove palavra do dicionário. Se não existir, exibe palavra inexistente no dicionario: <palavra>. Se remover, exibe palavra removida: <palavra>.
p	Imprime a árvore em pré-ordem no formato: chave: <palavra> fesq: <filho_esq> fdir: <filho_dir> (usa nil para filhos ausentes).
e	Encerra o programa.

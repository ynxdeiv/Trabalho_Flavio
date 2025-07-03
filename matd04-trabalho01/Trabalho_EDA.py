# Trabalho de Estruturas de Dados
# Aluno: Deivid Costa dos Santos
# Matricula: 224119988





class Node:
    
    # Representa um nó na lista encadeada, contendo a palavra, o tipo e ponteiros para os próximos nós

    def __init__(self, palavra, tipo):
        self.palavra = palavra
        self.tipo = tipo
        self.prox_tamanho = None 
        self.prox_tipo = None
        self.prox_alfabetica = None  
class LinkedList:
    def __init__(self):
        self.lista1 = None  # lista 1 a 5 letras
        self.lista2 = None  # lista 6 a 10 letras
        self.lista3 = None  # lista mais de 10 letras
        self.lista_adj = None # lista de adjetivos
        self.lista_subst = None # lista de substantivos
        self.lista_verbo = None # lista de verbos
        self.lista_alfabetica = None # lista de palavras em ordem alfabetica
    def busca_palavra(self, palavra):
        # Esse lower foi utilizado para evitar problemas com letras maiusculas e minusculas
        palavra = palavra.lower()
        if not self.lista1 and not self.lista2 and not self.lista3:
            return False
        
        for lista in [self.lista1, self.lista2, self.lista3]:
            atual = lista
            while atual:
                if atual.palavra == palavra:
                    return True
                atual = atual.prox_tamanho
        return False
    def insere_palavra(self, palavra, tipo):
        if tipo not in ["adj", "subst", "verbo"]:
            return
            
        if self.busca_palavra(palavra):
            print(f"palavra ja existente: {palavra}")
            return
        
        novo_node = Node(palavra, tipo)
        tamanho = len(palavra)
        
        self.lista_alfabetica = self.lista_ordem_alfabetica(novo_node)

        if 1 <= tamanho <= 5:
            self.lista1 = self.inserir_ordenado_tamanho(novo_node, self.lista1)
        elif 6 <= tamanho <= 10:
            self.lista2 = self.inserir_ordenado_tamanho(novo_node, self.lista2)
        elif tamanho > 10:
            self.lista3 = self.inserir_ordenado_tamanho(novo_node, self.lista3)
        
        if tipo == "adj":
            self.lista_adj = self.inserir_ordenado_tipo(novo_node, self.lista_adj)
        elif tipo == "subst":
            self.lista_subst = self.inserir_ordenado_tipo(novo_node, self.lista_subst)
        elif tipo == "verbo":
            self.lista_verbo = self.inserir_ordenado_tipo(novo_node, self.lista_verbo)
        
        print(f"palavra inserida: {palavra}")
    def lista_ordem_alfabetica(self, novo_node):
        # Lista auxiliar para inserir o nó na lista de forma ordenada alfabeticamente facilitando o print
        if not self.lista_alfabetica or novo_node.palavra < self.lista_alfabetica.palavra:
            novo_node.prox_alfabetica = self.lista_alfabetica
            self.lista_alfabetica = novo_node
            return novo_node
        atual = self.lista_alfabetica
        while atual.prox_alfabetica and atual.prox_alfabetica.palavra < novo_node.palavra:
            atual = atual.prox_alfabetica
        novo_node.prox_alfabetica = atual.prox_alfabetica
        atual.prox_alfabetica = novo_node
        return self.lista_alfabetica
    def print_lista_alfabetica(self):
        if not self.lista_alfabetica:
            print('lista vazia')
            return
        
        atual = self.lista_alfabetica
        while atual:
            print(atual.palavra)
            atual = atual.prox_alfabetica
    def inserir_ordenado_tamanho(self, novo_node, lista_head):
        # Insere o nó na lista de acordo com o tamanho da palavra
        if not lista_head or novo_node.palavra < lista_head.palavra:
            novo_node.prox_tamanho = lista_head
            return novo_node
        
        atual = lista_head
        while atual.prox_tamanho and atual.prox_tamanho.palavra < novo_node.palavra:
            atual = atual.prox_tamanho
        
        novo_node.prox_tamanho = atual.prox_tamanho
        atual.prox_tamanho = novo_node
        return lista_head
    def inserir_ordenado_tipo(self, novo_node, lista_head):
        # Insere o nó na lista de acordo com o tipo da palavra
        if not lista_head or novo_node.palavra < lista_head.palavra:
            novo_node.prox_tipo = lista_head
            return novo_node
        
        atual = lista_head
        while atual.prox_tipo and atual.prox_tipo.palavra < novo_node.palavra:
            atual = atual.prox_tipo
        
        novo_node.prox_tipo = atual.prox_tipo
        atual.prox_tipo = novo_node
        return lista_head
    def lista_palavras_basica(self, num: int):
        # Lista palavras de acordo com o tamanho da palavra
        lista_map = {1: self.lista1, 2: self.lista2, 3: self.lista3}
        if num not in lista_map:
            return
        
        lista_head = lista_map.get(num)
        
        if lista_head is None:
            print('lista vazia')
            return
        
        atual = lista_head
        while atual is not None:
            print(atual.palavra)
            atual = atual.prox_tamanho
        return
    def lista_palavras_tipo(self, tipo):
        # Lista palavras de acordo com o tipo da palavra
        tipo_map = {'adj': self.lista_adj, 'subst': self.lista_subst, 'verbo': self.lista_verbo}
        if tipo not in tipo_map:
            return
        lista_head = tipo_map.get(tipo)
        
        if lista_head is None:
            print('lista vazia')
            return
        
        atual = lista_head
        while atual is not None:
            print(atual.palavra)
            atual = atual.prox_tipo
        return
    def lista_palavras_tipo_tamanho(self, num: int, tipo):
        # Lista palavras de acordo com o tamanho e tipo da palavra
        tipo_map = {'adj': self.lista_adj, 'subst': self.lista_subst, 'verbo': self.lista_verbo}
        if tipo not in tipo_map:
            return
        if num <1:
            return
        lista_head = tipo_map.get(tipo)
        
        if lista_head is None:
            print('lista vazia')
            return
        
        atual = lista_head
        achou_palavra = False
        
        while atual is not None:
            if len(atual.palavra) == num:
                print(atual.palavra)
                achou_palavra = True
            atual = atual.prox_tipo
        
        if not achou_palavra:
            print('lista vazia')
        return
    def intercala_linhas(self, num1: int, num2: int):
        # Intercala palavras de duas listas diferentes
        
        
        lista_map = {1: self.lista1, 2: self.lista2, 3: self.lista3}
        if num1 not in lista_map or num2 not in lista_map:
            return
        
        lista1_head = lista_map.get(num1)
        lista2_head = lista_map.get(num2)
        
        if lista1_head is None and lista2_head is None:
            print('listas vazias')
            return 
        
        atual_l1 = lista1_head
        atual_l2 = lista2_head
        

        
        while atual_l1 or atual_l2:
            if atual_l1:
                print(atual_l1.palavra)
                atual_l1 = atual_l1.prox_tamanho
            if atual_l2:
                print(atual_l2.palavra)
                atual_l2 = atual_l2.prox_tamanho
        return
    def remove(self, palavra):
        # Remove uma palavra das listas, se existir
        palavra = palavra.lower()
        if not self.busca_palavra(palavra):
            print(f"palavra inexistente: {palavra}")
            return
        
        self.lista_alfabetica = self.remove_alfabetica(palavra)
        self.lista1 = self.remove_tamanho(palavra, self.lista1)
        self.lista2 = self.remove_tamanho(palavra, self.lista2)
        self.lista3 = self.remove_tamanho(palavra, self.lista3)
        self.lista_adj = self.remove_tipo(palavra, self.lista_adj)
        self.lista_subst = self.remove_tipo(palavra, self.lista_subst)
        self.lista_verbo = self.remove_tipo(palavra, self.lista_verbo)    
        print(f"palavra removida: {palavra}")
        
        return
    def remove_alfabetica(self, palavra):
        # Remove uma palavra da lista alfabetica
        palavra = palavra.lower()
        if not self.lista_alfabetica:
            return None
        if self.lista_alfabetica.palavra == palavra:
            return self.lista_alfabetica.prox_alfabetica
        atual = self.lista_alfabetica
        while atual.prox_alfabetica:
            if atual.prox_alfabetica.palavra == palavra:
                atual.prox_alfabetica = atual.prox_alfabetica.prox_alfabetica
                return self.lista_alfabetica
            atual = atual.prox_alfabetica
        return self.lista_alfabetica
    def remove_tamanho(self, palavra, lista_head):
        
        # Remove uma palavra da lista de acordo com o tamanho
        palavra = palavra.lower()
        if not lista_head:
            return lista_head
        
        if lista_head.palavra == palavra:
            return lista_head.prox_tamanho
        
        atual = lista_head
        while atual.prox_tamanho:
            if atual.prox_tamanho.palavra == palavra:
                atual.prox_tamanho = atual.prox_tamanho.prox_tamanho
                break
            atual = atual.prox_tamanho
        
        return lista_head
    def remove_tipo(self, palavra, lista_head):
        
        # Remove uma palavra da lista de acordo com o tipo
        palavra = palavra.lower()
        if not lista_head:
            return lista_head
        
        if lista_head.palavra == palavra:
            return lista_head.prox_tipo
        
        atual = lista_head
        while atual.prox_tipo:
            if atual.prox_tipo.palavra == palavra:
                atual.prox_tipo = atual.prox_tipo.prox_tipo
                break
            atual = atual.prox_tipo
        
        return lista_head
def main():
    sistema = LinkedList()
    while True:
        try:
            comando = input().strip()
            
            if comando == 'e':
                break
            elif comando == 'i':
                palavra = input().strip()
                tipo = input().strip()
                sistema.insere_palavra(palavra, tipo)
            elif comando == 'l':
                num = int(input())
                sistema.lista_palavras_basica(num)
            elif comando == 'm':
                tipo = input().strip()
                sistema.lista_palavras_tipo(tipo)
            elif comando == 'x':
                num = int(input())
                tipo = input().strip()
                sistema.lista_palavras_tipo_tamanho(num, tipo)
            elif comando == 'o':
                sistema.print_lista_alfabetica()
            elif comando == 'c':
                num1 = int(input())
                num2 = int(input())
                sistema.intercala_linhas(num1, num2)
            elif comando == 'r':
                palavra = input().strip()
                sistema.remove(palavra)
        except:
            continue

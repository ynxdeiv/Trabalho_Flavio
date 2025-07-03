class Node:
    def __init__(self, palavra, tipo, traducoes):
        self.palavra = palavra
        self.tipo = tipo
        self.traducoes = traducoes
        self.esquerda = None
        self.direita = None
        self.prox_alfabetica = None
        self.prox_tipo = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        self.lista_alfabetica = None
        self.lista_adjetivo = None 
        self.lista_verbo = None 
        self.lista_substantivo = None
        
    def busca(self, palavra):
        palavra = palavra.lower()
        current = self.raiz
        
        while current is not None:
            if palavra == current.palavra:
                return current 
            elif palavra < current.palavra:
                current = current.esquerda
            else:
                current = current.direita
        return None 
    
    def inserirAlfabetico(self, node_para_inserir): 
        if not self.lista_alfabetica or node_para_inserir.palavra < self.lista_alfabetica.palavra:
            node_para_inserir.prox_alfabetica = self.lista_alfabetica
            self.lista_alfabetica = node_para_inserir
            return
        
        current = self.lista_alfabetica
        while current.prox_alfabetica and current.prox_alfabetica.palavra < node_para_inserir.palavra:
            current = current.prox_alfabetica
        
        node_para_inserir.prox_alfabetica = current.prox_alfabetica
        current.prox_alfabetica = node_para_inserir

    def listar_alfabeticamente(self):
        if not self.lista_alfabetica:
            return
        current = self.lista_alfabetica
        while current:
            print(current.palavra)
            current = current.prox_alfabetica
    
    def inserirTipo(self, node_para_inserir):
        if node_para_inserir.tipo == "a":
            if not self.lista_adjetivo or node_para_inserir.palavra < self.lista_adjetivo.palavra:
                node_para_inserir.prox_tipo = self.lista_adjetivo
                self.lista_adjetivo = node_para_inserir
                return
            
            current = self.lista_adjetivo
            while current.prox_tipo and current.prox_tipo.palavra < node_para_inserir.palavra:
                current = current.prox_tipo
            
            node_para_inserir.prox_tipo = current.prox_tipo
            current.prox_tipo = node_para_inserir
        
        elif node_para_inserir.tipo == "v":
            if not self.lista_verbo or node_para_inserir.palavra < self.lista_verbo.palavra:
                node_para_inserir.prox_tipo = self.lista_verbo
                self.lista_verbo = node_para_inserir
                return
            
            current = self.lista_verbo
            while current.prox_tipo and current.prox_tipo.palavra < node_para_inserir.palavra:
                current = current.prox_tipo
            
            node_para_inserir.prox_tipo = current.prox_tipo
            current.prox_tipo = node_para_inserir
        
        elif node_para_inserir.tipo == "s":
            if not self.lista_substantivo or node_para_inserir.palavra < self.lista_substantivo.palavra:
                node_para_inserir.prox_tipo = self.lista_substantivo
                self.lista_substantivo = node_para_inserir
                return
            
            current = self.lista_substantivo
            while current.prox_tipo and current.prox_tipo.palavra < node_para_inserir.palavra:
                current = current.prox_tipo
            
            node_para_inserir.prox_tipo = current.prox_tipo
            current.prox_tipo = node_para_inserir

    def listar_por_tipo(self, tipo):
        if tipo == "a":
            current = self.lista_adjetivo
        elif tipo == "v":
            current = self.lista_verbo
        elif tipo == "s":
            current = self.lista_substantivo
        else:
            return
        
        if not current:
            return
        
        while current:
            print(current.palavra)
            current = current.prox_tipo

    def listar_por_tipo_tamaho(self, tipo, tamanho):
        if tipo == "a":
            current = self.lista_adjetivo
        elif tipo == "v":
            current = self.lista_verbo
        elif tipo == "s":
            current = self.lista_substantivo
        else:
            return

        if not current:
            return
        while current:
            if len(current.palavra) == tamanho:
                print(current.palavra)
            current = current.prox_tipo
        
    def busca_classe(self):
        palavra_digitada = input().strip().lower()
        current_node = self.busca(palavra_digitada) 
        
        if current_node is None:
            print(f"palavra inexistente no dicionario: {palavra_digitada}")
        else:
            tipo_extenso = {
                "s": "substantivo", 
                "v": "verbo",
                "a": "adjetivo",
            }
            tipo_para_mostrar = tipo_extenso.get(current_node.tipo) 
            if tipo_para_mostrar is None:
                return
            print(f"classe da palavra: {palavra_digitada}: {tipo_para_mostrar}")

    def listar_traducoes(self): 
        palavra_para_buscar = input().strip().lower() 
        
        node_encontrado = self.busca(palavra_para_buscar) 
        
        if node_encontrado is None:
            print(f"palavra inexistente: {palavra_para_buscar}") 
        else:
            print(f"traducoes da palavra: {palavra_para_buscar}")
            for traducao in node_encontrado.traducoes: 
                print(traducao) 

    def inserir(self):
        palavra = input().strip().lower()
        tipo = input().strip().lower() 
        num_traducoes = int(input().strip())
        traducoes = []
        for _ in range(num_traducoes):
            traducoes.append(input())
        
        if self.busca(palavra) is not None:
            print(f"palavra ja existente: {palavra}") 
            return
            
        novo_node_arvore = Node(palavra, tipo, traducoes) 

        if self.raiz is None:
            self.raiz = novo_node_arvore
        else:
            current = self.raiz
            while True: 
                if palavra < current.palavra:
                    if current.esquerda is None:
                        current.esquerda = novo_node_arvore
                        break 
                    else:
                        current = current.esquerda
                else:
                    if current.direita is None:
                        current.direita = novo_node_arvore
                        break 
                    else:
                        current = current.direita
        
        print(f"palavra inserida no dicionario: {palavra}")
        self.inserirAlfabetico(novo_node_arvore) 
        self.inserirTipo(novo_node_arvore)

    def _find_min_node(self, node):
        current = node
        while current.esquerda is not None:
            current = current.esquerda
        return current

    def _remover_from_linked_list(self, head, palavra_alvo, is_type_list=False):
        if not head:
            return None
        
        if head.palavra == palavra_alvo:
            return head.prox_tipo if is_type_list else head.prox_alfabetica
        
        current = head
        while (is_type_list and current.prox_tipo) or (not is_type_list and current.prox_alfabetica):
            next_node = current.prox_tipo if is_type_list else current.prox_alfabetica
            if next_node and next_node.palavra == palavra_alvo:
                if is_type_list:
                    current.prox_tipo = next_node.prox_tipo
                else:
                    current.prox_alfabetica = next_node.prox_alfabetica
                return head
            current = next_node
        return head

    def remover(self):
        palavra_remover = input().strip().lower()
        
        if self.busca(palavra_remover) is None:
            print(f"palavra inexistente no dicionario: {palavra_remover}")
            return

        def _remover_recursive_bst(node, palavra_alvo):
            if node is None:
                return node
            
            if palavra_alvo < node.palavra:
                node.esquerda = _remover_recursive_bst(node.esquerda, palavra_alvo)
            elif palavra_alvo > node.palavra:
                node.direita = _remover_recursive_bst(node.direita, palavra_alvo)
            else:
                if node.esquerda is None:
                    return node.direita
                elif node.direita is None:
                    return node.esquerda
                
                temp = self._find_min_node(node.direita)
                node.palavra = temp.palavra
                node.tipo = temp.tipo
                node.traducoes = temp.traducoes
                node.direita = _remover_recursive_bst(node.direita, temp.palavra)
            return node

        self.raiz = _remover_recursive_bst(self.raiz, palavra_remover)

        self.lista_alfabetica = self._remover_from_linked_list(self.lista_alfabetica, palavra_remover)
        self.lista_adjetivo = self._remover_from_linked_list(self.lista_adjetivo, palavra_remover, is_type_list=True)
        self.lista_verbo = self._remover_from_linked_list(self.lista_verbo, palavra_remover, is_type_list=True)
        self.lista_substantivo = self._remover_from_linked_list(self.lista_substantivo, palavra_remover, is_type_list=True)

        print(f"palavra removida: {palavra_remover}")

    def imprime_arvore(self, node):
        if node:
            fesq_val = node.esquerda.palavra if node.esquerda else "nil"
            fdir_val = node.direita.palavra if node.direita else "nil"
            print(f"chave: {node.palavra} fesq: {fesq_val} fdir: {fdir_val}")
            self.imprime_arvore(node.esquerda)
            self.imprime_arvore(node.direita)

if __name__ == "__main__":
    arvore = ArvoreBinaria()
    
    while True:
        try:
            comando = input().strip()
            if comando == "i":
                arvore.inserir()
            elif comando == "l":
                arvore.listar_alfabeticamente()
            elif comando == "c":
                arvore.busca_classe()
            elif comando == "a":
                tipo = input().strip().lower()
                arvore.listar_por_tipo(tipo)
            elif comando == "t":
                arvore.listar_traducoes() 
            elif comando == "s":
                tipo = input().strip().lower()
                tamanho = int(input().strip())
                arvore.listar_por_tipo_tamaho(tipo, tamanho)
            elif comando == "r": 
                arvore.remover()
            elif comando == "p": 
                arvore.imprime_arvore(arvore.raiz)
            elif comando == "e":
                break
            
        except EOFError:
            break
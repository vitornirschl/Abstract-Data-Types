# Abstract Data Types (ADT)

Esse é um pacote brinquedo desenvolvido como companhia para meus estudos no curso de Algoritmos e Estruturas de Dados (MAC0122) no IME-USP. 

O objetivo é aprender a implementar Tipos de Dados Abstrados (Abstract Data Types, ou ADT) em Python, utilizando o paradigma de Programação Orientada a Objetos (POO).

Trata-se ainda de uma boa oportunidade para colocar aplicar boas práticas de programação e tratamento de exceções.

### Tipos de Dados a serem implementados

- [ ] Conjuntos
- [ ] Vetores
- [ ] Matrizes
- [x] Frações
- [ ] Polinômios
- [x] Pilhas (Stacks)
- [ ] Filas (Queues)

#### Frações
Uma instância da Fraction recebe um numerador e um denominador, ambos inteiros, os quais são simplificados quando houver fator comum. O gerenciamento de exceções garante o funcionamento do módulo conforme planejado.

Foi implementada a sobrecarga dos operadores de soma, subtração, multiplicação, divisão, divisão inteira, resto, exponenciação, valor absoluto, além dos operadores de comparação e de conversão para outros tipos numéricos. Também foram implementadas as representações de string e abstrata da classe.

_TODO: Módulo de testagem da classe de frações_

#### Pilhas
A estrutura de dados Stack (pilha) obedece a lógica LIFO/FILO (Last Fn, First Out ou First In, Last Out) - em português, o último a entrar é o primeiro a sair e o primeiro a entrar é o último a sair. Como numa pilha de pratos, o último item a ser adicionado na pilha é o primeiro a ser retirado e vice-versa.

Foram implementadas duas formas de pilhas: uma com tamanho flexível, tendo sua alocação de espaço na memória aumentada conforme necessário, e outra com tamanho fixo. A primeira tem um tempo de execução maior em decorrência da alocação dinâmica da memória, diferentemente da segunda, que é mais ágil. 

Foram implementados os métodos

- is_empty() : verifica se a pilha está vazia;
- push() : adiciona um ítem ao topo da pilha;
- pop() : remove o último item da pilha;
- top() : mostra o último ítem da pilha.

Além disso, para as pilhas de tamanho fixo, foi implementado o método _expand(max_length)_ que aumenta a pilha até o tamanho max_length. Também foram implementadas as representações de string e abstrata das classes de pilhas e a sobrecarga do operador len.

 _TODO: Módulo de testagem da classe de pilhas_
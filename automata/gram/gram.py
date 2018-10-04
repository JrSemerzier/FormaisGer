from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
import copy
class GRAM:# O DFA deriva(acrescenta) a class FA do arquivo fa.py
    """A deterministic finite automaton."""

    def __init__(self, variables, symbols, productions,
                 initial_variable):
    	self.variables = variables.copy()
    	self.symbols=symbols.copy()
    	self.productions=copy.deepcopy(productions)
    	self.initial_variable=initial_variable

    def Gram_to_auto(self):
        transicoes={}#dicionario vazia
        for elem in self.productions.items():#cada item in the dicionario elem=('s',{'aS','bB'})
            val={}#dicionario vazia val={'a':'s','b':'B'}
            for elem1 in elem[1]:#elem1= 'bB/ c/ bB/ aS'
                # for sym in self.symbols:                   
                if len(elem1)>1: #for cada values in the dicionario
                    val[elem1[0]]= elem1[1]                     
                if len(elem1)==1:
                    val[elem1[0]]='φ'
            transicoes[elem[0]]=val
        #print(transicoes)  
        final_state={'φ'}  
        nfa = NFA(
        self.variables,
        self.symbols,
        transicoes,#{'S': {'a': 'S', 'b': 'B'}, 'B': {'c': 'φ', 'b': 'B'}}
        self.initial_variable,
        final_state
        )
        #return nfa
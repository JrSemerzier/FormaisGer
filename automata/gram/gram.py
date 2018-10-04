from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

class GRAM:# O DFA deriva(acrescenta) a class FA do arquivo fa.py
    """A deterministic finite automaton."""

    def __init__(self, variables, symbols, productions,
                 initial_variable):
    	self.variables = variables.copy()
    	self.symbols=symbols.copy()
    	self.productions=copy.deepcopy(productions)
    	self.initial_variable=initial_variable

    def Gram_to_auto(self):
        tansicoes={}#dicionario vazia
        estados={}#dicionario vazia
        for elem in self.productions.items():#cada item in the dicionario
        	if len(elem.values())>1: #for cada values in the dicionario
        	#criar uma dicionario (transiçaõ)
        		estados[elem.values[0]]= elem.values[1] 
        		tansicoes[elem.keys()]= estados
        		 #estado={'A':a}
        	if elem.values()==1:
        		estados[elem.values[0]]='φ'
        		tansicoes[elem.keys()]= estados	
        nfa = NFA(
	    self.variables,
	    self.symbols,
	    tansicoes,
	    self.initial_variable,
	    final_states='φ'
	    )
		#return nfa
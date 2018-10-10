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

def Gram_to_auto(gram):
    transicoes={}#dicionario vazia
    for elem in gram.productions.items():#cada item in the dicionario elem=('s',{'aS','bB'})
        val={}#dicionario vazia val={'a':'s','b':'B'}
        for elem1 in elem[1]:#elem1= 'bB/ c/ bB/ aS'
            # for sym in self.symbols:                   
            if len(elem1)>1: #for cada values in the dicionario
                val[elem1[0]]= elem1[1]                     
            if len(elem1)==1:
                val[elem1[0]]='φ'
        transicoes[elem[0]]=val
    final_state={'φ'}
    variables=set()
    variables=gram.variables
    variables.add('φ')
   # var=self.variables
    print(transicoes) 
    print(final_state) 
    print(variables) 
    print(gram.symbols)
    print(gram.initial_variable)
   
    # nfa = NFA(
    # variables,
    # gram.symbols,
    # transicoes,#{'S': {'a': 'S', 'b': 'B'}, 'B': {'c': 'φ', 'b': 'B'}}
    # gram.initial_variable,
    # final_state
    # )
    # return nfa

def Auto_to_gram(auto):
    intial_symbol=auto.initial_state
    variables=auto.states
    symbols= auto.input_symbols
    productions={}
    for states in auto.transitions.keys():#states='q0','q1','q2'
        val=auto.transitions.get(states) #val={'a': {'q0','q1'},'b':{'q0'}
        if  val.keys() is not None: #vl.keys=
            um_set=set()# n auxilar set use as value in a dictonary
            for sym in val.keys():  # 'a' e 'b'        
                val2=val.get(sym) # val2={'q0','q1'}
                if val2 is not set():
                    for elem2 in val2: #elem2='q0'
                        if elem2 in auto.final_states:
                            um_set.add(sym)
                        else:
                            conc=sym+elem2
                            um_set.add(conc)
                    #print(type(val2))#check type of a variable
        if len(um_set)!=0:# se o conjunto não está vazia
            productions.update({states:um_set }) 
    if auto.initial_state in auto.final_states:
        valueSymInical=productions.get(auto.initial_state)
        valueSymInical.add('ε')

    return productions
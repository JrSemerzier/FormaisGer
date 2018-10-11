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
    for elem in gram.productions.keys():#cada item in the dicionario elem='s'/'B'
        valu=gram.productions.get(elem) #valu={'aS','bB'}
        aux={}
        parteDireita={}
        for sym in gram.symbols:#sym='a'/'b'/'c'}
            val=set()#the table can have um set for each symbolo
            for elem1 in valu:#elem1='aS'
                if len(elem1)>1: #for cada values in the dicionario
                    if sym==elem1[0]:
                        val.add(elem1[1])             
                if len(elem1)==1:
                    if sym==elem1[0]:
                        val.add('φ')
            if  len(val)!=0:#para não colocar {}(conjunto vazia quando a tabela tem -)
                parteDireita.update({sym:val})

        transicoes.update({elem :parteDireita}) 

    final_state={'φ'}# estado adicional que um estado final
    variables=set() #recriando uma outra Conjunto de variavel para adicionar o novo variavel
    variables=gram.variables
    variables.add('φ')
    return transicoes                 
    

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
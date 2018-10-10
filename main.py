from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
from automata.gram.gram import *

if __name__== "__main__":
	# DFA which matches all binary strings ending in an odd number of '1's

# NFA which matches strings beginning with 'a', ending with 'a', and containing
# no consecutive 'b's
    # dfa = DFA(
    # states={'q0', 'q1', 'q2'},
    # input_symbols={'0', '1'},
    # transitions={
    #     'q0': {'0': 'q0', '1': 'q1'},
    #     'q1': {'0': 'q0', '1': 'q2'},
    #     'q2': {'0': 'q2', '1': 'q1'}
    # },
    # initial_state='q0',
    # final_states={'q1'}
    # )

    # print(dfa.read_input('01'))
    # for elem in list(dfa.read_input_stepwise('0111')):
    #     print(elem)
    
    # if dfa.accepts_input('01'):
    #     print('accepted')
    # else:
    #     print('rejected')

    # print(dfa.validate())
    # print(dfa._create_markable_states_table())
  # ==========================================================================================
# # MINIMIZAÇÃO DE AUTOMATO DFA
#     minimal_dfa = dfa.minify()
#     print(minimal_dfa)

#     print(minimal_dfa.transitions)
#     print(minimal_dfa.initial_state)
#     print(minimal_dfa.final_states)
# =========================================================================================
    # DETERMINIZAÇÃO COM YPSILONE('ε')
    # NFA which matches strings beginning with 'a', ending with 'a', and containing
    # no consecutive 'b's
    # nfa = NFA(
    # states={'q0', 'q1', 'q2'},
    # input_symbols={'a', 'b'},
    # transitions={
    #     'q0': {'a': {'q1'}},
    #     # Use 'ε' as the key name for empty string (lambda/epsilon) transitions
    #     'q1': {'a': {'q1'}, 'ε': {'q2'}},
    #     'q2': {'b': {'q0'}}
    # },
    # initial_state='q0',
    # final_states={'q1'}
    # )
    
    # dfa = DFA.from_nfa(nfa)
    # print(dfa)

    # print(dfa.transitions)
    # print(dfa.initial_state)
    # print(dfa.final_states)
# =============================================================================================
    # # DETERMINIZAÇÃO SEM YPSILONE

    # nfa = NFA(
    # states={'q0', 'q1', 'q2'},
    # input_symbols={'a', 'b'},
    # transitions={
    #     'q0': {'a': {'q0','q1'},'b':{'q0'}},
    #     # Use 'ε' as the key name for empty string (lambda/epsilon) transitions
    #     'q1': {'b': {'q2'}},
    #     'q2': {}
    # },
    # initial_state='q0',
    # final_states={'q2'}
    # )
    
    # dfa = DFA.from_nfa(nfa)
    # print(dfa)
    # print(dfa.transitions)
    # print(dfa.initial_state)
    # print(dfa.final_states)
        
	# ==============================================================================================
    #GRAMMAR TO AUTOMATA TO GRAMMAR
    # gram= GRAM(
    # variables={'S', 'B'},
    # symbols={'a', 'b','c'},
    # productions={'S':{'aS','bB'},
    #             'B':{'bB','c'}
    # },
    # initial_variable='S' 
    # )
    # aut=Gram_to_auto(gram)
#AUTOMATO TO GRAMMAR
    nfa = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': {'q0','q1'},'b':{'q0'}},
        # Use 'ε' as the key name for empty string (lambda/epsilon) transitions
        'q1': {'b': {'q2'}},
        'q2': {}
    },
    initial_state='q0',
    final_states={'q2','q0'}
    )

    gram=Auto_to_gram(nfa)

    print(gram)

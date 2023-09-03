from qiskit.circuit.library import PhaseOracle
from qiskit import QuantumCircuit
from qiskit.circuit.library import GroverOperator
from qiskit import Aer, transpile


problem = [   
    [1],
    [4,5,6],
    [7],
    [-3,-6],
    [-2,4,-5]]
 



def save_to_dimacs(file_path, clauses):
    with open(file_path, 'w') as file:
        file.write("p cnf 7 3\n")  

        for clause in clauses:
            file.write(" ".join(map(str, clause)) + " 0\n")


save_to_dimacs("formula.dimacs", problem)

def Grovers_algorithm(number_of_qubits):
  oracle = PhaseOracle.from_dimacs_file('formula.dimacs')
  init = QuantumCircuit(number_of_qubits)
  for i in range(number_of_qubits):
    init.h(i)
  grover_operator = GroverOperator(oracle)
  qc = init.compose(grover_operator)
  qc.measure_all()
  sim = Aer.get_backend('aer_simulator')
  t_qc = transpile(qc, sim)
  sim.run(t_qc).result().get_counts()

Grovers_algorithm(7)


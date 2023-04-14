class DFA:
  def __init__(self, Q, Sigma, delta, q0, F):
    self.Q = Q            # set of states
    self.Sigma = Sigma    # set of symbols
    self.delta = delta    # transition function as a dictionary
    self.q0 = q0          # initial state
    self.F = F            # set of final states

  def __repr__(self):
    return f"    DFA({self.Q},\n\t{self.Sigma},\n\t{self.delta},\n\t{self.q0},\n\t{self.F})"

  def run(self, w):
    q = self.q0
    while w != "":
      q = self.delta[(q,w[0])]
      w = w[1:]

    return q in self.F


if __name__ == "__main__":
  D0 = DFA({0,1,2}, {"a", "b"},
           {(0,"a"):0,(0,"b"):1,
            (1,"a"):2,(1,"b"):1,
            (2,"a"):2,(2,"b"):2},
           0,
           {0,1})
  print(repr(D0))

  print(f'aa:       {D0.run("aa")}')
  print(f'aabbb:    {D0.run("aabbb")}')
  print(f'ba:       {D0.run("ba")}')
  print(f'aba:      {D0.run("aba")}')
  print(f'ebsilon:  {D0.run("")}')






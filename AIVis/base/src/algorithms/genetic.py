import random, time, string

class GeneticAlgorithm:
  def __init__(self, pop, ideal, n, bits, cross_rate, mutation_rate):
    self.pop = pop
    self.n_pop = len(pop)
    self.ideal = ideal
    self.n = n
    self.bits = bits
    self.cross_rate = cross_rate
    self.mutation_rate = mutation_rate

  def fitness(self, chromosome):
    return sum( [int(c) * 2**(self.bits - i - 1) for i, c in enumerate(chromosome)] )

  def select(self, k=3):
    selection = random.choice(self.pop)
    for p in random.choices(self.pop, k=k):
      if self.fitness(p) > self.fitness(selection):
        selection = p
    
    return selection

  def crossover(self,p1, p2):
    pt = len(p1)
    if random.random() < self.cross_rate:
      pt = random.randint(1, len(p1)-2)

    return [
      p1[:pt] + p2[pt:],
      p2[:pt] + p1[pt:]
    ]

  def mutation(self, c):
    if random.random() < self.mutation_rate:
      idx = random.randint(0, len(c)-1)
      c[idx] = str(1 - int(c[idx]))
    return c
  
  def run(self, debug=False):
    best = random.choice(self.pop)
    fitness_matrix = []

    for i in range(self.n):
      oldbest = best
      fitness_matrix.append([])
      for ch in self.pop:
        b = self.fitness(best); f = self.fitness(ch)
        fitness_matrix[i].append(f)
        if f > b:
          best = ch
      
      fitness_matrix[i] = (best, fitness_matrix[i])

      if debug and best > oldbest:
        print(f"[{i}] {''.join(best), self.fitness(best)}")
      if best == self.ideal:
        break

      selected_pairs = [(self.select(), self.select()) for _ in range(int(self.n_pop/2))]
      children = []
      for p1, p2 in selected_pairs:
        c1, c2 = self.crossover(p1, p2)
        c1, c2 = self.mutation(c1), self.mutation(c2)
        children.extend((c1, c2))
      
      self.pop = children

    return i, ''.join(best), best == self.ideal, fitness_matrix

class TargetString(GeneticAlgorithm):
  def __init__(self, target, n_pop, max_gens, cross_rate, mutations_per_ch):
    self.pop_range = string.ascii_letters + string.punctuation + string.digits + ' '
    pop = [random.choices(self.pop_range, k=len(target)) for _ in range(n_pop)]
    super().__init__(pop, list(target), max_gens, len(target), cross_rate, mutations_per_ch/float(len(target)))

  def fitness(self, chromosome):
    f = sum( [1 for i, j in zip(chromosome, self.ideal) if i == j] )
    f -= sum( [ abs(ord(i) - ord(j))/57*len(chromosome) for i, j in zip(chromosome, self.ideal) if i != j  ] )
    return f
  
  def mutation(self,c):
    if random.random() < self.mutation_rate:
      idx = random.randint(0, len(c)-1)
      c[idx] = random.choice(self.pop_range.replace(c[idx], ''))
    return c

def genetic_algorithm(target, n_pop=50, max_gens=10000, cross_rate=0.9, mutations_per_ch=3.0):
  t = TargetString(target, n_pop, max_gens, cross_rate, mutations_per_ch)
  gens, best, found, fitness = t.run(False)
  return gens, best, found, fitness



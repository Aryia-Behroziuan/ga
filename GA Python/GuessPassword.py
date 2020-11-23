# Genetic Algoritm GA Python
# Guessing the password with a genetic algorithm

#Genes
geneSet = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!'
target = 'Hello World!'

#Generate a Guess
import random 

def generate_parent(length):
     genes = []
     SimpleSize = min(length - len(genes), len(geneSet))
     genes.extend(random.sample(geneSet, SimpleSize))
     return ''.join(genes)

# Fitness
def get_fitness(guess):
     return sum(1 for expected, actual in zip(target, guess)
                if expected == actual)

# Mutate
def mutate(parent):
     index = random.randrange(0, len(parent))
     ChildGenes = list(parent)
     NewGenes, alternate = random.sample(geneSet, 2)
     ChildGenes[index] = alternate \
          if NewGenes == ChildGenes[index] \
          else NewGenes
     return ''.join(ChildGenes)

def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
     random.seed()
# Display
import datetime

def display(guess):
     timeD = datetime.datetime.now() - startTime
     fitness = get_fitness(guess)
     print("{0}\t{1}\t{2}".format(guess, fitness, str(timeD)))

# Main
random.seed()
startTime = datetime.datetime.now()
bestparent = generate_parent(len(target))
bestfitness = get_fitness(bestparent)
display(bestparent)

while True:
     child = mutate(bestparent)
     childfitness = get_fitness(child)
     if bestfitness >= childfitness:
          continue
     display(child)
     if childfitness >= len(bestparent):
          break
     bestfitness = child
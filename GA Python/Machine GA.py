# Machine GA Genetic Algoritm
import random 

def _generate_parent(length, geneSet):
     genes = []
     SimpleSize = min(length - len(genes), len(geneSet))
     genes.extend(random.sample(geneSet, SimpleSize))
     return ''.join(genes)

def _mutate(parent, geneSet):
     index = random.randrange(0, len(parent))
     ChildGenes = list(parent)
     NewGenes, alternate = random.sample(geneSet, 2)
     ChildGenes[index] = alternate \
          if NewGenes == ChildGenes[index] \
          else NewGenes
     return ''.join(ChildGenes)


def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
     random.seed()
     bestparent = _generate_parent(targetLen, geneSet)
     bestfitness = get_fitness(bestparent)
     display(bestparent)
     if bestfitness >= optimalFitness:
          return bestparent

     while True:
          child = _mutate(bestparent, geneSet)
          childfitness = get_fitness(child)
          if bestfitness >= childfitness:
               continue
          display(child)
          if childfitness >= optimalFitness:
               return child
          bestfitness = child
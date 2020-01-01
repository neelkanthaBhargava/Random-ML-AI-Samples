#!/usr/bin/python -tt
# Supposedly a GA algo implementation to find the max of sin function
# can be extended to fine the max/min of other functions as well
# Let's see what happens!!!

import random
import math

# generate initial population
def generate_testset():
  x = [random.randint(0,(2**11)-1) for x in range(10)]
  return x

# generate equivalent x values for fitness function
def getEquiVal(chromosome, start = 0, end = math.pi):
  fraction = chromosome/(2**11)
  return start+fraction*(end-start)
  
# generate equivalent x values
def getEquiMatrix(chromosomes, start = 0, end = math.pi):
  x = [getEquiVal(chromosome,start,end) for chromosome in chromosomes]
  return x

# find fitness values for complete matrix
def fitnessMatrix(chromosomes, start = 0, end = math.pi):
  x = getEquiMatrix(chromosomes, start, end)
  fitness = [math.sin(xi) for xi in x]
  return fitness

# fitness Function
def fitnessFunction(chromosome, start = 0, end = math.pi):
  return math.sin(getEquiVal(chromosome,start,end))

# selection function
def selection(chromosomes, ran, start = 0, end = math.pi, maximize = False):
  sorted_chromosomes = sorted(chromosomes, key = fitnessFunction,reverse=maximize)
  return sorted_chromosomes[:ran]

# Crossover Function
def crossover(parents):
  child_population = []
  for i in range(0,8,2):
    child1 = parents[i]//8 + parents[i+1]%8
    child2 = parents[i+1]//8 + parents[i]%8
    child_population.append(child1)
    child_population.append(child2)
  return child_population

# Mutation Function
def mutation(individuals):
  child_population = []
  mutator = [2**x for x in range(11)]
  for i in range(8):
    random_child = random.randint(0,7)
    random_mutator = random.randint(0,10)
    child = individuals[random_child]^mutator[random_mutator]
    child_population.append(child)
    # print(bin(individuals[random_child]),bin(mutator[random_mutator]),bin(child))
  return child_population  

# print individual and its fitness
def print_fitness(population):
  for chrome in population:
    print(chrome,'-->',fitnessFunction(chrome))
  return

# GA Algo implemented
def ga_algo(generation=10):
  generation_results = []
  initialPop = generate_testset()
  print('initial population - ')
  print_fitness(initialPop)
  print()
  for i in range(generation):
    print('-------------- Generation %d --------------\n' % i)

    # Selection
    #
    selected_population = selection(initialPop,8,maximize = True)
    print('Selected Values - ')
    print_fitness(selected_population)
    print()

    # Crossover
    #
    crossover_population = crossover(selected_population)
    print('Crossover Population - ')
    print_fitness(crossover_population)
    print()

    # Mutation
    #
    mutated_population = mutation(selected_population)
    print('Mutated Population - ')
    print_fitness(mutated_population)
    print()

    # Elitist Selection
    #
    initialPop.extend(crossover_population)
    initialPop.extend(mutated_population)
    initialPop = selection(initialPop,10,maximize = True)
    print('Final Population - ')
    print_fitness(initialPop)
    print()

    # Print Generation Result
    #
    print('Max value at-')
    print_fitness(initialPop[0:1])
    generation_results.append(fitnessFunction(initialPop[0]))
    print()
  return generation_results
  
def main():
##  initialPop = generate_testset()
##  print('initial population - ',initialPop)
##  print()
##  print('equivalent values - ',getEquiVal(initialPop[0]))
##  print()
##  print('Equivalent Matrix - ',getEquiMatrix(initialPop))
##  print()
##  print('Fitness Matrix - ',fitnessMatrix(initialPop))
##  print()
##  selected_population = selection(initialPop,8,maximize = True)
##  print('Selected Values - ', selected_population)
##  print()
##  crossover_population = crossover(selected_population)
##  print('Crossover Child Population',crossover_population)
##  print()
##  mutated_population = mutation(selected_population)
##  print('Mutated Child Population',mutated_population)

  results = ga_algo(30)
  print(results)



if __name__ == '__main__':
  main()

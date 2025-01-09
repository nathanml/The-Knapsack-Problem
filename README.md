# The Knapsack Problem
## Instructions to run and test

From the root directory, run the following command in the 
command line:
```
python ga.py
```
Upon execution, a fitness graph plotting the path of the
genetic algorithm will be generated. The blue line 
represents the maximum fitness of each generation over time,
while the green line shows the average fitness of each
population over time. On most runs, these graphs will
increase and converge around a solution.

In addition to the graph, this program will return the 
solution that was found by the algorithm. It will
print the chromosome, the weight of the chromosome,
and the value.
```
RUNNING THE GENETIC ALGORITHM
ITEMS :  [(20, 6), (30, 5), (60, 8), (90, 7), (50, 6), (70, 9), (30, 4), (30, 5), (70, 4), (20, 9), (20, 2), (60, 1)]
Solution found!
Solution :  [1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1]
Solution Weight :  250
Solution Value :  44
```
## Genetic Algorithm Definition
The structure of the chromosome in this
algorithm is a 12-bit array, with each
bit representing whether the item is 
"selected" to be put in the knapsack.
Populations consist of a set of 30 
chromosomes.

### Initial Population
generate_initial_population() creates 30 chromosomes by
randomly assigning each bit as either
"selected" (1) or not (0).

### Fitness Function
fitness_function() takes as input a 
population of chromosomes and returns
an array of fitness values for each chromosome.

Chromosome fitness is based on the total value
of the knapsack and the proximity of the weight
to 250. This is calculated by adding the
value of the chromosome to the absolute value
of (250 - the weight).

This fitness metric can occasionally result
in the selection of a chromosome that 
exceeds the maximum weight. Initially, I set
the fitness of every chromosome with weight >250
to 0, however, this would frequently lead to 
solutions in which more items could be added to the
knapsack.

### Fringe Operators
reproduce() takes as input two parent
chromosomes and performs a single-point
crossover at a randomly selected index
of the chromosome.

mutate() randomly flips one of the bits
in a chromosome, adjusting the chromosome's
weight and value. This only occurs with
5% probability, which can be adjusted by
adjusting the variable MUTATION_RATE in 
globals.py.

### Solution Test
On several runs, the algorithm was able to find a
solution with a value of 44 and a weight of 250.
I decided to use this value to check if the 
solution is "acceptable."

### Termination Condition
The genetic algorithm will terminate when the
solution test passes (a chromosome with a 
value of 44 is found), or when the number
of iterations defined in global.py completes.

## Design
### External Libraries
random for simulating random probabilities
matplotlib.pyplot for plotting fitness graphs
statistics for calculating average fitness

### Project Structure
ga.py implements the genetic algorithm.
globals.py defines adjustable global variables
used for this algorithm:
POPULATION_SIZE: Size of population (20)
NUM_ITERATIONS: Number of iterations (30)
NUM_ITEMS: Number of items in problem (12, non-adjustable)
MUTATION_RATE: Probability of mutation (5)
ITEMS: Static array of tuples representing items (weight,value)

## What I learned
1. Genetic representations of problems
2. Genetic algorithm implementation
3. Pyplot

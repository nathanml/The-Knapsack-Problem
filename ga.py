import random
import matplotlib.pyplot as plt
import statistics as stats
import globals


# Return the weight of chromosome
def get_weight(chromosome):
    weight = 0
    for i in range(globals.NUM_ITEMS - 1):
        weight += globals.ITEMS[i][0] * chromosome[i]
    return weight


# Return the value of the chromosome
def get_value(chromosome):
    value = 0
    for i in range(globals.NUM_ITEMS - 1):
        value += globals.ITEMS[i][1] * chromosome[i]
    return value


# Calculate proximity to 250. Used by fitness function
def get_distance_from_250(chromosome):
    return abs(250 - get_weight(chromosome))


# Randomly creates population of chromosomes
# Iterates through size of the population,
# For each chromosome, append 12 random bits
def generate_initial_population():
    population = []
    for i in range(globals.POPULATION_SIZE):
        chromosome = []
        for j in range(globals.NUM_ITEMS):
            chromosome.append(random.randint(0, 1))
        population.append(chromosome)
    return population


# Returns fitness map of the population
# For each member of population, fitness
# is 0 if the weight exceeds 250, and the
# value of the chromosome if not
def fitness_function(population):
    fitness_map = []
    for i in range(globals.POPULATION_SIZE):
        fitness_map.append(get_value(population[i]) - (get_distance_from_250(population[i])))
    return fitness_map


# Algorithm implementation
def genetic_algorithm(population, fitness_fn):
    cycle = 0  # Tracks number of iterations
    # For plotting fitness graph
    x_coord = []
    max_coord = []
    avg_coord = []
    max_fitness = max(fitness_fn)  # Current best fitness

    while cycle <= globals.NUM_ITERATIONS and max_fitness < 44:
        # Cull 50% of population
        new_population = []
        parents = cull(population, fitness_fn)
        # Reproduce to generate other 50%
        num_parents = len(parents) - 1
        # Randomly select parents for each child
        for i in range(globals.POPULATION_SIZE):
            parent_1 = parents[random.randint(0, num_parents)]
            parent_2 = parents[random.randint(0, num_parents)]
            # Create child chromosome and add to population
            child = reproduce(parent_1, parent_2)
            # Randomly simulate mutation scenario
            if random.randint(0, 100) <= globals.MUTATION_RATE:
                mutate(child)
            new_population.append(child)
        # Reset values for next cycle
        population = new_population
        fitness_fn = fitness_function(population)
        max_fitness = max(fitness_fn)
        avg_fitness = stats.mean(fitness_fn)
        # Append coordinates
        x_coord.append(cycle)
        max_coord.append(max_fitness)
        avg_coord.append(avg_fitness)
        # Increment cycle
        cycle += 1

    # Plot X and Y coordinates
    # X represents cycle
    # Y represents the best fitness found that cycle
    plt.plot(x_coord, max_coord, 'b')
    plt.plot(x_coord, avg_coord, 'g')
    plt.xlabel("cycle")
    plt.ylabel("fitness")
    plt.show()
    # Return the best solution
    for i in range(globals.POPULATION_SIZE):
        if fitness_fn[i] == max_fitness:
            return population[i]


# Function for culling a population by 50%
# Returns list of the top 50% of chromosomes
def cull(population, fitness_fn):
    culled_population = []
    average_fitness = stats.mean(fitness_fn)
    for i in range(len(population)):
        if fitness_fn[i] >= average_fitness:
            culled_population.append(population[i])
    return culled_population


# Function for randomly mutating a gene in the
# child chromosome
def mutate(child):
    mutation = random.randint(0, globals.NUM_ITEMS - 1)
    if child[mutation] == 0:
        child[mutation] = 1
    else:
        child[mutation] = 0


# Function for simulating reproduction
# Implements single point crossover
def reproduce(parent_1, parent_2):
    x = random.randint(0, globals.NUM_ITEMS - 1)
    child = parent_1[0:x] + parent_2[x:]
    return child


print("RUNNING THE GENETIC ALGORITHM")
print("ITEMS : ", globals.ITEMS)
initial_population = generate_initial_population()
initial_fitness = fitness_function(initial_population)
solution = genetic_algorithm(initial_population, initial_fitness)
print("Solution found!")
print("Solution : ", solution)
print("Solution Weight : ", get_weight(solution))
print("Solution Value : ", get_value(solution))

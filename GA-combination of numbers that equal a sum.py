import random
import math
from copy import deepcopy as copy

'''Instructions:
   Each generation aims to have a set of numbers equal to a target sum
   ex. if the target sum is 9 and there are 3 numbers in each set, then [3,5,1] would be a solution
   Target is chosen randomly among all possible numbers the set can create
   
   commands:
   'gen(x,1)' will produce another generation of offpsring
   'gen(x,10)' would produce 10 etc.
   'display_dna(x)' displays all the offspring in the current generation
   'display_fit(x)' displays the fitness of the current generation
   'display_sum(x)' displays the sum of the current generation
   'history(n,m) displays the mth offspring from the nth generation
   
   the simulation ends automatically when the sum of a set equals the target sum'''
   
   
   
# initialize variables

genome_size=5
dna_range=100
pool_size=20
mutation_rate=5
mutation_count=0
current_generation=0
gen_history=[]
fitx=200

# select a target sum, but only if it is possible to create with dna range/genome size
target = random.randrange(0,dna_range*genome_size)

print("Target sum:",target)

#create a new generation where each offspring has a dna, sum, and fitness associated
class new_generation():
    def __init__(self):
        self.fitness=0
        self.dna=[]
        self.sum=0

        #creates a genome for each offspring, set by paramters above
        for i in range(genome_size):
            self.dna.append(random.randrange(0,dna_range))
            
        #calculates sum/fitness of offspring
        self.calc_sum()
        self.calc_fit()

    #calculates the sum of all dna in genome
    def calc_sum(self):
        self.sum=0
        for s in range(len(self.dna)):
            self.sum+=self.dna[s]

    #Calculates fitness of offspring (sums that are closer to the target are better)
    def calc_fit(self):
        self.fitness=0
        global target
        for i in range(len(self.dna)):
            difference=abs((self.sum)-target)
            if difference > 0:
                self.fitness=math.floor((1/difference)*fitx)
            #avoid dividing by 0
            elif difference == 0:
                self.fitness=math.floor((1/(difference+1))*fitx)*10
                global mutation_rate
                mutation_rate=0

            
#Creates the first pool of offpsring based on initial parameters      
def new_pool(pool):
    print("--Genome created--")
    for i in range(pool_size):
        pool.append(new_generation())

    #displays the results of the first generation
    display_result(pool)

    #collects a history of all generations that can be referenced whenever
    gen_history.append(pool)
    return pool

#Creates a new generation
def refresh_pool(pool):
    global pool_size
    global mutation_count
    global current_generation
    current_generation+=1
    mutation_count=0

    #avoids pointer T_T
    mating_pool=copy(pool)

    #Creates a mating pool
    for i in range(len(pool)):
        mating_pool.append(copy(pool[i]))
        for z in range(pool[i].fitness):
            
            mating_pool.append(copy(pool[i]))

    #Randomly selects all parents, equal to twice the pool size
    selection_pool=[]
    for i in range(pool_size*2):
        selection_pool.append(copy(mating_pool[random.randrange(len(mating_pool))]))

    #Creates a offspring pool equal to the pool size
    child_pool=copy(selection_pool[:pool_size])

    #Applies crossover , selecting randomly which parent to inherit each gene from
    for i in range(0,len(selection_pool),2):
        for z in range(genome_size):
            randomvalue=random.randrange(0,2)
            if randomvalue == 0:
                child_pool[int(i/2)].dna[z]=selection_pool[i].dna[z]
            else:
                child_pool[int(i/2)].dna[z]=selection_pool[i+1].dna[z]

    
    global mutation_rate
    
    avg_fitness=0
    for i in range(len(child_pool)):
        avg_fitness+=child_pool[i].fitness
        if avg_fitness != 0:
            avg_fitness=int(avg_fitness/len(child_pool))
        
    #Each gene in each offspring has a chance to mutate    
    for i in range(len(child_pool)):
        for z in range(genome_size):
            randomvalue=random.randrange(0,100)
            #if avg fitness is zero, mutation rate is increased
            if avg_fitness==0:
                if randomvalue < mutation_rate**3:
                    child_pool[i].dna[z]+=random.randrange(-dna_range,dna_range)
                    if child_pool[i].dna[z]>dna_range-1:
                        child_pool[i].dna[z]=dna_range-1
                    if child_pool[i].dna[z]<0:
                        child_pool[i].dna[z]=0
                    mutation_count+=1
            elif randomvalue < mutation_rate:
                child_pool[i].dna[z]+=random.randrange(-dna_range,dna_range)
                #child_pool[i].dna[z]=random.randrange(0,dna_range)
                if child_pool[i].dna[z]>dna_range-1:
                    child_pool[i].dna[z]=dna_range-1
                if child_pool[i].dna[z]<0:
                    child_pool[i].dna[z]=0
                mutation_count+=1
    #Assign a fitness score and sum to the new pool            
    for i in range(len(child_pool)):
        child_pool[i].calc_sum()
        child_pool[i].calc_fit()
        
    #Add the new pool to the generation history    
    gen_history.append(child_pool)

    #return pool with all the attributes of the created pool
    for w in range(len(child_pool)):
        pool[w].dna=copy(child_pool[w].dna)
        pool[w].calc_sum()
        pool[w].calc_fit()
        
    return pool
    
        
#Display the dna,sum, or fitness of a given offspring    
def display_dna(gen):
    for i in range(len(gen)):
        print("Group",i,"dna:",gen[i].dna)
def display_sum(gen):
    for i in range(len(gen)):
        print("Group",i,"sum:",gen[i].sum)
def display_fit(gen):
    for i in range(len(gen)):
        print("Group",i,"fitness:",gen[i].fitness)

#Display information about the generation and their target, also display if there is a match
def display_result(gen):
    avg_fitness=0
    avg_sum=0
    for i in range(len(gen)):
        global target
        global current_generation
        if gen[i].sum == target:
            print("WINNER:")
            print("Offspring",i,"dna:",gen[i].dna)
            print("fitness:",gen[i].fitness)
        avg_fitness+=gen[i].fitness
        avg_sum+=gen[i].sum
    if avg_fitness != 0:
        avg_fitness=int(avg_fitness/len(gen))
    if avg_sum != 0:
        avg_sum=int(avg_sum/len(gen))
    print("")
    print("Generation",current_generation)
    print("target:",target)
    print("total offspring",pool_size+(current_generation*pool_size))
    print("size of pool:",len(gen))
    print("average fitness:",avg_fitness)
    print("average sum:",avg_sum)
    print("mutations:",mutation_count)
    
#Creates x number of new generations, stops if there is a match, then displays results        
def gen(gen,repeat):
    exitloop=0
    global target
    for i in range(repeat):
        for z in range(len(gen)):
            if gen[z].sum == target:
                exitloop=1
                
        if exitloop==1:
            break
        else:
            gen=refresh_pool(gen)
    display_result(gen)
    
#Accesses the history of all created offspring
    
def history(generation_number,group_number):
    print(gen_history[generation_number][group_number].dna)
    
x=[]
x=new_pool(x)


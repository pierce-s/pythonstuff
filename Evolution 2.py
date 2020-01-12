import random
import math

gene_pool_size=16
number_of_genes=4
mutation_rate=20
gene_range=50
fitness_difficulty=50
target_met="no"


generation= 1

'''
force an even number since mating uses half of the genes from each parent
'''
if (number_of_genes % 2) != 0:
    number_of_genes+=1

'''
creates a target data set
'''
data=[]
for i in range(number_of_genes):
    data.append(random.randrange(1,gene_range))

print("Gene pool size:",gene_pool_size)
print("Number of genes:",number_of_genes)
print("Mutation rate:",mutation_rate)
print("Gene range:",gene_range)
print("Fitness difficulty:",fitness_difficulty)
print("---------------") 

    
class Group():
    def __init__(self):
        self.group=[]
        self.fitness=0
        for i in range(number_of_genes):
            self.group.append(random.randrange(1,gene_range))
        
def makegroup():
    group=Group()
    return group

def newgen():
    generations=[]
    '''
    Number of agents in gene pool
    '''
    for i in range(gene_pool_size):
        generations.append(makegroup())
    return generations



def fitness(gen):
    totalfitness=0
    for i in range(len(gen)):
        for w in range(number_of_genes):
            if abs(gen[i].group[w] - data[w]) < math.floor(gene_range/(fitness_difficulty)):
                gen[i].fitness+=1
            if abs(gen[i].group[w] - data[w]) < math.floor(gene_range/(fitness_difficulty*2)):
                gen[i].fitness+=1
            if abs(gen[i].group[w] - data[w]) < math.floor(gene_range/(fitness_difficulty)*4):
                gen[i].fitness+=1
            if abs(gen[i].group[w] - data[w]) == 0:
                gen[i].fitness+=10
        gen[i].fitness=math.floor(gen[i].fitness**2)
        totalfitness+=gen[i].fitness
        
        print("Group", i, "fitness =",gen[i].fitness)
        
    print("Total fitness =",totalfitness)
        

def makegenepool(gen):
    genepool=[]
    
    ''' each agent automatically gets a spot in the gene pool '''
    for i in range(len(gen)):
        genepool.append(gen[i])
        
        ''' add more offsprint per fitness'''
        for w in range(gen[i].fitness):
            genepool.append(gen[i])

    print("size:",len(genepool))

    '''
    print("---------------")        
    print("New gene pool:")
     
    for i in range(len(genepool)):
        print(genepool[i].group)
    print("size:",len(genepool))
    '''
    


    '''narrow gene pool'''
    narrowgenepool=[]

    for i in range(gene_pool_size*2):
        ''' pick a random group out of the gene pool'''
        randomval=random.randrange(len(genepool))
        narrowgenepool.append(genepool[randomval])

     
    print("---------------")
    print("Parent Selection:")  
    for i in range(len(narrowgenepool)):
        print(narrowgenepool[i].group)
    print("size:",len(narrowgenepool))
    



    newgenepool=newgen()
    
    newgenes=[]
    for i in range(0,len(narrowgenepool),2):
        
        for w in range(int(number_of_genes/2)):
            newgenes.append(narrowgenepool[i+0].group[w])
        for y in range(int(number_of_genes/2),number_of_genes):
            newgenes.append(narrowgenepool[i+1].group[y])
    for i in range(len(newgenepool)):
        newgenepool[i].group=[]
        for r in range(number_of_genes):
            newgenepool[i].group.append(newgenes[4*i + r])

    
    print("---------------")
    print("Children:")
    
    for i in range(len(newgenepool)):
        print(newgenepool[i].group)
    print("size:",len(newgenepool))
    


    '''mutation'''
    mutation=0
    for i in range(len(newgenepool)):
        for r in range(number_of_genes):
            chance=random.randrange(0,mutation_rate)
            if chance == 0:
                mutation+=1
                newgenepool[i].group[r]=random.randrange(0,gene_range)
               
    print("---------------")
    print("Post Mutation:")
     
    for i in range(len(newgenepool)):
        print("Group",i,newgenepool[i].group)
    print(mutation,"mutations")
    


    
    return newgenepool
        
    

    

print("Target data:",data)      
genepool=newgen()
print("---------------")
print("Generation:",generation)
for i in range(len(genepool)):
        print(genepool[i].group)
print("---------------")
print("Fitness of generation:")
fitness(genepool)

    
def nextgen(repeat):
    global target_met
    winner_is=0
    for i in range(repeat):
        global generation
        global genepool
        generation+=1
        print("---------------")
        print("Generation:",generation)
        genepool=makegenepool(genepool)
        
        print("---------------")
        print("Fitness of generation:")
        fitness(genepool)
        print("---------------")
        print("Target data:",data)
        for z in range(len(genepool)):
            if genepool[z].group==data:
                target_met="yes"
                winner_is=z
                winning_hand=genepool[z].group
        print("Winner?",target_met)
        for z in range(len(genepool)):
            if genepool[z].group==data:
                print("Winner is",winner_is,"at generation",generation)
                print("Winning numbers are",winning_hand)

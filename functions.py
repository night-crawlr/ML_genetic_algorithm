import random
from client import *


class individual():
    def __init__(self):
        self.vector = []
        self.error = []
        self.fitness = -1
        self.gen = 0


# def mutate(vector):
#     mutatedVector = []
#     for i in range(11):
#         mutatedVector.append(vector[i])
#     indexToBeMutated = random.randint(0, 10)
#     factor = random.uniform(0.6, 1.4)
#     newCoeff = factor * vector[indexToBeMutated]
#     if(newCoeff >= 10 or newCoeff <= -10):
#         newCoeff = vector[indexToBeMutated]
#     r = random.randint(1,100):
#     mutatedVector[indexToBeMutated] = newCoeff
#     return mutatedVector

def generateInitialPopulation(overfit):
    pop = []
    for i in range(6):
        p = individual()
        p.vector = copy(overfit)
        p.vector = mutate(overfit)
        for j in range(len(p.vector)):
            if(p.vector[j] == overfit[j]):
                p.vector[j] = 0
        pop.append(p)
    return pop


def mutate(vector):
    mutatedVector = []
    for i in range(11):
        p = 1
        if(i >= 0):
            r = random.randint(1, 100)
            if(r <= 20):
                p = random.uniform(0.3, 1.5)
        mutatedVector.append(p*vector[i])

    return mutatedVector


def Fitness(vectorobj, data):

    vector = vectorobj.vector
    for obj in data:
        if(obj.vector == vector):
            vectorobj.fitness = obj.fitness
            vectorobj.error = obj.error
            return obj.fitness, obj.error

    temp = get_errors(secretKey, vector)
    vectorobj.error = temp
    #vectorobj.fitness = (0.2*temp[0])+(0.3*temp[1])
    #vectorobj.fitness = (0.3*temp[1])/(0.2*temp[0])
    #fitness1 = (0.9*temp[0])+(1*temp[1])
    ##fitness1 = temp[0]
    #fitness2 = temp[1]/temp[0]
    #fitness3 = temp[0]/temp[1]
    #fitness = ((1.5)*(fitness1)) + ((1.1)*(fitness2)) + (0.9 * fitness3)
    #fitness = temp[1] + temp[0] + (0.8 * (temp[1] - temp[0]))
    fitness = 2*(abs(temp[1] - temp[0])) + temp[1] + 2*temp[0]
    #fitness = 2*temp[1] - temp[0]
    vectorobj.fitness = fitness
    data.append(vectorobj)
    return vectorobj.fitness, temp


def selectTop14From(intialpop, data):
    fitnessarray = []
    ans = []
    for i in range(len(intialpop)):
        vectorobj = intialpop[i]
        value, error = Fitness(vectorobj, data)
        fitnessarray.append([value, vectorobj.vector, error])
    fitnessarray = sorted(fitnessarray, key=lambda x: x[0])

    temp = 10
    if(len(fitnessarray) < temp):
        temp = len(fitnessarray)

    for i in range(temp):
        obj = individual()
        obj.vector = fitnessarray[i][1]
        obj.error = fitnessarray[i][2]
        obj.fitness = fitnessarray[i][0]
        # obj = {"vector": fitnessarray[i][1],
        #       "fitness": fitnessarray[i][0], "error": fitnessarray[i][2]}
        ans.append(obj)
    return ans


def copy(source):
    des = []
    for i in range(len(source)):
        des.append(source[i])
    return des


# def generateInitialPopulation(overfit):
#     overfitobj = individual()
#     overfitobj.vector = copy(overfit)
#     initPopulation = [overfitobj]
#     for i in range(9):
#         vecobj = individual()
#         vec = []
#         vec = copy(overfit)
#         vec = mutate(vec)
#         vecobj.vector = copy(vec)
#         initPopulation.append(vecobj)
#     return initPopulation


def removeDup(a):
    distinct = [a[0]]
    for i in range(1, len(a)):
        for j in range(len(distinct)):
            if(a[i].vector == distinct[j].vector):
                break
            distinct.append(a[i])
    return distinct


def evolve(selectionGen, breedingGen, mutationGen, data, gen):
    print(len(selectionGen))
    top3 = []
    childPop = []
    mini = 3
    if(len(selectionGen) < mini):
        mini = len(selectionGen)
    for i in range(mini):
        top3Obj = individual()
        top3Obj.vector = copy(selectionGen[i].vector)
        top3Obj.error = copy(selectionGen[i].error)
        top3Obj.fitness = selectionGen[i].fitness
        top3.append(top3Obj)
    noOfChilds = 3
    for i in range(noOfChilds):
        child1, child2 = breed(random.choice(
            top3), random.choice(top3), gen, data)
        childPop.append(child1)
        childPop.append(child2)
    print("child pop : before")
    print(len(childPop))
    childPop = removeDup(childPop)
    print("_()_")
    print(len(childPop))
    breedingGen = selectionGen + childPop
    print("bree pop : before")
    print(len(breedingGen))
    breedingGen = removeDup(breedingGen)
    for i in range(len(childPop)):
        childPop[i].vector = mutate(childPop[i].vector)
    print("mut pop : before")
    print(len(mutationGen))
    mutationGen = selectionGen + childPop
    mutationGen = removeDup(mutationGen)
    print(len(mutationGen))

    for i in range(len(mutationGen)):
        mutationGen[i].fitness, mutationGen[i].error = Fitness(
            mutationGen[i], data)

    return breedingGen, mutationGen


def breed(p1, p2, gen, data):
    childVec1 = copy(p1.vector)
    childVec2 = copy(p2.vector)

    childVec1[4] = p2.vector[4]
    childVec1[6] = p2.vector[6]
    childVec1[9] = p2.vector[9]
    childVec1[10] = p2.vector[10]

    childVec2[4] = p1.vector[4]
    childVec2[6] = p1.vector[6]
    childVec2[9] = p1.vector[9]
    childVec2[10] = p1.vector[10]

    c1obj = individual()
    c1obj.vector = childVec1

    c2obj = individual()
    c2obj.vector = childVec2

    f1, e1 = Fitness(c1obj, data)
    f2, e2 = Fitness(c2obj, data)

    c1obj.error = e1
    c1obj.fitness = f1
    c1obj.gen = gen

    c2obj.error = e2
    c2obj.fitness = f2
    c2obj.gen = gen
    return c1obj, c2obj

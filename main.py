from functions import *
# secretKey = "hKaLQ5AytqTJ4hShhK945QnqCTYxsPS6oGLu6RvQlN516HYN1L"
# overfit = [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -
#            1.83669770e-15, 8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]

initalPopulation = 10

underWentFitnessFunction = []
allGens = []


# class individual():
#     def __init__(https://github.com/night-crawlr/Genetic-Algorithms-overfit.gitfitness = -1


def top10(allGens):
    lastMutationGen = allGens[len(allGens) - 1]["mutationGen"]
    Top10 = sorted(lastMutationGen, key=lambda x: x.fitness)[:10]

    for i, v in enumerate(Top10):
        print(str(i+1) + ")")
        print(v.vector)
        print(v.error)
        print(v.fitness)
        print(v.gen)
        print("___________________________________________________")


def GA(underWentFitnessFunction, initialGen):
    generation = 0
    while(generation != 25):
        Gen = {
            "gen": generation+1,
            "selectionGen": [],
            "breedingGen": [],
            "mutationGen": [],
        }
        selectionGen = []
        breedingGen = []
        mutationGen = []
        selectionGen = selectTop14From(initialGen, underWentFitnessFunction)
        breedingGen, mutationGen = evolve(
            selectionGen, breedingGen, mutationGen, underWentFitnessFunction, generation+1)
        initialGen = mutationGen
        print("ALGO : 1  Generation : {}".format(generation+1))
        print("selectionGen :")
        for i in range(len(selectionGen)):
            print(selectionGen[i].vector)
            print(selectionGen[i].error)
            print(selectionGen[i].fitness)
            print(selectionGen[i].gen)
        print()
        print("breedingGen :")
        for i in range(len(breedingGen)):
            print(breedingGen[i].vector)
            print(breedingGen[i].error)
            print(breedingGen[i].fitness)
            print(breedingGen[i].gen)
        print()
        print("mutationGen :")
        for i in range(len(mutationGen)):
            print(mutationGen[i].vector)
            print(mutationGen[i].error)
            print(mutationGen[i].fitness)
            print(mutationGen[i].gen)
        print("______________________ ALGO : 1 generation {} completed _____________".format(
            generation+1))

        Gen["selectionGen"] = selectionGen
        Gen["breedingGen"] = breedingGen
        Gen["mutationGen"] = mutationGen
        allGens.append(Gen)
        generation += 1

    print("TOP 10 VECTORS")
    top10(allGens)


def create(vec):
    obj = individual()
    obj.vector = vec
    return obj


if(__name__ == "__main__"):
    initialGen = generateInitialPopulation(overfit)
    initialGen.append(create([0.0, 0.0, -2.598289733427603e-13, 0.0, -1.3047410946647114e-10,
                              0, 0, 0.0, -1.3078450530038356e-06, 0.0, 5.154401698834563e-10]))
    # initialGen.append(create(
    #    [0, -2.028359124057568e-12, 0, 0, 0, 0, 0, 7.322023749572365e-06, 0, 0, 0]))
    # initialGen.append(create([0.0, 0.0, 0.0, 2.0171482324414613e-11,
    #                          0.0, -1.8094666440723205e-15, 0.0, 0, 0.0, 0.0, 0.0]))
    # note these are the best
    # rank 51 best1 = create([0, -1.6060686419478017e-12, 0, 0, -2.2011224167503534e-10, -
    #                 1.9377462140934863e-15, 7.985595649901078e-16, 0, 0, 0.0, 0])
    # rank 51 best2 = create(
    #     [0.0, 0.0, 0, 0, 0.0, -2.288930511995357e-15, 0, 0.0, 0, 0.0, 0.0])
    # rank 51  best3.create([0.0, 0.0, 0.0, 0, -4.633140629974375e-10, -2.333682546699699e-15, 1.0935307190161998e-15, 0.0, 0, 0.0, 0.0])
    # initialGen.append(best1)
    # initialGen.append(best2)


# best while using 2*abs + train + test
# rank 29 [0.0, 0.0, -2.598289733427603e-13, 0.0, -1.3047410946647114e-10, 0, 0, 0.0, -1.3078450530038356e-06, 0.0, 5.154401698834563e-10]

# rank 50 [0.0, 0.0, 0.0, 0.0, -1.43379810127795e-10, -2.425734359584129e-15, 0.0, 0.0, 0.0, 0.0, 0.0]
# error  : [2228934692494.518, 2203644197591.585]

# rank 36 vec = [0, -2.028359124057568e-12, 0, 0, 0, 0, 0, 7.322023749572365e-06, 0, 0, 0]
# error [6229785467724.318, 14298348362405.34]

    list = [i.vector for i in initialGen]
    # print(list)
    GA(underWentFitnessFunction, initialGen)

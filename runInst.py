from main import timeTablingInstance

instances= [
    # "toy.ctt",    
    # "comp01.ctt",
    # "comp02.ctt",
     "comp03.ctt",
    # "comp04.ctt",
    # "comp05.ctt",
    # "comp06.ctt",
    # "comp07.ctt",
    # "comp08.ctt",
    # "comp09.ctt",
    # "comp10.ctt",
    # "comp11.ctt",
    # "comp12.ctt",
    # "comp13.ctt",
    # "comp14.ctt",
    # "comp15.ctt",
    # "comp16.ctt",
    # "comp17.ctt",
    # "comp18.ctt",
    # "comp19.ctt",'
    # "comp20.ctt",
    # "comp21.ctt"
]

print("Running instances:\n")
for instance in instances:
    f = open("results/" + instance, "w")
    print("Instance:", instance + "...")
    for j in range(1):
        path = "data/" + instance
        cost = timeTablingInstance(200, 0.1, path, 228, j)
        f.write(str(cost) + " ")
    f.close()


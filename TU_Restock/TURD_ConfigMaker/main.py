#Hey dear user! Check out this repository:
#https://github.com/likeproblem/TURD_ConfigMaker
#But shortly, config has VARIABLE;PROMPT;DEFAULT_VALUE structure, variable name(without $$), prompt which asks, and default value if user inputs nothing
#Also autodefault has values which will, well, default automatically without prompt, useful for variables you dont use often, like MOD
#After you answer all prompts, it will ask for init or add or meshify(about that later). IF YOU DIDN'T CREATE FILES MANUALLY OR WITH INIT USE INIT FIRST. Then you can add parts with ease using add.
#Also it will ask "meshes", you just first answer mesh YOU WANT TO COLOR, if multiple use ; same with exclude mesh, obtainable from ModelData as usual
#After you answer the exclude meshes, you may want to use meshify option when you restart, it will do same stuff but allows you to add material to mesh
paths_path = "paths.txt"
with open(paths_path, "r") as file:
    paths = file.read().split("\n")

config_path = paths[0]
autodefault_path = paths[1]
TextureSets_path = paths[2]
Default_path = paths[3]
DefaultMulti_path = paths[4]
Recolour_path = paths[5]
RecolourMulti_path = paths[6]

TextureSets_name = paths[7]
Default_name = paths[8]
Recolour_name = paths[9]



import copy

def variableReplacer(string, variable, value): #simple variable replacer
    doc = copy.copy(string)
    doc = doc.replace(variable, value)
    return doc

def allReplacer(string): #replace everything with known variables
    doc = copy.copy(string)
    for i in variables.keys():
        doc = variableReplacer(doc, i, variables[i])
    return doc

with open(config_path, "r") as file: #boring file openers
    config = file.read()
with open(autodefault_path, "r") as file:
    autodefault = file.read()
    
with open(TextureSets_path, "r") as file:
    TextureSets = file.read()

with open(Default_path, "r") as file:
    Default = file.read()
with open(DefaultMulti_path, "r") as file:
    DefaultMulti = file.read()

with open(Recolour_path, "r") as file:
    Recolour = file.read()
with open(RecolourMulti_path, "r") as file:
    RecolourMulti = file.read()

variableDict = dict()             #get data from config
for line in config.split("\n"):
    data = line.split(";")
    variableDict[data[0]] = [data[1], data[2]]

variables = dict()                #ask user, check default, check autodefault, check data for variables
for i in variableDict.keys():
    if not i in autodefault.split("\n"):
        data = input(variableDict[i][0] + ": ")
    else:
        data = ""
    if data != "":
        variables[f"${i}$"] = allReplacer(data)
    else:
        variables[f"${i}$"] = allReplacer(variableDict[i][1])



#fun stuff begins here :D



whar_i_do = input("Initiate files or add new part?(init/add/meshify): ")
if whar_i_do == "init":                                 #create files
    with open(allReplacer(TextureSets_name), "w") as file:
        file.write("//CREATED USING TURD_ConfigMaker\n" + allReplacer(TextureSets))
    with open(allReplacer(Default_name), "w") as file:
        file.write("//CREATED USING TURD_ConfigMaker\n")
    with open(allReplacer(Recolour_name), "w") as file:
        file.write("//CREATED USING TURD_ConfigMaker\n")
elif whar_i_do == "add" or whar_i_do == "meshify":       #edit files
    with open(allReplacer(Default_name), "a") as file:
        if whar_i_do == "add":
            file.write(allReplacer(Default) + "\n")
        finalMesh = ""
        if DefaultMulti.find("$mesh$") != -1:
            mesh = input("Meshes? Include: ").split(";")
            excludeMesh = input("Meshes? Exclude: ").split(";")
            if mesh != [""]:
                for i in mesh:
                    finalMesh += f"mesh = {i}\n"
            if excludeMesh != [""]:
                for i in excludeMesh:
                    finalMesh += f"excludeMesh = {i}\n"
        file.write(allReplacer(DefaultMulti).replace("$mesh$", finalMesh) + "\n")
    
    with open(allReplacer(Recolour_name), "a") as file:
        if whar_i_do == "add":
            file.write(allReplacer(Recolour) + "\n")
        file.write(allReplacer(RecolourMulti).replace("$mesh$", finalMesh) + "\n")
        
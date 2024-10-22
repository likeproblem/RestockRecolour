import io

paths_path = "paths.txt"
with open(paths_path, "r") as file:
    paths = file.read().split("\n")

Default_path = paths[0]
Wiki_path = paths[1]

with open(Default_path, "r") as file:
    Default = file.read()
with io.open(Wiki_path, mode="r", encoding="utf-8") as file:
    Wiki = file.read()

with open("output.txt", "w") as file:
    lines = Default.split("\n")
    out_lines = []
    for i in lines:
        if(i.find("@PART") != -1):
            out_lines.append(i)
    for i in range(len(out_lines)):
        out_lines[i] = out_lines[i][out_lines[i].find("[")+1:out_lines[i].find("]", out_lines[i].find("["))]
    i=0
    while i < len(out_lines):
        if(out_lines[i].find(",")):
            temp = out_lines[i].split(",")
            del out_lines[i]
            out_lines[i:i] = temp
        i+=1
    
    more_lines = []
    for i in out_lines:
        if(Wiki.find("["+i+"]") == -1):
            more_lines.append(i)

    end_lines = []
    for i in Wiki.split("\n"):
        for j in out_lines:
            if(i.find("["+j+"]") != -1 and i.find(u"\u2714") == -1):
                end_lines.append(j)
    
    file.write("PARTS FOUND: \n\n" + "\n".join(out_lines) + "\n\n\n" + "PARTS NOT FOUND IN WIKI: \n\n" + "\n".join(more_lines) + "\n\n\n" + "PARTS NOT CHECKED OFF IN WIKI: \n\n" + "\n".join(end_lines))
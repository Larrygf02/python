def save_scores(name_file, scores):
    file = open(name_file,"w")
    for name, score, time in scores:
        file.write(name+ ","+str(score)+","+time+"\n")
    file.close()

def get_scores(name_file):
    scores = []
    file = open(name_file,"r")
    for line in file:
        name, score, time = line.rstrip("\n").split(",")
        scores.append((name,int(score), time))
    file.close()
    return scores


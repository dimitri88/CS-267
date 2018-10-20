import numpy as np
def letterToNumber(cnfs):
    index = 1
    dict = {}
    for clause in cnfs:
        for i in range(len(clause)):
            var = clause[i]
            if var not in dict:
                if len(var) == 1:
                    dict[var] = index
                    dict['-' + var] = -1*index
                    index +=1
                else:
                    dict[var] = -1 * index
                    dict[var[-1]] = index
                    index += 1
            clause[i] = dict[var]
    return cnfs


def drwaSample(dist) :
    assignments = {}
    coin = [True,False]
    for key in dist:
        res = np.random.choice(coin, 1, p=[dist[key], 1-dist[key]]);
        #print(res)
        assignments[key] = res[0]
        assignments['-' + key] = not res[0]
    return assignments

def sub_eval(dist, cnf):
    sample = drwaSample(dist)
    true_count = 0
    for clause in cnf:
        for variable in clause:
            if sample[str(variable)]:
                true_count += 1
                break
    return true_count == len(cnf)

def main():
    var = [['a','b','-c'], ['b', 'c','d', '-e'], ['-b','-d','e'], ['-a','-b']]
    p_dist = { '1': 0.3, '2':0.6, '3':0.1, '4':0.8, '5':0.4}
    # p_dist = { '1': 0.3}
    # var = [['a'], ['a']]
    cnf = letterToNumber(var)
    for i in range(3):
        count = 0
        for i in range(1000):
            if sub_eval(p_dist, cnf) :
                count += 1
        print (float(count / 1000.0))
    
if __name__ == "__main__": 
    main()
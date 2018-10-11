from copy import copy, deepcopy

def sat_solver(cnfs):
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
    print(sat_helper(cnfs,1, index, []))

def sat_helper(cnfs, i, length, path) :
    if len(cnfs) == 0 :
        print(path)
        return True
    if i > length :
        return False
    
    false_list = deepcopy(cnfs)
    true_list = deepcopy(cnfs)
    
    index = 0
    for clause in list(false_list):
        if i in clause:
            clause.remove(i)
        if -1 * i in clause:
            del false_list[index]
        else:
            index += 1

    index = 0
    for clause in list(true_list):
        if -1 * 1 in clause:
            clause.remove(i*-1)
        if i in clause:
            del true_list[index]
        else:
            index += 1

    f_path = list(path)
    f_path.append(False)
    t_path = list(path)
    t_path.append(True)
    return sat_helper(false_list, i+1, length,f_path) or sat_helper(true_list, i+1, length,t_path)

var = [['x','y','z'],['x','y','-z'],['x','-y','-z'],['x','-y','z'],['-x','y','z'],['-x','y','-z'],['-x','-y','z'],['-x','-y','-z']]
sat_solver(var)

            


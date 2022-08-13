import copy
import json
import os

import threading



data = None

# Opening JSON file
file_path = os.path.abspath(os.getcwd())
filename = './zs2-to-xml-to-json/scripts/json_tranformation/test.json'

# f = open(file_path + '\\edited\\dummo\\test.json')
#file_path + '\\test.json'
with open(filename) as f:
    # returns JSON object as a dictionary
    data = json.load(f)




output = {}
temp_output = output


def get_json_paths():
    with open('./zs2-to-xml-to-json/scripts/json_tranformation/json_paths_minimal.txt', "r") as f:
        return  [line.strip() for line in f.readlines()]



def get_list_of_all_numbered_elems(element_name, json_data):
    name = element_name.split('[]')[0]
    list_of_keys = list(json_data)

    return [x for x in list_of_keys if name in x]


def get_value_from_data(key, d, full_pre=[]):
    check = True
    oo = copy.deepcopy(d)
    for i in key:
        if '[]' in i:
            list_of_keys = get_list_of_all_numbered_elems(i, oo)
            previous_keys = full_pre + key[:key.index(i)]

            for k in list_of_keys:
                new_keys = [k] + key[key.index(i)+1:]
                get_job_done(new_keys, oo, previous_keys)
            check = False

            break

        else:
            # print(key, i)
            
            if not oo.get(i):
                check = False
                break
            else:
                oo = oo.get(i)
    
    if check:
        return oo.get('@value')








def goto_path(keys, val):
    """
    goto that path and place its value
    """
    global temp_output, output
    temp_output = output
    for i in keys[:-1]:
        if i not in temp_output:
            temp_output[i] = {}
        temp_output = temp_output[i]    
    temp_output[keys[-1]] = val






def get_job_done(keys_list, data, pre_keys=[]):
    value = get_value_from_data(keys_list, data, pre_keys)
    if value:
        goto_path(pre_keys + keys_list, value)




def extract_from_json(path_rules):
    for path in path_rules:
        print(path)
        keys = path.split('.')[:-1]  # -1 for ignoring @value from keys
        get_job_done(keys, data)



rules = get_json_paths()
all_rules = []
all_threads = []


for i in range(0, len(rules), 12):
    all_rules.append(rules[i:i+12])



for ruleses in all_rules:
    # print(ruleses)
    # input()
    t = threading.Thread(target=extract_from_json, args=(ruleses,))
    t.start()
    all_threads.append(t)


[x.join() for x in all_threads]

with open('modified_json_1.json', 'w') as f:
    f.write(json.dumps(output))
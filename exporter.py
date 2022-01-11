import numpy as np
import pandas as pd
def export_sorted_to_csv(tuple_data,name):
    size = len(tuple_data)
    # print(size)
    index = np.zeros(size)
    metric =np.zeros(size)
    labels = ['']*size
    
    for ind, tuple in enumerate(tuple_data):
        # print("size: "+str(len(tuple)))
        index[ind] = tuple[0]
        metric[ind] = tuple[1]
        labels[ind] = tuple[2]
        pass
    
    
    df = {}
    df['index'] = index
    df['metric'] = metric
    df['labels'] = labels
    df = pd.DataFrame(df)
    df.to_csv('output/temp_data/sorted_'+name+'.csv', index=False)


def export_corres_checker(tuple_data, name):
    size = len(tuple_data[0])
    #print(size)
    mob_list = ['']*size    
    lab_list = ['']*size    
    
    for index in range(size):
       mob_list[index] = tuple_data[0][index] 
       lab_list[index] = tuple_data[1][index]
       
    df = {}
    df['mob_list'] = mob_list
    df['lab_list'] = lab_list 
    df = pd.DataFrame(df)
    df.to_csv('output/temp_data/correspendecy_'+name+'.csv', index=False)
    

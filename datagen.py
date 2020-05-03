import random as rd
import pandas as pd
import numpy as np


# function creates data for FCFS, SJF, RR and Priority Scheduling (done)
def filegen(num,max_burst,min_burst,avg_int_time,filename):
    df = pd.DataFrame(np.zeros([num,4],dtype=int),columns=['process_number','arrival_time','cpu_burst_time','priority'])  # columns= process number, arrival time, CPU burst, priority
    last_time=avg_int_time
    for i in range(num):
        this_time = rd.randint(last_time+1,last_time+avg_int_time)
        li = [i,this_time,rd.randint(min_burst,max_burst),rd.randint(0,10)]
        df.iloc[i] = li
        last_time=this_time
    df.to_csv(r"./CPU-Scheduler-Python/Random_data/"+filename + ".csv",index=False)


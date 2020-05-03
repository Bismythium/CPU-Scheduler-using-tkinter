import pandas as pd
import numpy as np
def fcfs(filename):
    df = pd.read_csv(filename,index_col=False)
    output = pd.DataFrame(np.zeros([df.shape[0], 7], dtype=int), columns=['process_number', 'arrival_time',
                                                                          'cpu_burst_time','priority','completion_time',
                                                                          'waiting_time','turnaround_time'])
    oi = output.iloc #nickname
    oi[:,0:4]=df
    #completion time
    oi[0,4]=oi[0,2] + oi[0,1]
    for i in range(1,output.shape[0]):
        oi[i,4] = oi[i-1,4] + oi[i,2]
    #waiting time
    oi[0,5]=oi[0,1]
    for i in range(1,output.shape[0]):
        x = oi[i-1,4] - oi[i,1]
        if(x>0):
            oi[i,5] = x
        else:
            oi[i,5] = 0
    #turnaround time
    for i in range(0,output.shape[0]):
        oi[i,6] = oi[i,2]+oi[i,5]

    return output

class Process:
    def __init__(self,pid,arrival_time,burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.prev_arrival_time = arrival_time
    def calculation(self,pid,arrival_time,burst_time):
        self.completion_time
        self.wait_time
        self.turnaround_time
    def update_burst(self,pid,time_used,time_now):
        self.burst_time = self.burst_time - time_used
        self.prev_arrival_time =time_now
    def returner(self,pid,time_count):
        df = pd.DataFrame([self.pid,self.prev_arrival_time,self.burst_time,time_count])
        return df

class Waiting:
    def __init__(self):
        self.process = []
    def update(self,process):
        self.process.append(process)
        self.process.sort(key=lambda x: x.burst_time)
    def smallest(self):
        return self.process[0]
    def remove(self,process):
        self.process.remove(process)

def sjf(filename):
    waiting = Waiting()
    i=0
    df = pd.read_csv(filename, index_col=False)
    intermediate = pd.DataFrame(columns=['process_number','arrival_time_now','burst_time_left','time_now'])
    output = pd.DataFrame(np.zeros([df.shape[0], 7], dtype=int),
                          columns=['process_number', 'arrival_time',
                                   'cpu_burst_time', 'priority', 'completion_time',
                                   'waiting_time', 'turnaround_time'])
    oi = output.iloc # nickname
    oi[:, 0:4] = df
    p0=Process(oi[0,0],oi[0,1],oi[0,2])
    time_count = oi[0,1]
    currentP=p0
    intermediate.append(currentP.returner(currentP.pid,time_count))
    waiting.update()
    while(i<df.shape[0]):
        nextP = Process(oi[i,0],oi[i,1],oi[i,2])
        if(time_count==nextP.arrival_time):
            if(nextP.burst_time<waiting.smallest().burst_time):
                currentP.update_burst(currentP.pid, time_count - currentP.prev_arrival_time, time_count)
                intermediate.append(currentP.returner(currentP.pid,time_count))
                waiting





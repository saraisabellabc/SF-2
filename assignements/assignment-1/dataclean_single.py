#Sara Isabella Barajas-Cruz 
import pandas as pd #necessary modules
import numpy as np

#function to detect start and stop times. dont forget end: sign1 != sign2 and v1 grandeur differente v2
def detect_fall(velocity, time):
    time = time.to_numpy()
    
    #identify start as when there is first a stable hold (quoi faire si il ny a pas de stable hold?)
    for start in range(len(velocity) - 1):
        if abs(velocity[start] - velocity[start + 1]) < 0.05:
            break
    #prof demande d'enlever 0.5 a 1s du debut
    start_time = time[start] - 0.5
    start = max(0, np.searchsorted(time, start_time)) 
    
    #slowly slide cursor up the time axis until you reach a point where the neighbouring point has an opposite sign and a different velocity (shows end of drop)
    for cursor_end in range(start + 1, len(velocity) - 1):
        if abs(velocity[cursor_end] - velocity[cursor_end + 1]) > 0.5 and np.sign(velocity[cursor_end]) != np.sign(velocity[cursor_end + 1]):
            cursor_end += 1
            break
    end = cursor_end

    return start, end

#load file in
nom_file = "single_filters.csv"
df = pd.read_csv(nom_file)

#to do for each file [1-10]
for i in range(1, 11):
    #formatting of column (c) headers
    ctime = f"Time (s) Run #{i}"
    cpos = f"Position (m) Run #{i}"
    cvel = f"Velocity (m/s) Run #{i}"
    acc_col = f"Acceleration (m/s²) Run #{i}"
    #processus of creating new files. stackoverflow page on phone for all this remember!! confused how ask for help after class teacher       
    start, end = detect_fall(df[cvel], df[ctime])       
    sliced_data = df.iloc[start:end][[ctime, cpos, cvel, acc_col]]
    filtered_multiple_file = f"filtered_single_file{i}.csv" #process of creating csv (pandas 2 end)
    sliced_data.to_csv(filtered_multiple_file, index=False)
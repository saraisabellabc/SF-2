# one of the streams may split into a left fork and a right fork, increasing the total number of streams by 1, or two streams may rejoin, reducing the total number of streams by 1
# There is always at least one stream and there are never more than 100 streams.
#The first line of input contains n, the initial number of streams at some high altitude

streams = int(input())
n_streams = list(range(1, streams + 1))
print(n_streams)

flow_streams = []

#Split location
def percentage_flow(n):
    split_percentage = int(input())
    if split_percentage < 0 or split_percentage > 100:
        print("Invalid percentage")
    else:
        snew_flow = int(flow_streams[n] - ((split_percentage / 100 ) * flow_streams[n] ))

        flow_streams[n] = int((split_percentage /100 ) * flow_streams[n])
        flow_streams.insert(n + 1, snew_flow)

# Join location
def join_loc(n):
    jnew_flow = int(flow_streams[n] + flow_streams[n+1])
    flow_streams[n] = jnew_flow
    flow_streams.remove(flow_streams[n+1])


#The next n lines give the flow in each of the streams from left-to-right. Proceeding down the mountainside, several split or rejoin locations are encountered.
for i in range(len(n_streams)):
    flow = int(input())
    flow_streams.append(flow)


split_or_join = 0
while split_or_join != 77:
    split_or_join = int(input())

    if split_or_join == 99:
        n_split = int(input())
        percentage_flow(n_split - 1)
        #split_loc()
    
    if split_or_join == 88:
        n_split = int(input()) 
        join_loc(n_split - 1)
        
for flows in flow_streams:
    print(flows)
    



    

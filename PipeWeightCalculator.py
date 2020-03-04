def pipe_calculator():
    from NumberInput import input_positive_integer, input_positive_float
    
    # Tuple=(Pipe Schedule, Diameter [in]) : (Weight/Length [lb/ft])
    gsPipeDims={(40,1):1.68, (40, 1.25):2.27, (40,2):3.66, (80,1):2.17, (80, 1.25): 3.0, (80, 2):5.03} #dictionary of pertinent, commonly used galvanized steel pipe dimensions
    pipeWeight=[]
    
    noPipes=input_positive_integer("Enter the number of pipes: ")
    print('Now, work down the pipe pieces one at a time...')

    for pipe in range(noPipes):
        pipeSchedule=input_positive_integer("Enter the pipe\'s schedule: ")
        pipeDiameter=input_positive_float("Enter that same pipe\'s diameter: ")
        pipeLength=input_positive_float("Enter that same pipe\'s length: ")
        weightUnit=float(gsPipeDims[pipeSchedule, pipeDiameter])
        pipeWeight.append(pipeLength*weightUnit)
    print("Individual Pipe Weights: {}".format(pipeWeight))
    totalWeight=sum(pipeWeight) 
    print("The total weight of all the pipe is: {} lbs".format(totalWeight))  
    return totalWeight

pipe_calculator()
   
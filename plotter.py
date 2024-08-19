import numpy as np
import matplotlib.pyplot as plt


def get_changing_variable_warehouse(warehouseArray):
    w1 = warehouseArray[0]
    w2 = warehouseArray[1]
    res = []

    #warehouse
    if w1.starting_point != w2.starting_point:
        for w in warehouseArray:
            res.append(w.starting_point)
        
        return "Starting Point", res
    
    elif w1.dropoff_location != w2.dropoff_location:
        for w in warehouseArray:
            res.append(w.dropoff_location)
        return "Dropoff Location", res
    
    
    elif w1.columns != w2.columns:
        for w in warehouseArray:
            res.append(w.columns)
        return "Warehouse Length", res
    
    elif w1.rows != w2.rows:
        for w in warehouseArray:
            res.append(w.rows)
        return "Warehouse Width", res
    
    elif w1.config_parser.getint('warehouse', 'TotalCrossAisles') != w2.config_parser.getint('warehouse', 'TotalCrossAisles'):
        for w in warehouseArray:
            res.append(w.config_parser.getint('warehouse', 'TotalCrossAisles'))
        return "TotalCrossAisles", res

    #racks
    elif w1.config_parser.getint('racks', 'MaxRacks') != w2.config_parser.getint('racks', 'MaxRacks'):
        for w in warehouseArray:
            res.append(w.config_parser.getint('racks', 'MaxRacks'))
        return "Maximum Racks", res
    
    elif w1.config_parser.getint('racks', 'MaxSKUPerRack') != w2.config_parser.getint('racks', 'MaxSKUPerRack'):
        for w in warehouseArray:
            res.append(w.config_parser.getint('racks', 'MaxSKUPerRack'))
        return "Max SKU per Rack", res
    
    elif w1.config_parser.get('racks', 'RacksOrientation') != w2.config_parser.get('racks', 'RacksOrientation'):
        for w in warehouseArray:
            res.append(w.config_parser.get('racks', 'RacksOrientation'))
        return "Racks Orientation", res
    
    elif w1.config_parser.getint('racks', 'PutTwoRacksTogether') != w2.config_parser.getint('racks', 'PutTwoRacksTogether'):
        for w in warehouseArray:
            res.append(w.config_parser.getint('racks', 'PutTwoRacksTogether'))
        return "# of Racks Together", res
    
    elif w1.config_parser.getint('racks', 'WalkableAisleBetweenRacks') != w2.config_parser.getint('racks', 'WalkableAisleBetweenRacks'):
        for w in warehouseArray:
            res.append(w.config_parser.getint('racks', 'WalkableAisleBetweenRacks'))
        return "Walkable Space Between Racks", res
    
    #SKU
    elif w1.config_parser.getint('SKU', 'TotalSKUInWarehouse') != w2.config_parser.getint('SKU', 'TotalSKUInWarehouse'):
        for w in warehouseArray:
            res.append(w.config_parser.getint('SKU', 'TotalSKUInWarehouse'))
        return "Total SKUs in Warehouse", res
    
    elif w1.config_parser.getint('SKU', 'MaxSKUWeight') != w2.config_parser.getint('SKU', 'MaxSKUWeight'):
        for w in warehouseArray:
            res.append(w.config_parser.getint('SKU', 'MaxSKUWeight'))
        return "Maximum SKU weight", res
    
    elif w1.config_parser.getint('SKU', 'MinSKUWeight') != w2.config_parser.getint('SKU', 'MinSKUWeight'):
        for w in warehouseArray:
            res.append(w.config_parser.getint('SKU', 'MinSKUWeight'))
        return "Minimum SKU weight", res
    
    else:    
        return None, None

def get_changing_variable_worker(workerArray):
    w1 = workerArray[0]
    w2 = workerArray[1]
    res = []

    if w1.carrying_capacity != w2.carrying_capacity:
        for w in workerArray:
            res.append(w.carrying_capacity)

        return "Carrying Capacity", res
    
    elif w1.speed != w2.speed:
        for w in workerArray:
            res.append(w.speed)

        return "Worker Speed", res
    
    else:
        return None, None
        

def create_graph(warehouseArray, workerArray, naive, sShape, lGap, combined, optimal):

    #get first changing variable from warehouse
    x_name, x_values = get_changing_variable_warehouse(warehouseArray)

    #if warehouse no change, check workers
    if x_name == None:
        x_name, x_values = get_changing_variable_worker(workerArray)
    
    #if still nothing, raise exception
    if x_name == None:
        raise Exception("All variables are the same, please check that a variable is different between the config files.")
    
    #if nonlinear variable, create bar graph instead
    elif x_name == "TotalCrossAisles" or x_name == "Starting Point" or x_name == "Dropoff Location" or x_name == "Racks Orientation":
        x_val = x_values

        r = np.arange(len(x_val))
        width = 0.1
        

        yt1 = np.array(naive.get_time()).mean(axis=1)
        yt2 = np.array(sShape.get_time()).mean(axis=1)
        yt3 = np.array(lGap.get_time()).mean(axis=1)
        yt4 = np.array(combined.get_time()).mean(axis=1)
        yt5 = np.array(optimal.get_time()).mean(axis=1)

        yd1 = np.array(naive.get_dist()).mean(axis=1)
        yd2 = np.array(sShape.get_dist()).mean(axis=1)
        yd3 = np.array(lGap.get_dist()).mean(axis=1)
        yd4 = np.array(combined.get_dist()).mean(axis=1)
        yd5 = np.array(optimal.get_dist()).mean(axis=1)

        #error bars
        sampleSize = np.size(naive.get_time())
        yt1Err = np.array(naive.get_time()).std(axis=1) / np.sqrt(sampleSize)
        yt2Err = np.array(sShape.get_time()).std(axis=1) / np.sqrt(sampleSize)
        yt3Err = np.array(lGap.get_time()).std(axis=1) / np.sqrt(sampleSize)
        yt4Err = np.array(combined.get_time()).std(axis=1) / np.sqrt(sampleSize)
        yt5Err = np.array(optimal.get_time()).std(axis=1) / np.sqrt(sampleSize)

        yd1Err = np.array(naive.get_dist()).std(axis=1) / np.sqrt(sampleSize)
        yd2Err = np.array(sShape.get_dist()).std(axis=1) / np.sqrt(sampleSize)
        yd3Err = np.array(lGap.get_dist()).std(axis=1) / np.sqrt(sampleSize)
        yd4Err = np.array(combined.get_dist()).std(axis=1) / np.sqrt(sampleSize)
        yd5Err = np.array(optimal.get_dist()).std(axis=1) / np.sqrt(sampleSize)

        plt.subplot(2, 1, 1)
        plt.grid(axis="y")
        plt.bar(r - 2*width, yt1, width = width, yerr=yt1Err, label = "Naive")
        plt.bar(r - width, yt2, width = width, yerr=yt2Err, label = "S Shape")
        plt.bar(r, yt3, width = width, yerr=yt3Err, label = "Largest Gap")
        plt.bar(r + width, yt4, width = width, yerr=yt4Err, label = "Combined")
        plt.bar(r + 2*width, yt5, width = width, yerr=yt5Err, label = "Optimal")
        plt.title("Time taken")
        plt.xlabel(x_name)
        plt.ylabel('Time taken (s)')
        plt.xticks(r + width/5, x_val) 
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        plt.tight_layout()

        plt.subplot(2, 1, 2)
        plt.grid(axis="y")
        plt.bar(r - 2*width, yd1, width = width, yerr=yd1Err, label = "Naive")
        plt.bar(r - width, yd2, width = width, yerr=yd2Err, label = "S Shape")
        plt.bar(r, yd3, width = width, yerr=yd3Err, label = "Largest Gap")
        plt.bar(r + width, yd4, width = width, yerr=yd4Err, label = "Combined")
        plt.bar(r + 2*width, yd5, width = width, yerr=yd5Err, label = "Optimal")
        plt.title("Distance Travelled")
        plt.xlabel(x_name)
        plt.ylabel('Distance travelled (m)')
        plt.xticks(r + width/5, x_val) 
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        plt.tight_layout()
    
    else:
        #graph results
        x_val = np.array(x_values)

        #time values
        yt1 = np.array(naive.get_time()).mean(axis=1)
        yt2 = np.array(sShape.get_time()).mean(axis=1)
        yt3 = np.array(lGap.get_time()).mean(axis=1)
        yt4 = np.array(combined.get_time()).mean(axis=1)
        yt5 = np.array(optimal.get_time()).mean(axis=1)

        #distance values
        yd1 = np.array(naive.get_dist()).mean(axis=1)
        yd2 = np.array(sShape.get_dist()).mean(axis=1)
        yd3 = np.array(lGap.get_dist()).mean(axis=1)
        yd4 = np.array(combined.get_dist()).mean(axis=1)
        yd5 = np.array(optimal.get_dist()).mean(axis=1)

        #error bars
        sampleSize = np.size(naive.get_time())
        yt1Err = np.array(naive.get_time()).std(axis=1) / np.sqrt(sampleSize)
        yt2Err = np.array(sShape.get_time()).std(axis=1) / np.sqrt(sampleSize)
        yt3Err = np.array(lGap.get_time()).std(axis=1) / np.sqrt(sampleSize)
        yt4Err = np.array(combined.get_time()).std(axis=1) / np.sqrt(sampleSize)
        yt5Err = np.array(optimal.get_time()).std(axis=1) / np.sqrt(sampleSize)

        yd1Err = np.array(naive.get_dist()).std(axis=1) / np.sqrt(sampleSize)
        yd2Err = np.array(sShape.get_dist()).std(axis=1) / np.sqrt(sampleSize)
        yd3Err = np.array(lGap.get_dist()).std(axis=1) / np.sqrt(sampleSize)
        yd4Err = np.array(combined.get_dist()).std(axis=1) / np.sqrt(sampleSize)
        yd5Err = np.array(optimal.get_dist()).std(axis=1) / np.sqrt(sampleSize)

        #plot time taken
        plt.subplot(2, 1, 1)
        plt.errorbar(x_val, yt1, yerr=yt1Err, label = "Naive")
        plt.errorbar(x_val, yt2, yerr=yt2Err, label = "S Shape", ls = ':')
        plt.errorbar(x_val, yt3, yerr=yt3Err, label = "Largest Gap", ls = '--')
        plt.errorbar(x_val, yt4, yerr=yt4Err, label = "Combined", ls = '-.')
        plt.errorbar(x_val, yt5, yerr=yt5Err, label = "Optimal")
        plt.title("Time taken")
        plt.xlabel(x_name)
        plt.ylabel('Time taken (s)')
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        plt.tight_layout()

        #plot distance
        plt.subplot(2, 1, 2)
        plt.errorbar(x_val, yd1, yerr=yd1Err, label = "Naive")
        plt.errorbar(x_val, yd2, yerr=yd2Err, label = "S Shape", ls = ':')
        plt.errorbar(x_val, yd3, yerr=yd3Err, label = "Largest Gap", ls = '--')
        plt.errorbar(x_val, yd4, yerr=yd4Err, label = "Combined", ls = '-.' )
        plt.errorbar(x_val, yd5, yerr=yd5Err, label = "Optimal")
        plt.title("Distance Travelled")
        plt.xlabel(x_name)
        plt.ylabel('Distance travelled (m)')
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
        plt.tight_layout()
        
    # plt.suptitle(x_name)
    plt.savefig("Result Graph.png")
    plt.show()
    


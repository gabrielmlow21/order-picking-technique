import glob
import configparser
from warehouse import Warehouse
from worker import Worker
import sys
from layouts import Layout
from results import Results
from plotter import create_graph
import time
import os
import matplotlib.pyplot as plt

# specify the directory you want to use
reports_directory = 'reports'

# create the directory if it does not exist
if not os.path.exists(reports_directory):
    os.makedirs(reports_directory)


sys.path.append("picking_algorithms")

# Get a list of all 'config-*.ini' files
config_files = glob.glob('config-*.ini')

# Create a ConfigParser object
constants_config = configparser.ConfigParser()
constants_config.read('constants.ini')


def calculate_average_weight(orders):
    total_orders = len(orders)
    weight = 0
    for i in range(total_orders):
        weight += orders[i].weight
    return weight / total_orders


if __name__ == "__main__":
    # record start time
    start_time = time.time()
    j = 0
    warehouseArray = []
    workerArray = []
    naiveRes = Results()
    sShapeRes = Results()
    lGapRes = Results()
    combinedRes = Results()
    optimalRes = Results()

    # Iterate over the list of files
    for filename in config_files:
        print("Currently reading file: " + str(filename))
        config = configparser.ConfigParser()
        config.read(filename)

        naiveTime = []
        naiveDist = []
        sShapeTime = []
        sShapeDist = []
        lGapTime = []
        lGapDist = []
        combinedTime = []
        combinedDist = []
        optimalTime = []
        optimalDist = []

        for i in range(constants_config.getint('orders', 'TotalOrders')):
            warehouse = Warehouse(i, config, constants_config)
            worker = Worker(config, warehouse)

            report_filename = f'report-order-{j+1}.txt'

            # create a file path
            file_path = os.path.join(reports_directory, report_filename)

            # print results
            with open(file_path, 'w') as f:
                print("================== Warehouse ==================", file=f)
                print("Top-View of Warehouse:", file=f)
                for row in warehouse.warehouse:
                    print(" ".join(row), file=f)
                print("\nWarehouse Length: " +
                      str(warehouse.columns), file=f)
                print("Warehouse Width: " +
                      str(warehouse.rows), file=f)
                print("Warehouse Starting Point: " +
                      str(warehouse.starting_point), file=f)
                print("Warehouse Dropoff Location: " +
                      str(warehouse.dropoff_location), file=f)
                print(
                    "\n\n================== Rack ==================", file=f)
                print("Total Racks in Warehouse: " +
                      str(len(warehouse.racks)), file=f)
                print("\n\n================== SKU ==================", file=f)
                print("Total SKUs in Warehouse: " +
                      str(len(warehouse.skus)), file=f)
                print(
                    "\n\n================== Orders ==================", file=f)
                print("Orders: " + str(', '.join(str(sku.sku_id)
                                                 for sku in warehouse.orders)), file=f)
                print("Order Size: " + str(len(warehouse.orders)), file=f)
                print("Average Order Weight: " +
                      str(calculate_average_weight(warehouse.orders)), file=f)
                print(
                    "\n\n================== Worker ==================", file=f)
                print("Worker Carrying Capacity: " +
                      str(worker.carrying_capacity), file=f)
                print("Worker Speed(s/u): " +
                      str(worker.speed), file=f)
                print(
                    "\n\n================== RNG Seed ==================", file=f)
                print("Random Number Generator Seed: " +
                      str(warehouse.rng_seed), file=f)
                print(
                    "\n\n================== Order Picking Techniques (Time Taken) ==================", file=f)

                print("Naive Approach: " +
                      str(worker.get_time_naive()), file=f)
                naiveTime.append(worker.get_time_naive())

                naiveDist.append(worker.get_distance_naive())

                print("S-Shape Routing: " +
                      str(worker.get_time_s_shape()), file=f)
                sShapeTime.append(worker.get_time_s_shape())

                print("Largest Gap Routing: " +
                      str(worker.get_time_largest_gap()), file=f)
                lGapTime.append(worker.get_time_largest_gap())

                print("Combined Routing: " +
                      str(worker.get_time_combined_routing()), file=f)
                combinedTime.append(worker.get_time_combined_routing())

                print("Optimal Routing: " +
                      str(worker.get_time_optimal_routing()), file=f)
                optimalTime.append(worker.get_time_optimal_routing())

                print(
                    "\n\n================== Order Picking Techniques (Distance Traversed) ==================", file=f)

                print("Naive Approach: " +
                      str(naiveDist[-1]), file=f)
            #     naiveDist.append(worker.get_distance_naive())

                print("S-Shape Routing: " +
                      str(worker.get_distance_s_shape()), file=f)
                sShapeDist.append(worker.get_distance_s_shape())

                print("Largest Gap Routing: " +
                      str(worker.get_distance_largest_gap()), file=f)
                lGapDist.append(worker.get_distance_largest_gap())

                print("Combined Routing: " +
                      str(worker.get_distance_combined_routing()), file=f)
                combinedDist.append(worker.get_distance_combined_routing())

                print("Optimal Routing: " +
                      str(worker.get_distance_optimal_routing()), file=f)
                optimalDist.append(worker.get_distance_optimal_routing())

                j += 1
        print("Simulations run ok")
        # adding to external array for comparison and graphing
        warehouseArray.append(warehouse)
        workerArray.append(worker)

        naiveRes.add_time(naiveTime)
        naiveRes.add_dist(naiveDist)

        sShapeRes.add_time(sShapeTime)
        sShapeRes.add_dist(sShapeDist)

        lGapRes.add_time(lGapTime)
        lGapRes.add_dist(lGapDist)

        combinedRes.add_time(combinedTime)
        combinedRes.add_dist(combinedDist)

        optimalRes.add_time(optimalTime)
        optimalRes.add_dist(optimalDist)

    # graph results

    print("Simulations Completed: " + str(j))
    print("Graphing results...")

    end_time = time.time()
    # execution time
    execution_time = "{:.3f}".format(end_time - start_time)
    print(f"Execution time: {execution_time} seconds")

    create_graph(warehouseArray, workerArray, naiveRes,
                 sShapeRes, lGapRes, combinedRes, optimalRes)
    print("Graphing completed")

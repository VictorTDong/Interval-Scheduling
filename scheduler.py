"""
Name: Victor Dong
Purpose: The purpose of script is to read in a list of intervals and output the maximum amount of intervals that can be scheduled
Details: Script will take in the file, start time, and end time. It will then read the file and output it into a list which only takes in
         intervals that start on or after the given start time and intervals that finish before or on the given end time. Script will then sort 
         the intervals based on the finish time in ascending order which helps the algorithm choose intervals with the shortest intervals which allows
         the maximum to be reached. The Script will check to see if the current interval in the list has a start time that is greater or equal to the
         previous start time in which if the first interval is being picked, it will comapre it with the start time that the user indicated. In this case
         the interval being added to the maximum list will be the first interval in the list. After it will take the current intervals finish time and
         use that as the new finish time to compare it to. The script will always pick the next interval with the shortest elapsed time as the list is sorted 
         by finish time. This causes the next interval to always be the shortest interval. All other intervals that have a start time less than the
         previous finish time or a start time that is equal to the previous start time to be ignored. 

         ** Algorithm taken from lecture **
         ** Some code was referenced from https://docs.python.org/3/library/csv.html and https://www.w3schools.com/python/python_ref_list.asp (Reading in from csv and python list) **
"""
import csv
import sys

# Checks for correct input
numberOfArgs = len(sys.argv)
if numberOfArgs < 4 or (int(sys.argv[2]) > int(sys.argv[3])):
    print("Invalid arguments... \nUsage: python scheduler.py [filename] [start time] [end time]")

else:
    intervals = []
    maxIntervals = []
    start = int(sys.argv[2])
    finish = int(sys.argv[3])

    # Opens the specified file and removes all 
    # intervals outside the range of the specified start and end time
    with open(sys.argv[1], 'r') as file:
        reader = csv.reader(file, skipinitialspace=True)
        intervals = [[int(interval) for interval in time] for time in csv.reader(file) ] # Converts data to tuple of integers
        intervals = [i for i in intervals if (i[0] >= start and i[1] <= finish)] # Cleans list to only have intervals in specified start and finish time


    itemCount = len(intervals)

    # Sorts the intervals based on finishing time in ascending order
    intervals.sort(key=lambda interval:interval[1])

    count = 0
    finishTime = start 

    # Iterates through the list of intervals within a range
    for currInterval in intervals:
        if currInterval[0] >= finishTime: # Checks to make sure that the start time doesn't overlap with previous finish time
            """
            Appends the current interval to new list if it doesn't overlap, tere is no need to remove 
            any intervals with equal start times as list is sorted by finish times and only the shortest intervals will be added to the list
            Therefore shortest interval will always be chosen and the next interval will not have a finish time lower than the current one.
            """
            maxIntervals.append(currInterval) 
            finishTime = currInterval[1]
            count += 1
        

    print("The intervals scheduled are: \n" , maxIntervals)
    print("Total scheduled:" , count)

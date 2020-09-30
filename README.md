# CP-1
A medium level question I was having trouble solving.
In a one-dimensional city with houses aligned at integral locations along a road. The Mayor wants to install radio transmitters on the roofs of the city's houses. Each transmitter has a fixed range meaning it can transmit a signal to all houses within that number of units distance away.

Given a map of city and the transmission range, determine the minimum number of transmitters so that every house is within range of at least one transmitter. Each transmitter must be installed on top of an existing house.

For example, assume houses are located at x=[1,2,3,4,5,9] and the transmission range k=1.3 antennae at houses 2 and 5 and 9 would provide complete coverage. There is no house at location 7 to cover both 5 and 9. Ranges of coverage, are [1,2,3], [5], and [9].

# Function Description

Complete the RadioTransmitters function in the editor below. It must return an integer that denotes the minimum number of transmitters to install.

# RadioTransmitters has the following parameter(s):

x: integer array that denotes the locations of houses
k: an integer that denotes the effective range of a transmitter
# Input Format

The first line contains two space-separated integers n and k, the number of houses in Hackerland and the range of each transmitter.
The second line contains  space-separated integers describing the respective locations of each house x[i].

# Constraints
1<=n,k<=10^5
1<=x[i]<=10^5
There may be more than one house at the same location.

# Output Format

Print a single integer denoting the minimum number of transmitters needed to cover all of the houses.

# Sample Input 0

5 1
1 2 3 4 5
# Sample Output 0

2
# Explanation 0

We can cover the entire city by installing  transmitters on houses at locations 2 and 4.

# Sample Input 1

8 2
7 2 4 6 5 9 12 11 
# Sample Output 1

3
# Explanation 1

We can cover the entire city by installing  transmitters on houses at locations 4, 9, and 12.

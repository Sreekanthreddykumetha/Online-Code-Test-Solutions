from random import choice,randint


def solution(d, k, c, station):
    stations = list(station)
    stations.insert(0,0)
    stations.append(d)
    distances = []

    for i in range(1,len(stations)):
        distances.append(stations[i]-stations[i-1])
    duplicates = []
    for cash in range(0,c):
        def minimum(l):
            try:
                return min(l)
            except ValueError:
                return 0
        min_distance_index = 0
        for i in range(len(distances)):
            if distances[i] == max(distances):
                if max(distances) in distances[i+1:]:
                    if minimum(distances[:i]) < minimum(distances[i+1:]):
                        min_distance_index = i
                        break
                    elif minimum(distances[:i]) > minimum(distances[i+1:]):
                        continue
                    elif minimum(distances[:i]) == minimum(distances[i+1:]):
                        min_distance_index = i
                        break
                else:
                    min_distance_index = i
                    break
            else:
                continue

        if min_distance_index == 0:
            distances[min_distance_index]-=1
            distances[min_distance_index+1]+=1
        elif min_distance_index == len(distances)-1:
            distances[min_distance_index]-=1
            distances[min_distance_index-1]+=1
        elif 0<min_distance_index<len(distances)+1:
            if distances[min_distance_index+1]< distances[min_distance_index-1]:
                distances[min_distance_index+1]+=1
                distances[min_distance_index]-=1
            elif distances[min_distance_index+1]>distances[min_distance_index-1]:
                distances[min_distance_index-1]+=1
                distances[min_distance_index]-=1
            elif distances[min_distance_index+1] == distances[min_distance_index-1]:
                if min(distances[:min_distance_index]) <min(distances[min_distance_index:]):
                    distances[min_distance_index-1] += 1
                    distances[min_distance_index] -= 1
                elif min(distances[:min_distance_index]) > min(distances[min_distance_index:]):
                    distances[min_distance_index+1] += 1
                    distances[min_distance_index]-=1
                elif min(distances[:min_distance_index]) == min(distances[min_distance_index:]):
                    if len(distances[:min_distance_index])<len(distances[min_distance_index:]):
                        distances[min_distance_index-1] +=1
                        distances[min_distance_index]-=1
                    elif len(distances[:min_distance_index])>len(distances[min_distance_index:]):
                        distances[min_distance_index+1] += 1
                        distances[min_distance_index] -=1
                    else:
                        distances[choice([distances[min_distance_index+1],distances[min_distance_index-1]])]+=1
                        distances[distances[min_distance_index]] -=1
        if max(distances) not in duplicates:
            duplicates.append(max(distances))

        print(cash,"--->",distances,"--->",max(distances),'--->',min_distance_index)
    return min(duplicates)


d, k, c = 65, 3, 500
stations_outer = [1, 12, 15, 26, 37, 38, 38, 40, 49, 64]
print(solution(d, k, c, stations_outer))


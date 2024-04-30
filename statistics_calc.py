
import statistics

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
        
def get_user_input():
    old_list=input().split(",")
    new_list = []
    for item in old_list:
        new_list.append(float(item))

    return new_list

def calc_average(new_list):
    listLength = len(new_list)
    
    if listLength==0:
        return False
    elif listLength>=1:
        avg_temp= [sum(new_list)/listLength]
        print("The average temperature is",avg_temp[0])
    return avg_temp[0]

def calc_min_max(new_list):
    listLength=len(new_list)
    if listLength==0:
        return False
    elif listLength>=1:
        minmax=[min(new_list),max(new_list)]
        print("The minimum temperature is",minmax[0])
        print("The maximum temperature is",minmax[1])
    return minmax

def sort_temp(list):
    new_list=sorted(list)
    print("The temperatures in ascending order are as such:")
    for item in new_list:
        print(item)

    return new_list

def calc_median(list):
    listLength= len(list)
    if listLength==0:
        return False
    elif listLength>=1:
        new_list=sorted(list)
        median_temp=[statistics.median(new_list)]
        print("The median temperature is",median_temp[0])
    return median_temp[0]

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    calc_min_max(num_list)
    sort_temp(num_list)
    calc_median(num_list)

if __name__ == "__main__":
    main()


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

    avg_temp= sum(new_list)/listLength
    print("The average temperature is",avg_temp)
    return avg_temp

def calc_min_max_temp(new_list):
    minmax=[min(new_list),max(new_list)]
    print("The minimum temperature is",minmax[0])
    print("The maximum temperature is",minmax[1])
    return minmax

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    calc_min_max_temp(num_list)

if __name__ == "__main__":
    main()

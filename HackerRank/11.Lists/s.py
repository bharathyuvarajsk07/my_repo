if __name__ == '__main__':
    N=int(input())
    my_list = []
    for _ in range(N):
        task, *num = input().split()

        nums = list(map(int, num))

        if task == "insert":
            my_list.insert(int(nums[0]),int(num[1]))

        elif task == "print":
            print(my_list)

        elif task == "remove":
            my_list.remove(int(num[0]))

        elif task == "append":
            my_list.append(int(num[0]))

        elif task == "sort":
            my_list.sort()

        elif task == "pop":
            my_list.pop()

        elif task == "reverse":
            my_list.reverse()

        else :
            print("Unkown Command")

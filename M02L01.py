while True:
    # get two arrays as strings
    original_list = input("First list (enter elements of a list separated by spaces):\n")
    check_list = input("Check list (enter elements of a list separated by spaces):\n")

    # make from to strings two arrays (still each element is string)
    original_list = original_list.split()
    check_list = check_list.split()

    # convert elements type from string to int
    original_list = [eval(i) for i in original_list]
    check_list = [eval(i) for i in check_list]

    # array of partial powerset (subgroups with only 3 elements) and its length
    collect_list = []

    for first in range(0, len(original_list)):
        for second in range(first + 1, len(original_list)):
            for third in range(second + 1, len(original_list)):
                collect_list.append([original_list[first], original_list[second], original_list[third]])


    def TranslateToChars(main_list):
        # change [1, 3, 2] to ['S', 'L', 'M']
        for sub_list in main_list:
            min_index = sub_list.index(min(sub_list))
            max_index = sub_list.index(max(sub_list))

            sub_list[min_index] = 'S'  # small
            sub_list[max_index] = 'L'  # large

            # change the third element to STR value
            for element in sub_list:
                if type(element) != int:
                    continue
                elif type(element) == int:
                    sub_list[sub_list.index(element)] = 'M'  # medium
                else:
                    # just in case I missed something
                    print("ERROR")


    def IsAvoid(main_list, check_list):
        for sub_list in main_list:
            if sub_list == check_list:
                return False
        return True


    TranslateToChars(collect_list)
    TranslateToChars([check_list])  # brackets for "kostil"
    result = IsAvoid(collect_list, check_list)

    print(result)
    input('Press any key to continue')

    # print(collect_list)
    # print(check_list)

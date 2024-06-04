# Created by        : MyWork
# Created on        : 2024-05-18

import time
from configs import logger


def bubble_sort(lst: list[int]) -> (list[int], float):
    logger.info("bubble sorting")
    t0 = time.time()
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[i], lst[j] = lst[j], lst[i]
    tn = time.time()
    return lst, tn - t0


def selection_sort(lst: list[int]) -> (list[int], float):
    logger.info("selection sorting")
    t0 = time.time()
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    tn = time.time()
    return lst, tn - t0


SORTING_TYPES = {"1": bubble_sort, "2": selection_sort, }
if __name__ == "__main__":
    logger.info("Sorting module")
    num_lst = input("enter comma(,) separated numbers : ")
    try:
        num_lst = [int(_.strip()) for _ in num_lst.split(",")]
        logger.info(f"input : {num_lst}")
        msg = "Select sorting algorithm for ascending: \n"
        msg += "0. Run all\n"
        msg += "1. Bubble Sort\n"
        msg += "2. Selection Sort\n"
        sort_type = input(msg)
        sort_type = sort_type.strip()
        if sort_type in SORTING_TYPES:
            result = SORTING_TYPES[sort_type](num_lst)
            logger.info(f"result : {result[0]}")
            logger.info(f"time taken : {result[1]} secs")
        elif sort_type == "0":
            logger.info("running all")
        else:
            logger.warning("Not an option")
    except Exception as exp:
        logger.exception(exp)

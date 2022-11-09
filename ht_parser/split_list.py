from typing import List

def split_list(l: List[str], delimiter="", keep_delimiter=False) -> List[List[str]]:
    result = []
    chunk = []
    for element in l:
        if element == delimiter:
            result.append(chunk)
            chunk = []
            if keep_delimiter:
                chunk.append(element)
        else:
            chunk.append(element)
    result.append(chunk)
    return result

if __name__ == "__main__":
    list1 = ["this", "that", "", "other", "another", "", "and", "y"]
    result1 = split_list(list1)
    print(result1)
    list2 = ["this", "that", ";", "other", "another", ";", "and", "y"]
    result2 = split_list(list2, delimiter=";")
    print(result2)
    list3 = ["this", "that", ";", "other", "another", ";", "and", "y"]
    result3 = split_list(list3, delimiter=";", keep_delimiter=True)
    print(result3)
    list4 = ["this", "that"]
    result4 = split_list(list4)
    print(result4)

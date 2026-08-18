# l = [2,4,6,7,10]

# is_even = all((n := i) % 2 == 0 for i in l)
# print(is_even)
# print(n)

# def add_integer(a,b):
#     if not isinstance(a,int) or not isinstance(b,int):
#         raise Exception()
#     return a+b

# add_integer(1,2)


# from typing import Union

# def add(a: int,b: int)  -> int:
#     return a+b

# def add(a: Union[int,float],b: Union[int,float]) -> Union[int,float]:
#     return a+b

Num = int | float
def add(a: Num,b: Num) -> Num | None:
    if a<=0 or b<=0:
        return None
    return a+b


result=add(1,2)

from typing import Optional
def print_num(n: Num) -> None:
    print(n)

if result is not None:
    print_num(result)

from typing import List

num_list: List[Num] =[1,2,3]
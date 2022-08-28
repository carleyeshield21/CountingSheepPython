# This is the link to this Python coding challenge
# https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
def count_sheeps(sheep):
    counter = 0
    for i in sheep:
        if i == True:
            counter += 1
    print(f'Number of sheep/s:\n{counter}')
count_sheeps([True,  True,  True,  False, True,  True,  True,  True ,True,  False,True,  False,True,  False, False, True ,True,  True,  True,  True ,False, False, True,  True])
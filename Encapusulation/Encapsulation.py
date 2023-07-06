# class tv:
#     def __init__(self):
#         self.__status="off"
#         self.__channel=1
#         self.__volume=50

#     def __str__(self) -> str:
#         return f"{self.__status},{self.__volume},{self.__channel}"
    

# tv1=tv()
# print(tv1)

# print(tv1._tv__channel)
# tv1._tv__volume=4
# print(tv1._tv__volume)
# print(tv1)


# TODO getter and setter

class tv:
    def __init__(self):
        self.__status="off"
        self.__channel=1
        self.__volume=50

    def __str__(self) -> str:
        return f"{self.__status},{self.__volume},{self.__channel}"
    

    
class Person:

    def __init__(self, name, address, teleNumber):
        self.__name = name
        self.__address = address
        self.__teleNumber = teleNumber

    def print_person(self):
        print(self.__name)
        print(self.__address)
        print(self.__teleNumber)


class Customer(Person):
    def __init__(self, name, address, teleNumber, customerNumber, mailingList):
        Person.__init__(self, name, address, teleNumber)

        self.__customerNumber = customerNumber
        self.__mailingList = mailingList

    def print_person(self):
        Person.print_person()
        print("Customer Number: ", self.__customerNumber)
        if self.__mailingList:
            print("On mailing list")
        else:
            print("Not on mailing list")

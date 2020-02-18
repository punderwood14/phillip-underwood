class Home:

# constructor

    def __init__(self):

        self.__squarefeet = 0
        self.__squarefeet = 0
        self.__address = ""
        self.__city = ""
        self.__state = ""
        self.__zipcode = 0
        self.__modelname = ""
        self.__slaestatus = ""

# add method
    def addNewHome(self):
        self.__squarefeet = int(input('Enter squarefeet: '))
        self.__address = input('Enter address: ')
        self.__city = input('Enter city: ')
        self.__state = input('Enter state: ')
        self.__zipcode = int(input('Enter zipcode: '))
        self.__modelname = input('Enter Modelname: ')
        self.__slaestatus = input('Enter salestatus (sold, avilable, under contract): ')

    def removeHome(self):
        self.__squarefeet = 0
        self.__address = ""
        self.__city = ""
        self.__state = ""
        self.__zipcode = 0
        self.__modelname = ""
        self.__slaestatus = ""
        print(" removed! ")

    def updateHome(self):
        self.__squarefeet = int(input('Enter squarefeet: '))
        self.__address = input('Enter address: ')
        self.__city = input('Enter city: ')
        self.__state = input('Enter state: ')
        self.__zipcode = int(input('Enter zipcode: '))
        self.__modelname = input('Enter Modelname: ')
        self.__slaestatus = input('Enter salestatus (sold, avilable, under contract): ')

    def getAddress(self):
        return self.__address

    def getSquarefeet(self):
        return self.__squarefeet

    def getCity(self):
        return self.__city

    def getState(self):
        return self.__state

    def getZipcode(self):
        return self.__zipcode

    def getModelName(self):
        return self.__modelname

    def getSaleStatus(self):
        return self.__slaestatus

home = []

while True:
    print('1. Create new home ')
    print('2. Update home')
    print('3. remove home')
    print('4. save to file')
    print('5. Exit')
    option = int(input('Enter your response [1, 2, 3, 4, 5]: '))
    if option == 1:
        temp = Home()
        temp.addNewHome()
        home.append(temp)
    elif option == 2:
        address = input('Enter adress to update: ')
        index = -1
        for i in range(len(home)):
            if home[i].getAddress() == address:
                index = i
                break
            else:
                print('Address not found')

        if(index != -1):
            home[index].updateHome()
    elif option == 3:
        address = input('Enter address to update: ')
        index = -1
        for i in range(len(home)):
            if home[i].getAddress() == address:
                index = i
                break

        if(index != -1):
            home[index].removeHome()
            del home[index]
        else:
            print('Address not found')
    elif option == 4:
        myfile = open("home.txt","w")
        for x in range(len(home)):
            myfile.write(str(home[x].getAddress())+'\n')
            myfile.write(str(home[x].getSquarefeet())+'\n')
            myfile.write(str(home[x].getCity())+'\n')
            myfile.write(str(home[x].getState())+'\n')
            myfile.write(str(home[x].getZipcode())+'\n')
            myfile.write(str(home[x].getModelName())+'\n')
            myfile.write(str(home[x].getSaleStatus())+'\n')
    elif option == 5:
        break
    else:
        print("wrong option !")

import csv
from datetime import datetime #csv and datetime library imported

#The Menu.txt file was created and the Menu information was entered into it.
file = open("Menu.txt", "w")
file.write('* Please Choose a Pizza Base:')
file.write('\n1: Classic\n2: Margherita\n3: TurkPizza\n4: PlainPizza\n')
file.write('* and sauce of your choice:')
file.write('\n11: Olives\n12: Mushrooms\n13: GoatCheese\n14: Meat\n15: Onions\n16: Corn\n')
file.write('* Thank you!')
file.close()

#Pizza class defined.
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        self.description

    def get_cost(self):
        return self.cost

#Classic Pizza subclass defined.
class Classic(Pizza):
    def __init__(self):
        super().__init__(
            "Classic Pizza Sauce, Thin Dough, Classic Edge, Medium Size, Corn, Salami,",
            13.50)

#Margherita Pizza subclass defined.
class Margherita(Pizza):
    def __init__(self):
        super().__init__(
            "Mozzarella Cheese, Pizza Sauce, Basil, Thin Dough, Thin Edge, Medium Size",
            16.00)

#Turk Pizza subclass defined.
class TurkPizza(Pizza):
    def __init__(self):
        super().__init__(
            "Turkish Sauce, Thin Dough, Thin Edge, Medium Salami, Sausage, Green Olives",
            16.75
        )

#Dominos Pizza subclass defined.
class DominosPizza(Pizza):
    def __init__(self):
        super().__init__(
            "Classic Pizza Sauce, Thin Dough, Thin Edge",
            18.99
        )

#The Decorator class is defined.
class Decorator(Pizza):
    def __init__(self, component):
        self.component = component
        self.description = ""
        self.cost = 0

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)

#Olivies class is defined.
class Olives(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Olives Sauce"
        self.cost = 0.50

#Mushrooms class is defined.
class Mushrooms(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mushrooms Sauce"
        self.cost = 1.50

#GoatCheese class is defined.
class GoatCheese(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Goat Cheese"
        self.cost = 2.70

#Meat class is defined.
class Meat(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Meat Sauce"
        self.cost = 4.25

#Onions class is defined.
class Onions(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Onions Sauce"
        self.cost = 0.99

#Corn class is defined.
class Corn(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Corn Sauce"
        self.cost = 1.25


def main():

    #Menu.txt is printed.
    file = open("Menu.txt", "r")
    print(file.read())
    file.close()

    #Identification done.
    totalPrice=0
    orderDescription=""

    print("\n***Welcome Pizza Order System***")
    while True:
        #The user was asked to choose the pizza base.
        print("Pizza Base Types: ")
        print("(1) Classic $", Classic().cost, "(2) Margherita $", Margherita().cost,
            "(3) TurkPizza $", TurkPizza().cost, "(4) PlainPizza $", DominosPizza().cost)
    
        choosePizza = input("> Enter your pizza choose: ")
        yesOrNo = input("\nDo you approve of the classic pizza base? (Y | N): ")

        if yesOrNo == "y" or yesOrNo == "Y":

            #Description, price and price of sauces were defined for each type of pizza.
            classicDescription=""
            classicPrice=0
            totalSauceCost_Classic = 0

            margheritaDescription=""
            margheritaPrice=0
            totalSauceCost_Margherita = 0

            turkDescription=""
            turkPrice=0
            totalSauceCost_Turk = 0
            
            dominosDescription=""
            dominosPrice=0
            totalSauceCost_Dominos = 0


            if choosePizza == "1":
                #Description of Classic Pizza is printed.
                print("Classic Pizza Description: ")
                classicDescription=Classic().description
                print(classicDescription)

                classicPrice=Classic().cost
                totalDescription=""

                #User was asked if you want extra sauce
                yesOrNo = input("\nPizza Would You Like Extra Sauce? (Y | N): ")

                if yesOrNo == "y" or yesOrNo == "Y":
                    #Types of sauces printed
                    print("Pizza Extra Sauce")
                    print("(11) Olives $", Olives(Decorator).cost, " (12) Mushrooms $", Mushrooms(Decorator).cost, "(13) GoatCheese $", GoatCheese(Decorator).cost,
                        " (14) Meat $", Meat(Decorator).cost, " (15) Onions $", Onions(Decorator).cost, " (16) Corn $", Corn(Decorator).cost, "(17) No Exstra Sauce")
                    
                    while True:
                        #The prices and descriptions of the sauces selected by the user were kept.
                        chooseSauce = input("> Enter your Sauce choose: ")
                        if chooseSauce == "11":
                            totalSauceCost_Classic += Olives(Decorator).cost
                            totalDescription=Olives(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "12":
                            totalSauceCost_Classic += Mushrooms(Decorator).cost
                            totalDescription=Mushrooms(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "13":
                            totalSauceCost_Classic += GoatCheese(Decorator).cost
                            totalDescription=GoatCheese(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "14":
                            totalSauceCost_Classic += Meat(Decorator).cost
                            totalDescription=Meat(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "15":
                            totalSauceCost_Classic += Onions(Decorator).cost
                            totalDescription=Meat(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "16":
                            totalSauceCost_Classic += Corn(Decorator).cost
                            totalDescription=Meat(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "17":
                            #When the user did not want more sauce, no more sauce was asked by choosing number 17.
                            totalSauceCost_Classic += 0
                            break

                if yesOrNo == "N" or yesOrNo == "n":
                    #If the user did not select a sauce, the price of the sauce was defined as 0.
                    totalSauceCost_Dominos += 0
                                              
            elif choosePizza == "2":
                #Description of Margherita Pizza is printed.
                print("Margherita Pizza Description: ")
                margheritaDescription=Margherita().description
                print(margheritaDescription)

                margheritaPrice=Margherita().cost
                totalDescription=""

                #User was asked if you want extra sauce
                yesOrNo = input("\nPizza Would You Like Extra Sauce? (Y | N): ")

                if yesOrNo == "y" or yesOrNo == "Y":
                    #Types of sauces printed
                    print("Pizza Extra Sauce")
                    print("(11) Olives $", Olives(Decorator).cost, " (12) Mushrooms $", Mushrooms(Decorator).cost, "(13) GoatCheese $", GoatCheese(Decorator).cost,
                        " (14) Meat $", Meat(Decorator).cost, " (15) Onions $", Onions(Decorator).cost, " (16) Corn $", Corn(Decorator).cost, "(17) No Exstra Sauce")

                    while True:
                        #The prices and descriptions of the sauces selected by the user were kept.
                        chooseSauce = input("> Enter your Sauce choose: ")
                        if chooseSauce == "11":
                            totalSauceCost_Margherita += Olives(Decorator).cost
                            totalDescription=Olives(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "12":
                            totalSauceCost_Margherita += Mushrooms(Decorator).cost
                            totalDescription=Mushrooms(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "13":
                            totalSauceCost_Margherita += GoatCheese(Decorator).cost
                            totalDescription=GoatCheese(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "14":
                            totalSauceCost_Margherita += Meat(Decorator).cost
                            totalDescription=Meat(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "15":
                            totalSauceCost_Margherita += Onions(Decorator).cost
                            totalDescription=Meat(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "16":
                            totalSauceCost_Margherita += Corn(Decorator).cost
                            totalDescription=Meat(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "17":
                            #When the user did not want more sauce, no more sauce was asked by choosing number 17.
                            totalSauceCost_Margherita += 0
                            break

                if yesOrNo == "N" or yesOrNo == "n":
                    #If the user did not select a sauce, the price of the sauce was defined as 0.
                    totalSauceCost_Dominos += 0
                  
            elif choosePizza == "3":
                #Description of Turk Pizza is printed.
                print("Turk Pizza Description: ")
                turkDescription=TurkPizza().description
                print(turkDescription)

                turkPrice=TurkPizza().cost
                totalDescription=""

                #User was asked if you want extra sauce
                yesOrNo = input("\nPizza Would You Like Extra Sauce? (Y | N): ")

                if yesOrNo == "y" or yesOrNo == "Y":
                    #Types of sauces printed
                    print("Pizza Extra Sauce")
                    print("(11) Olives $", Olives(Decorator).cost, " (12) Mushrooms $", Mushrooms(Decorator).cost, "(13) GoatCheese $", GoatCheese(Decorator).cost,
                        " (14) Meat $", Meat(Decorator).cost, " (15) Onions $", Onions(Decorator).cost, " (16) Corn $", Corn(Decorator).cost, "(17) No Exstra Sauce")

                    while True:
                        #The prices and descriptions of the sauces selected by the user were kept.
                        chooseSauce = input("> Enter your Sauce choose: ")
                        if chooseSauce == "11":
                            totalSauceCost_Turk += Olives(Decorator).cost
                            totalDescription=Olives(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "12":
                            totalSauceCost_Turk += Mushrooms(Decorator).cost
                            totalDescription=Mushrooms(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "13":
                            totalSauceCost_Turk += GoatCheese(Decorator).cost
                            totalDescription=GoatCheese(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "14":
                            totalSauceCost_Turk += Meat(Decorator).cost
                            totalDescription=Meat(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "15":
                            totalSauceCost_Turk += Onions(Decorator).cost
                            totalDescription=Meat(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "16":
                            totalSauceCost_Turk += Corn(Decorator).cost
                            totalDescription=Meat(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "17":
                            #When the user did not want more sauce, no more sauce was asked by choosing number 17.
                            totalSauceCost_Turk += 0
                            break

                if yesOrNo == "N" or yesOrNo == "n":
                    #If the user did not select a sauce, the price of the sauce was defined as 0.
                    totalSauceCost_Dominos += 0

            elif choosePizza == "4":
                #Description of Turk Pizza is printed.
                print("Plain Pizza Description: ")
                dominosDescription=DominosPizza().description
                print(dominosDescription)

                dominosPrice=DominosPizza().cost
                totalDescription=""

                #User was asked if you want extra sauce
                yesOrNo = input("\nPizza Would You Like Extra Sauce? (Y | N): ")

                if yesOrNo == "y" or yesOrNo == "Y":
                    #Types of sauces printed
                    print("Pizza Extra Sauce")
                    print("(11) Olives $", Olives(Decorator).cost, " (12) Mushrooms $", Mushrooms(Decorator).cost, "(13) GoatCheese $", GoatCheese(Decorator).cost,
                        " (14) Meat $", Meat(Decorator).cost, " (15) Onions $", Onions(Decorator).cost, " (16) Corn $", Corn(Decorator).cost, "(17) No Exstra Sauce")

                    while True:
                        #The prices and descriptions of the sauces selected by the user were kept.
                        chooseSauce = input("> Enter your Sauce choose: ")
                        if chooseSauce == "11":
                            totalSauceCost_Dominos += Olives(Decorator).cost
                            totalDescription=Olives(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "12":
                            totalSauceCost_Dominos += Mushrooms(Decorator).cost
                            totalDescription=Mushrooms(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "13":
                            totalSauceCost_Dominos += GoatCheese(Decorator).cost
                            totalDescription=GoatCheese(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "14":
                            totalSauceCost_Dominos += Meat(Decorator).cost
                            totalDescription=Meat(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "15":
                            totalSauceCost_Dominos += Onions(Decorator).cost
                            totalDescription=Meat(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "16":
                            totalSauceCost_Dominos += Corn(Decorator).cost
                            totalDescription=Meat(Decorator).description+"-"+totalDescription
                        elif chooseSauce == "17":
                            #When the user did not want more sauce, no more sauce was asked by choosing number 17.
                            totalSauceCost_Dominos += 0
                            break
                if yesOrNo == "N" or yesOrNo == "n":
                    totalSauceCost_Dominos += 0

            #The total price of the selected sauces was calculated.                     
            print("Total Sauce Cost $", totalSauceCost_Classic+totalSauceCost_Margherita+totalSauceCost_Turk+totalSauceCost_Dominos)

            #The description of the selected orders and the total sauce price were calculated and printed.
            print("\n********Orders******** ")
            print("Classic Pizza Base: ",
                  classicDescription+"\n"+
                  margheritaDescription+"\n"+
                  turkDescription+"\n"+
                  dominosDescription
                  )
            print("Price $",totalSauceCost_Classic+totalSauceCost_Margherita+totalSauceCost_Turk+totalSauceCost_Dominos+classicPrice+margheritaPrice+turkPrice+dominosPrice)

            orderDescription+=classicDescription+margheritaDescription+turkDescription+dominosDescription+"-"

            #The total price (including sauce) of the selected orders was calculated.
            totalPrice+=totalSauceCost_Classic+totalSauceCost_Margherita+totalSauceCost_Turk+totalSauceCost_Dominos+classicPrice+margheritaPrice+turkPrice+dominosPrice
            print("Total Price $ ",totalPrice)

            #The user was asked to checkout or if wanted to order more.
            yesOrNo = input("\nDo You Confirm The Order? (Y: Payment | N: Add Another Order): ")
            if yesOrNo == "y" or yesOrNo == "Y":
                #For payment transactions, the user's name, ID number, card number and card password are requested.
                print("\n********Payment********")

                try:
                    name = input("> Enter your name: ")
                    idNumber = int(input("> Enter your ID number: "))
                    cardNumber = int(input("> Enter your credit card number: "))
                    cardPassword = int(input("> Enter your credit card password: "))

                    #The name, id number, card number, card password, order description, total price and the time the order was placed were printed in the orders.csv file.
                    file= open("orders.csv", "a", newline="")
                    writer = csv.writer(file)
                    now = datetime.now()
                    date_time = now.strftime("%m/%d/%Y %H:%M:%S")
                    writer.writerow([name, idNumber, cardNumber, cardPassword, orderDescription, totalPrice, date_time])

                    print("\nPayment Received...")

                    break
                except:
                    #If another character is entered in the places where numbers should be entered, it gives an error.
                    print("An Error Occurred While Receiving Payment!!!")
                    break

            else:
                continue
            
        elif yesOrNo == "n" or yesOrNo == "N":
            #If it does not accept any order base, the program is exited.
            exit()
            print("Exit..")

#The main function is executed.            
if __name__ == "__main__":
    main()

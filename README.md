## **Coffee Machine Project**

This Python project simulates a coffee machine with the ability to take orders, manage resources, and handle payments. The project consists of four main files: **coffee\_maker.py**, **menu.py**, **money\_machine.py**, and **main.py**.

### **coffee\_maker.py**

This file contains the **CoffeeMaker** class, which models the coffee-making machine. It includes methods for reporting resources, checking resource sufficiency for a given drink, and making coffee by deducting the required ingredients from the available resources.

### **menu.py**

The **menu.py** file defines two classes: **MenuItem** and **Menu**. **MenuItem** models each menu item with specific ingredients and costs, while **Menu** manages a list of available drinks. It provides methods to get a list of available items and find a drink by name.

### **money\_machine.py**

In this file, the **MoneyMachine** class is implemented to handle payments. It includes methods for reporting the current profit, processing coins, and making payments. The class keeps track of the profit and the money received.

### **main.py**

The **main.py** file integrates the functionalities of the other files to create a fully functional coffee machine simulation. It imports the **Menu**, **CoffeeMaker**, and **MoneyMachine** classes and runs a loop to take user input, process orders, and manage the coffee machine operations.

### **Usage:**

1.  Run **main.py** to start the coffee machine simulation.
2.  Enter the desired drink when prompted (espresso/latte/cappuccino).
3.  Use the command "report" to get a report of the available resources.
4.  Use the command "off" to turn off the coffee machine and exit the program.

**Note:** The program will continuously run until the "off" command is entered.
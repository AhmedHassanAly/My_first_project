# Ahmed Aly
# CS115-J101
# Spring 2019
# Programming Assisgnment #2
# This program calcolates the sale from the total price




# Asking the user to enter the number of fancy syrup sold

num_of_quart_fancy = int(input("Enter the number of quart containers of Fancy Grade sold: "))
num_of_pint_fancy = int(input("Enter the number of pints containers of Fancy Grade sold: "))
num_of_cup_fancy = int(input("Enter the number of cups containers of Fancy Grade sold: "))

# Asking the user to enter the number of Grade A Medium sold

num_of_quart_medium  = int(input("Enter the number of quart containers of Grade A Meduim Amber Syrups: "))           
num_of_pint_meduim  = int(input('Enter the number of pints container of Grade A Meduim Amber Syrups: ')) 
num_of_cup_meduim  = int(input('Enter the number of cups containers of Grade A Meduim Amber Syrups: ')) 

# Asking the user to enter the number of Grade A Dark syrup sold

num_of_quart_dark = int(input('Enter the number of quart containers of Grade A Dark Syrups: '))           
num_of_pint_dark = int(input('Enter the number of pints containersf Grade A Dark Syrups: ')) 
num_of_cup_dark = int(input('Enter the number of cups contianers f Grade A Dark Syrups: '))

# Asking the user to enter the number of Grade B syrup sold

num_of_quart_b = int(input('Enter the number of quart of Grade B syrup sold:'))
num_of_pint_b = int(input('Enter the number of pints containers of Grade B Syrup sold: '))                       
num_of_cup_b = int(input('Enter the number of cups containers of Grade B syrup sold:  '))




# Displaying the Amount of each kind of syrups and its size that has been sold

print("Amount of Fancy Grade syrup sold:", int(num_of_quart_fancy), 'quart(s)', int(num_of_pint_fancy), 'pint(s)', int(num_of_cup_fancy), 'cup(s)')
print("Amount of Grade A meduim syrup sold:", int(num_of_quart_medium), 'quart(s)', int(num_of_pint_meduim), "pint(s)", int(num_of_cup_meduim), 'cup(s)')
print("Amount of Grade A Dark syrup sold:", int(num_of_quart_dark), 'quart(s)', int(num_of_pint_dark), 'pint(s)', int(num_of_cup_dark), 'cup(s)')
print("Amount of Grade B sold:", int(num_of_quart_b), 'quart(s)', int(num_of_pint_b), 'pint(s)', int(num_of_pint_b), 'cup(s)')



# Calcoulating the total number of each size sold seperatly 
                      
q = int(num_of_quart_fancy) + int(num_of_quart_medium) + int(num_of_quart_dark) + int(num_of_quart_b)

p = int(num_of_pint_fancy) + int(num_of_pint_meduim) + int(num_of_pint_dark) + int(num_of_pint_b)

c = int(num_of_cup_fancy) + int(num_of_cup_meduim) + int(num_of_cup_dark) + int(num_of_cup_b)




h = c // 2

p += h
c -= 2*h

j = p // 2

q += j
p -= 2*j


print("Total amount of syrup sold:", int(q), "quart(s)", int(p), "pint(s)", int(c), "cup(s)")



# Displaying total cost
total_cost = (q * 9 ) + (p * 5) + (c * 3)

print(" Total cost:", "$", total_cost)
















    
    


 


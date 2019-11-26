welcome = str("Welcome to your magnificent holiday programme! \n")
print(welcome)


city = input("Which city are you flying to? (Los Angeles, New York, Las Vegas, San Francisco or San Diego California): \n") #user_input
def planeCosts(city):                                                 #defining a variable
    if city == "Las Vegas":
        return 500                                                    #set price for ticket as per user choice
    elif city == "New York":
        return 600                                                    #set price for ticket as per user choice
    elif city == "Los Angeles":
        return 650                                                    #set price for ticket as per user choice
    elif city == "San Francisco":
        return 700                                                    #set price for ticket as per user choice
    elif city == "San Diego California":
        return 750                                                    #set price for ticket as per user choice

nights = int(input("How many nights will you be staying here for?: \n")) #user_input
def hotelCosts(nights):                                                  #defining_a_variable
    price  = 300                                                         #set_price_per_night
    total_nights = nights * price                                        #calulation
    return total_nights                                                  #returns_calculated_price



car = int(input("How many days are you gonna rent this car for?: \n")) #user_input
def carRental(car):                                                    #defining_a_variable
    price = 150                                                        #set price to rent a car                                               
    total_car = price * car                                            #calculations
    return total_car                                                   #returns_price_of_car c num of days


var1 = hotelCosts(nights) #storing_a_function with parameters
var2 = planeCosts(city)   #storing_a_function with parameters
var3 = carRental(car)     #storing_a_function with parameters

print(f"The total cost for staying at this hotel for {nights} nights are ${hotelCosts(nights)}") #printing_prices_of hotel costs
print(f"The total cost of the flight tickets will be ${planeCosts(city)}") #printing_prices_of flight costs
print(f"The total cost of renting out the car for {car} days are ${carRental(car)} \n") #printing_prices_of car rental costs

print(f"The entire cost of this holiday will total up to ${var1 + var2 + var3}") #printing_prices_of total holiday costs







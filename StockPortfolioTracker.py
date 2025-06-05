#Stock Portfolio Tracker implementation in Python
import time #time module has been imported to offer time delay between print statements
predefined_stocks=stock_prices = { #Dictionary of predefined stocks with their respective prices
    "AAPL": 202.82,
    "MSFT": 463.87,
    "GOOGL": 168.05,
    "AMZN": 207.23,
    "TSLA": 332.05,
    "META": 687.95,
    "BRK.A": 737820.0,
    "JPM": 264.22,
    "V": 368.0,
    "JNJ": 153.22,
    "WMT": 99.35,
    "PG": 165.95,
    "MA": 584.13,
    "NVDA": 141.92,
    "HD": 372.4,
    "DIS": 113.49,
    "UNH": 300.38,
    "VZ": 43.24,
    "PFE": 23.39,
    "KO": 71.37,
    "T": 27.36
}
print("Hello and Welcome to the Stock Portfolio Tracker") 
time.sleep(1) #time delay of 1s
print("We provide Support of the following stocks as listed below") 
for key in predefined_stocks.keys():                #Displaying all the stocks supported by the Stock Portfolio Tracker
  print(key)
time.sleep(1) #time delay of 1s 
print("Start Entering your stocks and type stop when you are done with stocks")
stocks,quantity=[],[] #empty lists of stocks and quantity to store stocks and their respective quantities entered by the user
stock_input=input() #Taking input of stock from the user
while stock_input!="stop": #While loop to implement stock storage in stock list as well as stop functionality
    if stock_input in predefined_stocks.keys():
      stocks.append(stock_input)
      stock_input=input() #Resetting the stock input by again using input function and taking input again
    else:
        print("Invalid Stock! Try Again") #Implementing invalid stock input handling if stock input entered by the user is not in the predefined_stocks
        stock_input=input() ##Taking stock input again after invalid input
        continue
else:
    print("Your stocks have been recorded")
print("Now Start Entering the quantity of your stocks respectively and type stop when you are done with the quantities")
quantity_input=input() #Taking input of quantity from the user
while quantity_input!="stop": #While loop to implement stock storage in stock list as well as stop functionality
    if quantity_input.isnumeric():
      quantity.append(int(quantity_input))
      quantity_input=input() #Resetting the quantity input by again using input function and taking input again
    else:
       print("Invalid Quantity! Try Again")  #Implementing invalid quantity input handling if stock input entered by the user is non numeric
       quantity_input=input() #Taking quantity input again after invalid input
       continue
else:
    print("The quantities for your stocks have been recorded successfully")
Total_Investment=0 #Total Invenstment to store total investment or portfolio by the user
for index in range(len(stocks)): #For loop to implement calculation of total investment 
    Total_Investment+=predefined_stocks.get(stocks[index])*quantity[index] #Updating total investment 
print(f"Your total investment or portfolio is {Total_Investment} rupees and it has been saved successfully in Portfolio.csv")
with open("Portfolio.csv","a") as writer: #Creating the Portfolio.csv and opening it in append mode
    writer.write(f"Portfolio: {Total_Investment} rupees\n") #Writing the portfolio of the user in the Portfolio csv file



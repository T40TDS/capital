import entities as en
firms = {}
player_inventory = 0
player_cash = 0
name_to_id_ = {}
id_to_name = {}
london_market = None


def main():
	global firms,player_inventory,player_cash,name_to_id_,london_market,id_to_name
	iron = en.Commodity("base",0,"iron", 60.0)
	coal = en.Commodity("base",1,"coal", 30.0)
	wood = en.Commodity("base",2,"wood", 25.0)
	water = en.Commodity("base",3,"water", 10.0)
	stone = en.Commodity("base",4,"stone", 20.0)

	name_to_id_ = {"iron":0,"coal":1,"wood":2,"water":3,"stone":4}
	for key,value in name_to_id_.items():
		id_to_name[value] = key


	london_market = en.Market("London","the London Grand Exchange", [iron,coal,wood,water,stone])
	london_bank = en.Bank("bank",0, "London Vivaldi Bank")

	london_bank.inv = [0,0,0,0,0]
	london_bank.inv[0] = 10000 #iron
	london_bank.inv[1] = 5000 #coal
	london_bank.inv[2] = 10000 #wood
	london_bank.inv[3] = 100 #water
	london_bank.inv[4] = 15000 #stone

	firms = {london_bank.id_:london_bank}	
	player_inventory = [0,0,0,0,0]
	player_cash = en.PLAYER_STARTING_CASH


	print("Welcome to {} in {}".format(london_market.name,london_market.location))


	response = ""
	exit_flag = 0
	while(exit_flag == 0):
		print("The current market prices are:")
		print("------------------------------")
		for item in london_market.commodities:
			print("{0}: ${1}".format(item.name,item.price))
		print("------------------------------")	
		response = input()
		if(response == "/exit"):
			exit_flag = 0
			break
		tokens = response.split()

		if(tokens[0] == "buy"): #currently only buying from bank supported
			return_flag = buy(name_to_id_[tokens[1]],int(tokens[3]),float(tokens[2]),0)
			if(return_flag == en.TRADE_SUCCESS):
				print("-----------------------------------")
				print("The trade was sucessfully executed.")
				print("-----------------------------------")

			elif(return_flag == en.TRADE_REJECT_NOT_ENOUGH_CASH):
				print("-----------------------------------")
				print("You don't have enough cash for the trade.")
				print("-----------------------------------")

			elif(return_flag == en.TRADE_REJECT_NOT_ENOUGH_INV):
				print("-----------------------------------")
				print("The firm doesn't have enough of {0} to sell to you.".format(tokens[1]))
				print("-----------------------------------")

			elif(return_flag == en.TRADE_REJECT):
				print("-----------------------------------")
				print("The firm does not like your price.")
				print("-----------------------------------")

		if(tokens[0] == "sell"): #currently only buying from bank supported
			return_flag = sell(name_to_id_[tokens[1]],int(tokens[3]),float(tokens[2]),0)
			if(return_flag == en.TRADE_SUCCESS):
				print("-----------------------------------")
				print("The trade was sucessfully executed.")
				print("-----------------------------------")

			elif(return_flag == en.TRADE_REJECT_NOT_ENOUGH_CASH):
				print("-----------------------------------")
				print("The firm doesn't have enough cash for the trade.")
				print("-----------------------------------")

			elif(return_flag == en.TRADE_REJECT_NOT_ENOUGH_INV):
				print("-----------------------------------")
				print("You don't have enough of {0} to sell to the firm.".format(tokens[1]))
				print("-----------------------------------")

			elif(return_flag == en.TRADE_REJECT):
				print("-----------------------------------")
				print("The firm does not like your price.")
				print("-----------------------------------")

		if(tokens[0] == "report"):
			print("-----------------------------------")
			print("Your report:")
			print("Your cash: {}".format(player_cash))
			print("Your assets:")
			for i in range(0,len(player_inventory)):
				print("{0}: {1}".format(id_to_name[i], player_inventory[i]))
			print("-----------------------------------")				

def buy(id_,amount,price,firm_id_):
	global firms,player_inventory,player_cash,name_to_id_,london_market,id_to_name
	if(amount*price > player_cash):
		return en.TRADE_REJECT_NOT_ENOUGH_CASH
	trade_flag = firms[firm_id_].buy_request(london_market,id_,amount,price)
	if(trade_flag == en.TRADE_SUCCESS):
		player_inventory[id_] = player_inventory[id_] + amount
		london_market.commodities[id_].price = price
		player_cash = player_cash - amount*price

	return trade_flag 

def sell(id_,amount,price,firm_id_):
	global firms,player_inventory,player_cash,name_to_id_,london_market,id_to_name
	if(player_inventory[id_] < amount):
		return en.TRADE_REJECT_NOT_ENOUGH_INV
	trade_flag = firms[firm_id_].sell_request(london_market,id_,amount,price)
	if(trade_flag == en.TRADE_SUCCESS):
		player_inventory[id_] = player_inventory[id_] - amount
		london_market.commodities[id_].price = price
		player_cash = player_cash + amount*price

	return trade_flag



if __name__ == "__main__":
	main()	






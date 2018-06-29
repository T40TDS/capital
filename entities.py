BANK_STARTING_CASH = 10000000
TRADE_SUCCESS = 1
TRADE_REJECT = -1
TRADE_REJECT_NOT_ENOUGH_INV = -2
TRADE_REJECT_NOT_ENOUGH_CASH = -3
PLAYER_STARTING_CASH = 2000
class Commodity:
	def __init__(self,type_,id_,name,init_price):
		self.type_ = type_
		self.id_ = id_
		self.name = name
		self.price = init_price

class Firm:
	def __init__(self,type_,id_,name, cash):
		self.type_ = type_
		self.id_ = id_ 
		self.name = name
		self.cash = cash
		self.inv = [];

class Market:
	def __init__(self,location,name,commodities):
		self.location = location
		self.name = name
		self.commodities = commodities		

class Bank(Firm):
	#The bank tries to mantain its inventory. To this end, it will hesitate to sell large parts of its inventory.
	#It will also be willing to buy at a high price if its inventory is low
	#The bank has no shortage of money supply - this needs to change
	def __init__(self,type_,id_,name):
		Firm.__init__(self,type_,id_,name, BANK_STARTING_CASH)

	def sell_request(self,market,id_,amount,price):
		if(amount <= .50*self.inv[id_]):
			if(market.commodities[id_].price >= price):
				self.inv[id_] = self.inv[id_] + amount
				market.commodities[id_].price = price
				return TRADE_SUCCESS
		elif(amount <= self.inv[id_]):
			if(market.commodities[id_].price*(1 + (amount/self.inv[id_])/4) >= price):
				self.inv[id_] = self.inv[id_] + amount
				market.commodities[id_].price = price
				return TRADE_SUCCESS
		elif(amount >= self.inv[id_]):
			if(market.commodities[id_].price*(1 + (amount/self.inv[id_])/2) >= price):
				self.inv[id_] = self.inv[id_] + amount
				market.commodities[id_].price = price
				return TRADE_SUCCESS
		return TRADE_REJECT

				
	def buy_request(self,market,id_,amount,price):
		if(amount <= .10*self.inv[id_]):
			if (market.commodities[id_].price <= price): #if the market price is less than the offered price
				#execute the trade			
				self.inv[id_] = self.inv[id_] - amount
				market.commodities[id_].price = price #the price is the last traded price
				return TRADE_SUCCESS
		elif(amount <= .50*self.inv[id_]):
			if(market.commodities[id_].price*(1 + (amount/self.inv[id_])/2) <= price):
				self.inv[id_] = self.inv[id_] - amount
				market.commodities[id_].price = price #the price is the last traded price
				return TRADE_SUCCESS
		elif(amount <= self.inv[id_]):
			if(market.commodities[id_].price*(1 + (amount/self.inv[id_])) <= price):
				self.inv[id_] = self.inv[id_] - amount
				market.commodities[id_].price = price #the price is the last traded price
				return TRADE_SUCCESS
		else:
			return TRADE_REJECT_NOT_ENOUGH_INV
		return TRADE_REJECT
				
		





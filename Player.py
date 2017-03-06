

class Player():
	
	def __init__(self):
		self.name="Bartholomew"
		self.money=0
		self.gear=[]
		self.location="Valley"

if __name__ == "__main__":
	print("Player main")
	p = Player()
	dir(p)
	print(p.name) 
	print("Money: " + str(p.money))
	print(p.location)
	

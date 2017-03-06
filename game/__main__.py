#!/usr/local/venv/alpinism/bin/python3

from Player import Player 
from Location import Location



def go():
	p=Player()
	print(p.name)
	p.name="Fredfred"
	print(p.name)
	
	loco = Location()
	print(loco.name)

if __name__=="__main__":
	print("main.py")
	go()

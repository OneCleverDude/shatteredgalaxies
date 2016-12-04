#
#  StarSystem Creation
#	Python 3 project
#	First python coding attempt
#
import random
import json

def spectralclass(argument):
		# Updated to the table in the VBAM Galaxies Google Doc
		spectralclass = {
			2: "Class O Extremely Bright Blue",
			3: "Class B Bright Blue",
			4: "Class A Blue-White",
			5: "Class F White",
			6: "Class G Yellow",
			7: "Class K Orange",
			8: "Class M Red",
			9: "Class M Red",
			10: "Class M Red",
			11: "Class T Brown",
			12: "Class D White",
		}
		return spectralclass.get(argument, "Sleepy Dwarf")
def luminosity(argument):
	# Updated to the VBAM Galaxies Ruleset.
	if (argument<12):
		s = (random.randint(1,6)+random.randint(1,6));
	if (argument>11):
		s = 13;	
	luminosity = {
		2: "Class I Supergiant",
		3: "Class II Bright Giant",
		4: "Class III Giant",
		5: "Class IV Subgiant",
		6: "Class V Main Sequence",
		7: "Class V Main Sequence",
		8: "Class V Main Sequence",
		9: "Class V Main Sequence",
		10: "Class V Main Sequence",
		11: "Class VI Subdwarf",
		12: "Class VI Subdwarf",
		13: "Class VII White Dwarf",
	}
	return luminosity.get(s, "white hole")
def stellarsystem():
	r=(random.randint(1,6)+random.randint(1,6)-7)
	r = r+1 
	# This (r=r+1) is  because the rules describe this roll 
	# to be how many companion stars there might be.
	# but I need to know how many stars there are.
	if (r<1):
		r=1
	if (r<1):
		stellartype = "black hole"
	if (r==1):
		stellartype = "single star"
	if (r==2):
		stellartype = "binary star"
	if (r==3):
		stellartype = "trinary star"
	if (r==4):
		stellartype = "quaternary star"
	if (r==5):
		stellartype = "quinternary star"
	if (r>5):
		stellartype = "sextenary star"
	return stellartype
def numofstars(argument):
	numberofstars = {
		"black hole": 0,
		"single star": 1,
		"binary star": 2,
		"trinary star": 3,
		"quaternary star": 4,
		"quinternary star": 5,
		"sextenary star": 6,
	}
	return numberofstars.get(argument, 0)
def systemimportancelevel(argument):
	# Brings in the 2d6 Roll from Spectral and then we apply the modifier.
	# Importantance Modifier by Spectral class 
	if (argument==2):
		s = -6  #Class O
	if (argument==3):
		s = -4	#Class B 
	if (argument==4):
		s = -2 	# Class A
	if (argument==5):
		s = 1 #Class F
	if (argument==6):
		s = 2	#Class G Yellow
	if (argument==7):
		s = 0	#Class K Orange
	if (argument>7 and argument<11):
		s = -1	#class M Red
	if (argument==11):
		s = -5	#Class T Brown
	if (argument==12):
		s = -3	#class D White Dwarf 
	s = (s + (random.randint(1,6)+random.randint(1,6)));
	if s < 2:
		s=2
	if s > 12:
		s=12
	return s
def systemimportance(argument):
	# Updated to the VBAM Galaxies Ruleset.
	systemimportance = {
		2: "Unimportant",
		3: "Unimportant",
		4: "Unimportant",
		5: "Unimportant",
		6: "Minor",
		7: "Minor",
		8: "Minor",
		9: "Minor",
		10: "Major",
		11: "Major",
		12: "Major",
	}
	return systemimportance.get(argument, "BespinCity")

def starinnerplanets(argument):
	# Brings in the 2d6 Roll from Spectral and then we apply the modifier.
	# Importantance Modifier by Spectral class 
	if (argument<4):
		s = 0
	if (argument>3 and argument<7):
		s = 1
	if (argument>6 and argument<10):
		s = 2
	if (argument>9 and argument<12):
		s = 3
	if (argument>11):
		s = 4
	return s	
def starmiddleplanets(argument):
	# Brings in the 2d6 Roll from Spectral and then we apply the modifier.
	# Importantance Modifier by Spectral class 
	if (argument<3):
		s = 0
	if (argument>2 and argument<6):
		s = 1
	if (argument>5 and argument<9):
		s = 2
	if (argument>8):
		s = 3
	return s	
def starouterplanets(argument):
	# Brings in the 2d6 Roll from Spectral and then we apply the modifier.
	# Importantance Modifier by Spectral class 
	if (argument<5):
		s = 1
	if (argument>4 and argument<8):
		s = 2
	if (argument>7):
		s = 3
	return s	
	
class planet():
	def __init__(self,name,starname,zone):
		# OLD: rawweight = [0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,3,4,5,6]
		# OLD: bioweight = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,3,4]
		innerzone = ["Asteroid Belt", "Gas Giant", "Hothouse", "Hothouse", "Dead", "Dead", "Superterrestrial", "Garden"]
		middlezone = ["Asteroid Belt", "Gas Giant", "Gas Giant", "Gas Giant", "Dead", "Dead", "Dead", "Barren", "Barren"]
		outerzone = ["Asteroid Belt", "Gas Giant", "Gas Giant", "Gas Giant", "Gas Giant", "Gas Giant", "Gas Giant", "Dead", "Dead", "Dead"]
		#  TODO: Add Moons
		self.planetName = name
		self.starName = starname
		planettype = ""
		if (zone=="inner"):
			planettype = (random.choice(innerzone))
		if (zone=="middle"):
			planettype = (random.choice(middlezone))
		if (zone=="outer"):
			planettype = (random.choice(outerzone))
		self.zone = zone 
		self.planettype = planettype 
		if (planettype == "Asteroid Belt"):
			self.planetSize = 2
			self.planetBio = 0
			self.planetRaw = 1
		if (planettype == "Gas Giant"):
			self.planetSize = 4
			self.planetBio = 0
			self.planetRaw = 1
		if (planettype == "Hothouse"):
			self.planetSize = 2
			self.planetBio = 0
			self.planetRaw = 2
		if (planettype == "Superterrestrial"):
			self.planetSize = 6
			self.planetBio = 1
			self.planetRaw = 2
		if (planettype == "Dead"):
			self.planetSize = 4
			self.planetBio = 0
			self.planetRaw = 1
		if (planettype == "Barren"):
			self.planetSize = 6
			self.planetBio = 1
			self.planetRaw = 2
		if (planettype == "Garden"):
			self.planetSize = 8
			self.planetBio = 3
			self.planetRaw = 4
		# OLD: self.planetSize = (random.randint(1,4))
		# OLD: self.planetBio = (random.choice(bioweight))
		# OLD: self.planetRaw = (random.choice(rawweight))
	def detailedPlanet(self):
		return self.zone + ": " + self.planetName + "(" + self.planettype + ") size: " + str(self.planetSize) + ", BIO: " + str(self.planetBio) + ", RAW: " + str(self.planetRaw)
	
class star():
	def __init__(self,name,systemname):
		self.starName = name
		self.starSystemName = systemname
		#
		# Star generation now follows the VBAM Galaxies ruleset on Google Docs.
		#
		# Star Spectral Class
		# Roll 2d6 for Spectral class.
		r=(random.randint(1,6)+random.randint(1,6));
		# assign starspectral values
		self.starSpectral  = spectralclass(r);
		self.starLuminosity = luminosity(r);
		self.systemimportancelevel = systemimportancelevel(r);
		self.systemimportance = systemimportance(self.systemimportancelevel)
		self.numofinnerplanets = starinnerplanets(self.systemimportancelevel);
		self.numofmiddleplanets =starmiddleplanets(self.systemimportancelevel);
		self.numofouterplanets = starouterplanets(self.systemimportancelevel);
		self.planets = [];
	def populateStar(self):
		x = self.numofinnerplanets
		for i in range(x):
			self.planets.append(planet("planet",self.starName,"inner"))
		x = self.numofmiddleplanets
		for i in range(x):
			self.planets.append(planet("planet",self.starName,"middle"))
		x = self.numofouterplanets
		for i in range(x):
			self.planets.append(planet("planet",self.starName,"outer"))
	def add_planet(self,planetname):
		self.planets.append(planet("planet",self.starName,zone))
	def detailedStar(self):
		returntxt = self.starSystemName + " " + self.starName + ", a " + self.starSpectral + " " +self.starLuminosity 
		returntxt = returntxt + " (" + self.systemimportance + ")"
		if (self.numofinnerplanets+self.numofmiddleplanets+self.numofouterplanets > 1):
			returntxt = returntxt + " with " + str(self.numofinnerplanets+self.numofmiddleplanets+self.numofouterplanets) + " planets."
		if (self.numofinnerplanets+self.numofmiddleplanets+self.numofouterplanets==1):
			returntxt = returntxt + " with a planet."
		if (self.numofinnerplanets+self.numofmiddleplanets+self.numofouterplanets<1):
			returntxt = returntxt + ", it is planetless."
		return returntxt
	
class starSystem():
	def __init__(self,name):
		self.starSystemName = name
		self.stellartype = stellarsystem()
		self.numofstars = numofstars(self.stellartype)	
		self.coord_x = random.randint(1,500);
		self.coord_y = random.randint(1,500);
		self.coord_z = random.randint(1,20);
		self.stars = [];
		possiblejumps = [2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,5,5,6,6,7]
		jumppoints = (random.choice(possiblejumps))
		jumppoints = (jumppoints-self.numofstars)
		if (jumppoints<1):
			jumppoints=1
		if (jumppoints>6):
			jumppoints=6
		self.numofJumps = jumppoints
	def add_star(self,starname):
		self.stars.append(star(starname,self.starSystemName))
	def populateSystem(self):
		x = self.numofstars
		for i in range(x):
			if (i==6):
				self.stars.append(star("eta",self.starSystemName))
			if (i==5):
				self.stars.append(star("zeta",self.starSystemName))
			if (i==4):
				self.stars.append(star("epsilon",self.starSystemName))
			if (i==3):
				self.stars.append(star("delta",self.starSystemName))
			if (i==2):
				self.stars.append(star("gamma",self.starSystemName))
			if (i==1):
				self.stars.append(star("beta",self.starSystemName))
			if (i==0):
				self.stars.append(star("prime",self.starSystemName))
			self.stars[(i)].populateStar()
	def detailedStarSystem(self):
		x = self.numofstars
		systemDetails=self.starSystemName + " is a " + self.stellartype + " system "
		systemDetails=systemDetails + "located at (" + str(self.coord_x) + "," + str(self.coord_y) + ","+ str(self.coord_z) +") "
		systemDetails=systemDetails + "with " + str(self.numofJumps) + " jumppoints.\n" 
		while (x > 0):
			systemDetails = systemDetails + self.stars[x-1].detailedStar() + "\n"
			y=self.stars[x-1].numofinnerplanets+self.stars[x-1].numofmiddleplanets+self.stars[x-1].numofouterplanets
			while (y > 0):
				systemDetails = systemDetails + "   " + self.stars[x-1].planets[y-1].detailedPlanet() + "\n"
				y=y-1
			x=x-1
		return systemDetails

def buildStarCluster():
	n = int(input('How many star systems?" '))
	systempicks = ['Aldbaran','Andromeda','Capella','Centauri','Cerberus','Draconis','Gallus','Leo','Malus','Nihal','Orion','Rana']
	for i in range(n):
		demostarsystem = starSystem(random.choice(systempicks));
		starSystem.populateSystem(demostarsystem);
		print(demostarsystem.detailedStarSystem());
		
def main():
	buildStarCluster();


if __name__ == "__main__":
	main()
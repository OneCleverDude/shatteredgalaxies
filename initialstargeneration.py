#
#  StarSystem Creation
#	Python 3 project
#	First python coding attempt
#
import random
import json

def spectralclass(argument):
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
			11: "Class D White",
			12: "Class D White",
		}
		return spectralclass.get(argument, "Brown Dwarf")
def luminosity(argument):
	if (argument>10):
		s = 1
	if ((argument<11) and (argument >5)):
		s = (random.randint(1,6)+random.randint(1,6));
	if (argument<6):
		s = ((random.randint(1,6)+random.randint(1,6)) + 6-argument);
	if (s<3):
		s = 3
	if (s>12):
		s= 12
	luminosity = {
		2: "subdwarf",
		3: "subdwarf",
		4: "dwarf",
		5: "dwarf",
		6: "dwarf",
		7: "dwarf",
		8: "dwarf",
		9: "subgiant",
		10: "giant",
		11: "bright giant",
		12: "supergiant",
	}
	return luminosity.get(s, "white hole")
def stellarsystem():
	r=(random.randint(1,6)+random.randint(1,6));
	stellartype =str(r)
	if (r<3):
		stellartype = "black hole"
	if ((r>2) and (r <8)):
		stellartype = "single star"
	if ((r>7) and (r<11)):
		stellartype = "binary star"
	if (r>10):
		stellartype = "star cluster"
	return stellartype
def numofstars(argument):
	multi = (random.randint(3,6))
	numberofstars = {
		"black hole": 0,
		"single star": 1,
		"binary star": 2,
		"star cluster": 3,
	}
	return numberofstars.get(argument, 0)

class planet():
	def __init__(self,name,starname):
		rawweight = [0,0,0,0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,3,4,5,6]
		bioweight = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,3,4]
		self.planetName = name
		self.starName = starname
		self.planetSize = (random.randint(1,4))
		self.planetBio = (random.choice(bioweight))
		self.planetRaw = (random.choice(rawweight))
	def detailedPlanet(self):
		return self.planetName + "size: " + str(self.planetSize) + ", BIO: " + str(self.planetBio) + ", RAW: " + str(self.planetRaw)
	
class star():
	def __init__(self,name,systemname):
		self.starName = name
		self.starSystemName = systemname
		# Star Spectral Class
		r=(random.randint(1,6)+random.randint(1,6));
		# assign starspectral values
		self.starSpectral  = spectralclass(r);
		self.starLuminosity = luminosity(r);
		self.numofPlanets = random.randint(0,5);
		self.planets = [];
	def populateStar(self):
		x = self.numofPlanets
		for i in range(x):
			self.planets.append(planet("planet",self.starName))
	def add_planet(self,planetname):
		self.planets.append(planet("planet",self.starName))
	def detailedStar(self):
		returntxt = self.starSystemName + " " + self.starName + ", a " + self.starSpectral + " " +self.starLuminosity
		if (self.numofPlanets > 1):
			returntxt = returntxt + " with " + str(self.numofPlanets) + " planets."
		if (self.numofPlanets==1):
			returntxt = returntxt + " with a planet."
		if (self.numofPlanets<1):
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
			if (i>1):
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
			y=self.stars[x-1].numofPlanets
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
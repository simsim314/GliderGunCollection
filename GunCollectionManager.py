#Copy-Paste your gun into GunCollection.rle (collection of best guns p14-p1000) and run this script. 
#The script reads gun collection. Analyzes your gun. 
#Compares the best result and your gun - if yours better the script will replace the best by yours. 
#Updates for the latest GunCollection.rle: http://www.conwaylife.com/forums/viewtopic.php?f=2&t=1300&start=0
#Written By Michael Simkin 2014.
import golly as g 
import glob

'''Number Placement'''

snakeLineHor = g.parse("2obob2obo$ob2obob2o!")
snakeLineVer = g.transform(snakeLineHor, -3, 3, 0, 1, 1, 0)

figure8 = [snakeLineVer, g.transform(snakeLineVer, 0, 13),  snakeLineHor, g.transform(snakeLineHor, 0, 13), g.transform(snakeLineHor, 0, 26), g.transform(snakeLineVer, 13, 0), g.transform(snakeLineVer, 13, 13)]

def PlaceDigit(digit, x = 0, y = 0):
	digitIdx = [[0,1,2,4,5,6], [5,6],[1,2,3,4,5],[2,3,4,5,6],[0,3,5,6],[0,2,3,4,6],[0,1,2,3,4,6],[2,5,6],[0,1,2,3,4,5,6],[0,2,3,4,5,6]]
	
	if digit >= 0 and digit <= 9:
		for idx  in digitIdx[digit]:
			g.putcells(figure8[idx], x, y)
def NumDigit(num):
	if num < 10: 
		return 1 
	else: 
		return 1 + NumDigit(int((num - (num % 10))/10))
		
def PlaceNumber(number, x = 0, y = 0):
	if number < 0: 
		g.putcells(figure8[3], x, y)
		PlaceNumber(-number, x, y)
		return
	  
	curNum = number
	d = 20 * NumDigit(number)
	
	while True:
		PlaceDigit(curNum%10, x + d, y)
		curNum = (curNum - curNum%10) / 10 
		
		if curNum == 0:
			return 
		
		d -= 20


'''Code starts here''' 

gld = g.parse("bo$2bo$3o!")		
		
def PeriodCalculator():
	
	g.setbase(8)
	g.setstep(3)
	g.step()
	g.step()
	g.step()
	g.step()
	
	cells = g.getrect()
	
	rect = g.getrect()
	cells = g.getcells(rect)
	
	for i in xrange(0, 10000):
		g.run(1)
		if str(g.getcells(rect)) == str(cells):
			#g.show(str(i + 1))
			#g.reset
			return i + 1
	
	return -1
	
def GunsReader():
	
	result = [] 
	
	for i in xrange(0, 10000):
		cells = g.getcells([0, i * 650, 500, 550])
		
		if len(cells) == 0:
			return result 
		
		g.select([-200, i * 650 - 10, 800, 550])
		g.clear(0)
		
		result.append(cells)
	

def GunPlacer(gunCollection):

	g.new("")
	
	for i in xrange(0, len(gunCollection)):
		g.putcells(gunCollection[i], 0, 0);
		PlaceNumber(i + 14, -150, i * 650)

def EdgeGlider():
	
	for i in xrange(0, 4):
		rect = g.getrect()
		
		x0 = rect[0] + rect[2] - 3
		y0 = rect[1] + rect[3] - 3
		
		gldFound = True
		
		for j in xrange(0, len(gld), 2):
			if g.getcell(x0 + gld[j], y0 + gld[j + 1]) == 0:
				gldFound = False
				break
		
		if gldFound:
			return g.getcells([x0, y0, 3, 3])
			
		g.run(1)
	
	return -1
	
def Erase(glider):
	for j in xrange(0, len(glider), 2):
		g.setcell(glider[j], glider[j + 1], 0)

def DevolveGlider(glider, delta):	
	return g.evolve(g.transform(glider, -delta, -delta), 3 * delta)

def PerformDelete(glider, gunPeriod):

	initCells = g.getcells(g.getrect())
	
	for j in xrange(0, len(glider), 2):
		if g.getcell(glider[j], glider[j + 1]) != 1:
			return False
	
	Erase(glider)
	rect = g.getrect()
	cells = g.getcells(rect)
	g.run(gunPeriod)
	
	if str(g.getcells(rect)) == str(cells):
		g.new("")
		g.putcells(cells)
		return True
	else:
		g.new("")
		g.putcells(initCells)
		return False

def AppendBox(maxBox, rect):

	if maxBox == []:
		return [rect[0], rect[1], rect[0] + rect[2] - 1, rect[1] + rect[3] - 1]
		
	if maxBox[0] > rect[0]:
		maxBox[0] = rect[0]
	
	if maxBox[1] > rect[1]:
		maxBox[1] = rect[1]
		
	if maxBox[2] < rect[0] + rect[2] - 1:
		maxBox[2] = rect[0] + rect[2] - 1
	
	if maxBox[3] < rect[1] + rect[3] - 1:
		maxBox[3] = rect[1] + rect[3] - 1
	
	return maxBox
	
def BoxValue(box):
	return (box[3] - box[1]) *  (box[2] - box[0])


def GunArea(cells, curGunPeriod):

	maxBox = []
	minpop = -100000
	
	for i in xrange(0, curGunPeriod, 4):
		
		g.new(str(i))
		g.putcells(g.evolve(cells, i))
		
		g.setbase(8)
		g.setstep(3)
		g.step()
		g.step()
		
		edgeGlider = EdgeGlider()

		while PerformDelete(edgeGlider, curGunPeriod):
			edgeGlider = DevolveGlider(edgeGlider, curGunPeriod)
		
		for j in xrange(0, 4):
		
			if g.getpop() > minpop:
				maxpop = g.getpop()
				maxpopgun = g.getcells(g.getrect())
				
			maxBox = AppendBox(maxBox, g.getrect())
			g.run(1)
		
	return [BoxValue(maxBox), maxpopgun, maxBox]
	
g.show("Reading guns into memory...")
g.update()
guns = GunsReader()
cells = g.getcells(g.getrect())

curGunPeriod = PeriodCalculator()

g.show("Calculating Period...")
g.update()

if curGunPeriod == -1:
	note("Failed to find gun period")
	g.exit("No gun found")

edgeGlider = EdgeGlider()

if edgeGlider == -1:
	g.note("Please orient the gun properly")
	g.exit("No glider found in bottom right corner")


g.show("searching box for your gun...")
g.update()

valueGun = GunArea(cells, curGunPeriod)


g.show("searching box for known gun...")
g.update()

dbValue =  GunArea(guns[curGunPeriod - 14], curGunPeriod)

if dbValue[0] > valueGun[0]:
	
	g.show("Success! Placing the gun array with your gun")
	g.update()

	g.new("")
	g.putcells(valueGun[1])
	rect = g.getrect()
	
	g.new("")
	g.putcells(cells, -rect[0], -rect[1] + 650 * (curGunPeriod - 14))
	cells = g.getcells(g.getrect())
	guns[curGunPeriod - 14] = cells
	
	GunPlacer(guns)
	g.setpos("0", str(650 * (curGunPeriod - 14)))
	g.setmag(-1)
	g.note("Congrats! You've found a better gun! \n  You gun value = {0}, The best known value = {1}".format(valueGun[0], dbValue[0]))
	g.exit("Please save the file, and post it as attachemnt on the forum")
else:
	g.new("")
	g.putcells(valueGun[1])
	g.note("This is not a better gun :( \n You gun value = {0}, The best value = {1}".format(valueGun[0], dbValue[0]))
	g.exit("Here is your gun")
	
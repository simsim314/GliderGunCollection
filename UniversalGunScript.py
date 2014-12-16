import golly as g
from glife import *
import random
from glife.text import *


class Glider:
   def __init__(self, x, y, dx, dy, gen, state):
      self.x = x
      self.y = y
      self.gen = gen
      self.state = state 
      self.dx = dx
      self.dy = dy
   def Place(self):
      gld = g.parse("3o$2bo$bo!", 0, 0, self.dx, 0, 0, self.dy)
      gld = g.evolve(gld, self.state)
      g.putcells(gld, self.x, self.y)
   def PlaceD(self, deltax, deltay):
      gld = g.parse("3o$2bo$bo!", 0, 0, self.dx, 0, 0, self.dy)
      gld = g.evolve(gld, self.state)
      g.putcells(gld, self.x + deltax, self.y + deltay)
      
   def Description(self):
      return " x {0} , y {1} , gen {2} , state {3}, dx {4}, dy {5} ".format(self.x, self.y, self.gen, self.state, self.dx, self.dy)
   
   def NextIter(self):
      if(self.state < 3):
         self.state += 1
      else:
         self.x += self.dx
         self.y -= self.dy
         self.state = 0
      self.gen += 1
      
   def PrevIter(self):
      if(self.state > 0):
         self.state -= 1
      else:
         self.x -= self.dx
         self.y += self.dy
         self.state = 3
      self.gen -= 1
      
   def NextIters(self, n):
      
      if n == 0: 
         return
      
      if n > 0: 
         for x in xrange(0, n):
            self.NextIter()
      
      if n < 0: 
         for x in xrange(0, -n):
            self.PrevIter()
            
   def BringToGeneration(self, n):
      self.NextIters(n - self.gen)
      
   def Copy(self):
      return Glider(self.x, self.y, self.dx, self.dy, self.gen, self.state)
      
class Snark:
   def __init__(self, glider, dist, isRight):
      self.glider = glider
      self.dist = dist
      self.isRight = isRight ^ (glider.dx == 1) ^ (glider.dy == 1)
      
      self.x = glider.x + dist * glider.dx 
      self.y = glider.y - dist * glider.dy 
      
      if self.isRight:
         self.outputGlider = Glider(self.x + 7 * self.glider.dx, self.y, self.glider.dx, -self.glider.dy, 32 + self.glider.gen + 4 * (dist - 1) + (4 - self.glider.state), 0)
      else: 
         self.outputGlider = Glider(self.x, self.y - 9 * self.glider.dy, -self.glider.dx, self.glider.dy, 40 + self.glider.gen + 4 * (dist - 1) + (4 - self.glider.state), 0)
         
   def Place(self):
      if self.isRight:
         mir = g.parse("5$8b2o3b2o$8b2o2bob3o$12bo4bo$8b4ob2o2bo$8bo2bobobob2o$11bobobobo$12b2obobo$16bo2$2b2o$3bo7b2o$3bobo5b2o$4b2o7$14b2o$14bo$15b3o$17bo!", -10, -20, 1, 0, 0, 1)
      else:
         mir = g.parse("14$22bo$4b2o14b5o$5bo13bo5bo$5bobo12b3o2bo$6b2o15bob2o$20b4o2bo$15b2o3bo3b2o$15b2o4b3o$23bo$23bob2o$22b2ob2o3$14b2o$14bo$15b3o$17bo!", -10, -20, 1, 0, 0, 1)
         
      mir = g.transform(mir, 0, 0, self.glider.dx, 0, 0, self.glider.dy)
      g.putcells(mir, self.x, self.y) 

class StaticMirror:
   def __init__(self, glider, dist, isRight):
      self.glider = glider
      self.dist = dist
      self.isRight = isRight ^ (glider.dx == 1) ^ (glider.dy == 1)
      
      self.x = glider.x + dist * glider.dx 
      self.y = glider.y - dist * glider.dy 
      
      if self.isRight:
         self.outputGlider = Glider(self.x + 78 * self.glider.dx, self.y - 10 * self.glider.dy, self.glider.dx, -self.glider.dy, 359 + self.glider.gen + 4 * (dist - 1) + (4 - self.glider.state), 0)
      else: 
         self.outputGlider = Glider(self.x + 10 * self.glider.dx, self.y - 80 * self.glider.dy, -self.glider.dx, self.glider.dy, 351 + self.glider.gen + 4 * (dist - 1) + (4 - self.glider.state), 0)
         
   def Place(self):
      if self.isRight:
         mir = g.parse("12$69b2o$69b2o9$84b2o$84b2o10$64b2o$65bo$62b3o$13b2o47bo$14bo$14bobo$15b2o8$18bo34bo$16b3o32b3o$15bo34bo$15b2o33b2o20b2o$5b2o56b2o7b2o$6bo57bo$6bobo55bobo$7b2o4b2o44b2o4b2o$12bo2bo44bo20b2o$13b2o45bobo18bo$25b2o34b2o16bobo$25b2o52b2o8$11b2o3b2o32b2o$12bo3bo20b2o11b2o$9b3o5b3o18bo$9bo9bo15b3o35b2o$35bo37b2o2b2o$77bobo$79bo$79b2o5$48b2o$49bo$46b3o$46bo!", -10, -60, 1, 0, 0, 1)
      else:
         mir = g.parse("7$58b2o$58b2o2$26bo$24b3o$8bo14bo$8b3o12b2o$11bo$10b2o3$11b2o$11b2o17b2o$30b2o2$68b2o$68b2o3$27b2o$27bo19b2o$28b3o15bobo$30bo15bo$24b2o19b2o$24bo$25b3o$27bo6$33b2o$33bo$14b2o15bobo$14b2o15b2o$2b2o$bobo$bo$2o8$13b2o$12bobo$12bo$11b2o9$23b2o$23b2o6$12b2o$13bo19b2o$13bobo17bo$14b2o15bobo8b2o$26bo4b2o9bo$25bobo15b3o$25bobo17bo$14b2o10bo$13bobo$13bo$12b2o$27b2o$27bo$28b3o$30bo!", -20, -80, 1, 0, 0, 1)
         
      mir = g.transform(mir, 0, 0, self.glider.dx, 0, 0, self.glider.dy)
      g.putcells(mir, self.x, self.y) 

class ColorSwitch:
   def __init__(self, glider, dist):
      self.glider = glider
      self.dist = dist
      
      self.x = glider.x + dist * glider.dx 
      self.y = glider.y - dist * glider.dy 
      
      self.outputGlider = Glider(self.x + 79 * self.glider.dx, self.y - 50 * self.glider.dy, self.glider.dx, self.glider.dy, 368 + self.glider.gen + 4 * (dist - 1) + (4 - self.glider.state), 0)
         
   def Place(self):
      mir = g.parse("5$66b2o$66b2o11$80b2o$80bobo$82bo$82b2o6$61b2o$62bo$59b3o$59bo3$13b2o$14bo$14bobo$15b2o61b2o$78bo$79b3o$81bo2$15bo34bo$13b3o32b3o$12bo34bo$12b2o33b2o20b2o$2b2o56b2o7b2o$3bo57bo$3bobo55bobo$4b2o4b2o44b2o4b2o$9bo2bo44bo20b2o$10b2o45bobo18bo$22b2o34b2o16bobo$22b2o52b2o8$8b2o3b2o32b2o$9bo3bo20b2o11b2o$6b3o5b3o18bo$6bo9bo15b3o35b2o$32bo37b2o2b2o$74bobo$76bo$2b2o72b2o$2bobo$4bo$4b2o2$45b2o$46bo$43b3o$43bo!", 0, -60, 1, 0, 0, 1)
      mir = g.transform(mir, 0, 0, self.glider.dx, 0, 0, self.glider.dy)
      g.putcells(mir, self.x, self.y) 
      
class UniversalGliderGun():
   def __init__(self, x, y, period):
      self.x = x
      self.y = y
      self.period = period
      self.numBits = 3
   
   def PlaceStart(self, turnOnBit): 
      startPart = g.parse("6$44bo$43bobo$43bobo$44bo18$64b2o$65bo$65bobo$66b2o5$63b2o$64bo$64bobo$65b2o18$104b2o3b2o$102b3obo2b2o$60b2o39bo4bo$59bobo39bo2b2ob4o$59bo25b2o13b2obobobo2bo$58b2o25bo15bobobobo$66b2o15bobo15bobob2o$66b2o15b2o17bo2$115b2o$106b2o7bo$106b2o5bobo$113b2o7$65b2o36b2o$64bobo37bo$64bo36b3o$63b2o36bo2$103b2o3b2o$103b2o2bob3o$107bo4bo$103b4ob2o2bo$103bo2bobobob2o$106bobobobo$107b2obobo$75b2o34bo$75b2o$87b2o8b2o$87bobo8bo7b2o$89bo8bobo5b2o$89b2o8b2o2$64b2o$65bo19b2o$65bobo17bo56bo$66b2o15bobo38b2o14b5o$70b2o6bo4b2o40bo13bo5bo$69bo2bo4bobo29b2o14bobo12b3o2bo$70b2o5bobo29bo16b2o15bob2o$66b2o10bo31b3o27b4o2bo$65bobo44bo22b2o3bo3b2o$65bo69b2o4b3o$64b2o77bo$79b2o62bob2o$79bo62b2ob2o$80b3o$82bo$98b2o34b2o$99bo34bo$99bobo33b3o$100b2o2b2o31bo5bo$104b2o35b3o15bo9bo$140bo18b3o5b3o$127b2o11b2o20bo3bo$127b2o32b2o3b2o8$40bo57b2o52b2o$38b5o14b2o38bobo16b2o34b2o$37bo5bo13bo39bo18bobo45b2o$37bo2b3o12bobo38b2o20bo44bo2bo$36b2obo15b2o55b2o4b2o44b2o4b2o$36bo2b4o69bobo55bobo$37b2o3bo3b2o66bo57bo$39b3o4b2o57b2o7b2o56b2o$39bo65b2o20b2o33b2o$36b2obo88bo34bo$36b2ob2o84b3o32b3o$125bo34bo2$47b2o$48bo$45b3o47b2o$45bo50bo$96bobo$97b2o2$49bo$47b3o$46bo69bo$46b2o66b3o$113bo$113b2o5$36b2o$35bobo5b2o47b2o$35bo7b2o48bo$34b2o57bobo$94b2o$48bo39bo$44b2obobo38b3o$43bobobobo41bo$40bo2bobobob2o39b2o$40b4ob2o2bo$44bo4bo$40b2o2bob3o$40b2o3b2o3$100b2o6b2o$93b2o5bobo5b2o$93b2o7bo$102b2o2$89bo$88bobob2o$88bobobobo$87b2obobobo2bo$88bo2b2ob4o$88bo4bo$89b3obo2b2o$91b2o3b2o26$238bo$236b3o$235bo$235b2o7$225b2o$224bobo5b2o$224bo7b2o$223b2o2$237bo$233b2obobo$232bobobobo$229bo2bobobob2o$229b4ob2o2bo$233bo4bo$229b2o2bob3o$229b2o3b2o!", 0, -60, 1, 0, 0, 1)      
      g.putcells(startPart, self.x, self.y) 
      
      if turnOnBit:
         blocker = g.parse("$b2o$bo$2b3o$4bo!", 60,-43, 1, 0, 0, 1)
         g.putcells(blocker, self.x, self.y) 
   
   def PlaceEnd(self, turnOnBit, numBits): 
      startPart = g.parse("121bo$81b2o38b3o$82bo41bo14bo$82bobo38b2o12b3o$83b2o2b2o47bo$87b2o47b2o3$135b2o$116b2o17b2o$116b2o6$81b2o36b2o$80bobo16b2o19bo$80bo18bobo15b3o$79b2o20bo15bo$95b2o4b2o19b2o$95bobo25bo$97bo22b3o$88b2o7b2o21bo$88b2o7$78b2o$79bo$79bobo$80b2o$96bo$94b3o$93bo$93b2o28b2o$122bobo$122bo29b2o$121b2o29bobo$61b2o91bo$38bo23bo64b2o25b2o$36b3o23bobo61bobo4b2o$35bo27b2o61bo7bo$35b2o88b2o4b3o$131bo$12bo42bo83b2o$12b3o38b3o44b2o36bobo$5bo9bo36bo47b2o36bo$5b3o6b2o23b2o11b2o83b2o$8bo30b2o$7b2o$95b2o$95b2o$99b2o54b2o$99b2o54bobo$157bo$157b2o$64b2o27b2o$3bo23b2o35b2o11b2o14b2o$2bobo22bo49bo$3bo14b2o8b3o47b3o$18bo11bo49bo$19b3o$21bo125b2o$138b2o7b2o$5b2o32b2o98bo$4bobo33bo98bobo$4bo32b3o100b2o$3b2o32bo85bo32b2o$19b2o100b3o32bo$19bobo52b2o21bo22bo33bobo$21bo52b2o21b3o20b2o32b2o$12b2o7b2o40b2o35bo$12b2o50bo34b2o38bo$64bobo72b3o$65b2o63bo11bo$130b3o8b2o14bo$133bo22bobo$132b2o23bo2$2b2o58b2o25b2o$3bo59bo25b2o$3bobo57bobo$4b2o58b2o3$77b2o$77bobo6b2o32b2o$22b2o55bo6bo20b2o11b2o23b2o23bo$22bo56b2o6b3o18bo36bo22b3o$20bobo66bo15b3o38b3o18bo$20b2o83bo42bo18b2o2$124b2o$125bo49b2ob2o$75b2o45b3o51bob2o$75bobo44bo53bo$77bo90b2o4b3o$77b2o89b2o3bo3b2o$173b4o2bo$159b2o15bob2o$158bobo12b3o2bo$158bo13bo5bo$2b2o15b2o38b2o96b2o14b5o$bobo15b2o37bobo114bo$bo25b2o29bo25b2o129b2o$2o25bo29b2o25bo131bo$25bobo37b2o15bobo131bobo$25b2o38b2o15b2o133b2o$242b2o$242b2o2$210bo$208b3o$192bo14bo$192b3o12b2o$195bo$194b2o3$64b2o129b2o$63bobo129b2o17b2o$63bo150b2o$62b2o$252b2o$252b2o3$20b2o58b2o129b2o$20bobo57bobo128bo19b2o$22bo59bo40bo88b3o15bobo$22b2o58b2o39b3o88bo15bo$126bo81b2o19b2o$125b2o81bo$209b3o$18b2o191bo$18bobo93b2ob2o$20bo93b2obo$20b2o50b2o43bo$63b2o7b2o43b3o4b2o$64bo50b2o3bo3b2o$64bobo47bo2b4o96b2o$65b2o47b2obo15b2o82bo$48bo32b2o32bo2b3o12bobo62b2o15bobo$46b3o32bo33bo5bo13bo62b2o15b2o$22bo22bo33bobo34b5o14b2o$22b3o20b2o32b2o37bo$25bo$24b2o38bo$64b3o$55bo11bo$55b3o8b2o14bo$58bo22bobo$57b2o23bo3$197b2o$196bobo$196bo$195b2o2$77b2o$45b2o30bo$32b2o11b2o23b2o6b3o$33bo36bo9bo$30b3o38b3o82b2o$30bo42bo82b2o2$49b2o156b2o$50bo156b2o$47b3o93b2o$47bo96bo$144bobo$145b2o2$196b2o$197bo19b2o5b2o$163b2o32bobo17bo6bo$163b2o15bo17b2o15bobo7b3o$178b3o29bo4b2o10bo$145b2o30bo31bobo$144bobo30b2o30bobo$144bo53b2o10bo$143b2o52bobo$197bo$196b2o$211b2o$154b2o55bo$153bobo56b3o$153bo60bo$152b2o5$174b2o$174bobo$176bo$176b2o17$215b2o$216bo$216bobo$217b2o$242b2o$242b2o2$210bo$208b3o$192bo14bo$192b3o12b2o$195bo$194b2o3$195b2o$195b2o17b2o$214b2o2$252b2o$252b2o3$211b2o$211bo19b2o$212b3o15bobo$214bo15bo$208b2o19b2o$208bo$209b3o$211bo6$217b2o$217bo$198b2o15bobo$198b2o15b2o12$197b2o$196bobo$196bo$195b2o9$207b2o$207b2o6$196b2o$197bo19b2o5b2o$197bobo17bo6bo$198b2o15bobo7b3o$210bo4b2o10bo$209bobo$209bobo$198b2o10bo$197bobo$197bo$196b2o$211b2o$211bo$212b3o$214bo!", 1, -108, 1, 0, 0, 1)      
      g.putcells(startPart, self.x + 75 * numBits, self.y - numBits * 75) 
      
      if turnOnBit:
         blocker = g.parse("$b2o$bo$2b3o$4bo!", 60,-43, 1, 0, 0, 1)
         g.putcells(blocker, self.x + 75 * numBits, self.y - numBits * 75) 
   
   def PlaceBitStream(self, blocks): 
      d = 0
      
      for toBlock in blocks:
         bit = g.parse("87b2o$88bo$43bo44bobo$41b3o45b2o$40bo$40b2o2$17bo42bo$17b3o38b3o15bo$10bo9bo36bo18b3o6b2o$10b3o6b2o23b2o11b2o20bo6bo$13bo30b2o32b2o6bobo$12b2o73b2o5$75b2o$75b2o2$8bo23b2o$7bobo22bo$8bo14b2o8b3o$23bo11bo$24b3o55b2o$26bo56bo$80b3o6bo$10b2o32b2o34bo7bobo$9bobo33bo43bo$9bo32b3o$8b2o32bo$24b2o$24bobo52b2o$26bo52b2o$17b2o7b2o40b2o$17b2o50bo$69bobo$70b2o5$7b2o58b2o25b2o$8bo59bo25b2o$8bobo57bobo$9b2o58b2o3$82b2o$82bobo6b2o$27b2o55bo6bo$27bo56b2o6b3o$25bobo66bo$25b2o4$80b2o$80bobo$82bo$82b2o5$7b2o15b2o38b2o$6bobo15b2o37bobo$6bo25b2o29bo25b2o$5b2o25bo29b2o25bo$30bobo37b2o15bobo$30b2o38b2o15b2o5$12b2o$13bo$13bobo$14b2o4$69b2o$bo66bobo$b3o6b2o56bo$4bo6bo55b2o$3b2o6bobo$12b2o3$25b2o58b2o$25bobo57bobo$2o25bo59bo$2o25b2o58b2o4$23b2o$23bobo$7b2o16bo$8bo16b2o50b2o$5b3o6bo53b2o7b2o$5bo7bobo53bo$14bo54bobo$70b2o$53bo32b2o$51b3o32bo$4b2o21bo22bo33bobo$4b2o21b3o20b2o32b2o$30bo$29b2o38bo$69b3o$60bo11bo$60b3o8b2o14bo$63bo22bobo$62b2o23bo2$19b2o$19b2o5$7b2o73b2o$7bobo6b2o32b2o30bo$9bo6bo20b2o11b2o23b2o6b3o$9b2o6b3o18bo36bo9bo$19bo15b3o38b3o$35bo42bo2$54b2o$55bo$5b2o45b3o$5bobo44bo$7bo$7b2o!", 71, -142, 1, 0, 0, 1)      
         g.putcells(bit, self.x + d, self.y - d) 
         
         if toBlock: 
            blocker = g.parse("$b2o$bo$2b3o$4bo!", 60,-43, 1, 0, 0, 1)
            g.putcells(blocker,self.x + 75 + d, self.y - 75 - d) 
            
         d += 75
   def PlaceReflector(self): 
      blocker = g.parse("9b2o$10bo$10bobo$11b2o2b2o37bo$15b2o35b3o15bo9bo$51bo18b3o5b3o$38b2o11b2o20bo3bo$38b2o32b2o3b2o8$9b2o52b2o$8bobo16b2o34b2o$8bo18bobo45b2o$7b2o20bo44bo2bo$23b2o4b2o44b2o4b2o$23bobo55bobo$25bo57bo$16b2o7b2o56b2o$o15b2o20b2o33b2o$3o36bo34bo$3bo32b3o32b3o$2b2o32bo34bo6$71b2o$71bobo$73bo$73b2o2$27bo$25b3o$24bo$24b2o10$4b2o$4b2o9$19b2o$19b2o!", 263,-15, 1, 0, 0, 1)
      g.putcells(blocker, self.x - 112, self.y + 112) 
   
   def ZeroPeriodMod8(self, mod8Value): 
      if mod8Value == 0: 
         return 8248
      
      if mod8Value == 1:
         return 8281
      
      if mod8Value == 2:
         return 8642

      if mod8Value == 3:
         return 8115
      
      if mod8Value == 4:
         return 8212
      
      if mod8Value == 5:
         return 8045
      
      if mod8Value == 6:
         return 8414
      
      if mod8Value == 7:
         return 8559
   
   def HoldMechanismGliderPrepare(self, mod8Value):
      
      if mod8Value == 0:
      
         golly.select( [self.x +111 + 75,self.y-140 - 75,4,4] )
         golly.clear(0)
         gld = Glider(self.x +113 + 75,self.y -140 - 75, 1,1,0,0)
         snk = Snark(gld, 15, False)
         snk.Place()
         return snk.outputGlider
         
      if mod8Value == 1:
      
         golly.select( [self.x +111,self.y -140,4,4] )
         golly.clear(0)
         gld = Glider(self.x +113, self.y -140, 1,1,0,0)
         snk = Snark(gld, 15, False)
         snk.Place()
         return snk.outputGlider
         
      if mod8Value == 2:
         
         golly.select( [self.x +111 +  75,self.y-140 - 75,4,4] )
         golly.clear(0)
         gld = Glider(self.x +113 +  75, self.y-140 -  75, 1,1,0,0)
         snk = Snark(gld, 15, False)
         snk.Place()
         return snk.outputGlider
         
      if mod8Value == 3:

         golly.select( [self.x +111 + 75,self.y-140 - 75,4,4] )
         golly.clear(0)
         gld = Glider(self.x +113 + 75, self.y-140 - 75, 1,1,0,0)
         snk = Snark(gld, 15, False)
         snk.Place()
         return snk.outputGlider
         
      if mod8Value == 4:

         golly.select( [self.x +78,self.y-100,4,4] )
         golly.clear(0)
         gld = Glider(self.x +80, self.y-100, -1,1,0,0)
         return gld
         
         
      if mod8Value == 5:

         golly.select( [self.x +81,self.y-133,4,4] )
         golly.clear(0)
         gld = Glider(self.x +82,self.y -133, -1,1,0,0)
         return gld 
         
      if mod8Value == 6:
      
         golly.select( [self.x +111,self.y-140,4,4] )
         golly.clear(0)
         gld = Glider(self.x +113, self.y-140, 1,1,0,0)
         snk = Snark(gld, 15, False)
         snk.Place()
         return snk.outputGlider
      
      if mod8Value == 7:
      
         golly.select( [self.x +81,self.y-133,4,4] )
         golly.clear(0)
         gld = Glider(self.x +82, self.y-133, -1,1,0,0)
         return gld
   
   def SnarkSnake(self, Mod8Multiplier, gld):
   
      a = [0,-1, -1, -1, -1, -1, -1]
      
      if self.SnarkSnakeCalculationsNew(Mod8Multiplier, gld, [0], False) <= 0:
         return Mod8Multiplier
      
      i = 0 
      idx = 0 
      while  self.SnarkSnakeCalculationsNew(Mod8Multiplier, gld, a , False) > 0:
         i+= 1
         
         if i > 75 * (self.numBits - 1) - 40:
            idx += 1
            i = 0 
            
         a[idx] = i
         
      
      a[idx] -= 1
      
      return self.SnarkSnakeCalculationsNew(Mod8Multiplier, gld, a, True)

      '''
      bestDist = -1
      bestD = -1 
      
      if not self.SnarkSnakeCalculations(Mod8Multiplier, gld, 0, False):
         return Mod8Multiplier
      
      for d in xrange(0, 75 * (self.numBits - 1) - 40):
         val = self.SnarkSnakeCalculations(Mod8Multiplier, gld, d, False)
         if  val > bestDist:
            val = bestDist
            bestD = d
         
      return self.SnarkSnakeCalculations(Mod8Multiplier, gld, bestD, True)
      '''      
      
   def SnarkSnakeCalculations(self, Mod8Multiplier, gldIn, delta, toPlace):
      
      curDist = Mod8Multiplier
      
      gld = gldIn.Copy()
      
      i = 0 
      x = gld.x
      
      while True: 
         if curDist < 55 + (x - gld.x) + delta: 
            if toPlace: 
               return curDist   
            break
         
         if i == 0: 
            degrees = [(True, 22), (False, 15 + delta), (False, 15), (True, 17 + delta)]
         else: 
            degrees = [(True, 15), (False, 15 + delta), (False, 15), (True, 17 + delta)]
         for deg in degrees: 
            sn = Snark(gld, deg[1], deg[0])
            if toPlace:
               sn.Place()
            gld = sn.outputGlider
      
         curDist -= (26 + delta)
         i += 1
      
      return curDist
   
   def SnarkSnakeCalculationsNew(self, Mod8Multiplier, gldIn, delta, toPlace):
      
      curDist = Mod8Multiplier
      
      gld = gldIn.Copy()
      
      i = 0 
      x = gld.x
      
      for i in xrange(0, len(delta)):
         if delta[i] >= 0:
            if curDist < 75 + (x - gld.x) + delta[i]: 
               return -1
            
            if i == 0: 
               degrees = [(True, 25), (False, 15 + delta[i]), (False, 15), (True, 17 + delta[i])]
            else: 
               degrees = [(True, 15), (False, 15 + delta[i]), (False, 15), (True, 17 + delta[i])]
               
            for deg in degrees: 
               sn = Snark(gld, deg[1], deg[0])
               if toPlace:
                  sn.Place()
               gld = sn.outputGlider
         
            curDist -= (26 + delta[i])
            
      return curDist
      
   def PlaceHoldMechanism(self, period0):
      
      mod8Value = period0 % 8 
      Mod8Multiplier = (period0 - self.CalculateZeroPeriod(self.numBits, mod8Value)) / 8
      gld = self.HoldMechanismGliderPrepare(mod8Value)
      Mod8Multiplier = self.SnarkSnake(Mod8Multiplier, gld)
      
      if mod8Value == 0: 
      
         snk = Snark(gld, 15 + Mod8Multiplier, False)
         snk.Place()
         sw = ColorSwitch(snk.outputGlider, 10)
         sw.Place()
         snk = Snark(sw.outputGlider, 88 + 75, False)
         snk.Place()
         return 8248 + 8 * Mod8Multiplier
      
      if mod8Value == 1:
      
         snk = Snark(gld, 15 + Mod8Multiplier, False)
         snk.Place()
         snk = StaticMirror(snk.outputGlider, 122, False)
         snk.Place()
         return 8281 + 8 * Mod8Multiplier
      
      if mod8Value == 2:
         
         snk = StaticMirror(gld, 15 + Mod8Multiplier, False)
         snk.Place()
         sw = ColorSwitch(snk.outputGlider, 10)
         sw.Place()
         snk = StaticMirror(sw.outputGlider, 17 +75, False)
         snk.Place()
         return 8642 + 8 * Mod8Multiplier

      if mod8Value == 3:

         snk = Snark(gld, 15 + Mod8Multiplier, False)
         snk.Place()
         snk = StaticMirror(snk.outputGlider, 122 + 75, False)
         snk.Place()
         return 8115 + 8 * Mod8Multiplier
      
      if mod8Value == 4:

         snk = Snark(gld, 15 + Mod8Multiplier, False)
         snk.Place()
         sw = ColorSwitch(snk.outputGlider, 10)
         sw.Place()
         snk = Snark(sw.outputGlider, 32, False)
         snk.Place()
         return 8212 + 8 * Mod8Multiplier
      
      if mod8Value == 5:
      
         snk = Snark(gld, 15 + Mod8Multiplier, False)
         snk.Place()
         snk = Snark(snk.outputGlider, 124, False)
         snk.Place()
         return 8045 + 8 * Mod8Multiplier
      
      if mod8Value == 6:
      
         snk = Snark(gld, 15 + Mod8Multiplier, False)
         snk.Place()
         sw = ColorSwitch(snk.outputGlider, 10)
         sw.Place()
         snk = Snark(sw.outputGlider, 88, False)
         snk.Place()
         return 8414 + 8 * Mod8Multiplier
      
      if mod8Value == 7:
      
         snk = StaticMirror(gld, 30 + Mod8Multiplier, False)
         snk.Place()
         snk = StaticMirror(snk.outputGlider, 53, False)
         snk.Place()
         return 8559 + 8 * Mod8Multiplier
   
   
   def RotationPeriod(self, numBits):
      return 3415 + 1200 * (numBits - 3)
   
   def RotationPeriodHoldBack(self, numBits):
      return 1200 * (numBits - 3)
   
   def BitHoldBack(self, numBits): 
      return 932 * (numBits - 3)
   
   def CalculateZeroPeriod(self, numBits, periodMod8):
      return self.BitHoldBack(numBits) + self.ZeroPeriodMod8(periodMod8) + self.RotationPeriodHoldBack(numBits)
   
   def CalculateMaxPeriod(self, numBits, periodMod8):
      return self.CalculateZeroPeriod(numBits, periodMod8) + (2**numBits - 1) * self.RotationPeriod(numBits)
   
   def CalculateNumBits(self, period):
      
      while self.CalculateMaxPeriod(self.numBits, period%8) < period:
         self.numBits += 2
      
      return self.numBits
   
   def DoAllCalculations(self):
      period = self.period
      
      if period < self.ZeroPeriodMod8(period % 8):
         golly.exit("The period is too low")
      
      numBits = self.CalculateNumBits(period)
      
      rot = self.RotationPeriod(numBits)
      zero = self.CalculateZeroPeriod(numBits, (period - self.RotationPeriod(numBits)) % 8)

      zeroMultiplier = (zero - zero % rot) / rot
      periodMultipler = (period - period % rot) / rot
      multiplier = periodMultipler - zeroMultiplier - 10
      period -= multiplier * rot 
      
      while period >= self.CalculateZeroPeriod(numBits, period % 8):
         multiplier += 1
         period -= rot     
         
      bits = 2**numBits - multiplier
      
      endBit = bits < 2**(numBits - 1)
      
      if not endBit: 
         bits -= 2**(numBits - 1)
         
      startBit = bits % 2 == 0
      bits = (bits - bits%2) / 2
      
      middlebits = []
      
      for i in xrange(0, self.numBits - 2):
         middlebits.extend([bits % 2 == 0])
         bits = (bits - bits%2) / 2
      
      period0 = period  + rot
      
      #golly.show('{0}, {1}, {2}'.format(startBit, middlebits[0], endBit))
      return [startBit, middlebits, endBit, period0]
      
   def Place(self): 
      values = self.DoAllCalculations();
      self.PlaceStart(values[0])
      self.PlaceBitStream(values[1])
      self.PlaceEnd(values[2],self.numBits - 1)
      self.PlaceReflector()
      gld = Glider(self.x + 167, self.y + 63, -1,-1,0,0)
      gld.Place()
      self.PlaceHoldMechanism(values[3])
      
      periodText = make_text (str(self.period))
      g.putcells(periodText,self.x - 50, self.y + 200) 
     

gen = g.getstring("Enter Gun Period: ")

g.select([0,0,1,1])
g.clear(1)
g.clear(0)



gun = UniversalGliderGun(0,0,int(gen))
gun.Place()

'''
for x in xrange(0, 100):
   gun = UniversalGliderGun(0,2000 * x,17985 + 12289 *  x)
   gun.Place()
'''

g.fit() 
   
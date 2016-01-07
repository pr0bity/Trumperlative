# Trump superlative generator

import random

#---- Clauses ----#

# Intro
intro = ["", "And by the way... ", "", "Believe me: ", "", "As I have been saying... "] 

# Route a:
a0 = ["I am ", "I'm ", "I will be ", "I'll be ", "As of this moment, I am ", "I'm going to be ",] 

## Route a1
a1 = [["really ", "so ", "tremendously ", "incredibly ", "very ", "unbelievably "],
			["rich. ", "awesome. ", "healthy. ", "handsome. ", "good for women. ", "militaristic. "]]

## Route a2
a2 = [["the best ", "the most humble ", "the smartest ", "the most fantastic ", "the most successful ", "the greatest "],
		  ["president ", "person ", "negotiator ", "mind ", "leader ", "businessman "],
		  ["in the history of the United States.", "ever.", ".", "that God ever created." , "there is.", "in the world."]]

# Route b:
b = [["I'd ", "I would ", "we will ", "I'll ", "we'll ", "we are going to "],
		["hit ISIS ", "protect America ", "create jobs ", "build walls ", "win ", "fight back ", "serve our veterans " ],
		["so hard, ", "so much, ", "so easily, " , "with strength and stamina -- ", "with so much energy, ", "so fabulously," ],
		["your head would spin. ", "it will make a grand statement. ", "it will be unrivaled. " , "it'll be a home run! " , "it will be iconic. " ,"and that is 100 percent true. "]]

# Route c: in progress
#c = [["You know who cheats at golf? ", "I greatly respect ", "I'm very proud of ", "One of my best friends is ", "I'm not a fan of "
# Closing
conclusion = [ "I'll show you!", "", "And yes, it is my hair.", "", "It's high-priority.", " I'm very proud of it.", "", "", ""]

#------------------#


TrumpLative = ""

# Use a Trump opener
TrumpLative = TrumpLative + random.choice(intro)

# Pick a route
route = random.randrange(2)

if(route == 0):# Go with what Trump is
	TrumpLative = TrumpLative + random.choice(a0)

	# Flip another coin
	coin = random.randrange(2)
	if (coin == 0):
		for line in range(2):
			TrumpLative = TrumpLative + random.choice(a1[line])
	else:
		for line in range(3):
			TrumpLative = TrumpLative + random.choice(a2[line])

else:	# Go with what Trump will do
	for line in range(4):
		TrumpLative = TrumpLative + random.choice(b[line])

# Wrap it up
TrumpLative = TrumpLative + random.choice(conclusion)

print(TrumpLative)
return(TrumperLative)
 








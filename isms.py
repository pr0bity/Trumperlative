# Trump superlative generator

import random
from flask import Flask, request, url_for


#---- Clauses ----#

# Intro
intro = ["", "And by the way, ", "", "Believe me: ", "", "As I have been saying, "] 

# Route a:
a0 = ["I am ", "I'm ", "I will be ", "I'll be ", "As of this moment, I am ", "I'm going to be "] 

## Route a1
a1 = [["really ", "so ", "tremendously ", "incredibly ", "very much ", "unbelievably "],
			["rich ", "awesome ", "healthy ", "handsome ", "good for women ", "militaristic "]]

## Route a2
a2 = [["the best ", "the most humble ", "the smartest ", "the most fantastic ", "the most successful ", "the greatest "],
		  ["president ", "person ", "negotiator ", "mind ", "leader ", "businessman "],
		  ["in the history of the United States.", "ever.", ".", "that God ever created." , "there is.", "in the world."]]

# Route b:
b = [["I'd ", "I would ", "We will ", "I'll ", "We'll ", "We are going to "],
		["hit ISIS ", "protect America ", "create jobs ", "build walls ", "win ", "fight back " ],
		["so hard, ", "so much, ", "so easily, " , "with strength and stamina -- ", "with so much energy, ", " so fabulously," ],
		[" your head would spin.", " it will make a grand statement.", " it will be unrivaled." , " it'll be a home run!" , " it will be iconic." ," and that is 100 percent true."]]

# Closing
conclusion = [ " I'll show you!", "", " And yes, it is my hair.", "", " It's high-priority.", " I'm very proud of it."]

#------------------#

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

@app.route('/')
def main_page():
    return """
        <p>TRUMP SUPERLATIVE GENERATOR</p>
        <form method="POST" action="%s">
		<button type="submit"> The Donald says...</button>
		</form>
        """ % (url_for('generate_ism'),)

@app.route('/trumperlative', methods=['POST'])
def generate_ism():
	TrumpLative = ""

	# Use a Trump opener
	TrumpLative = TrumpLative + random.choice(intro)

	# Flip a coin
	if(random.randrange(1)):# Go with what Trump is
		TrumpLative = TrumpLative + random.choice(a0)
	
		# Flip another coin
		if (random.randrange(1)):
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
	 
	return """ <p>%s</p> """ % (TrumpLative, url_for('main_page'))







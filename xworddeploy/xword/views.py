from xword import app
from xword import Crossword
from flask import render_template
import pprint

word_list = ['saffron', 'The dried, orange yellow plant used to as dye and as a cooking spice.'], \
    ['pumpernickel', 'Dark, sour bread made from coarse ground rye.'], \
    ['leaven', 'An agent, such as yeast, that cause batter or dough to rise.'], \
    ['coda', 'Musical conclusion of a movement or composition.'], \
    ['paladin', 'A heroic champion or paragon of chivalry.'], \
    ['syncopation', 'Shifting the emphasis of a beat to the normally weak beat.'], \
    ['albatross', 'A large bird of the ocean having a hooked beek and long, narrow wings.'], \
    ['harp', 'Musical instrument with 46 or more open strings played by plucking.'], \
    ['piston', 'A solid cylinder or disk that fits snugly in a larger cylinder and moves under pressure as in an engine.'], \
    ['caramel', 'A smooth chery candy made from suger, butter, cream or milk with flavoring.'], \
    ['coral', 'A rock-like deposit of organism skeletons that make up reefs.'], \
    ['dawn', 'The time of each morning at which daylight begins.'], \
    ['pitch', 'A resin derived from the sap of various pine trees.'], \
    ['fjord', 'A long, narrow, deep inlet of the sea between steep slopes.'], \
    ['lip', 'Either of two fleshy folds surrounding the mouth.'], \
    ['lime', 'The egg-shaped citrus fruit having a green coloring and acidic juice.'], \
    ['mist', 'A mass of fine water droplets in the air near or in contact with the ground.'], \
    ['plague', 'A widespread affliction or calamity.'], \
    ['yarn', 'A strand of twisted threads or a long elaborate narrative.'], \
    ['snicker', 'A snide, slightly stifled laugh.']
 
a = Crossword(13, 13, None, 5000, word_list)
a.compute_crossword(2)

print a.word_find()
print a.display()
print a.legend()
print len(a.current_word_list), 'out of', len(word_list)
print a.debug


@app.route('/')
def submit_words():
	return render_template('submitwords.html',word_list=word_list)

@app.route('/wordbank')
def word_bank():
	return render_template('wordbank.html', wordbank=a.current_word_list)

@app.route('/puzzle')
def puzzle():
	down_list = []
	across_list = []
	for word in a.current_word_list:
		if word.down_across() is "down":
			down_list.append(word)
		else:
			across_list.append(word)
				
	return render_template('puzzle.html', puzzle=a, down_list = down_list, across_list = across_list)
	

@app.route('/display')
def display():
	return "<pre>" + a.display() + "</pre>" + "<br>" + a.legend()
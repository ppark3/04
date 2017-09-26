from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def root():
	return 'Hey guys!'
	
@my_app.route('/memes')
def meme():
	return "Oh, you woulda THOUGHT I had memes"
	
@my_app.route('/bio')
def bio():
	return "Philip Park is a boy."
	
if __name__ == '__main__':
	my_app.debug == True
	my_app.run()
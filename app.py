from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	food=["pasta","kosa w wrk","pizza","hamburger"]
	
	opposite_day=False
	least=["msh kosa"]
	return render_template("index.html",foods=food,opposite_days=opposite_day,leasts=least)

if __name__ == '__main__':
   app.run(debug = True)


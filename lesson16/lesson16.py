from flask import Flask,render_template,request,url_for,redirect
import datasource

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.j2')

@app.route("/product")
def product():
    cities:list[dict] = datasource.get_cities()
    page = request.args.get('page',1, type=int)
    per_page = 6
    start = (page-1) * per_page
    end = start + per_page
    total_pages = (len(cities) + per_page - 1 ) // per_page
    items_on_page = cities[start:end]
    return render_template('product.j2',
                           items_on_page=items_on_page,
                           total_pages=total_pages,
                           page = page)

@app.route("/pricing")
def pricing():
    cities:list[dict] = datasource.get_cities()
    page = request.args.get('page',1, type=int)
    per_page = 6
    start = (page-1) * per_page
    end = start + per_page
    total_pages = (len(cities) + per_page - 1 ) // per_page
    items_on_page = cities[start:end]
    return render_template('pricing.j2',
                            items_on_page=items_on_page,
                            total_pages=total_pages,
                            page = page) 

@app.route("/faqs",methods=['POST','GET'])
def faqs():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        #checked = request.form['checked']
        print(username,password)
        if username=='123@gmail.com'and password=='12345':
            return redirect(url_for('success'))    
    return render_template('faqs.j2')

@app.route("/about")
def about():
    return render_template('about.j2')

@app.route("/success")
def success():
    return "<h1>登入成功</h1>"
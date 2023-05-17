from flask import Flask,request,render_template

from src.search_query import Search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/search',methods=['GET','POST'])
def search():
    if request.method == 'GET':
        return render_template('chatgpt.html')
    else:
        search_initiate=Search(inp_query=request.form.get('inp_query'),top_k=request.form.get('top_k'))
    
        results=search_initiate.predict()
        res=[]
        for i in range(len(results)):
            res.append([i+1,results[i]])
        print(res)
        return render_template('home.html',results=res)

if __name__=="__main__":
    app.run(port=8000,debug=True)

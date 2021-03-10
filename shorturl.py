from flask import Flask,request,render_template,redirect
import base64
import pymysql

localhost = 'localhost'
user = 'root'
password = '0923xx..'
data = 'short_url'

try:
    db = pymysql.connect(localhost,user,password,data)
    cursor = db.cursor()
except :
    print("失败")

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('index.html')


@app.route('/get_short_url', methods = ['post'])
def get():
    long_url = request.form.get('url')
    if len(long_url)<=0:
        return render_template('index.html')
    cursor.execute("select count(url) from S_URL")
    results = cursor.fetchall()
    id = int(results[0][0])+1
    execute = "insert into S_URL(url) values('{}')".format(long_url)
    cursor.execute(execute)
    id = hex(id)
    db.commit()
    return render_template('index.html',short_url = 'http://120.78.201.120:5000/' + str(id))

@app.route('/<id>')
def id(id):
    id_ = int(id,16)
    cursor.execute('select url from S_URL where id={}'.format(id_))
    results_ = cursor.fetchone()
    return redirect (location= results_[0]+"/")


if __name__ == '__main__' :
    app.run('172.18.163.117',debug=True)
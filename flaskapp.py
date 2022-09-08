from flask import Flask, render_template, url_for
from flask import request
import requests

app = Flask(__name__, static_url_path='/static')
x=""
@app.route("/", methods=["POST", "GET"])
def home():

    return render_template('app2.html')


@app.route("/switch", methods=["POST", "GET"])
def switch():
    count=0
    command = request.args.get("command")
    id = request.args.get("id")
    print(command,id)
    url = "http://dev-onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-WiSUN/Data"
    headers = {
        "X-M2M-Origin": "devtest:devtest",
        "Content-type": "application/json;ty=4"
    }
    on={
        "m2m:cin": {
                    "con":id,
                    "lbl":"",
                    "cnf":"text"
        }
    }
    off = {
        "m2m:cin": {
            "con":id,
            "lbl":"",
            "cnf":"text"
        }
    }
    dim={
        "m2m:cin":{
            "con":'.dim5',
            "lbl":"",
            "cnf":"text"
        }
    }
    test={}
    if (command == "on"):
        x=requests.post(url,headers=headers,json=on)
        test=x.text
        print(x.text)
    if(command=="off"):
        x=requests.post(url,headers=headers,json=off)
        test=x.text
        print(x.text)
    if(command=="dim"):
        x=requests.post(url,headers=headers,json=dim)
        test=x.text
        print(x.text)
    return test

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    # app.run()

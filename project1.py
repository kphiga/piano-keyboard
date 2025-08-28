from flask import Flask, request, render_template, jsonify

app=Flask(__name__)

sound={
    "Do":"./static/audio-asset/do.ogg",
    "Re":"./static/audio-asset/re.ogg",
    "Mi":"./static/audio-asset/mi.ogg",
    "Fa":"./static/audio-asset/fa.ogg",
    "So":"./static/audio-asset/so.ogg",
    "Ra":"./static/audio-asset/ra.ogg",
    "Si":"./static/audio-asset/si.ogg"
    }

@app.route("/")
def index():
    return render_template("project1.html")

@app.route("/button_action", methods=["POST"])
def button_action():
    data=request.get_json()
    key=data.get("key")

    soundfile=sound[key]
    return jsonify({"soundfile":soundfile})

if __name__=="__main__":
    app.run(host="127.0.0.1",port=5000, debug=True)


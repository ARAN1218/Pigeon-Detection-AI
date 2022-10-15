# 各種インポート
from flask import Flask,render_template,request
import subprocess
import os


# Flaskオブジェクトの生成
app = Flask(__name__)

# 画像のアップロードのための設定
ALLOWED_TYPES = ['.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff', '.dng', '.webp', '.mpo']
app.config['UPLOAD_FOLDER'] = 'pigeon_app/static/media'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024


# ホーム
@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    elif request.method == 'POST':
        img_result = request.files['result']
        suffix = "." + img_result.filename.split(".")[1] if "." in img_result.filename else ""
        if img_result.filename == '' or suffix.lower() not in ALLOWED_TYPES:
            return render_template("home.html", img_result=False, error_flag=True)
        img_result.save(os.path.join(app.config['UPLOAD_FOLDER'], 'result'+suffix))
        subprocess.run(['python', 'pigeon_app/yolov5/detect.py', '--source', 'pigeon_app/static/media/result'+suffix, '--weights', 'pigeon_app/yolov5/pigeon_5.pt', '--conf', '0.3', '--name', '../../../static/media', '--exist-ok'])
        return render_template("home.html", img_result=True, suffix=suffix)


@app.route("/info")
def info():
    return render_template("info.html")


@app.route("/pigeons")
def pigeons():
    return render_template("pigeons.html")


@app.route("/tech")
def tech():
    return render_template("tech.html")

@app.route("/sitemap.xml")
def sitemap():
    return app.send_static_file("sitemap.xml")

if __name__ == "__main__":
    app.run(debug=True)
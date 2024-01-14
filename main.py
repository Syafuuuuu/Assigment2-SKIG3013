from flask import Flask, send_file
from flask.templating import render_template

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/download_pdf/<filename>')
def download_pdf(filename):
    path_to_pdf = app.static_folder + "/download/" + filename
    return send_file(path_to_pdf, as_attachment=True)


@app.route("/")
def main():
    return render_template("Landing_Page.html")


@app.route("/Syafiq")
def Syafiq_Page():
    return render_template("Syafiq-index.html")


@app.route("/Phong")
def Phong_Page():
    return render_template("Phiraphong-index.html")


@app.route("/Ahmad")
def Ahmad_Page():
    return render_template("Ahmad-index.html")



if __name__ == '__main__':
    app.run()

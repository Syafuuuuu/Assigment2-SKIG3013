from flask import Flask, request, redirect, url_for, flash, send_file
from flask.templating import render_template
from sqlite3 import Error
import sqlite3

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'your_secret_key'  # for flashing messages


def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('static/db/sent-contact.db')  # create a database connection
        return conn
    except Error as e:
        print(e)

    return conn


@app.route('/form_route', methods=['POST'])
def form_route():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        conn = create_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO contacts (name, email, subject, message) VALUES (?, ?, ?, ?)",
                    (name, email, subject, message))
        conn.commit()

        # return redirect(request.url)  # redirect to the same page

        redirect_page = request.form.get('redirect')

        if redirect_page == 'Ahmad':
            flash('Your message has been sent successfully!')
            return redirect(request.url)  # redirect to the same page
            return render_template('Ahmad-index.html')  # default template

        elif redirect_page == 'Phong':
            flash('Your message has been sent successfully!')
            return redirect(request.url)  # redirect to the same page
            return render_template('Phong-index.html')  # default template

        elif redirect_page == 'Syafiq':
            flash('Your message has been sent successfully!')
            return redirect(request.url)  # redirect to the same page
            return render_template('Syafiq-index.html')  # default template

        else:
            flash('Your message has not been sent!')
            return redirect(request.url)  # redirect to the same page
            return render_template('Landing_Page.html')  # default template


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

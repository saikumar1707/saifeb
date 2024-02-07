from flask import Flask, render_template, request, flash, send_from_directory

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

from pymongo.errors import AutoReconnect
from pymongo import MongoClient

MONGO_USERNAME = 'saikumarmanchala2003'
MONGO_PASSWORD = 'dsNxl8PJ1gKSmOu2'
MONGO_CLUSTER_URL = 'cluster0.lclg6oj.mongodb.net'
MONGO_DATABASE = 'cluster0'

MONGO_URI = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER_URL}/{MONGO_DATABASE}?retryWrites=true&w=majority"

# Connect to MongoDB Atlas
client = MongoClient(MONGO_URI)
db = client[MONGO_DATABASE]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/level1', methods=['GET', 'POST'])
def one():
    if request.method == 'POST':
        answer1 = request.form.get('data').lower()
        answer2=request.form.get('data7').lower()
        answer3=request.form.get('data9').lower()
        db1=request.form.get('dat').lower()
        data = {
            'questionrose':db1}

        db['feb'].insert_one(data)
        if answer1 != 'sunday':  # Replace 'correct_answer' with the actual correct answer
            flash('Incorrect answer. Please try again.', 'error')  # Flash error message
            return render_template('index.html')
        if answer2 != 'kallu':  # Replace 'correct_answer' with the actual correct answer
            flash('Incorrect answer. Please try again.', 'error')  # Flash error message
            return render_template('index.html')
        if answer3 != 'rose':  # Replace 'correct_answer' with the actual correct answer
            flash('Incorrect answer. Please try again.', 'error')  # Flash error message
            return render_template('index.html')
    return render_template('pday.html')

@app.route('/level2', methods=['GET', 'POST'])
def two():
    if request.method == 'POST':
        answer1 = request.form.get('data1').lower()
        answer2 = request.form.get('data0').lower()
        answer3 = request.form.get('datap').lower()

        db2=request.form.get('dat')
        data = {
            'questionpropose':db2}

        db['feb'].insert_one(data)
        if answer1 != 'i':  # Replace 'correct_answer' with the actual correct answer
            flash('Incorrect answer. Please try again.', 'error')  # Flash error message
            return render_template('pday.html')
        if answer2 != 'u':  # Replace 'correct_answer' with the actual correct answer
            flash('Incorrect answer. Please try again.', 'error')  # Flash error message
            return render_template('pday.html')
        if answer3 != 'love':  # Replace 'correct_answer' with the actual correct answer
            flash('Incorrect answer. Please try again.', 'error')  # Flash error message
            return render_template('pday.html')
    return render_template('cday.html')

@app.route('/level3', methods=['GET', 'POST'])
def three():
    if request.method == 'POST':
        answer2 = request.form.get('data0').lower()
        answer3 = request.form.get('datap').lower()

        db2=request.form.get('dat')
        data = {
            'questionchocolate':db2}

        db['feb'].insert_one(data)
        answer1 = request.form.get('data2').lower()
        if answer1 != 'tuesday':  # Replace 'correct_answer' with the actual correct answer
            flash('Incorrect answer. Please try again.', 'error')  # Flash error message
            return render_template('cday.html')
        if answer2 != 'kitkat':  # Replace 'correct_answer' with the actual correct answer
            flash('Incorrect answer. Please try again.', 'error')  # Flash error message
            return render_template('cday.html')
        if answer3 != 'temptations':  # Replace 'correct_answer' with the actual correct answer
            flash('Incorrect answer. Please try again.', 'error')  # Flash error message
            return render_template('cday.html')
    return render_template('tday.html')

@app.route('/level4', methods=['GET', 'POST'])
def four():
    
    if request.method == 'POST':
        db2=request.form.get('dat')
        data = {
            'questionteddy':db2}
        db['feb'].insert_one(data)
        answer1 = request.form.get('data2').lower()
        answer2=request.form.get('data0').lower()
        answer3=request.form.get('datap').lower()
        if answer1 != 'diwali':  # Replace 'correct_answer' with the actual correct answer
            flash('Incorrect answer. Please try again.', 'error')  # Flash error message
            return render_template('tday.html')
        if answer2 != 'kush':  # Replace 'correct_answer' with the actual correct answer
            flash('Incorrect answer. Please try again.', 'error')  # Flash error message
            return render_template('tday.html')
        if answer3 != 'teddybear':  # Replace 'correct_answer' with the actual correct answer
            flash('Incorrect answer. Please try again.', 'error')  # Flash error message
            return render_template('tday.html')
    return render_template('prday.html')


@app.route('/level5', methods=['GET', 'POST'])
def five():
    if request.method == 'POST':
        db2=request.form.get('data4')
        data = {
            'questionpromise':db2}
        db['feb'].insert_one(data)
        answer1 = request.form.get('datap').lower()
        answer2 = request.form.get('datal').lower()
        if answer1 != 'welivetogetherforever':  # Replace 'correct_answer' with the actual correct answer
            flash('Incorrect answer. Please try again.', 'error')  # Flash error message
            return render_template('prday.html')
        if answer2 != 'praanam':  # Replace 'correct_answer' with the actual correct answer
            flash('Incorrect answer. Please try again.', 'error')  # Flash error message
            return render_template('prday.html')
    return render_template('hday.html')

@app.route('/level6', methods=['GET', 'POST'])
def six():
    if request.method == 'POST':
        db2=request.form.get('data4')
        data = {
            'questionhug':db2}
        db['feb'].insert_one(data)
        answer1 = request.form.get('data5').lower()
        answer2 = request.form.get('dataq').lower()
        if answer1 != 'pasidi':  # Replace 'correct_answer' with the actual correct answer
            flash('Incorrect answer. Please try again.', 'error')  # Flash error message
            return render_template('hday.html')
        if answer2 != 'cuddle':  # Replace 'correct_answer' with the actual correct answer
            flash('Incorrect answer. Please try again.', 'error')  # Flash error message
            return render_template('hday.html')
    return render_template('kday.html')


@app.route('/level7', methods=['GET', 'POST'])
def seven():
    return render_template('final.html')

@app.route('/download/<filename>')
def download_file(filename):
    # Assuming your video files are located in a directory named 'videos' within the static folder
    return send_from_directory('static/videos', filename, as_attachment=True)


if __name__ == '__main__':

    app.run(debug=True)

import sqlite3 as lite
from flask import request, Flask, render_template, url_for

app = Flask(__name__)

@app.route('/getdata', methods=['POST'])


def getdata():

    data = None

    conn = lite.connect(':memory')
    with conn:

        conn.row_factory = lite.Row
        cursor = conn.cursor()

    if request.method == 'POST':

        # Then get the data from the form
            grade = request.form['grade']
            text_grade = grade.upper()

            query = "SELECT * FROM restaurants id IN (SELECT id FROM restaurants ORDER BY RANDOM() LIMIT 10) WHERE grade=?"
            cursor.execute(query, (text_grade))

            rows = cursor.fetchall()

            for row in rows:
                data = '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (row['CAMIS'], row['DBA'], row['BORO'], row['BUILDING'], row['STREET'], row['ZIPCODE'], row['PHONE'], row['CUISINE DESCRIPTION'], row['INSPECTION DATE'], row['ACTION'], row['VIOLATION CODE'], row['VIOLATION DESCRIPTION'], row['CRITICAL FLAG'], row['SCORE'], row['GRADE'], row['GRADE DATE'], row['RECORD DATE'], row['INSPECTION TYPE'])

    return render_template('restaurants.html', data)


if __name__ == '__main__':
    app.run(debug=True)

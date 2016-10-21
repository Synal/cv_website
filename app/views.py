# -*- coding: utf-8 -*-
# __author__ = 'z002wpta'

from flask import url_for, render_template, flash, request
from app import app


@app.route('/')
def home():
    technologies = [('Apache2', 'https://httpd.apache.org/', 'Apache_PoweredBy.png'),
                    ('Flask', 'http://flask.pocoo.org/', 'flask.png'),
                    ('Jinja2', 'http://jinja.pocoo.org/', 'jinja-small.png'),
                    ('Bootstrap', 'http://getbootstrap.com/', 'Boostrap_logo.png'),
                    ('MySQL', 'http://www.mysql.com/', 'MySQL-Logo.png'),
                    ('SQLAlchemy', 'http://www.sqlalchemy.org/', 'sqla_logo.png'),
                    ('Bitbucket', 'https://bitbucket.org/dashboard/overview', 'bitbucket_rgb_blue.png')]
    return render_template('home.html', technologies=technologies)


@app.route('/projects', methods=['GET', 'POST'])
def projects():
    message_types = [(1, '#FCF8E3', 'warning'), (2, '#F2DEDE', 'danger'), (3, '#D9EDF7', 'info'),
                     (4, '#DFF0D8', 'success')]
    if request.method == 'POST':
        mess = request.form['message']
        mess_id = request.form['message_type']
        print mess, mess_id
        flash(mess, message_types[int(mess_id)-1][2])
    return render_template('projects.html', message_types=message_types)


@app.route('/interests')
def interests():
    favorites = [('Homebrewing', url_for('homebrewing'), 'beer.png'),
                 ('Instruments', url_for('instruments'), 'clarinet.png')]

    return render_template('interests.html', favorites=favorites)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/homebrewing')
def homebrewing():
    from os import listdir
    import os
    from os.path import isfile, join
    homebrewing_path = os.getcwd()+r'\app\static\images\homebrewing'
    labels = [f for f in listdir(homebrewing_path) if isfile(join(homebrewing_path, f))]
    return render_template('homebrewing.html', labels=labels)


@app.route('/instruments')
def instruments():
    return

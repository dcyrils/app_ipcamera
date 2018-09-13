#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 08:56:10 2018

@author: kdg
"""
from flask import render_template, flash, redirect, url_for
from AppCamera import app
from AppCamera.forms import MoveForm
from AppCamera.ptzmovez import PTZmovez

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/input', methods=['GET', 'POST'])
def inp():
    form = MoveForm()
    if form.validate_on_submit():
        flash('...процесс пошел...'.format(form.X.data, form.Y.data, form.Z.data))
        # camera is moving...
        PTZmovez(X=form.X.data, Y=form.Y.data, Z=form.Z.data)
        return redirect(url_for('index'))
    return render_template('input.html', 
                           title='ЗАДАЙТЕ КООРДИНАТЫ', form=form)
    


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 13:47:49 2018

@author: kdg
"""

from flask_wtf import FlaskForm
from wtforms import DecimalField, BooleanField, SubmitField
from wtforms.validators import NumberRange

class MoveForm(FlaskForm):
    X = DecimalField('Panorama/горизонталь', validators=[NumberRange(-1.0,1.0)])
    Y = DecimalField('Tilt/наклон(вертикаль)', validators=[NumberRange(-1.0,1.0)])
    Z = DecimalField('Zoom/масштабирование', validators=[NumberRange(-1.0,1.0)])
    submit = SubmitField('Submit/отправить')
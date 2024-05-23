#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

view = Blueprint('demo-app-index', __name__)

@view.route('/contact', methods=['GET'])
@view.route('/level', methods=['GET'])
@view.route('/', methods=['GET'])
def home():
  locals = {}
  locals['title'] = 'Bienvenido'
  locals['csss'] = ['dist/app']
  locals['jss'] = ['dist/app']
  return render_template('home.html', locals = locals)

@view.route('/error/access/<code>', methods=['GET'])
def error_access(code):
  # lang = session_language(session)
  # locals_dic = { }
  # return render_template('demo/index.html', locals=locals_dic)
  return 'Recurso no encontrado', code

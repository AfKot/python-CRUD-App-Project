from application import app, db
from application.models import Movies, Directors
from application.forms import MovieForm, DirectorForm
from flask import Flask, redirect, url_for, render_template, request

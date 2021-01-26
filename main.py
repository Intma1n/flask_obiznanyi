from app import app
import cursor as cursor
from config import Configuration
from posts.blueprint import posts
from flask import Flask, render_template, request, json
from flask import Blueprint
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy


@app.route('/')
def main():
    app.run()


if __name__ == '__main__':
    main()

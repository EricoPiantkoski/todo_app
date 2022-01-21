from flask import Flask, Blueprint, render_template, redirect, url_for, request
from pymongo import MongoClient
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

uri = 'mongodb+srv://adm:root@tododb.z2qbh.mongodb.net/taskdb?retryWrites=true&w=majority")&tlsAllowInvalidCertificates=true'
#mongo = PyMongo(uri)

def test_connection(uri):
    client = MongoClient(uri)
    print(client.server_info())
    # todos_collection = mongo.db.todos
    # todos = todos_collection.find()
    # print(todos)
    # return pymongo.MongoClient(client_uri)
    

test_connection(uri)
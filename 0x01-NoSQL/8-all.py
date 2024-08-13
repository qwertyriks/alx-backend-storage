#!/usr/bin/env python3
"""This lists all documents in Python"""
import pymongo


def list_all(mongo_collection):
    """This function list all doc in a collection"""
    if not mongo_collection:
        return []
    documents = mongo_collection.find()
    return [post for post in documents]

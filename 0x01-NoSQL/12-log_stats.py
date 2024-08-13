#!/usr/bin/env python3
"""
Provide some stats about Nginx logs stored in MongoDB
Database; logs, Collection: nginx, Display same as example
first line, x logs, x number of documents in this collection
"""
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """
    Prototype: def log_stats(mongo_collection, option=None)
    Providing some stats about Nginx logs stored in MongoDB
    """
    items = {}
    if option:
        value = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {value}")
        return

    result = mongo_collection.count_documents(items)
    print(f"{result} logs")
    print("Methods:")
    for method in METHODS:
        log_stats(nginx_collection, method)
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://104.28.239.10').logs.nginx
    log_stats(nginx_collection)

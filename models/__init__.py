#!/usr/bin/python3
"""Initialization for the package
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

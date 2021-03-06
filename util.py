#!/usr/bin/env python3
#
# Copyright (c) 2010 Gavin Andresen
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
"""Utility functions for bitcointool."""
from base64 import b64encode
from binascii import hexlify, unhexlify
import hashlib
import os
import os.path
import platform
import struct

def sha256(s):
    return hashlib.new('sha256', s).digest()

def ripemd160(s):
    return hashlib.new('ripemd160', s).digest()

def hash256(s):
    return sha256(sha256(s))

def hash160(s):
    return hashlib.new('ripemd160', sha256(s)).digest()

def bytes_to_hex_str(byte_str):
    return hexlify(byte_str).decode('ascii')

def determine_datadir():
    if platform.system() == "Darwin":
        return os.path.expanduser("~/Library/Application Support/Bitcoin/")
    elif platform.system() == "Windows":
        return os.path.join(os.environ['APPDATA'], "Bitcoin")
    return os.path.expanduser("~/.bitcoin")

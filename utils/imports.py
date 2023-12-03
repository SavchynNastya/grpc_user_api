# server - client
import grpc

import proto_pb2.users.users_pb2 as users_pb2
import proto_pb2.users.users_pb2_grpc as users_pb2_grpc

from proto_pb2.users.users_pb2_grpc import add_UserServiceServicer_to_server as add_UserServiceServicer_to_server

import asyncio
import os
import re


# regex
EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# helper dicts
statuses = {
    0: 'User',
    1: 'Admin',
    2: 'Analyst',
    3: 'Developer/tester',
    4: 'User-Admin'
}


# database
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, DATETIME, ForeignKey, or_, and_, BINARY, update
from sqlalchemy.sql import func
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import sessionmaker

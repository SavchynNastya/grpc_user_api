from utils.imports import sessionmaker, or_, and_, users_pb2_grpc, users_pb2, re, EMAIL_REGEX, statuses, os, update
from utils.keygen import generate_random_string
from database.engine import engine
from database.tables import users

Session = sessionmaker(bind=engine)


class UsersServicer(users_pb2_grpc.UserServiceServicer):
    def CreateUsersRecord(self, request, context):
        error_messages = []
        try:
            with Session() as session:
                # int64 admin_id = 1;
                # string admin_hash = 2;
                # string user_username = 3;
                # string user_email = 4;

                # check <Admin_id>
                if not request.admin_id:
                    error_messages.append(
                        'Error: <Admin_id> cannot be empty.')
                    
                # check <Admin_hash>
                if not request.admin_hash:
                    error_messages.append(
                        'Error: <Admin_hash> cannot be empty.')

                # check <User_username>
                if not request.user_username or not request.user_username.strip():
                    error_messages.append(
                        'Error: <User_username> cannot be empty or include whitespaces only.')

                # check <User_email>
                if not request.user_email or not request.user_email.strip():
                    error_messages.append(
                        'Error: <User_email> cannot be empty or include whitespaces only.')

                if not re.match(EMAIL_REGEX, request.user_email):
                    error_messages.append(
                        'Error: <User_email> has an invalid format.')

                # # check <User_status>
                # if request.user_status not in range(0, 5):
                #     error_messages.append(
                #         f'Error: <Status> cannot be "{request.user_status}". Allowed values - 0-4.')

                 # if errors - do not do database query
                if error_messages:
                    result = {"status": 400, "message": error_messages}
                else:
                    new_record = users.insert().values(
                        name=''.encode('utf-8'),
                        key=generate_random_string(15).encode('utf-8'),
                        hash=''.encode('utf-8'),
                        username=request.user_username,
                        firstEmail=request.user_email,
                        status=0, # user
                    ).returning(users)
                    # session.execute(new_record)
                    result = session.execute(new_record)
                    session.commit()
                    inserted_record = result.fetchone()
                    result = {"status": 200,
                              "message": "USERS: Record created",
                              "key_api": inserted_record.key}
        except Exception as ex:
            result = {"status": 400, "message": str(ex)}
        return users_pb2.CreateUsersResponse(**result)

    def ReadUsersRecord(self, request, context):
        try:
            with Session() as session:
                conditions = []
                if request.id:
                    conditions.append(users.c.id.in_(request.id))
                if request.name:
                    conditions.append(users.c.name.in_(request.name))
                if request.key:
                    conditions.append(users.c.key.in_(request.key))
                if request.hash:
                    conditions.append(users.c.hash.in_(request.hash))
                if request.salt:
                    conditions.append(users.c.salt.in_(request.hash))
                if request.status:
                    conditions.append(users.c.status.in_(request.status))
                if request.description:
                    conditions.append(
                        users.c.description.in_(request.description))
                if request.timestamp:
                    conditions.append(users.c.timestamp.in_(request.timestamp))

                if not conditions:
                    results = session.query(users).all()
                else:
                    results = session.query(users).filter(
                        or_(*conditions)).all()

                if results:
                    data = {
                        "status": 200,
                        "data": [{
                            "id": result.id,
                            "name": result.name,
                            "username": result.username,
                            "first_email": result.firstEmail,
                            "second_email": result.secondEmail,
                            "key": result.key,
                            "hash": result.hash,
                            "salt": result.salt,
                            "status": result.status,
                            "description": result.description,
                            "timestamp": str(result.timestamp)} for result in results]
                    }
                else:
                    data = {"status": 400, "message": "USERS: No results"}
        except Exception as ex:
            data = {"status": 400, "message": str(ex)}
        return users_pb2.ReadUsersResponse(**data)

    def UpdateUsersRecord(self, request, context):
        try:
            with Session() as session:
                # {
                #     "id": 2, 
                #     "hash": "5b3ad3145fd1518a9f8742c5fa850b60a6b82774e47bf8edf3d1ffc0d339701c".encode('utf-8'),
                #     "first_email": "anasav0004@gmail.com",
                #     "second_email": "anasav00041@gmail.com",
                #     "username": "tatasiyka8e9w89e",
                #     "description": "desc"
                # }
                conditions = []
                if request.id:
                    conditions.append(users.c.id==request.id)
                if request.hash:
                    conditions.append(users.c.hash==request.hash.encode('utf-8'))
                
                if not session.query(users).filter(or_(*conditions)).count():
                    return users_pb2.UpdateUsersResponse(status=400, message="No matching records found.")

                if conditions:
                    update_data = {
                        # "name": request.update_data.name if request.update_data.name else None,
                        "username": request.username if request.username else None,
                        # "key": request.update_data.key if request.update_data.key else None,
                        "hash": request.hash.encode('utf-8') if request.hash else None,
                        "firstEmail": request.first_email if request.first_email else None,
                        "secondEmail": request.second_email if request.second_email else None,
                        # "salt": request.update_data.salt if request.update_data.salt else None,
                        # "status": request.update_data.status if request.update_data.status else None,
                        "description": request.description if request.description else None,
                    }

                    if any(update_data.values()):
                        update_query = users.update().where(or_(*conditions)).values(
                            **{k: v for k, v in update_data.items() if v is not None}
                        )
                        session.execute(update_query)
                        session.commit()
                        result = {"status": 200, "message": "Record updated"}

                    else:
                        result = {"status": 400,
                                  "message": "No parameters to update."}
                else:
                    result = {"status": 400,
                              "message": "No parameters. Provide at least an id."}
        except Exception as ex:
            result = {"status": 400, "message": str(ex)}
        return users_pb2.UpdateUsersResponse(**result)

    def DeleteUsersRecord(self, request, context):
        try:
            with Session() as session:
                # {
                #     "admin_id": 1,
                #     "admin_hash": "5b3ad3145fd1518a9f8742c5fa850b60a6b82774e47bf8edf3d1ffc0d339701b".encode('utf-8'),
                #     "user_name": "User12",
                #     "user_username": "Username12",
                #     "with_data": True,
                #     "reason": "just bad guy"
                # }
                conditions = []
                if request.user_name:
                    conditions.append(users.c.name==request.user_name)
                if request.user_username:
                    conditions.append(users.c.username==request.user_username)
                if not session.query(users).filter(or_(*conditions)).count():
                    return users_pb2.DeleteUsersResponse(status=400, message="No matching records found.")

                if conditions:
                    delete_query = users.delete().where(or_(*conditions))
                    message = "Record deleted."
                else:
                    delete_query = users.delete()
                    message = "Records deleted."

                session.execute(delete_query)
                session.commit()
                session.close()
                result = {"status": 200, "message": message}
        except Exception as ex:
            result = {"status": 400, "message": str(ex)}
        return users_pb2.UpdateUsersResponse(**result)

    def ResetUserAuthRecord(self, request, context):
        try:
            with Session() as session:
                # {
                #     "id": 2,
                #     "username": "tatasiyka8e9w89e",
                #     "hash": "5b3ad3145fd1518a9f8742c5fa850b60a6b82774e47bf8edf3d1ffc0d339701c".encode('utf-8'),
                # }
                conditions = []
                if request.id:
                    conditions.append(users.c.id==request.id)
                if request.username:
                    conditions.append(users.c.username==request.username)
                if request.hash:
                    conditions.append(users.c.hash==request.hash.encode('utf-8'))

                if not session.query(users).filter(and_(*conditions)).count():
                    return users_pb2.ResetAdminAuthResponse(status=400, message="No matching records found.")

                if conditions:
                    reset_query = update(users).where(and_(*conditions)).values(key=''.encode('utf-8'))
                    session.execute(reset_query)
                    session.commit()
                    session.close()
                    message = "Auth was reset."
                else:
                    return users_pb2.ResetAdminAuthResponse(status=400, message="Provide parameters to filter users.")

                result = {"status": 200, "message": message}
        except Exception as ex:
            result = {"status": 400, "message": str(ex)}
        return users_pb2.ResetAdminAuthResponse(**result)
    
    def ResetAdminAuthRecord(self, request, context):
        try:
            with Session() as session:
                # {
                #     "admin_id": 1,
                #     "admin_hash": "5b3ad3145fd1518a9f8742c5fa850b60a6b82774e47bf8edf3d1ffc0d339701b".encode('utf-8'),
                #     "user_name": "Anastasiia",
                #     "user_username": "tatasiyka8e9w89e",
                #     "reason": "lost key"
                # }
                conditions = []
                if request.user_name:
                    conditions.append(users.c.name==request.user_name)
                if request.user_username:
                    conditions.append(users.c.username==request.user_username)
                if not session.query(users).filter(and_(*conditions)).count():
                    return users_pb2.ResetAdminAuthResponse(status=400, message="No matching records found.")

                if conditions:
                    reset_query = update(users).where(and_(*conditions)).values(key=''.encode('utf-8'))
                    session.execute(reset_query)
                    session.commit()
                    session.close()
                    message = "Auth was reset."
                else:
                    return users_pb2.ResetAdminAuthResponse(status=400, message="Provide parameters to filter users.")
                
                result = {"status": 200, "message": message}
        except Exception as ex:
            result = {"status": 400, "message": str(ex)}
        return users_pb2.ResetAdminAuthResponse(**result)
    
    def CheckAdminRecord(self, request, context):
        try:
            with Session() as session:
                conditions = []
                if request.admin_id:
                    conditions.append(users.c.id==request.admin_id)
                if request.admin_hash:
                    conditions.append(users.c.hash==request.admin_hash.encode('utf-8'))
                conditions.append(users.c.status==1) # check if user is admin
                
                if not session.query(users).filter(and_(*conditions)).count():
                    return users_pb2.CheckAdminResponse(status=400, message="No matching admins records found.")

                result = {"status": 200, "message": "Admin exists"}
        except Exception as ex:
            result = {"status": 400, "message": str(ex)}
        return users_pb2.ResetAdminAuthResponse(**result)
    
    def UpdateUserStatusRecord(self, request, context):
        try:
            with Session() as session:
                conditions = []
                # if request.admin_id:
                #     conditions.append(users.c.id==request.admin_id)
                # if request.admin_hash:
                #     conditions.append(users.c.hash==request.admin_hash.encode('utf-8'))
                if request.user_username:
                    conditions.append(users.c.username==request.user_username)
                # user was logged in at least once
                conditions.append(users.c.hash!=''.encode('utf-8'))
                
                if conditions:
                    update_query = update(users).where(and_(*conditions)).values(status=request.status)
                    session.execute(update_query)
                    session.commit()
                    session.close()
                    message = f"User status was updated to {statuses[request.status]}."
                else:
                    return users_pb2.UpdateUserStatusResponse(status=400, message="Provide parameters to filter users.")

                result = {"status": 200, "message": message}
        except Exception as ex:
            result = {"status": 400, "message": str(ex)}
        return users_pb2.UpdateUserStatusResponse(**result)
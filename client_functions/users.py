from utils.imports import users_pb2


def check_data_params(param_name, list_type, data):
    if param_name in data:
        if isinstance(data[param_name], list) and not all(isinstance(x, list_type) for x in data[param_name]) or not data[param_name]:
            return f"Error: invalid '{param_name}' value. Expected a non-empty list of {list_type}."
        elif not isinstance(data[param_name], list_type):
            return f"Error: invalid '{param_name}' value."
    return ''


def check_users_data(data):
    error_messages = []
    if not isinstance(data, dict):
        error_messages.append(
            f'Error: incorrect type for data transfer - {type(data)}. Expected - dictionary.')
    else:
        error = check_data_params("id", int, data)
        if error:
            error_messages.append(error)
        error = check_data_params("name", str, data)
        if error:
            error_messages.append(error)
        error = check_data_params("username", str, data)
        if error:
            error_messages.append(error)
        error = check_data_params("key", bytes, data)
        if error:
            error_messages.append(error)
        error = check_data_params("hash", bytes, data)
        if error:
            error_messages.append(error)
        error = check_data_params("salt", str, data)
        if error:
            error_messages.append(error)
        error = check_data_params("description", str, data)
        if error:
            error_messages.append(error)
        error = check_data_params("status", int, data)
        if error:
            error_messages.append(error)
        error = check_data_params("timestamp", int, data)
        if error:
            error_messages.append(error)
    return error_messages


async def create_record_users(stub, data):
    error_messages = []

    def check_data(param_name, expected_type, allow_empty=False):
        if param_name not in data or not isinstance(data[param_name], expected_type):
            if param_name not in data:
                error_messages.append(
                    f'Error: no <{param_name.capitalize()}> parameter provided.')
            elif not isinstance(data[param_name], expected_type):
                error_messages.append(
                    f'Error: parameter <{param_name.capitalize()}> has unexpected type - {type(data["name"])}. Expected - string.')
            elif expected_type is str and not allow_empty and (not data[param_name] or not data["name"].strip()):
                error_messages.append(
                    f'Error: parameter <{param_name.capitalize()}> cannot be empty or have whitespaces only.')

    if not isinstance(data, dict):
        error_messages.append(
            f'Error: incorrect type for data transfer - {type(data)}. Expected - dictionary.')
    else:
        # check_data("name", str,)
        check_data("admin_id", int,)
        check_data("admin_hash", bytes,)
        check_data("user_username", str,)
        check_data("user_email", str,)
        # check_data("key", bytes,)
        # check_data("hash", bytes, )
        # check_data("salt", str, allow_empty=True)
        # check_data("user_status", int, )
        # check_data("description", str, allow_empty=True)
    # if errors - do not send request
    if error_messages:
        return {"status": 400, "message": error_messages}
    else:
        # check admin data
        response = await stub.CheckAdminRecord(users_pb2.CheckAdminRequest(admin_id=data['admin_id'], admin_hash=data['admin_hash']))
        if response.status == 200:
            response = await stub.CreateUsersRecord(users_pb2.CreateUsersRequest(**data))
        return response


async def read_record_users(stub, data):
    error_messages = check_users_data(data)
    if error_messages:
        return {"status": 400, "message": error_messages}
    else:
        response = await stub.ReadUsersRecord(users_pb2.ReadUsersRequest(**data))
    return response


async def update_record_users(stub, data):
    error_messages = check_users_data(data)
    if error_messages:
        return {"status": 400, "message": error_messages}
    else:
        response = await stub.UpdateUsersRecord(users_pb2.UpdateUsersRequest(**data))
    return response


async def delete_record_users(stub, data):
    error_messages = check_users_data(data)
    if error_messages:
        return {"status": 400, "message": error_messages}
    else:
        # check admin data
        response = await stub.CheckAdminRecord(users_pb2.CheckAdminRequest(admin_id=data['admin_id'], admin_hash=data['admin_hash']))
        if response.status == 200:
            response = await stub.DeleteUsersRecord(users_pb2.DeleteUsersRequest(**data))
    return response


async def update_status_record_users(stub, data):
    error_messages = check_users_data(data)
    if error_messages:
        return {"status": 400, "message": error_messages}
    else:
        # IGNORE for testing to enable changing user statuses

        # response = await stub.CheckAdminRecord(users_pb2.CheckAdminRequest(admin_id=data['admin_id'], admin_hash=data['admin_hash']))
        # if response.status == 200:
        response = await stub.UpdateUserStatusRecord(users_pb2.UpdateUserStatusRequest(**data))
    return response


async def reset_user_auth_users(stub, data):
    error_messages = check_users_data(data)
    if error_messages:
        return {"status": 400, "message": error_messages}
    else:
        response = await stub.ResetUserAuthRecord(users_pb2.ResetUserAuthRequest(**data))
    return response


async def reset_admin_auth_users(stub, data):
    error_messages = check_users_data(data)
    if error_messages:
        return {"status": 400, "message": error_messages}
    else:
        response = await stub.CheckAdminRecord(users_pb2.CheckAdminRequest(admin_id=data['admin_id'], admin_hash=data['admin_hash']))
        if response.status == 200:
            response = await stub.ResetAdminAuthRecord(users_pb2.ResetAdminAuthRequest(**data))
    return response


"""
 # check <Name>
        if "name" not in data or not isinstance(data["name"], str) or not data["name"].strip():
            if "name" not in data:
                error_messages.append('Error: no <Name> parameter provided.')
            elif not isinstance(data["name"], str):
                error_messages.append(f'Error: parameter <Name> has unexpected type - {type(data["name"])}. Expected - string.')
            else:
                error_messages.append('Error: parameter <Name> cannot be empty or have whitespaces only.')

        # check <UserName>
        if "username" not in data or not isinstance(data["username"], str) or not data["username"].strip():
            if "username" not in data:
                error_messages.append('Error: no <Username> parameter provided.')
            elif not isinstance(data["username"], str):
                error_messages.append(
                    f'Error: parameter <Username> has unexpected type - {type(data["username"])}. Expected - string.')
            else:
                error_messages.append(
                    'Error: parameter <Username> cannot be empty or have whitespaces only.')

        # check <Key>
        if "key" not in data or not isinstance(data["key"], bytes):
            if "key" not in data:
                error_messages.append('Error: no <Key> parameter provided.')
            elif not isinstance(data["key"], bytes):
                error_messages.append(
                    f'Error: parameter <Key> has unexpected type - {type(data["key"])}. Expected - bytes.')
                
        # check <Hash>
        if "hash" not in data or not isinstance(data["hash"], bytes):
            if "hash" not in data:
                error_messages.append('Error: no <Hash> parameter provided.')
            elif not isinstance(data["hash"], bytes):
                error_messages.append(
                    f'Error: parameter <Hash> has unexpected type - {type(data["hash"])}. Expected - bytes.')
                
        # check <Salt>
        if "salt" not in data or not isinstance(data["salt"], str):
            if "salt" not in data:
                data["salt"] = ''
            elif not isinstance(data["salt"], str):
                error_messages.append(
                    f'Error: parameter <Salt> has unexpected type - {type(data["salt"])}. Expected - string.')
                
         # check <Status>
        if "status" not in data or not isinstance(data["status"], int):
            if "status" not in data:
                error_messages.append('Error: no <Status> parameter provided.')
            elif not isinstance(data["status"], int):
                error_messages.append(
                    f'Error: parameter <Status> has unexpected type - {type(data["status"])}. Expected - integer.')
                
        # check <Description>
        if "description" not in data or not isinstance(data["description"], str) or not data["description"].strip():
            if "description" not in data:
                data["description"] = ''
            elif not isinstance(data["description"], str):
                error_messages.append(
                    f'Error: parameter <Description> has unexpected type - {type(data["description"])}. Expected - string.')
            else:
                error_messages.append(
                    'Error: parameter <Description> cannot be empty or have whitespaces only.')
"""

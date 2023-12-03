from utils.imports import grpc, asyncio, users_pb2_grpc
from client_functions.users import *


async def run() -> None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = users_pb2_grpc.UserServiceStub(channel)
        print(f"Create record users:")
        create_result = await create_record_users(
            stub, 
            {
                "user_email": "admin@gmail.com",
                "user_username": "username1",
                "admin_id": 10,
                "admin_hash": "5b3ad3145fd1518a9f8742c5fa850b60a6b82774e47bf8edf3d1ffc0d339701c".encode('utf-8'),
            }
        )
        print(create_result)

        # --0 - user, 1 - admin, 2 - analyst, 3 - developer/tester, 4 - user_admin
        create_result = await create_record_users(
            stub, 
            {
                "user_email": "user@test.com",
                "user_username": "username132",
                "admin_hash": "5b3ad3145fd1518a9f8742c5fa850b60a6b82774e47bf8edf3d1ffc0d339701b".encode('utf-8'),
                "admin_id": 1,
            }
        )
        print(create_result)

        print(f"Read record users:")
        read_result = await read_record_users(stub, {})
        print(read_result)

        print(f"Update result users:")
        update_result = await update_record_users(
            stub, 
            {
                "id": 10, 
                "hash": "5b3ad3145fd1518a9f8742c5fa850b60a6b82774e47bf8edf3d1ffc0d339701c".encode('utf-8'),
                "first_email": "anasav0004@gmail.com",
                "second_email": "anasav00041@gmail.com",
                "username": "tatasiyka8e9w89e",
                "description": "desc"
            }
        )
        print(update_result)

        print(f"Delete result users:")
        delete_result = await delete_record_users(
            stub, 
            {
                "admin_id": 10,
                "admin_hash": "5b3ad3145fd1518a9f8742c5fa850b60a6b82774e47bf8edf3d1ffc0d339701c".encode('utf-8'),
                "user_username": "username1",
                "with_data": True,
                "reason": "just bad guy"
            }
        )
        print(delete_result)

        print(f"Update user status:")
        update_status_result = await update_status_record_users(
            stub, 
            {
                "admin_id": 10,
                "admin_hash": "5b3ad3145fd1518a9f8742c5fa850b60a6b82774e47bf8edf3d1ffc0d339701c".encode('utf-8'),
                "user_username": "tatasiyka8e9w89e",
                "status": 1,
            }
        )
        print(update_status_result)

        print(f"Reset user auth:")
        reset_user_auth_result = await reset_user_auth_users(
            stub, 
            {
                "id": 10,
                "username": "tatasiyka8e9w89e",
                "hash": "5b3ad3145fd1518a9f8742c5fa850b60a6b82774e47bf8edf3d1ffc0d339701c".encode('utf-8'),
            }
        )
        print(reset_user_auth_result)

        print(f"Reset user auth by admin:")
        reset_admin_auth_result = await reset_admin_auth_users(
            stub, 
            {
                "admin_id": 10,
                "admin_hash": "5b3ad3145fd1518a9f8742c5fa850b60a6b82774e47bf8edf3d1ffc0d339701c".encode('utf-8'),
                # "user_name": "Anastasiia",
                "user_username": "username132",
                "reason": "lost key"
            }
        )
        print(reset_admin_auth_result)


if __name__ == "__main__":
    asyncio.run(run())

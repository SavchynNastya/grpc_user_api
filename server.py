from utils.servicers_imports import UsersServicer
from utils.imports import load_dotenv, grpc, asyncio, users_pb2_grpc
from database.connection_params import server_port

load_dotenv()


async def serve() -> None:
    server = grpc.aio.server(options=[
        ('grpc.max_receive_message_length', 100 * 1024 * 1024),  # 100 MB
        ('grpc.max_send_message_length', 100 * 1024 * 1024)  # 100 MB
    ])
    users_pb2_grpc.add_UserServiceServicer_to_server(
        UsersServicer(), server)
    server.add_insecure_port(f"[::]:{server_port}")
    await server.start()
    await server.wait_for_termination()

if __name__ == "__main__":
    asyncio.run(serve())

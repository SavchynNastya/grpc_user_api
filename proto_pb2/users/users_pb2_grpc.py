# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import proto_pb2.users.users_pb2 as users__pb2


class UserServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUsersRecord = channel.unary_unary(
                '/UserService/CreateUsersRecord',
                request_serializer=users__pb2.CreateUsersRequest.SerializeToString,
                response_deserializer=users__pb2.CreateUsersResponse.FromString,
                )
        self.ReadUsersRecord = channel.unary_unary(
                '/UserService/ReadUsersRecord',
                request_serializer=users__pb2.ReadUsersRequest.SerializeToString,
                response_deserializer=users__pb2.ReadUsersResponse.FromString,
                )
        self.UpdateUsersRecord = channel.unary_unary(
                '/UserService/UpdateUsersRecord',
                request_serializer=users__pb2.UpdateUsersRequest.SerializeToString,
                response_deserializer=users__pb2.UpdateUsersResponse.FromString,
                )
        self.DeleteUsersRecord = channel.unary_unary(
                '/UserService/DeleteUsersRecord',
                request_serializer=users__pb2.DeleteUsersRequest.SerializeToString,
                response_deserializer=users__pb2.DeleteUsersResponse.FromString,
                )
        self.ResetUserAuthRecord = channel.unary_unary(
                '/UserService/ResetUserAuthRecord',
                request_serializer=users__pb2.ResetUserAuthRequest.SerializeToString,
                response_deserializer=users__pb2.ResetUserAuthResponse.FromString,
                )
        self.ResetAdminAuthRecord = channel.unary_unary(
                '/UserService/ResetAdminAuthRecord',
                request_serializer=users__pb2.ResetAdminAuthRequest.SerializeToString,
                response_deserializer=users__pb2.ResetAdminAuthResponse.FromString,
                )
        self.CheckAdminRecord = channel.unary_unary(
                '/UserService/CheckAdminRecord',
                request_serializer=users__pb2.CheckAdminRequest.SerializeToString,
                response_deserializer=users__pb2.CheckAdminResponse.FromString,
                )
        self.UpdateUserStatusRecord = channel.unary_unary(
                '/UserService/UpdateUserStatusRecord',
                request_serializer=users__pb2.UpdateUserStatusRequest.SerializeToString,
                response_deserializer=users__pb2.UpdateUserStatusResponse.FromString,
                )


class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateUsersRecord(self, request, context):
        """USERS
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadUsersRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUsersRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUsersRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetUserAuthRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetAdminAuthRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAdminRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUserStatusRecord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUsersRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUsersRecord,
                    request_deserializer=users__pb2.CreateUsersRequest.FromString,
                    response_serializer=users__pb2.CreateUsersResponse.SerializeToString,
            ),
            'ReadUsersRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadUsersRecord,
                    request_deserializer=users__pb2.ReadUsersRequest.FromString,
                    response_serializer=users__pb2.ReadUsersResponse.SerializeToString,
            ),
            'UpdateUsersRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUsersRecord,
                    request_deserializer=users__pb2.UpdateUsersRequest.FromString,
                    response_serializer=users__pb2.UpdateUsersResponse.SerializeToString,
            ),
            'DeleteUsersRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUsersRecord,
                    request_deserializer=users__pb2.DeleteUsersRequest.FromString,
                    response_serializer=users__pb2.DeleteUsersResponse.SerializeToString,
            ),
            'ResetUserAuthRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetUserAuthRecord,
                    request_deserializer=users__pb2.ResetUserAuthRequest.FromString,
                    response_serializer=users__pb2.ResetUserAuthResponse.SerializeToString,
            ),
            'ResetAdminAuthRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetAdminAuthRecord,
                    request_deserializer=users__pb2.ResetAdminAuthRequest.FromString,
                    response_serializer=users__pb2.ResetAdminAuthResponse.SerializeToString,
            ),
            'CheckAdminRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAdminRecord,
                    request_deserializer=users__pb2.CheckAdminRequest.FromString,
                    response_serializer=users__pb2.CheckAdminResponse.SerializeToString,
            ),
            'UpdateUserStatusRecord': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUserStatusRecord,
                    request_deserializer=users__pb2.UpdateUserStatusRequest.FromString,
                    response_serializer=users__pb2.UpdateUserStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateUsersRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UserService/CreateUsersRecord',
            users__pb2.CreateUsersRequest.SerializeToString,
            users__pb2.CreateUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadUsersRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UserService/ReadUsersRecord',
            users__pb2.ReadUsersRequest.SerializeToString,
            users__pb2.ReadUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUsersRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UserService/UpdateUsersRecord',
            users__pb2.UpdateUsersRequest.SerializeToString,
            users__pb2.UpdateUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUsersRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UserService/DeleteUsersRecord',
            users__pb2.DeleteUsersRequest.SerializeToString,
            users__pb2.DeleteUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetUserAuthRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UserService/ResetUserAuthRecord',
            users__pb2.ResetUserAuthRequest.SerializeToString,
            users__pb2.ResetUserAuthResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetAdminAuthRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UserService/ResetAdminAuthRecord',
            users__pb2.ResetAdminAuthRequest.SerializeToString,
            users__pb2.ResetAdminAuthResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAdminRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UserService/CheckAdminRecord',
            users__pb2.CheckAdminRequest.SerializeToString,
            users__pb2.CheckAdminResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUserStatusRecord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UserService/UpdateUserStatusRecord',
            users__pb2.UpdateUserStatusRequest.SerializeToString,
            users__pb2.UpdateUserStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

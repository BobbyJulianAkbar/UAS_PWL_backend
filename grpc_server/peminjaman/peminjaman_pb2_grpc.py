# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import peminjaman_pb2 as peminjaman__pb2


class PeminjamanServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPeminjamanList = channel.unary_unary(
                '/peminjaman.PeminjamanService/GetPeminjamanList',
                request_serializer=peminjaman__pb2.PeminjamanListRequest.SerializeToString,
                response_deserializer=peminjaman__pb2.PeminjamanListResponse.FromString,
                )
        self.GetPeminjaman = channel.unary_unary(
                '/peminjaman.PeminjamanService/GetPeminjaman',
                request_serializer=peminjaman__pb2.PeminjamanRequest.SerializeToString,
                response_deserializer=peminjaman__pb2.PeminjamanResponse.FromString,
                )
        self.CreatePeminjaman = channel.unary_unary(
                '/peminjaman.PeminjamanService/CreatePeminjaman',
                request_serializer=peminjaman__pb2.PeminjamanCreateRequest.SerializeToString,
                response_deserializer=peminjaman__pb2.PeminjamanCreateResponse.FromString,
                )
        self.UpdatePeminjaman = channel.unary_unary(
                '/peminjaman.PeminjamanService/UpdatePeminjaman',
                request_serializer=peminjaman__pb2.PeminjamanUpdateRequest.SerializeToString,
                response_deserializer=peminjaman__pb2.PeminjamanUpdateResponse.FromString,
                )
        self.DeletePeminjaman = channel.unary_unary(
                '/peminjaman.PeminjamanService/DeletePeminjaman',
                request_serializer=peminjaman__pb2.PeminjamanDeleteRequest.SerializeToString,
                response_deserializer=peminjaman__pb2.PeminjamanDeleteResponse.FromString,
                )


class PeminjamanServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetPeminjamanList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPeminjaman(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePeminjaman(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePeminjaman(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeletePeminjaman(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PeminjamanServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPeminjamanList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPeminjamanList,
                    request_deserializer=peminjaman__pb2.PeminjamanListRequest.FromString,
                    response_serializer=peminjaman__pb2.PeminjamanListResponse.SerializeToString,
            ),
            'GetPeminjaman': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPeminjaman,
                    request_deserializer=peminjaman__pb2.PeminjamanRequest.FromString,
                    response_serializer=peminjaman__pb2.PeminjamanResponse.SerializeToString,
            ),
            'CreatePeminjaman': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePeminjaman,
                    request_deserializer=peminjaman__pb2.PeminjamanCreateRequest.FromString,
                    response_serializer=peminjaman__pb2.PeminjamanCreateResponse.SerializeToString,
            ),
            'UpdatePeminjaman': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePeminjaman,
                    request_deserializer=peminjaman__pb2.PeminjamanUpdateRequest.FromString,
                    response_serializer=peminjaman__pb2.PeminjamanUpdateResponse.SerializeToString,
            ),
            'DeletePeminjaman': grpc.unary_unary_rpc_method_handler(
                    servicer.DeletePeminjaman,
                    request_deserializer=peminjaman__pb2.PeminjamanDeleteRequest.FromString,
                    response_serializer=peminjaman__pb2.PeminjamanDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'peminjaman.PeminjamanService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PeminjamanService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetPeminjamanList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/peminjaman.PeminjamanService/GetPeminjamanList',
            peminjaman__pb2.PeminjamanListRequest.SerializeToString,
            peminjaman__pb2.PeminjamanListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPeminjaman(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/peminjaman.PeminjamanService/GetPeminjaman',
            peminjaman__pb2.PeminjamanRequest.SerializeToString,
            peminjaman__pb2.PeminjamanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreatePeminjaman(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/peminjaman.PeminjamanService/CreatePeminjaman',
            peminjaman__pb2.PeminjamanCreateRequest.SerializeToString,
            peminjaman__pb2.PeminjamanCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdatePeminjaman(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/peminjaman.PeminjamanService/UpdatePeminjaman',
            peminjaman__pb2.PeminjamanUpdateRequest.SerializeToString,
            peminjaman__pb2.PeminjamanUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeletePeminjaman(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/peminjaman.PeminjamanService/DeletePeminjaman',
            peminjaman__pb2.PeminjamanDeleteRequest.SerializeToString,
            peminjaman__pb2.PeminjamanDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

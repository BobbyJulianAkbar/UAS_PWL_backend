# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import rest.grpc_client.kategori.kategori_pb2 as kategori__pb2


class KategoriServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
            "/kategori.KategoriService/Get",
            request_serializer=kategori__pb2.KategoriRequest.SerializeToString,
            response_deserializer=kategori__pb2.KategoriResponse.FromString,
        )
        self.List = channel.unary_unary(
            "/kategori.KategoriService/List",
            request_serializer=kategori__pb2.KategoriListRequest.SerializeToString,
            response_deserializer=kategori__pb2.KategoriListResponse.FromString,
        )
        self.Create = channel.unary_unary(
            "/kategori.KategoriService/Create",
            request_serializer=kategori__pb2.KategoriCreateRequest.SerializeToString,
            response_deserializer=kategori__pb2.KategoriCreateResponse.FromString,
        )
        self.Update = channel.unary_unary(
            "/kategori.KategoriService/Update",
            request_serializer=kategori__pb2.KategoriUpdateRequest.SerializeToString,
            response_deserializer=kategori__pb2.KategoriUpdateResponse.FromString,
        )
        self.Delete = channel.unary_unary(
            "/kategori.KategoriService/Delete",
            request_serializer=kategori__pb2.KategoriDeleteRequest.SerializeToString,
            response_deserializer=kategori__pb2.KategoriDeleteResponse.FromString,
        )


class KategoriServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_KategoriServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Get": grpc.unary_unary_rpc_method_handler(
            servicer.Get,
            request_deserializer=kategori__pb2.KategoriRequest.FromString,
            response_serializer=kategori__pb2.KategoriResponse.SerializeToString,
        ),
        "List": grpc.unary_unary_rpc_method_handler(
            servicer.List,
            request_deserializer=kategori__pb2.KategoriListRequest.FromString,
            response_serializer=kategori__pb2.KategoriListResponse.SerializeToString,
        ),
        "Create": grpc.unary_unary_rpc_method_handler(
            servicer.Create,
            request_deserializer=kategori__pb2.KategoriCreateRequest.FromString,
            response_serializer=kategori__pb2.KategoriCreateResponse.SerializeToString,
        ),
        "Update": grpc.unary_unary_rpc_method_handler(
            servicer.Update,
            request_deserializer=kategori__pb2.KategoriUpdateRequest.FromString,
            response_serializer=kategori__pb2.KategoriUpdateResponse.SerializeToString,
        ),
        "Delete": grpc.unary_unary_rpc_method_handler(
            servicer.Delete,
            request_deserializer=kategori__pb2.KategoriDeleteRequest.FromString,
            response_serializer=kategori__pb2.KategoriDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "kategori.KategoriService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class KategoriService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Get(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/kategori.KategoriService/Get",
            kategori__pb2.KategoriRequest.SerializeToString,
            kategori__pb2.KategoriResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def List(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/kategori.KategoriService/List",
            kategori__pb2.KategoriListRequest.SerializeToString,
            kategori__pb2.KategoriListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Create(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/kategori.KategoriService/Create",
            kategori__pb2.KategoriCreateRequest.SerializeToString,
            kategori__pb2.KategoriCreateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Update(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/kategori.KategoriService/Update",
            kategori__pb2.KategoriUpdateRequest.SerializeToString,
            kategori__pb2.KategoriUpdateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Delete(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/kategori.KategoriService/Delete",
            kategori__pb2.KategoriDeleteRequest.SerializeToString,
            kategori__pb2.KategoriDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
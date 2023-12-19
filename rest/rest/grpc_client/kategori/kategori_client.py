import rest.grpc_client.kategori.kategori_pb2_grpc as kategori_pb2_grpc
import rest.grpc_client.kategori.kategori_pb2 as kategori_pb2
import grpc


class KategoriClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5005

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = kategori_pb2_grpc.KategoriServiceStub(self.channel)

    def list_kategori(self):
        response = self.stub.List(kategori_pb2.KategoriListRequest())

        if len(response.kategori) == 0:
            return None

        return [
            dict(id=kategori.id, nama=kategori.nama) for kategori in response.kategori
        ]

    def create_kategori(self, nama):
        response = self.stub.Create(kategori_pb2.KategoriCreateRequest(nama=nama))

        if response is None:
            return None

        return dict(id=response.id, nama=response.nama)

    def update_kategori(self, id, nama):
        response = self.stub.Update(
            kategori_pb2.KategoriUpdateRequest(id=id, nama=nama)
        )

        if response is None:
            return None

        return dict(id=response.id, nama=response.nama)

    def get_kategori(self, id):
        response = self.stub.Get(kategori_pb2.KategoriRequest(id=id))

        if response is None:
            return None

        return dict(id=response.kategori.id, nama=response.kategori.nama)

    def delete_kategori(self, id):
        response = self.stub.Delete(kategori_pb2.KategoriRequest(id=id))

        if response is None:
            return None

        return dict(message=response.message)

from pyramid.view import view_config, view_defaults
from pyramid.response import Response

from rest.grpc_client.kategori.kategori_client import KategoriClient


@view_defaults(route_name="kategori", renderer="json")
class KategoriController:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET")
    def get(self):
        try:
            if self.request.params.get("id") is not None:
                client = KategoriClient()
                result = client.get_kategori(int(self.request.params.get("id")))

                if result == None:
                    return Response(
                        status=404,
                        json_body={"status": False, "message": "Not Found"},
                    )

                return result
            client = KategoriClient()
            result = client.list_kategori()

            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(request_method="POST")
    def post(self):
        try:
            if "nama" not in self.request.json_body:
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "Nama kategori harus diisi",
                    },
                )

            client = KategoriClient()
            result = client.create_kategori(self.request.json_body["nama"])

            if result == None:
                return Response(
                    status=400,
                    json_body={"status": False, "message": "Gagal membuat kategori"},
                )

            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(request_method="PUT")
    def put(self):
        try:
            if (
                "id" not in self.request.json_body
                or "nama" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "ID dan nama kategori harus diisi",
                    },
                )

            client = KategoriClient()
            result = client.update_kategori(
                self.request.json_body["id"], self.request.json_body["nama"]
            )

            if result == None:
                return Response(
                    status=400,
                    json_body={"status": False, "message": "Gagal mengubah kategori"},
                )

            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(request_method="DELETE")
    def delete(self):
        try:
            if self.request.params.get("id") is None:
                return Response(
                    status=400,
                    json_body={"status": False, "message": "ID harus diisi"},
                )

            client = KategoriClient()
            result = client.delete_kategori(int(self.request.params.get("id")))

            if result == None:
                return Response(
                    status=400,
                    json_body={"status": False, "message": "Gagal menghapus kategori"},
                )

            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

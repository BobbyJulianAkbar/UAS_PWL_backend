from pyramid.view import view_config, view_defaults
from pyramid.response import Response

from rest.grpc_client.buku.client import BukuClient
import grpc


@view_defaults(route_name="buku", renderer="json")
class BukuController:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET")
    def get(self):
        try:
            if self.request.params.get("id") is not None:
                client = BukuClient()
                result = client.get_buku(int(self.request.params.get("id")))

                if result == None:
                    return Response(
                        status=404,
                        json_body={"status": False, "message": "Not Found"},
                    )

                return result
            client = BukuClient()
            result = client.list_buku()

            return result

        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(request_method="POST")
    def post(self):
        try:
            if (
                "judul" not in self.request.json_body
                or "pengarang" not in self.request.json_body
                or "penerbit" not in self.request.json_body
                or "tahun_terbit" not in self.request.json_body
                or "kategori_id" not in self.request.json_body
                or "isbn" not in self.request.json_body
                or "jumlah_buku" not in self.request.json_body
                or "deskripsi" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "Judul, pengarang, penerbit, tahun_terbit, kategori_id, isbn, jumlah_buku, dan deskripsi harus diisi",
                    },
                )

            client = BukuClient()
            result = client.create_buku(
                self.request.json_body["judul"],
                self.request.json_body["pengarang"],
                self.request.json_body["penerbit"],
                self.request.json_body["tahun_terbit"],
                self.request.json_body["kategori_id"],
                self.request.json_body["isbn"],
                self.request.json_body["jumlah_buku"],
                self.request.json_body["deskripsi"],
            )

            if result == None:
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "Judul, pengarang, penerbit, tahun_terbit, kategori_id, isbn, jumlah_buku, dan deskripsi harus diisi",
                    },
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
                    json_body={
                        "status": False,
                        "message": "ID harus diisi",
                    },
                )

            client = BukuClient()
            result = client.delete_buku(int(self.request.params.get("id")))

            if result == None:
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "ID harus diisi",
                    },
                )

            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

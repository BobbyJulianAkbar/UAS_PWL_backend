from pyramid.view import view_config, view_defaults
from pyramid.response import Response

from rest.grpc_client.peminjaman.peminjaman_cleint import PeminjamanClient


@view_defaults(route_name="peminjaman", renderer="json")
class PeminjamanController:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET")
    def get(self):
        try:
            if self.request.params.get("id") is not None:
                client = PeminjamanClient()
                result = client.get_peminjaman(int(self.request.params.get("id")))

                if result == None:
                    return Response(
                        status=404,
                        json_body={"status": False, "message": "Not Found"},
                    )

                return result
            client = PeminjamanClient()
            result = client.list_peminjaman()

            if result == None:
                return Response(
                    status=404,
                    json_body={"status": False, "message": "Not Found"},
                )

            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(request_method="POST")
    def post(self):
        try:
            if "id_buku" not in self.request.json_body:
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "id_buku harus diisi",
                    },
                )
            if "id_anggota" not in self.request.json_body:
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "id_anggota harus diisi",
                    },
                )
            if "tanggal_peminjaman" not in self.request.json_body:
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "tanggal_peminjaman harus diisi",
                    },
                )
            if "tanggal_pengembalian" not in self.request.json_body:
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "tanggal_pengembalian harus diisi",
                    },
                )

            client = PeminjamanClient()
            result = client.create_peminjaman(
                self.request.json_body["id_buku"],
                self.request.json_body["id_anggota"],
                self.request.json_body["tanggal_peminjaman"],
                self.request.json_body["tanggal_pengembalian"],
                "dipinjam",
            )

            if result == None:
                return Response(
                    status=400,
                    json_body={"status": False, "message": "Gagal membuat peminjaman"},
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
                        "message": "id harus diisi",
                    },
                )

            client = PeminjamanClient()
            result = client.delete_peminjaman(int(self.request.params.get("id")))

            if result == None:
                return Response(
                    status=404,
                    json_body={"status": False, "message": "Not Found"},
                )

            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

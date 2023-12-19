from pyramid.view import view_config, view_defaults
from pyramid.response import Response

from rest.grpc_client.anggota.anggota_client import AnggotaClient


@view_defaults(route_name="anggota", renderer="json")
class AnggotaController:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET")
    def get(self):
        try:
            if self.request.params.get("id") is not None:
                client = AnggotaClient()
                result = client.get_anggota(int(self.request.params.get("id")))

                if result == None:
                    return Response(
                        status=404,
                        json_body={"status": False, "message": "Not Found"},
                    )

                return result
            client = AnggotaClient()
            result = client.list_anggota()

            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(request_method="POST")
    def post(self):
        try:
            if (
                "nama" not in self.request.json_body
                or "email" not in self.request.json_body
                or "nis" not in self.request.json_body
                or "password" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "Nama, email, nis, dan password harus diisi",
                    },
                )

            client = AnggotaClient()
            result = client.create_anggota(
                self.request.json_body["nama"],
                self.request.json_body["email"],
                self.request.json_body["nis"],
                self.request.json_body["password"],
            )

            if result == None:
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "Gagal mendaftarkan anggota",
                    },
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
                or "email" not in self.request.json_body
                or "nis" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "ID, nama, email, dan nis harus diisi",
                    },
                )

            client = AnggotaClient()
            result = client.update_anggota(
                self.request.json_body["id"],
                self.request.json_body["nama"],
                self.request.json_body["email"],
                self.request.json_body["nis"],
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

            client = AnggotaClient()
            result = client.delete_anggota(int(self.request.params.get("id")))

            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(route_name="login-anggota", request_method="POST")
    def login(self):
        try:
            if (
                "email" not in self.request.json_body
                or "password" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "Email dan password harus diisi",
                    },
                )

            client = AnggotaClient()
            result = client.login_anggota(
                self.request.json_body["email"],
                self.request.json_body["password"],
            )

            if result == None:
                return Response(
                    status=401,
                    json_body={"status": False, "message": "Login gagal"},
                )

            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(route_name="logout-anggota", request_method="POST")
    def logout(self):
        try:
            if "token" not in self.request.json_body:
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "Token harus diisi",
                    },
                )

            client = AnggotaClient()
            result = client.logout_anggota(
                self.request.json_body["token"],
            )

            if result == None:
                return Response(
                    status=401,
                    json_body={"status": False, "message": "Logout gagal"},
                )

            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

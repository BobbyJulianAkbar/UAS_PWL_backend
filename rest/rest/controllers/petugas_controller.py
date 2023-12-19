import traceback
from pyramid.view import view_config, view_defaults
from pyramid.response import Response

from rest.grpc_client.petugas.petugas_client import PetugasClient


@view_defaults(route_name="petugas", renderer="json")
class PetugasController:
    def __init__(self, request):
        self.request = request

    @view_config(renderer="json", request_method="OPTIONS")
    def options(self):
        return dict()

    @view_config(request_method="GET")
    def get(self):
        try:
            if self.request.params.get("id") is not None:
                client = PetugasClient()
                result = client.get_petugas(int(self.request.params.get("id")))

                if result == None:
                    return Response(
                        status=404,
                        json_body={"status": False, "message": "Not Found"},
                    )

                return result
            client = PetugasClient()
            result = client.list_petugas()

            return result
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(request_method="POST")
    def post(self):
        try:
            if (
                "fnama" not in self.request.json_body
                or "email" not in self.request.json_body
                or "password" not in self.request.json_body
                or "username" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "Nama, email, password, username harus diisi",
                    },
                )

            client = PetugasClient()
            result = client.create_petugas(
                self.request.json_body["fnama"],
                self.request.json_body["email"],
                self.request.json_body["password"],
                self.request.json_body["username"],
            )

            if result == None:
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "Gagal membuat petugas",
                    },
                )

            return Response(
                status=201,
                json_body={
                    "status": True,
                    "message": "Berhasil membuat petugas",
                    "data": result,
                },
            )
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(request_method="PUT")
    def put(self):
        try:
            if (
                "id" not in self.request.json_body
                or "fnama" not in self.request.json_body
                or "email" not in self.request.json_body
                or "password" not in self.request.json_body
                or "username" not in self.request.json_body
                or "status" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "Nama, email, password, username, dan status harus diisi",
                    },
                )

            client = PetugasClient()
            result = client.update_petugas(
                self.request.json_body["id"],
                self.request.json_body["fnama"],
                self.request.json_body["email"],
                self.request.json_body["password"],
                self.request.json_body["username"],
                self.request.json_body["status"],
            )

            if result == None:
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "Gagal membuat petugas",
                    },
                )

            return Response(
                status=201,
                json_body={
                    "status": True,
                    "message": "Berhasil membuat petugas",
                    "data": result,
                },
            )
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

            client = PetugasClient()
            result = client.delete_petugas(int(self.request.params.get("id")))

            if result == None:
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "Gagal menghapus petugas",
                    },
                )

            return Response(
                status=201,
                json_body={
                    "status": True,
                    "message": "Berhasil menghapus petugas",
                    "data": result,
                },
            )
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(route_name="petugas_login", request_method="POST")
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

            client = PetugasClient()
            result = client.login_petugas(
                self.request.json_body["email"],
                self.request.json_body["password"],
            )

            if result == None:
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "Gagal login",
                    },
                )

            return result
        except Exception as e:
            print(traceback.format_exc())

            return Response(json_body={"error": {"message": str(e)}}, status=500)

    @view_config(route_name="petugas_logout", request_method="POST")
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

            client = PetugasClient()
            result = client.logout_petugas(
                self.request.json_body["token"],
            )

            if result == None:
                return Response(
                    status=400,
                    json_body={
                        "status": False,
                        "message": "Gagal logout",
                    },
                )

            return Response(
                status=201,
                json_body={
                    "status": True,
                    "message": "Berhasil logout",
                    "data": result,
                },
            )
        except Exception as e:
            return Response(json_body={"error": {"message": str(e)}}, status=500)

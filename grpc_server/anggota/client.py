import anggota_pb2_grpc as anggota_pb2_grpc
import anggota_pb2 as anggota_pb2
import grpc


class AnggotaClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5001

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = anggota_pb2_grpc.AnggotaServiceStub(self.channel)

    def list_anggota(self):
        response = self.stub.List(anggota_pb2.AnggotaListRequest())

        if len(response.anggota) == 0:
            return None

        return [
            dict(
                id=anggota.id,
                nama=anggota.nama,
                email=anggota.email,
                nis=anggota.nis,
            )
            for anggota in response.anggota
        ]

    def create_anggota(self, nama, email, nis, password):
        response = self.stub.Create(
            anggota_pb2.AnggotaCreateRequest(
                nama=nama, email=email, nis=nis, password=password
            )
        )

        if response is None:
            return None

        return dict(
            nama=response.anggota.nama,
            email=response.anggota.email,
            nis=response.anggota.nis,
            password=response.anggota.password,
        )

    def get_anggota(self, id):
        response = self.stub.Get(anggota_pb2.AnggotaRequest(id=id))

        if response is None:
            return None

        return dict(
            id=response.anggota.id,
            nama=response.anggota.nama,
            email=response.anggota.email,
            nis=response.anggota.nis,
        )

    def update_anggota(self, id, nama, email, nis):
        response = self.stub.Update(
            anggota_pb2.AnggotaUpdateRequest(id=id, nama=nama, email=email, nis=nis)
        )

        if response is None:
            return None

        return dict(
            id=response.anggota.id,
            nama=response.anggota.nama,
            email=response.anggota.email,
            nis=response.anggota.nis,
        )

    def delete_anggota(self, id):
        response = self.stub.Delete(anggota_pb2.AnggotaRequest(id=id))

        if response is None:
            return None

        return dict(
            message=response.message,
        )

    def login_anggota(self, email, password):
        response = self.stub.Login(
            anggota_pb2.AnggotaLoginRequest(email=email, password=password)
        )

        if response is None:
            return None

        return dict(
            token=response.token,
        )

    def logout_anggota(self, token):
        response = self.stub.Logout(anggota_pb2.AnggotaLogoutRequest(token=token))

        if response is None:
            return None

        return dict(
            message=response.message,
        )


if __name__ == "__main__":
    # create program to select action by input until exit
    while True:
        print("1. List Anggota")
        print("2. Create Anggota")
        print("3. Update Anggota")
        print("4. Delete Anggota")
        print("5. Get Anggota")
        print("6. Login")
        print("7. Logout")

        action = input("Select action: ")

        if action == "1":
            client = AnggotaClient()
            print(client.list_anggota())
        elif action == "2":
            client = AnggotaClient()
            print(
                client.create_anggota(
                    "Anggota 3", "anggota3@gmail.com", "123456879", "password"
                )
            )

        elif action == "3":
            client = AnggotaClient()
            id = input("Input id: ")
            print(
                client.update_anggota(
                    int(id),
                    "test update",
                    "test update",
                    "test update",
                )
            )

        elif action == "4":
            client = AnggotaClient()
            id = input("Input id: ")
            print(client.delete_anggota(int(id)))
        elif action == "5":
            client = AnggotaClient()
            print(client.get_anggota(5))

        elif action == "6":
            client = AnggotaClient()
            email = input("Input email: ")
            password = input("Input password: ")

            print(client.login_anggota(email, password))

        elif action == "7":
            client = AnggotaClient()
            token = input("Input token: ")

            print(client.logout_anggota(token))
        else:
            break

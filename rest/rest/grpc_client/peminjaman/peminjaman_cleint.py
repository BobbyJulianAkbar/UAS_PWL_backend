import traceback
import rest.grpc_client.peminjaman.peminjaman_pb2_grpc as peminjaman_pb2_grpc
import rest.grpc_client.peminjaman.peminjaman_pb2 as peminjaman_pb2
import grpc

from rest.grpc_client.buku.client import BukuClient
from rest.grpc_client.anggota.anggota_client import AnggotaClient


class PeminjamanClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5006

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = peminjaman_pb2_grpc.PeminjamanServiceStub(self.channel)

    def list_peminjaman(self):
        try:
            response = self.stub.GetPeminjamanList(
                peminjaman_pb2.PeminjamanListRequest()
            )

            if response == None or len(response.peminjaman) == 0:
                return None

            buku_client = BukuClient()

            anggota_client = AnggotaClient()

            return [
                dict(
                    id=peminjaman.id,
                    id_buku=peminjaman.id_buku,
                    id_anggota=peminjaman.id_anggota,
                    tanggal_peminjaman=peminjaman.tanggal_peminjaman,
                    tanggal_pengembalian=peminjaman.tanggal_pengembalian,
                    status=peminjaman.status,
                    buku=buku_client.get_buku(peminjaman.id_buku),
                    anggota=anggota_client.get_anggota(peminjaman.id_anggota),
                )
                for peminjaman in response.peminjaman
            ]
        except grpc.RpcError as e:
            print(
                f"RPC Error: {e.code()}\nDetails: {e.details()}\nDebug info: {e.debug_error_string()}"
            )
            return None
        except Exception as e:
            print(traceback.format_exc())
            print(f"Error: {e}")
            return None

    def get_peminjaman(self, id):
        response = self.stub.GetPeminjaman(peminjaman_pb2.PeminjamanRequest(id=id))

        if response is None:
            return None

        buku_client = BukuClient()

        anggota_client = AnggotaClient()

        return dict(
            id=response.peminjaman.id,
            id_buku=response.peminjaman.id_buku,
            id_anggota=response.peminjaman.id_anggota,
            tanggal_peminjaman=response.peminjaman.tanggal_peminjaman,
            tanggal_pengembalian=response.peminjaman.tanggal_pengembalian,
            status=response.peminjaman.status,
            buku=buku_client.get_buku(response.peminjaman.id_buku),
            anggota=anggota_client.get_anggota(response.peminjaman.id_anggota),
        )

    def create_peminjaman(
        self, id_buku, id_anggota, tanggal_peminjaman, tanggal_pengembalian, status
    ):
        response = self.stub.CreatePeminjaman(
            peminjaman_pb2.PeminjamanCreateRequest(
                id_buku=id_buku,
                id_anggota=id_anggota,
                tanggal_peminjaman=tanggal_peminjaman,
                tanggal_pengembalian=tanggal_pengembalian,
                status=status,
            )
        )

        if response is None:
            return None

        buku_client = BukuClient()

        anggota_client = AnggotaClient()

        return dict(
            id=response.peminjaman.id,
            id_buku=response.peminjaman.id_buku,
            id_anggota=response.peminjaman.id_anggota,
            tanggal_peminjaman=response.peminjaman.tanggal_peminjaman,
            tanggal_pengembalian=response.peminjaman.tanggal_pengembalian,
            status=response.peminjaman.status,
            buku=buku_client.get_buku(response.peminjaman.id_buku),
            anggota=anggota_client.get_anggota(response.peminjaman.id_anggota),
        )

    def update_peminjaman(
        self, id, id_buku, id_anggota, tanggal_peminjaman, tanggal_pengembalian, status
    ):
        response = self.stub.UpdatePeminjaman(
            peminjaman_pb2.PeminjamanUpdateRequest(
                id=id,
                id_buku=id_buku,
                id_anggota=id_anggota,
                tanggal_peminjaman=tanggal_peminjaman,
                tanggal_pengembalian=tanggal_pengembalian,
                status=status,
            )
        )

        if response is None:
            return None

        return dict(message=response.message)

    def delete_peminjaman(self, id):
        response = self.stub.DeletePeminjaman(
            peminjaman_pb2.PeminjamanDeleteRequest(id=id)
        )

        if response is None:
            return None

        return dict(message=response.message)

    def get_peminjaman_by_buku_id(self, id_buku):
        response = self.stub.GetPeminjamanList(peminjaman_pb2.PeminjamanListRequest())

        if response == None or len(response.peminjaman) == 0:
            return None

        jumlah = 0

        for peminjaman in response.peminjaman:
            if peminjaman.id_buku == id_buku:
                jumlah += 1

        return jumlah


# if __name__ == "__main__":
#     while True:
#         print("Choose an option:")
#         print("1. List Peminjaman")
#         print("2. Create Peminjaman")
#         print("3. Update Peminjaman")
#         print("4. Delete Peminjaman")
#         print("5. Get Peminjaman")
#         print("6. Exit")
#         choice = input("Enter your choice (1-6): ")

#         if choice == "1":
#             peminjaman = PeminjamanClient()
#             print(peminjaman.list_peminjaman())
#         elif choice == "2":
#             id_buku = input("Enter id_buku: ")
#             id_anggota = input("Enter id_anggota: ")
#             tanggal_peminjaman = input("Enter tanggal_peminjaman: ")
#             tanggal_pengembalian = input("Enter tanggal_pengembalian: ")
#             status = input("Enter status: ")
#             peminjaman = PeminjamanClient()
#             print(peminjaman.create_peminjaman(int(id_buku),int(id_anggota),tanggal_peminjaman,tanggal_pengembalian,status))
#         elif choice == '3':
#             id = input("Enter id: ")
#             id_buku = input("Enter id_buku: ")
#             id_anggota = input("Enter id_anggota: ")
#             tanggal_peminjaman = input("Enter tanggal_peminjaman: ")
#             tanggal_pengembalian = input("Enter tanggal_pengembalian: ")
#             status = input("Enter status: ")
#             peminjaman = PeminjamanClient()
#             print(peminjaman.update_peminjaman(int(id),int(id_buku),int(id_anggota),tanggal_peminjaman,tanggal_pengembalian,status))
#         elif choice == '4':
#             id = input("Enter id: ")
#             peminjaman = PeminjamanClient()
#             print(peminjaman.delete_peminjaman(int(id)))
#         elif choice == '5':
#             id = input("Enter id: ")
#             peminjaman = PeminjamanClient()
#             print(peminjaman.get_peminjaman(int(id)))
#         elif choice == '6':
#             break

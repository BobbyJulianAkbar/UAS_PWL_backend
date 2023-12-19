import buku_pb2_grpc as buku_pb2_grpc
import buku_pb2 as buku_pb2
import grpc


class BukuClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5004

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = buku_pb2_grpc.BukuServiceStub(self.channel)

    def list_buku(self):
        response = self.stub.List(buku_pb2.BukuListRequest())

        if len(response.buku) == 0:
            return None

        return [
            dict(
                id=buku.id,
                judul=buku.judul,
                pengarang=buku.pengarang,
                penerbit=buku.penerbit,
                tahun_terbit=buku.tahun_terbit,
                kategori_id=buku.kategori_id,
                isbn=buku.isbn,
                jumlah_buku=buku.jumlah_buku,
                deskripsi=buku.deskripsi,
            )
            for buku in response.buku
        ]

    def create_buku(
        self,
        judul,
        pengarang,
        penerbit,
        tahun_terbit,
        kategori_id,
        isbn,
        jumlah_buku,
        deskripsi,
    ):
        try:
            response = self.stub.Create(
                buku_pb2.BukuCreateRequest(
                    judul=judul,
                    pengarang=pengarang,
                    penerbit=penerbit,
                    tahun_terbit=tahun_terbit,
                    kategori_id=int(kategori_id),
                    isbn=isbn,
                    jumlah_buku=int(jumlah_buku),
                    deskripsi=deskripsi,
                )
            )

            if response is None:
                return None

            return dict(
                id=response.buku.id,
                judul=response.buku.judul,
                pengarang=response.buku.pengarang,
                penerbit=response.buku.penerbit,
                tahun_terbit=response.buku.tahun_terbit,
                kategori_id=response.buku.kategori_id,
                isbn=response.buku.isbn,
                jumlah_buku=response.buku.jumlah_buku,
                deskripsi=response.buku.deskripsi,
            )
        except grpc.RpcError as e:
            print(e)
            return None


if __name__ == "__main__":
    while True:
        print("1. List Buku")
        print("2. Create Buku")
        print("3. Update Buku")
        print("4. Delete Buku")
        print("5. Exit")

        option = input("Masukkan pilihan: ")

        if option == "1":
            client = BukuClient()
            print(client.list_buku())
        elif option == "2":
            client = BukuClient()
            judul = input("Judul: ")
            pengarang = input("Pengarang: ")
            penerbit = input("Penerbit: ")
            tahun_terbit = input("Tahun Terbit: ")
            kategori_id = input("Kategori ID: ")
            isbn = input("ISBN: ")
            jumlah_buku = input("Jumlah Buku: ")
            deskripsi = input("Deskripsi: ")
            print(
                client.create_buku(
                    judul,
                    pengarang,
                    penerbit,
                    tahun_terbit,
                    kategori_id,
                    isbn,
                    jumlah_buku,
                    deskripsi,
                )
            )

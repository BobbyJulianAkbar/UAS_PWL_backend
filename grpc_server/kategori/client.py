import kategori_pb2_grpc as kategori_pb2_grpc
import kategori_pb2 as kategori_pb2
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
            dict(
                id=kategori.id,
                nama=kategori.nama
            )
            for kategori in response.kategori
        ]
    
    def create_kategori(self, nama):
        response = self.stub.Create(
            kategori_pb2.KategoriCreateRequest(
                nama=nama
            )
        )
        
        if response is None:
            return None
        
        return dict(
            id=response.id,
            nama=response.nama
        )
    
    def update_kategori(self, id, nama):
        response = self.stub.Update(
            kategori_pb2.KategoriUpdateRequest(
                id=id,
                nama=nama
            )
        )
        
        if response is None:
            return None
        
        return dict(
            id=response.id,
            nama=response.nama
        )
    
    def get_kategori(self, id):
        response = self.stub.Get(kategori_pb2.KategoriRequest(id=id))
        
        if response is None:
            return None
        
        return dict(
            id=response.kategori.id,
            nama=response.kategori.nama
        )
    
    def delete_kategori(self, id):
        response = self.stub.Delete(kategori_pb2.KategoriRequest(id=id))
        
        if response is None:
            return None
        
        return dict(
            message=response.message
        )

if __name__ == "__main__":
    while True:
        print("Kategori Client")
        print("1. List Kategori")
        print("2. Create Kategori")
        print("3. Update Kategori")
        print("4. Get Kategori")
        print("5. Delete Kategori")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            kategori_client = KategoriClient()
            kategoris = kategori_client.list_kategori()
            print(kategoris)
        elif choice == "2":
            kategori_client = KategoriClient()
            nama = input("Enter nama: ")
            kategori = kategori_client.create_kategori(nama)
            print(kategori)
        elif choice == "3":
            kategori_client = KategoriClient()
            id = input("Enter id: ")
            nama = input("Enter nama: ")
            kategori = kategori_client.update_kategori(int(id), nama)
            print(kategori)
        elif choice == "4":
            kategori_client = KategoriClient()
            id = input("Enter id: ")
            kategori = kategori_client.get_kategori(int(id))
            print(kategori)
        elif choice == "5":
            kategori_client = KategoriClient()
            id = input("Enter id: ")
            kategori = kategori_client.delete_kategori(int(id))
            print(kategori)
        elif choice == "6":
            break
        else:
            print("Invalid choice")
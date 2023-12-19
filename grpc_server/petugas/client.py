import petugas_pb2_grpc as petugas_pb2_grpc
import petugas_pb2 as petugas_pb2
import grpc
import traceback

class PetugasClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5003
        
        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = petugas_pb2_grpc.PetugasServiceStub(self.channel)
    
    def list_petugas(self):
        try:
            response = self.stub.List(petugas_pb2.PetugasListRequest())
            
            if len(response.petugas) == 0:
                return None
            
            return [
                dict(
                    id=petugas.id,
                    username=petugas.username,
                    password=petugas.password
                )for petugas in response.petugas
            ]
        except Exception as e:
            print(e)
            print (traceback.format_exc())
    
    def create_petugas(self,fnama,email,password,username,status):
        response = self.stub.Create(petugas_pb2.PetugasCreateRequest(
            fnama=fnama,
            email=email,
            password=password,
            username=username,
            status='active'
        ))
        if response is None:
            return None
        
        return dict(
            nama=response.petugas.fnama,
            email=response.petugas.email,
            password=response.petugas.password,
            username=response.petugas.username
        )
    
    def get_petugas(self,id):
        response = self.stub.Detail(petugas_pb2.PetugasDetailRequest(id=id))
        if response is None:
            return None
        
        return dict(
            id=response.petugas.id,
            fnama=response.petugas.fnama,
            email=response.petugas.email,
            password=response.petugas.password,
            username=response.petugas.username
        )
    
    def update_petugas(self,id,fnama,email,password,username,status):
        response = self.stub.Update(petugas_pb2.PetugasUpdateRequest(
            id=id,
            fnama=fnama,
            email=email,
            password=password,
            username=username,
            status='active'
        ))
        if response is None:
            return None
        
        return dict(
            id=response.petugas.id,
            fnama=response.petugas.fnama,
            email=response.petugas.email,
            password=response.petugas.password,
            username=response.petugas.username
        )
    
    def delete_petugas(self,id):
        response = self.stub.Delete(petugas_pb2.PetugasDeleteRequest(id=id))
        
        if response is None:
            return None
        
        return dict(
            message=response.message
        )
    
    def login_petugas(self,email,password):
        response = self.stub.Login(petugas_pb2.PetugasLoginRequest(email=email,password=password))
        
        if response is None:
            return None
        
        return dict(
            token=response.token
        )
    
    def logout_petugas(self,token):
        response = self.stub.Logout(petugas_pb2.PetugasLogoutRequest(token=token))
        
        if response is None:
            return None
        
        return dict(
            message=response.message
        )

if __name__ == "__main__":
    while True:
        print("Petugas Client")
        print("1. List Petugas")
        print("2. Create Petugas")
        print("3. Get Petugas")
        print("4. Update Petugas")
        print("5. Delete Petugas")
        print("6. Login Petugas")
        print("7. Logout Petugas")
        print("0. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            petugas = PetugasClient()
            print(petugas.list_petugas())
        elif choice == "2":
            petugas = PetugasClient()
            fnama = input("Enter fnama: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            username = input("Enter username: ")
            status = 'active'
            print(petugas.create_petugas(fnama,email,password,username,status))
        elif choice == "3":
            petugas = PetugasClient()
            id = input("Enter id: ")
            print(petugas.get_petugas(int(id)))
        elif choice == "4":
            petugas = PetugasClient()
            id = input("Enter id: ")
            fnama = input("Enter fnama: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            username = input("Enter username: ")
            status = "active"
            print(petugas.update_petugas(int(id),fnama,email,password,username,status))
        elif choice == "5":
            petugas = PetugasClient()
            id = input("Enter id: ")
            print(petugas.delete_petugas(int(id)))
        elif choice == "6":
            petugas = PetugasClient()
            email = input("Enter email: ")
            password = input("Enter password: ")
            print(petugas.login_petugas(email,password))
        elif choice == "7":
            petugas = PetugasClient()
            token = input("Enter token: ")
            print(petugas.logout_petugas(token))
        elif choice == "0":
            break
        else:
            print("Invalid choice")
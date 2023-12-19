from concurrent import futures
import time
import logging
import grpc
import petugas_pb2
import petugas_pb2_grpc
import jwt
import traceback

from database.config import engine
from sqlalchemy import insert, text, values, select, update, delete, desc

from model.petugas import Petugas

class PetugasService(petugas_pb2_grpc.PetugasServiceServicer):
    def List(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                res = conn.execute(select(Petugas).order_by(desc(Petugas.id)))
                petugas = []
                for row in res:
                    petugas.append(
                        petugas_pb2.Petugas(
                            id=row[0],
                            fnama=row[1],
                            email=row[2],
                            password=row[3],
                            username=row[4],
                            status=row[5]
                        )
                    )
                return petugas_pb2.PetugasListResponse(petugas=petugas)
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return petugas_pb2.PetugasListResponse()
    
    def Detail(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                res = conn.execute(
                    select(Petugas).where(Petugas.id == request.id)
                ).first()

                conn.commit()

                if res is None:
                    return petugas_pb2.PetugasDetailResponse(petugas=None)

                return petugas_pb2.PetugasDetailResponse(
                    petugas=petugas_pb2.Petugas(
                        id=res[0],
                        fnama=res[1],
                        email=res[2],
                        password=res[3],
                        username=res[4],
                        status=res[5]
                    )
                )
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return petugas_pb2.Petugas()
    
    def Create(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                res = conn.execute(
                    insert(Petugas).values(
                        fnama=request.fnama,
                        email=request.email,
                        password=request.password,
                        username=request.username,
                        status='active',
                    )
                )
                conn.commit()
                if res is None:
                    context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                    return petugas_pb2.PetugasCreateResponse(petugas=Petugas)

                return petugas_pb2.PetugasCreateResponse(
                    petugas=petugas_pb2.Petugas(
                        id=res.inserted_primary_key[0],
                        fnama=request.fnama,
                        email=request.email,
                        password=request.password,
                        username=request.username,
                        status='active'
                    )
                )
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return petugas_pb2.PetugasCreateResponse()
    
    def Update(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                res = conn.execute(
                    update(Petugas).where(Petugas.id == request.id).values(
                        fnama=request.fnama,
                        email=request.email,
                        password=request.password,
                        username=request.username,
                        status='active',
                    )
                )
                conn.commit()
                if res is None:
                    context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                    return petugas_pb2.PetugasUpdateResponse(petugas=Petugas)

                return petugas_pb2.PetugasUpdateResponse(
                    petugas=petugas_pb2.Petugas(
                        id=request.id,
                        fnama=request.fnama,
                        email=request.email,
                        password=request.password,
                        username=request.username,
                        status='active'
                    )
                )
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return petugas_pb2.PetugasUpdateResponse()

    def Delete(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                conn.execute(delete(Petugas).where(Petugas.id == request.id))
                conn.commit()
                return petugas_pb2.PetugasDeleteResponse(message="Data berhasil dihapus")
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return petugas_pb2.PetugasDeleteResponse()
    
    def Login(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                res = conn.execute(select(Petugas).where(Petugas.email == request.email)).first()
                
                if res is None:
                    return petugas_pb2.PetugasLoginResponse(token="")
                
                if res[3] != request.password:
                    return petugas_pb2.PetugasLoginResponse(token="")
                
                token = jwt.encode({"email": request.email, "fnama": res[1]}, "secret", algorithm="HS256")
                
                conn.execute(update(Petugas).where(Petugas.email == request.email).values(token=token))
                
                res = conn.execute(select(Petugas).where(Petugas.email == request.email)).first()
                
                conn.commit()
                
                return petugas_pb2.PetugasLoginResponse(token=token,email=request.email,fnama=res[1])
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return petugas_pb2.PetugasLoginResponse()
    
    def Logout(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                decoded = jwt.decode(request.token,"secret",algorithms=["HS256"])
                
                res = conn.execute(select(Petugas).where(Petugas.email == decoded["email"])).first()
                
                if res is None:
                    return petugas_pb2.PetugasLogoutResponse(message="")
                
                conn.execute(update(Petugas).where(Petugas.email == decoded["email"]).values(token=""))
                
                conn.commit()
                
                return petugas_pb2.PetugasLogoutResponse(message="Berhasil Logout")
            
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return petugas_pb2.PetugasLogoutResponse()
        
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    petugas_pb2_grpc.add_PetugasServiceServicer_to_server(PetugasService(), server)
    server.add_insecure_port('localhost:5003')
    server.start()
    print('Server started at localhost:5003')
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()

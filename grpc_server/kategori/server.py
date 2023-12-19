from concurrent import futures
import time
import logging
import grpc
import kategori_pb2
import kategori_pb2_grpc
import traceback

from database.config import engine
from sqlalchemy import insert, text, values, select, update, delete, desc

from model.kategori import Kategori

class KategoriService(kategori_pb2_grpc.KategoriServiceServicer):
    def List(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                res = conn.execute(select(Kategori).order_by(desc(Kategori.id)))
                kategori = []
                for row in res:
                    kategori.append(
                        kategori_pb2.Kategori(
                            id=row[0],
                            nama=row[1],
                        )
                    )

                return kategori_pb2.KategoriListResponse(kategori=kategori)
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return kategori_pb2.KategoriListResponse()
    
    def Get(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                res = conn.execute(
                    select(Kategori).where(Kategori.id == request.id)
                ).first()

                conn.commit()

                if res is None:
                    return kategori_pb2.KategoriResponse(kategori=None)

                return kategori_pb2.KategoriResponse(
                    kategori=kategori_pb2.Kategori(
                        id=res[0],
                        nama=res[1],
                    )
                )
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return kategori_pb2.Kategori()
    
    def Create(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                res = conn.execute(
                    insert(Kategori).values(
                        kategori=request.nama
                    )
                )

                conn.commit()

                if res is None:
                    context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                    return kategori_pb2.KategoriCreateResponse(kategori=Kategori)

                return kategori_pb2.KategoriCreateResponse(nama=request.nama,id=res.inserted_primary_key_rows[0][0])
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return kategori_pb2.Kategori()
    
    def Update(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                res = conn.execute(
                    update(Kategori)
                    .where(Kategori.id == request.id)
                    .values(
                        kategori=request.nama
                    )
                )

                conn.commit()

                if res is None:
                    return kategori_pb2.KategoriUpdateResponse(kategori=Kategori)

                return kategori_pb2.KategoriUpdateResponse(nama=request.nama,id=request.id)
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return kategori_pb2.Kategori()
    
    def Delete(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                conn.execute(delete(Kategori).where(Kategori.id == request.id))

                conn.commit()

                return kategori_pb2.KategoriDeleteResponse(
                    message="Data berhasil dihapus"
                )
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return kategori_pb2.Kategori()
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    kategori_pb2_grpc.add_KategoriServiceServicer_to_server(KategoriService(), server)
    server.add_insecure_port("localhost:5005")
    server.start()
    print("Server started at localhost:5005")
    server.wait_for_termination()
    
if __name__ == "__main__":
    logging.basicConfig()
    serve()
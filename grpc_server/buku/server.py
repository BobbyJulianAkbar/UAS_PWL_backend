from concurrent import futures
import time
import logging
import grpc
import buku_pb2
import buku_pb2_grpc

import traceback

from database.config import engine
from sqlalchemy import insert, text, values, select, update, delete, desc

from models.buku import Buku
from models.kategori import Kategori


class BukuService(buku_pb2_grpc.BukuServiceServicer):
    def List(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                res = conn.execute(select(Buku).order_by(desc(Buku.id)))
                buku = []
                for row in res:
                    buku.append(
                        buku_pb2.Buku(
                            id=row[0],
                            judul=row[1],
                            pengarang=row[2],
                            penerbit=row[3],
                            tahun_terbit=row[4],
                            kategori_id=row[5],
                            isbn=row[6],
                            jumlah_buku=row[7],
                            deskripsi=row[8],
                        )
                    )
                return buku_pb2.BukuListResponse(buku=buku)
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return buku_pb2.BukuListResponse()

    def Create(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                # kategoriId = conn.execute(
                #     select(Kategori).where(Kategori.id) == request.kategori_id
                # ).first()

                # if kategoriId is None:
                #     context.set_code(grpc.StatusCode.NOT_FOUND)
                #     return buku_pb2.BukuCreateResponse(buku=None)

                res = conn.execute(
                    insert(Buku).values(
                        judul=request.judul,
                        pengarang=request.pengarang,
                        penerbit=request.penerbit,
                        tahun_terbit=request.tahun_terbit,
                        kategori_id=request.kategori_id,
                        isbn=request.isbn,
                        jumlah_buku=request.jumlah_buku,
                        deskripsi=request.deskripsi,
                    )
                )

                conn.commit()

                return buku_pb2.BukuCreateResponse(
                    buku=buku_pb2.Buku(
                        id=res.inserted_primary_key_rows[0][0],
                        judul=request.judul,
                        pengarang=request.pengarang,
                        penerbit=request.penerbit,
                        tahun_terbit=request.tahun_terbit,
                        kategori_id=request.kategori_id,
                        isbn=request.isbn,
                        jumlah_buku=request.jumlah_buku,
                        deskripsi=request.deskripsi,
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return buku_pb2.BukuCreateResponse(buku=None)

    def Detail(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                res = conn.execute(select(Buku).where(Buku.id == request.id)).first()

                conn.commit()

                if res is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    return buku_pb2.BukuDetailResponse(buku=None)

                return buku_pb2.BukuDetailResponse(
                    buku=buku_pb2.Buku(
                        id=res[0],
                        judul=res[1],
                        pengarang=res[2],
                        penerbit=res[3],
                        tahun_terbit=res[4],
                        kategori_id=res[5],
                        isbn=res[6],
                        jumlah_buku=res[7],
                        deskripsi=res[8],
                    )
                )
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return buku_pb2.BukuDetailResponse(buku=None)

    def Delete(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                res = conn.execute(delete(Buku).where(Buku.id == request.id))

                conn.commit()

                if res is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    return buku_pb2.BukuDeleteResponse(message="Not Found")

                return buku_pb2.BukuDeleteResponse(message="Deleted")
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return buku_pb2.BukuDeleteResponse(message="Error")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    buku_pb2_grpc.add_BukuServiceServicer_to_server(BukuService(), server)
    server.add_insecure_port("localhost:5004")
    server.start()
    print("Server started at localhost:5004")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

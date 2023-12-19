from concurrent import futures
import time
import logging
import grpc
import traceback
import peminjaman_pb2
import peminjaman_pb2_grpc

from database.config import engine
from sqlalchemy import insert, text, values, select, update, delete, desc

from model.peminjaman import Peminjaman


class PeminjamanService(peminjaman_pb2_grpc.PeminjamanServiceServicer):
    def GetPeminjamanList(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                res = conn.execute(select(Peminjaman).order_by(desc(Peminjaman.id)))
                conn.commit()
                peminjaman = []
                for row in res:
                    peminjaman.append(
                        peminjaman_pb2.Peminjaman(
                            id=row[0],
                            id_buku=row[1],
                            id_anggota=row[2],
                            tanggal_peminjaman=row[3],
                            tanggal_pengembalian=row[4],
                            status=row[5],
                        )
                    )
                return peminjaman_pb2.PeminjamanListResponse(peminjaman=peminjaman)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return peminjaman_pb2.PeminjamanListResponse()

    def CreatePeminjaman(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    insert(Peminjaman).values(
                        id_buku=request.id_buku,
                        id_anggota=request.id_anggota,
                        tanggal_peminjaman=request.tanggal_peminjaman,
                        tanggal_pengembalian=request.tanggal_pengembalian,
                        status=request.status,
                    )
                )

                conn.commit()

                return peminjaman_pb2.PeminjamanCreateResponse(
                    peminjaman=peminjaman_pb2.Peminjaman(
                        id=res.inserted_primary_key_rows[0][0],
                        id_buku=request.id_buku,
                        id_anggota=request.id_anggota,
                        tanggal_peminjaman=request.tanggal_peminjaman,
                        tanggal_pengembalian=request.tanggal_pengembalian,
                        status=request.status,
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return peminjaman_pb2.PeminjamanCreateResponse()

    def GetPeminjaman(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    select(Peminjaman).where(Peminjaman.id == request.id)
                ).first()

                conn.commit()

                if res is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    return peminjaman_pb2.PeminjamanResponse()

                return peminjaman_pb2.PeminjamanResponse(
                    peminjaman=peminjaman_pb2.Peminjaman(
                        id=res[0],
                        id_buku=res[1],
                        id_anggota=res[2],
                        tanggal_peminjaman=res[3],
                        tanggal_pengembalian=res[4],
                        status=res[5],
                    )
                )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return peminjaman_pb2.PeminjamanResponse()

    def UpdatePeminjaman(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    update(Peminjaman)
                    .where(Peminjaman.id == request.id)
                    .values(
                        id_buku=request.id_buku,
                        id_anggota=request.id_anggota,
                        tanggal_peminjaman=request.tanggal_peminjaman,
                        tanggal_pengembalian=request.tanggal_pengembalian,
                        status=request.status,
                    )
                )

                conn.commit()

                if res is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    return peminjaman_pb2.PeminjamanUpdateResponse()

                return peminjaman_pb2.PeminjamanUpdateResponse(message="Success")

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return peminjaman_pb2.PeminjamanUpdateResponse()

    def DeletePeminjaman(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    delete(Peminjaman).where(Peminjaman.id == request.id)
                )

                conn.commit()

                if res is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    return peminjaman_pb2.PeminjamanDeleteResponse()

                return peminjaman_pb2.PeminjamanDeleteResponse(message="Success")

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            context.set_code(grpc.StatusCode.UNKNOWN)
            return peminjaman_pb2.PeminjamanDeleteResponse()


def servev():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    peminjaman_pb2_grpc.add_PeminjamanServiceServicer_to_server(
        PeminjamanService(), server
    )
    server.add_insecure_port("localhost:5006")
    server.start()
    print("Server started at localhost:5006")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    servev()

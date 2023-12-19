from concurrent import futures
import time
import logging
import grpc
import anggota_pb2
import anggota_pb2_grpc
import jwt

from database.config import engine
from sqlalchemy import insert, text, values, select, update, delete, desc

from model.anggota import Anggota


class AnggotaService(anggota_pb2_grpc.AnggotaServiceServicer):
    def List(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                res = conn.execute(select(Anggota).order_by(desc(Anggota.id)))
                anggota = []
                for row in res:
                    anggota.append(
                        anggota_pb2.Anggota(
                            id=row[0],
                            nama=row[1],
                            email=row[2],
                            nis=row[3],
                        )
                    )

                return anggota_pb2.AnggotaListResponse(anggota=anggota)
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return anggota_pb2.AnggotaListResponse()

    def Create(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                res = conn.execute(
                    insert(Anggota).values(
                        nama=request.nama,
                        email=request.email,
                        nis=request.nis,
                        password=request.password,
                    )
                )
                conn.commit()
                if res is None:
                    context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                    return anggota_pb2.AnggotaCreateResponse(anggota=Anggota)

                return anggota_pb2.AnggotaCreateResponse(
                    anggota=anggota_pb2.Anggota(
                        id=res.inserted_primary_key[0],
                        nama=request.nama,
                        email=request.email,
                        nis=request.nis,
                        password=request.password,
                    )
                )
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return anggota_pb2.Anggota()

    def Get(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                res = conn.execute(
                    select(Anggota).where(Anggota.id == request.id)
                ).first()

                conn.commit()

                if res is None:
                    return anggota_pb2.AnggotaResponse(anggota=None)

                return anggota_pb2.AnggotaResponse(
                    anggota=anggota_pb2.Anggota(
                        id=res[0],
                        nama=res[1],
                        email=res[2],
                        nis=res[3],
                    )
                )
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return anggota_pb2.Anggota()

    def Update(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                res = conn.execute(
                    update(Anggota)
                    .where(Anggota.id == request.id)
                    .values(
                        nama=request.nama,
                        email=request.email,
                        nis=request.nis,
                    )
                )

                conn.commit()

                if res is None:
                    return anggota_pb2.AnggotaUpdateResponse(anggota=Anggota)

                return anggota_pb2.AnggotaResponse(
                    anggota=anggota_pb2.Anggota(
                        id=request.id,
                        nama=request.nama,
                        email=request.email,
                        nis=request.nis,
                    )
                )
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return anggota_pb2.Anggota()

    def Delete(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                conn.execute(delete(Anggota).where(Anggota.id == request.id))

                conn.commit()

                return anggota_pb2.AnggotaDeleteResponse(
                    message="Data berhasil dihapus"
                )
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return anggota_pb2.Anggota()

    def Login(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                # res = conn.execute(
                #     select(Anggota).where(Anggota.email == request.email)
                # ).first()
                # check if email is exist
                res = conn.execute(
                    select(Anggota).where(Anggota.email == request.email)
                ).first()

                if res is None:
                    return anggota_pb2.AnggotaLoginResponse(token="")

                # check if password is match
                if res[4] != request.password:
                    return anggota_pb2.AnggotaLoginResponse(token="")

                # generate token
                token = jwt.encode(
                    {"email": request.email, "nama": res[1]},
                    "secret",
                    algorithm="HS256",
                )

                # update token
                conn.execute(
                    update(Anggota)
                    .where(Anggota.email == request.email)
                    .values(token=token)
                )

                # get data
                res = conn.execute(
                    select(Anggota).where(Anggota.email == request.email)
                ).first()

                conn.commit()

                return anggota_pb2.AnggotaLoginResponse(
                    token=token,
                    email=request.email,
                    nama=res[1],
                    id=res[0],
                )
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return anggota_pb2.Anggota()

    def Logout(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                decoded = jwt.decode(request.token, "secret", algorithms=["HS256"])

                res = conn.execute(
                    select(Anggota).where(Anggota.email == decoded["email"])
                ).first()

                if res is None:
                    return anggota_pb2.AnggotaLogoutResponse(message="")

                # update token
                conn.execute(
                    update(Anggota)
                    .where(Anggota.email == decoded["email"])
                    .values(token="")
                )

                conn.commit()

                return anggota_pb2.AnggotaLogoutResponse(
                    message="Berhasil Logout",
                )
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.UNKNOWN)
            return anggota_pb2.Anggota()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    anggota_pb2_grpc.add_AnggotaServiceServicer_to_server(AnggotaService(), server)
    server.add_insecure_port("localhost:5001")
    server.start()
    print("Server started at localhost:5001")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

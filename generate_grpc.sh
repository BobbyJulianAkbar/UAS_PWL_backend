# create env
python3 -m venv env

# activate env in windows
./env/Scripts/activate.bat

# generate grpc buku
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/buku --pyi_out=./grpc_server/buku --grpc_python_out=./grpc_server/buku ./grpc/buku.proto

# generate grpc petugas
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/petugas --pyi_out=./grpc_server/petugas --grpc_python_out=./grpc_server/petugas ./grpc/petugas.proto

# generate grpc anggota
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/anggota --pyi_out=./grpc_server/anggota --grpc_python_out=./grpc_server/anggota ./grpc/anggota.proto

# generate grpc peminjaman
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/peminjaman --pyi_out=./grpc_server/peminjaman --grpc_python_out=./grpc_server/peminjaman ./grpc/peminjaman.proto

# generate grpc kategori
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./grpc_server/kategori --pyi_out=./grpc_server/kategori --grpc_python_out=./grpc_server/kategori ./grpc/kategori.proto
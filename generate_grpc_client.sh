# create env
python3 -m venv env

# activate env in windows
./env/Scripts/activate.bat

# generate grpc buku
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest/rest/grpc_client/buku --pyi_out=./rest/rest/grpc_client/buku --grpc_python_out=./rest/rest/grpc_client/buku ./grpc/buku.proto

# generate grpc petugas
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest/rest/grpc_client/petugas --pyi_out=./rest/rest/grpc_client/petugas --grpc_python_out=./rest/rest/grpc_client/petugas ./grpc/petugas.proto

# generate grpc anggota
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest/rest/grpc_client/anggota --pyi_out=./rest/rest/grpc_client/anggota --grpc_python_out=./rest/rest/grpc_client/anggota ./grpc/anggota.proto

# generate grpc peminjaman
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest/rest/grpc_client/peminjaman --pyi_out=./rest/rest/grpc_client/peminjaman --grpc_python_out=./rest/rest/grpc_client/peminjaman ./grpc/peminjaman.proto

# generate grpc kategori
./env/Scripts/python -m grpc_tools.protoc -I./grpc --python_out=./rest/rest/grpc_client/kategori --pyi_out=./rest/rest/grpc_client/kategori --grpc_python_out=./rest/rest/grpc_client/kategori ./grpc/kategori.proto
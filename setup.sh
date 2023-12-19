# create env
python3 -m venv env

# activate env in windows
./env/Scripts/activate.bat

# install requirements
./env/Scripts/pip install -e .

# run migrate
./env/Scripts/alembic upgrade head

# deactivate env
deactivate

# setup rest server
python3 -m venv ./rest/env

# activate env in windows
./rest/env/Scripts/activate.bat

# install requirements
./rest/env/Scripts/pip install -e ./rest

# deactivate env
deactivate

# setup grpc server
cd grpc_server

# create env anggota
python3 -m venv ./anggota/env

# activate env in windows
./anggota/env/Scripts/activate.bat

# install requirements
./anggota/env/Scripts/pip install -e ./anggota

# deactivate env
deactivate

# create env buku
python3 -m venv ./buku/env

# activate env in windows
./buku/env/Scripts/activate.bat

# install requirements
./buku/env/Scripts/pip install -e ./buku

# deactivate env
deactivate

# create env kategori
python3 -m venv ./kategori/env

# activate env in windows
./kategori/env/Scripts/activate.bat

# install requirements
./kategori/env/Scripts/pip install -e ./kategori

# deactivate env
deactivate

# create env peminjaman
python3 -m venv ./peminjaman/env

# activate env in windows
./peminjaman/env/Scripts/activate.bat

# install requirements
./peminjaman/env/Scripts/pip install -e ./peminjaman

# deactivate env
deactivate

# create env petugas
python3 -m venv ./petugas/env

# activate env in windows
./petugas/env/Scripts/activate.bat

# install requirements
./petugas/env/Scripts/pip install -e ./petugas

# deactivate env
deactivate





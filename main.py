import grpc_client.anggota.anggota_client as anggota_client

client = anggota_client.AnggotaClient()

print(client.list_anggota())

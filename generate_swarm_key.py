import secrets

hex_key = secrets.token_hex(32)
output = f"/key/swarm/psk/1.0.0/\n/base16/\n{hex_key}"

with open("swarm.key", "w") as f:
    f.write(output)

print("swarm.key generated successfully")

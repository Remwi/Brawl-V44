import os
import Configuration
from Classes.ServerConnection import ServerConnection
from Static.StaticData import StaticData

if not os.path.exists(f"HexDumpV{Configuration.settings['DumpMajor']}"):
    os.mkdir(f"HexDumpV{Configuration.settings['DumpMajor']}")

StaticData.Preload()

# Автоматически берем порт от облака, а если запускаем на телефоне — будет 9338
port = int(os.environ.get("PORT", 9338))

ServerConnection(("0.0.0.0", port))
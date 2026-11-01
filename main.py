from cloudlink import cloudlink
import os

if __name__ == "__main__":
    # Read the port from the cloud provider environment, default to 3000
    port = int(os.environ.get("PORT", 3000))

    server = cloudlink()
    # Bind to 0.0.0.0 so the cloud platform can route traffic to it
    server.server(addr="0.0.0.0", port=port, offline_mode=False)

import subprocess
import os


def create_keystore(keystore_path="keystore"):
    if not os.path.exists(keystore_path):
        print("🔐 Creating keystore...")
        subprocess.run([
            "ros2", "security", "create_keystore", keystore_path
        ])
    else:
        print("ℹ️ Keystore already exists")


def create_keys_for_nodes(nodes, keystore_path="keystore"):
    import subprocess

    for node in nodes:
        node_name = node["name"]

        # 🚫 DO NOT generate keys for attacker
        if node_name == "attacker":
            print("🚫 Skipping key generation for attacker")
            continue

        print(f"🔑 Generating keys for node: {node_name}")

        subprocess.run([
            "ros2", "security", "create_enclave",
            keystore_path,
            f"/{node_name}"
        ])
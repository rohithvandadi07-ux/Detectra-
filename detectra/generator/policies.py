def generate_permissions(nodes, keystore_path="keystore"):
    import os

    enclaves_path = os.path.join(keystore_path, "enclaves")

    for node in nodes:
        node_name = node["name"]

        if node_name == "attacker":
            print("🚫 No permissions for attacker → blocked")
            continue

        node_path = os.path.join(enclaves_path, node_name)
        permissions_file = os.path.join(node_path, "permissions.xml")

        with open(permissions_file, "w") as f:
            f.write(f"""<permissions>
  <grant>
    <subject_name>/{node_name}</subject_name>

    <permissions>
      <publish>
        <topic>chatter</topic>
      </publish>

      <subscribe>
        <topic>chatter</topic>
      </subscribe>
    </permissions>

  </grant>
</permissions>
""")

        print(f"📜 Permissions created for {node_name}")
import click

from detectra.scanner.workspace import find_python_nodes
from detectra.generator.certificates import create_keystore, create_keys_for_nodes
from detectra.generator.policies import generate_permissions
from detectra.validator.simulate import validate_setup


@click.group()
def cli():
    """Detectra CLI"""
    pass


@cli.command()
@click.argument("workspace")
def secure(workspace):
    print(f"🔐 Scanning workspace: {workspace}")

    # 🔍 Scan nodes
    nodes = find_python_nodes(workspace)

    # 👇 add attacker as "valid node"
    nodes.append({"name": "attacker"})

    print("\n📦 Detected Nodes:")
    all_nodes = nodes + [{"name": "listener", "path": "system_node"}]

    for node in all_nodes:
        print(f" - {node['name']} ({node.get('path', 'unknown')})")

    if not nodes:
        print("⚠️ No ROS2 nodes found")
        return

    # 🔐 Step 1: Create keystore
    create_keystore()

    # 🔑 Step 2: Generate certificates
    create_keys_for_nodes(nodes)

    # 📜 Step 3: Generate permissions
    generate_permissions(nodes)

    # 🧪 Step 4: Validate setup
    success = validate_setup()

    if success:
        print("\n✅ Detectra setup complete and validated!")
    else:
        print("\n❌ Detectra setup failed validation. Check configuration.")


if __name__ == "__main__":
    cli()
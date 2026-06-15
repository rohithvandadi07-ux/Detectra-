import click

from detectra.scanner.workspace import find_python_nodes
from detectra.generator.certificates import create_keystore, create_keys_for_nodes
from detectra.generator.policies import generate_permissions
from detectra.validator.simulate import validate_setup
from detectra.core.logger import info, warning, alert, success


@click.group()
def cli():
    """Detectra CLI"""
    pass


@cli.command()
@click.argument("workspace")
def secure(workspace):
    info(f"Scanning workspace: {workspace}")

    # 🔍 Scan nodes
    nodes = find_python_nodes(workspace)

    info("Detected Nodes:")

    for node in nodes:
        info(f"{node['name']} ({node.get('path', 'system_node')})")

    if not nodes:
        alert("No ROS2 nodes found")
        return

    # 🔐 Step 1: Create keystore
    info("Creating keystore...")
    create_keystore()

    # 🔑 Step 2: Generate certificates
    info("Generating certificates...")
    create_keys_for_nodes(nodes)

    # 📜 Step 3: Generate permissions
    info("Generating permissions...")
    generate_permissions(nodes)

    # 🧪 Step 4: Validate setup
    info("Running validation...")
    validation_result = validate_setup()

    if validation_result:
        success("Detectra setup complete and validated!")
    else:
        alert("Detectra setup failed validation. Check configuration.")


if __name__ == "__main__":
    cli()
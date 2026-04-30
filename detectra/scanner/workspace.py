import os
import re

def find_python_nodes(workspace_path):
    nodes = []

    for root, dirs, files in os.walk(workspace_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                        # Detect ROS2 Node class
                        if "Node(" in content or "rclpy.node" in content:
                            node_name = extract_node_name(content)
                            nodes.append({
                                "name": node_name if node_name else file.replace(".py", ""),
                                "path": file_path
                            })

                except Exception as e:
                    print(f"⚠️ Skipped {file_path}: {e}")

    return nodes


def extract_node_name(content):
    """
    Try to extract node name from code like:
    super().__init__('talker')
    """
    match = re.search(r"super\(\)\.__init__\(['\"](.*?)['\"]\)", content)
    if match:
        return match.group(1)

    return None
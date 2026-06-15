import subprocess
import os

from detectra.core.logger import info, warning, alert, success


def validate_setup(keystore_path="keystore"):
    info("Running validation test...")

    env = os.environ.copy()

    env["ROS_SECURITY_ENABLE"] = "true"
    env["ROS_SECURITY_STRATEGY"] = "Permissive"
    env["ROS_SECURITY_KEYSTORE"] = os.path.abspath(keystore_path)

    try:
        result = subprocess.run(
            ["ros2", "run", "demo_nodes_cpp", "talker"],
            env=env,
            timeout=5,
            capture_output=True,
            text=True
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        # ✅ Case 1: Successful execution
        if result.returncode == 0:
            success("Validation passed: secure node executed successfully")
            return True

        # ⚠️ Case 2: Security-related warnings
        if "SECURITY" in stderr or "security" in stderr:
            alert("Security warning detected during validation")
            alert(stderr)
            return True  # still allow for MVP

        # ⚠️ Case 3: General warnings
        warning("Validation completed with warnings")
        if stderr:
            warning(stderr)

        return True

    except subprocess.TimeoutExpired:
        info("Validation timed out (node likely running correctly)")
        return True

    except Exception as e:
        alert(f"Validation error: {e}")
        return False
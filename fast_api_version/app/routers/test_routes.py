from fastapi import APIRouter
import subprocess
import os

router = APIRouter()

@router.get("/run_tests")
def run_tests():
    """Запускает pytest и возвращает результат"""

    env = os.environ.copy()
    env["PYTHONPATH"] = "/app" 

    result = subprocess.run(
        ["pytest", "app/tests"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=env
    )

    return {
        "returncode": result.returncode,
        "success": result.returncode == 0,
        "stdout": result.stdout.splitlines(),
        "stderr": result.stderr.splitlines()
    }
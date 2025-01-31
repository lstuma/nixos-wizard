import subprocess
from .settings import get_option
from .log import exception

def execute(bash_code: str, capture: bool = False, allow_single_quotes: bool = False) -> str | None:
    """
    Execute the given code using bash.

    :param bash_code: The code to execute.
    :param capture: Whether to capture the output or simply print it.
    :return: The output of the code if capture is True.
    """
    if "'" in bash_code and not allow_single_quotes:
        raise ValueError("Single quotes are not allowed in bash code.")
    bash_binary = get_option("bash")
    command = f"{bash_binary} -c '{bash_code}'"
    if not capture:
        subprocess.run(command, shell=True)
        return

    with subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
        stdout, stderr = proc.communicate()
        error_output = stderr.decode()
        if error_output:
            exception("Error executing command", RuntimeError(error_output))
            raise RuntimeError(f"Error executing command `{command}`: {error_output}")
        return stdout.decode()

def nix_exec(bash_code: str, capture: bool = False, packages: list[str] | None = None) -> str:
    if "'" in bash_code:
        raise ValueError("Single quotes are not allowed in bash code.")
    packages = packages or []
    packages_str = " ".join(packages)
    return execute(f"nix-shell -p \\'{packages_str}\\' --run \\'{bash_code}\\'", capture=capture, allow_single_quotes=True) or ''

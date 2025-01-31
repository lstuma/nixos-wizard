from argparse import ArgumentParser
from .log import info, success, error, warning, yesno, banner
from .exec import nix_exec
from .settings import get_option

def rebuild():
    banner()
    info("Rebuilding NixOS configuration...")
    dotfiles = get_option("dotfiles")
    nixos = get_option("nixos")
    # check that no changes have been made
    diff: str = nix_exec(f"cd {dotfiles}; git status --porcelain", capture=True, packages=["git"])
    if diff.strip():
        # if changes have been made, ask wether to add and commit them
        warning("Changes have been made to the configuration. Commit them before rebuilding.")
        if yesno("Add and commit changes?"):
            nix_exec(f"git add .", packages=["git"])
            commit_message = nix_exec(f"cd {dotfiles}; {nixos}-rebuild list-generations | grep current")
            info(f"Committing changes with message: {commit_message}")
            nix_exec(f"git commit -m \"{commit_message}\"", packages=["git"])
            success("Changes committed.")
        else:
            return
    # rebuild the configuration
    rebuild_cmd = f"nixos-rebuild switch --flake .# --log-format internal-json -v |& nom --json"
    rebuild_packages = ["nix-output-monitor"]
    info("Rebuilding configuration...")
    nix_exec(rebuild_cmd, packages=rebuild_packages)
    success("Configuration rebuilt.")

def cleanup():
    pass

def update():
    pass

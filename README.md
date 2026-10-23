# AshOS Packages Repository

This repository is the official package registry for **AshOS** (`ash`), a Linux-like operating system for the ESP32-S3 microcontroller.

Packages hosted here can be searched, downloaded, and installed directly onto an ESP32-S3 device running AshOS via its built-in package manager.

## Connecting AshOS to this Repository

On your AshOS terminal, configure the repository URL to point to this GitHub repository (using raw GitHub content):

```bash
# Point AshOS to your repository
ash repo https://raw.githubusercontent.com/BloodLetters/ashos-packages/main

# Update the local package cache from packages.json
ash update

# Search for available packages
ash search <query>

# Install a package (e.g., neofetch)
ash install neofetch

# Run the installed application
neofetch
```

## Adding a New Package

1. Create a new directory under the repository root (e.g. `cowsay/`).
2. Add `metadata.json` with your package information.
3. Add your executable (`.ash` script or `.bin` binary).
4. Register the package in [packages.json](./packages.json).
5. Push to GitHub and test with `ash update && ash install <pkg>`.
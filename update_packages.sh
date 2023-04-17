#!/bin/bash

function display_help() {
    echo "Usage: $0 [OPTIONS]"
    echo "This script is used to update pip packages or Ubuntu packages based on the provided options."
    echo
    echo "Options:"
    echo "  --pip           Update pip packages"
    echo "  --app           Update Ubuntu packages"
    echo "  --help          Display this help message"
}


function update_pip_packages() {
    echo "Checking for pip updates..."
    pip_version=$(pip --version | awk '{print $2}')
    pip_latest_version=$(curl -s https://pypi.org/pypi/pip/json | awk -F'"version":' 'NF>1 {print $2}' | awk -F'"' '{print $2}')
    
    if [ "$pip_version" != "$pip_latest_version" ]; then
        echo "Updating pip from version $pip_version to version $pip_latest_version..."
        sudo -u $SUDO_USER python3 -m pip install --upgrade pip
        echo "Pip updated successfully."
    else
        echo "Pip is already up-to-date (version $pip_version)."
    fi
    
    echo "Checking for available pip package updates..."
    pip_packages_to_update=$(pip list --outdated --format=columns | awk 'NR>2 {print $1}')
    if [ -z "$pip_packages_to_update" ]; then
        echo "All pip packages are up-to-date."
    else
        echo "Updating pip packages..."
        echo "$pip_packages_to_update" | xargs -I {} sudo -u $SUDO_USER pip install --upgrade {}
        echo "Pip packages updated successfully."
    fi
}

function update_ubuntu_packages() {
    echo "Updating Ubuntu packages..."
    sudo apt update
    sudo apt upgrade -y
    echo "Ubuntu packages updated successfully."
}

if [ "$#" -eq 0 ] || [ "$1" == "--help" ]; then
    display_help
    elif [ "$1" == "--pip" ]; then
    update_pip_packages
    elif [ "$1" == "--app" ]; then
    update_ubuntu_packages
else
    echo "Invalid option provided. Use --help for more information."
fi

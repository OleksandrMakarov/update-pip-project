import sys
import argparse
from update_project.update_app import update_app_packages
from update_project.update_pip import update_pip_packages
from update_project.utils import get_project_version


def main() -> None:
    parser = argparse.ArgumentParser(description="Update pip and app packages")
    parser.add_argument('--pip', action='store_true',
                        help='Update pip packages')
    parser.add_argument('--app', action='store_true',
                        help='Update app packages')
    parser.add_argument('-v', '--version', action='store_true',
                        help='Display the version of the package')
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.version:
        version = get_project_version()
        print(f"update-pip-packages version: {version}")
        sys.exit(0)

    if args.pip:
        update_pip_packages()
    if args.app:
        update_app_packages()


if __name__ == "__main__":
    main()

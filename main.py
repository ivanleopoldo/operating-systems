import os

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

if __name__ == "__main__":
    choice = inquirer.select(
        message="Select Algorithm Category",
        default=0,
        choices=[
            Choice(0, "CPU Scheduling"),
            Choice(1, "Page Replacement"),
            Choice(2, "Disk Scheduling"),
        ],
    ).execute()

    if choice == 0:
        os.system("python ./cpu-scheduling/main.py")
    elif choice == 1:
        os.system("python ./page_replacement_algorithms/main.py")
    elif choice == 2:
        os.system("python ./io-management/main.py")

#!/usr/bin/env python3
"""HEM — Molecular Biology Workbench entry point."""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Ensure project root is on sys.path so all modules resolve correctly
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from ui.main_window import MainWindow


def main():
    # High-DPI support
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    app = QApplication(sys.argv)
    app.setApplicationName("HEM")
    app.setApplicationDisplayName("HEM — Molecular Biology Workbench")
    app.setOrganizationName("BinaryPersonal")

    window = MainWindow()
    window.show()

    # If a file was passed on the command line, open it immediately
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.isfile(path):
            try:
                window.core.load_file(path)
            except Exception as e:
                print(f"Warning: could not load {path}: {e}", file=sys.stderr)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

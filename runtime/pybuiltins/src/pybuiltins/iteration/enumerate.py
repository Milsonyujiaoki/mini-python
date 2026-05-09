"""
Implementation of Python built-in: enumerate.py

Part of the mini-python runtime system.
"""

from __future__ import annotations

from typing import Any


__all__ = []


class NotImplementedBuiltinError(NotImplementedError):
    """
    Raised when builtin implementation is incomplete.
    """


def main() -> None:
    """
    Local development entrypoint.
    """
    raise NotImplementedBuiltinError(
        "enumerate.py is not implemented yet."
    )


if __name__ == "__main__":
    main()

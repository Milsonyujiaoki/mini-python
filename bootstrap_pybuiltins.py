#!/usr/bin/env python3
"""
Bootstrap script for pybuiltins structure.

Creates a production-ready directory tree for the
mini-python runtime/pybuiltins package.

Features:
- Idempotent (safe to run multiple times)
- Creates __init__.py automatically
- Generates starter module templates
- Generates README.md placeholders
- Creates optional test structure
- Uses pathlib (Pythonic and cross-platform)
- Fully typed
"""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent
from typing import Final

# ============================================================================
# CONFIGURATION
# ============================================================================

PROJECT_ROOT: Final[Path] = Path.cwd()

PYBUILTINS_ROOT: Final[Path] = (
    PROJECT_ROOT
    / "runtime"
    / "pybuiltins"
    / "src"
    / "pybuiltins"
)

TESTS_ROOT: Final[Path] = (
    PROJECT_ROOT
    / "runtime"
    / "pybuiltins"
    / "tests"
)

# ============================================================================
# STRUCTURE DEFINITION
# ============================================================================

STRUCTURE: Final[dict[str, list[str]]] = {
    "core": [
        "object.py",
        "type.py",
        "bool.py",
        "none.py",
    ],
    "introspection": [
        "isinstance.py",
        "issubclass.py",
        "getattr.py",
        "setattr.py",
        "hasattr.py",
        "dir.py",
        "vars.py",
    ],
    "iteration": [
        "iter.py",
        "next.py",
        "enumerate.py",
        "zip.py",
        "map.py",
        "filter.py",
        "all.py",
        "any.py",
    ],
    "containers": [
        "len.py",
        "sorted.py",
        "reversed.py",
        "slice.py",
    ],
    "functional": [
        "property.py",
        "classmethod.py",
        "staticmethod.py",
        "super.py",
        "callable.py",
    ],
    "protocols": [
        "iterator_protocol.py",
        "descriptor_protocol.py",
        "callable_protocol.py",
        "sequence_protocol.py",
    ],
    "internal": [
        "sentinels.py",
        "validation.py",
        "dispatch.py",
        "errors.py",
    ],
    "registry": [
        "builtins_registry.py",
    ],
}

AUXILIARY_DIRS: Final[list[str]] = [
    "docs",
    "research",
    "examples",
    "benchmarks",
]

TEST_CATEGORIES: Final[list[str]] = [
    "unit",
    "integration",
    "edge_cases",
    "property",
]

# ============================================================================
# TEMPLATE GENERATORS
# ============================================================================


def create_module_template(module_name: str) -> str:
    """
    Generate a starter template for Python modules.
    """

    return dedent(
        f'''\
        """
        Implementation of Python built-in: {module_name}

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
                "{module_name} is not implemented yet."
            )


        if __name__ == "__main__":
            main()
        '''
    )


def create_init_template(package_name: str) -> str:
    """
    Generate __init__.py template.
    """

    return dedent(
        f'''\
        """
        {package_name} package.

        Part of the mini-python runtime system.
        """
        '''
    )


def create_readme_template(directory_name: str) -> str:
    """
    Generate README.md template.
    """

    return dedent(
        f"""\
        # {directory_name}

        Documentation and implementation notes for `{directory_name}`.

        ## Goals

        - Recreate Python runtime semantics
        - Study CPython internals
        - Experiment with runtime behavior
        - Build educational implementations

        ## References

        - CPython source code
        - Python Data Model
        - Python Language Reference
        """
    )


def create_test_template(module_name: str) -> str:
    """
    Generate pytest starter template.
    """

    safe_name = module_name.replace(".py", "")

    return dedent(
        f'''\
        """
        Tests for {safe_name}.
        """

        import pytest


        def test_placeholder() -> None:
            """
            Placeholder test.
            """
            assert True
        '''
    )


# ============================================================================
# FILESYSTEM HELPERS
# ============================================================================


def ensure_directory(path: Path) -> None:
    """
    Create directory recursively if it does not exist.
    """

    path.mkdir(parents=True, exist_ok=True)


def write_file(path: Path, content: str) -> None:
    """
    Write file only if it does not already exist.
    """

    if path.exists():
        print(f"[SKIP] {path}")
        return

    path.write_text(content, encoding="utf-8")
    print(f"[CREATE] {path}")


# ============================================================================
# MAIN BOOTSTRAP LOGIC
# ============================================================================


def create_package_structure() -> None:
    """
    Create pybuiltins package structure.
    """

    print("\n[INFO] Creating pybuiltins structure...\n")

    ensure_directory(PYBUILTINS_ROOT)

    write_file(
        PYBUILTINS_ROOT / "__init__.py",
        create_init_template("pybuiltins"),
    )

    for package_name, modules in STRUCTURE.items():
        package_path = PYBUILTINS_ROOT / package_name

        ensure_directory(package_path)

        # Package __init__
        write_file(
            package_path / "__init__.py",
            create_init_template(package_name),
        )

        # Auxiliary directories
        for aux_dir in AUXILIARY_DIRS:
            aux_path = package_path / aux_dir

            ensure_directory(aux_path)

            write_file(
                aux_path / "README.md",
                create_readme_template(aux_dir),
            )

        # Module files
        for module in modules:
            module_path = package_path / module

            write_file(
                module_path,
                create_module_template(module),
            )


def create_tests_structure() -> None:
    """
    Create testing structure.
    """

    print("\n[INFO] Creating tests structure...\n")

    ensure_directory(TESTS_ROOT)

    for category in TEST_CATEGORIES:
        category_path = TESTS_ROOT / category

        ensure_directory(category_path)

        write_file(
            category_path / "__init__.py",
            create_init_template(category),
        )

        for modules in STRUCTURE.values():
            for module in modules:
                test_name = f"test_{module}"

                write_file(
                    category_path / test_name,
                    create_test_template(module),
                )


def main() -> None:
    """
    Script entrypoint.
    """

    create_package_structure()
    create_tests_structure()

    print("\n[OK] pybuiltins bootstrap completed.\n")


if __name__ == "__main__":
    main()

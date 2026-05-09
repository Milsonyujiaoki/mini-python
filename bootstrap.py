from __future__ import annotations

from pathlib import Path
from typing import Iterable


ROOT = Path.cwd()


DIRECTORIES: tuple[str, ...] = (
    # =========================================================
    # FOUNDATIONS
    # =========================================================
    "foundations/pyiter/docs/comparisons",
    "foundations/pyiter/src/pyiter/core",
    "foundations/pyiter/src/pyiter/advanced",
    "foundations/pyiter/src/pyiter/infinite",
    "foundations/pyiter/src/pyiter/combinatorics",
    "foundations/pyiter/src/pyiter/typing",
    "foundations/pyiter/src/pyiter/utils",
    "foundations/pyiter/tests/unit",
    "foundations/pyiter/tests/integration",
    "foundations/pyiter/tests/property",
    "foundations/pyiter/tests/edge_cases",
    "foundations/pyiter/benchmarks/comparisons",
    "foundations/pyiter/examples",
    "foundations/pyiter/research",

    "foundations/pyfunctools/docs",
    "foundations/pyfunctools/src/pyfunctools/decorators",
    "foundations/pyfunctools/src/pyfunctools/caching",
    "foundations/pyfunctools/src/pyfunctools/utils",
    "foundations/pyfunctools/tests",
    "foundations/pyfunctools/benchmarks",
    "foundations/pyfunctools/examples",
    "foundations/pyfunctools/research",

    "foundations/pycollections/docs",
    "foundations/pycollections/src/pycollections/internal",
    "foundations/pycollections/src/pycollections/utils",
    "foundations/pycollections/tests",
    "foundations/pycollections/benchmarks",
    "foundations/pycollections/examples",
    "foundations/pycollections/research",

    "foundations/pyheap/docs",
    "foundations/pyheap/src/pyheap/algorithms",
    "foundations/pyheap/tests",
    "foundations/pyheap/benchmarks",
    "foundations/pyheap/examples",

    "foundations/pypath/docs",
    "foundations/pypath/src/pypath/utils",
    "foundations/pypath/tests",
    "foundations/pypath/examples",
    "foundations/pypath/research",

    # =========================================================
    # SYSTEMS
    # =========================================================
    "systems/pyio/docs",
    "systems/pyio/src/pyio/encodings",
    "systems/pyio/tests",
    "systems/pyio/benchmarks",

    "systems/pyhttp/docs",
    "systems/pyhttp/src/pyhttp/parsers",
    "systems/pyhttp/src/pyhttp/transports",
    "systems/pyhttp/src/pyhttp/pooling",
    "systems/pyhttp/tests",
    "systems/pyhttp/benchmarks",
    "systems/pyhttp/examples",
    "systems/pyhttp/wireshark",

    "systems/pyasync/docs",
    "systems/pyasync/src/pyasync/synchronization",
    "systems/pyasync/tests",
    "systems/pyasync/examples",
    "systems/pyasync/visualizations",

    "systems/pycache/src/pycache/storage",
    "systems/pycache/docs",
    "systems/pycache/tests",

    "systems/pyserialization/docs",
    "systems/pyserialization/src/pyserialization/formats",
    "systems/pyserialization/tests",
    "systems/pyserialization/examples",

    # =========================================================
    # DATABASES
    # =========================================================
    "databases/pyorm/docs",
    "databases/pyorm/src/pyorm/migrations",
    "databases/pyorm/src/pyorm/dialects",
    "databases/pyorm/src/pyorm/backends",
    "databases/pyorm/tests",
    "databases/pyorm/examples",

    "databases/pysql",
    "databases/pykv",

    # =========================================================
    # SCIENTIFIC
    # =========================================================
    "scientific/pynumpy/docs",
    "scientific/pynumpy/src/pynumpy/linalg",
    "scientific/pynumpy/src/pynumpy/random",
    "scientific/pynumpy/src/pynumpy/memory",
    "scientific/pynumpy/tests",
    "scientific/pynumpy/benchmarks",
    "scientific/pynumpy/visualizations",

    "scientific/pylinalg",
    "scientific/pystats",

    # =========================================================
    # LANGUAGE
    # =========================================================
    "language/pytokenizer/src/pytokenizer/grammar",
    "language/pytokenizer/docs",
    "language/pytokenizer/tests",

    "language/pyparser/src/pyparser/recursive_descent",
    "language/pyparser/docs",
    "language/pyparser/tests",

    "language/pyast",
    "language/pybytecode",
    "language/pyvm",

    # =========================================================
    # WEB
    # =========================================================
    "web/pywsgi",
    "web/pyasgi",
    "web/pyweb",
    "web/pyapi",

    # =========================================================
    # TOOLING
    # =========================================================
    "tooling/pytesting/src/pytesting",
    "tooling/pytesting/tests",
    "tooling/pytesting/docs",
    "tooling/pytesting/examples",

    "tooling/pybench",
    "tooling/pylogging",
    "tooling/pycli",

    # =========================================================
    # SHARED
    # =========================================================
    "shared/typing",
    "shared/testing",
    "shared/exceptions",
    "shared/protocols",
    "shared/utilities",
    "shared/profiling",
    "shared/benchmarking",
    "shared/constants",

    # =========================================================
    # DOCS
    # =========================================================
    "docs/architecture",
    "docs/internals",
    "docs/benchmarks",
    "docs/design-decisions",
    "docs/tradeoffs",
    "docs/implementation-notes",
    "docs/learning-path",
    "docs/diagrams",
    "docs/references",

    # =========================================================
    # EXPERIMENTS
    # =========================================================
    "experiments/performance",
    "experiments/memory",
    "experiments/networking",
    "experiments/parsing",
    "experiments/concurrency",
    "experiments/prototyping",

    # =========================================================
    # RESEARCH
    # =========================================================
    "research/cpython",
    "research/pypy",
    "research/asyncio",
    "research/networking",
    "research/compilers",
    "research/interpreters",
    "research/databases",
    "research/scientific_computing",
)


FILES: tuple[str, ...] = (
    # =========================================================
    # ROOT FILES
    # =========================================================
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "ROADMAP.md",
    "ARCHITECTURE.md",
    "Makefile",
    "pyproject.toml",
    ".gitignore",
    ".editorconfig",
    ".pre-commit-config.yaml",
    "mypy.ini",
    "pytest.ini",
    "ruff.toml",

    # =========================================================
    # PYITER
    # =========================================================
    "foundations/pyiter/README.md",
    "foundations/pyiter/pyproject.toml",

    "foundations/pyiter/docs/architecture.md",
    "foundations/pyiter/docs/iterators.md",
    "foundations/pyiter/docs/generators.md",
    "foundations/pyiter/docs/lazy-evaluation.md",
    "foundations/pyiter/docs/performance.md",
    "foundations/pyiter/docs/comparisons/itertools.md",

    "foundations/pyiter/src/pyiter/__init__.py",
    "foundations/pyiter/src/pyiter/protocols.py",
    "foundations/pyiter/src/pyiter/exceptions.py",

    "foundations/pyiter/src/pyiter/core/map.py",
    "foundations/pyiter/src/pyiter/core/filter.py",
    "foundations/pyiter/src/pyiter/core/zip.py",
    "foundations/pyiter/src/pyiter/core/enumerate.py",
    "foundations/pyiter/src/pyiter/core/range.py",

    "foundations/pyiter/src/pyiter/advanced/chain.py",
    "foundations/pyiter/src/pyiter/advanced/islice.py",
    "foundations/pyiter/src/pyiter/advanced/groupby.py",
    "foundations/pyiter/src/pyiter/advanced/tee.py",
    "foundations/pyiter/src/pyiter/advanced/batched.py",

    "foundations/pyiter/src/pyiter/infinite/count.py",
    "foundations/pyiter/src/pyiter/infinite/cycle.py",
    "foundations/pyiter/src/pyiter/infinite/repeat.py",

    "foundations/pyiter/src/pyiter/combinatorics/permutations.py",
    "foundations/pyiter/src/pyiter/combinatorics/combinations.py",
    "foundations/pyiter/src/pyiter/combinatorics/product.py",

    "foundations/pyiter/src/pyiter/typing/aliases.py",

    "foundations/pyiter/src/pyiter/utils/validation.py",
    "foundations/pyiter/src/pyiter/utils/helpers.py",

    "foundations/pyiter/benchmarks/benchmark_map.py",
    "foundations/pyiter/benchmarks/benchmark_chain.py",

    "foundations/pyiter/examples/lazy_pipeline.py",
    "foundations/pyiter/examples/infinite_iterators.py",
    "foundations/pyiter/examples/streaming.py",

    "foundations/pyiter/research/cpython_notes.md",
    "foundations/pyiter/research/iterator_protocol.md",
)


def create_directories(paths: Iterable[str]) -> None:
    """
    Create all directories recursively.

    Parameters
    ----------
    paths : Iterable[str]
        Collection of directory paths.
    """
    for path in paths:
        directory = ROOT / path
        directory.mkdir(parents=True, exist_ok=True)

        print(f"[DIR ] {directory}")


def create_files(paths: Iterable[str]) -> None:
    """
    Create all files if they do not exist.

    Parameters
    ----------
    paths : Iterable[str]
        Collection of file paths.
    """
    for path in paths:
        file_path = ROOT / path

        file_path.parent.mkdir(parents=True, exist_ok=True)

        if not file_path.exists():
            file_path.touch()

            print(f"[FILE] {file_path}")

        else:
            print(f"[SKIP] {file_path}")


def main() -> None:
    """
    Bootstrap the project structure.
    """
    print("=" * 60)
    print("BOOTSTRAPPING MINI-PYTHON PROJECT")
    print("=" * 60)

    create_directories(DIRECTORIES)
    create_files(FILES)

    print("\n[OK] Project structure created successfully.")


if __name__ == "__main__":
    main()

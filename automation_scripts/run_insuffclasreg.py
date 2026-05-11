"""Create a CodeQL DB from selected files and analyze with LintQ.

Example:
    python -m automation_scripts.run_insuffclasreg
"""

from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path
from typing import Iterable, List


def copy_selected_files(source_dir: Path, target_dir: Path, filenames: Iterable[str]) -> List[Path]:
    """Copy the selected files into the target directory and return their paths."""
    target_dir.mkdir(parents=True, exist_ok=True)
    copied: List[Path] = []
    for name in filenames:
        src = source_dir / name
        if not src.exists():
            raise FileNotFoundError(f"Missing source file: {src}")
        dst = target_dir / name
        shutil.copy(src, dst)
        copied.append(dst)
    return copied


def build_codeql_db(codeql_db: Path, source_root: Path) -> None:
    """Create or overwrite the CodeQL database."""
    codeql_db.parent.mkdir(parents=True, exist_ok=True)
    cmd = (
        f"codeql database create {codeql_db} "
        f"--language=python --overwrite --source-root={source_root}"
    )
    print(cmd)
    os.system(cmd)


def analyze_codeql(codeql_db: Path, qls_path: Path, sarif_out: Path) -> None:
    """Run the LintQ queries and output SARIF results."""
    sarif_out.parent.mkdir(parents=True, exist_ok=True)
    cmd = (
        f"codeql database analyze {codeql_db} "
        f"--format=sarifv2.1.0 --threads=10 "
        f"--output={sarif_out} --rerun -- {qls_path}"
    )
    print(cmd)
    os.system(cmd)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze specific InSuffClasReg files with LintQ."
    )
    parser.add_argument(
        "--dataset-folder",
        default=str(Path("data") / "datasets" / "InSuffClasReg"),
        help="Folder containing the source files.",
    )
    parser.add_argument(
        "--files",
        nargs="+",
        default=[
            "run1_ex.py",
            "run3_ex.py",
            "run6_ex.py",
            "run8_ex.py",
            "run10_ex.py",
        ],
        help="Exact filenames to include in the CodeQL DB.",
    )
    parser.add_argument(
        "--qls",
        default=str(Path("LintQ.qls")),
        help="Path to the LintQ .qls file.",
    )
    parser.add_argument(
        "--output",
        default=str(Path("data") / "datasets" / "InSuffClasReg" / "insuffclasreg_result.sarif"),
        help="Output SARIF path.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    dataset_folder = Path(args.dataset_folder)
    qls_path = Path(args.qls)
    output_sarif = Path(args.output)

    selected_files_dir = dataset_folder / "files_selected"
    codeql_db = dataset_folder / "codeql_db"

    # Refresh the selection folder to ensure only the target files are included.
    if selected_files_dir.exists():
        shutil.rmtree(selected_files_dir)

    copy_selected_files(dataset_folder, selected_files_dir, args.files)
    build_codeql_db(codeql_db, selected_files_dir)
    analyze_codeql(codeql_db, qls_path, output_sarif)


if __name__ == "__main__":
    main()

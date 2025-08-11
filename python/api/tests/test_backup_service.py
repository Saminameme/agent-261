import os
import tempfile
import asyncio
import sys

# Ensure repository root is on PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from python.helpers.backup import BackupService


def test_test_patterns_truncates_results_when_exceeding_max_files():
    service = BackupService()
    max_files = 5

    with tempfile.TemporaryDirectory(dir=service.agent_zero_root) as tmpdir:
        # Limit search scope to our temporary directory
        service.base_paths = {tmpdir: tmpdir}

        # Create more files than max_files
        for i in range(max_files + 3):
            file_path = os.path.join(tmpdir, f"file_{i}.txt")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("dummy")

        metadata = {
            "include_patterns": [os.path.join(tmpdir, "**")],
            "exclude_patterns": [],
            "include_hidden": False,
        }

        matched_files = asyncio.run(service.test_patterns(metadata, max_files=max_files))
        truncated = len(matched_files) >= max_files

    assert len(matched_files) == max_files
    assert truncated is True

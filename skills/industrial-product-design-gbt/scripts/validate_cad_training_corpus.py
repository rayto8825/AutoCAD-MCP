#!/usr/bin/env python3
"""Validate private CAD instruction-tuning JSONL before a local training run."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_TOP_LEVEL = {
    "schema_version",
    "example_id",
    "project_group",
    "system",
    "task",
    "evidence",
    "answer",
    "review",
    "privacy",
}
SYSTEMS = {
    "floor_plan",
    "elevation",
    "reflected_ceiling",
    "electrical",
    "plumbing",
    "furniture_equipment",
    "detail",
    "schedule",
    "sheet_layout",
    "integrated_set",
    "other",
    "not_available",
}


def validate(path: Path, *, training_ready: bool) -> tuple[list[str], int]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    count = 0
    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw in enumerate(handle, start=1):
            if not raw.strip():
                continue
            count += 1
            prefix = f"line {line_number}"
            try:
                item = json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"{prefix}: invalid JSON ({exc.msg})")
                continue
            if not isinstance(item, dict):
                errors.append(f"{prefix}: each JSONL row must be an object")
                continue
            missing = REQUIRED_TOP_LEVEL - item.keys()
            if missing:
                errors.append(f"{prefix}: missing keys: {', '.join(sorted(missing))}")
                continue
            example_id = item.get("example_id")
            if not isinstance(example_id, str) or not example_id.strip():
                errors.append(f"{prefix}: example_id must be a non-empty string")
            elif example_id in seen_ids:
                errors.append(f"{prefix}: duplicate example_id {example_id!r}")
            else:
                seen_ids.add(example_id)
            if item.get("schema_version") != 1:
                errors.append(f"{prefix}: unsupported schema_version")
            if item.get("system") not in SYSTEMS:
                errors.append(f"{prefix}: unknown system classification")
            for key in ("task", "answer", "project_group"):
                if not isinstance(item.get(key), str) or not item[key].strip():
                    errors.append(f"{prefix}: {key} must be a non-empty string")
            evidence = item.get("evidence")
            if not isinstance(evidence, dict) or not evidence.get("source_ref"):
                errors.append(f"{prefix}: evidence.source_ref is required")
            review = item.get("review")
            if not isinstance(review, dict):
                errors.append(f"{prefix}: review must be an object")
            elif training_ready and review.get("status") not in {"accepted", "corrected"}:
                errors.append(f"{prefix}: training-ready rows must be reviewed as accepted/corrected")
            privacy = item.get("privacy")
            if not isinstance(privacy, dict):
                errors.append(f"{prefix}: privacy must be an object")
            else:
                if privacy.get("contains_client_data") is True and privacy.get("may_leave_local_machine") is True:
                    errors.append(f"{prefix}: client data cannot be marked shareable outside the local machine")
                if training_ready and privacy.get("rights_checked") is not True:
                    errors.append(f"{prefix}: training-ready rows require rights_checked=true")
                if training_ready and privacy.get("contains_client_data") is True and privacy.get("may_leave_local_machine") is True:
                    errors.append(f"{prefix}: client-bearing rows are not eligible for export")
    if count == 0:
        errors.append("corpus has no examples")
    return errors, count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("jsonl", type=Path, help="Local corpus in one-example-per-line JSONL format")
    parser.add_argument(
        "--training-ready",
        action="store_true",
        help="Require reviewed rows and rights_checked=true in addition to structural checks",
    )
    args = parser.parse_args()
    if not args.jsonl.is_file():
        parser.error(f"corpus file does not exist: {args.jsonl}")
    errors, count = validate(args.jsonl, training_ready=args.training_ready)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Invalid corpus: {len(errors)} issue(s), {count} row(s)", file=sys.stderr)
        return 1
    mode = "training-ready" if args.training_ready else "structure-only"
    print(f"OK: {count} row(s) passed {mode} validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

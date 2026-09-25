#!/usr/bin/env python3
"""Compare monetary and time costs for user-supplied decision options."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def load_payload() -> dict:
    if len(sys.argv) > 2:
        raise SystemExit("usage: compare_options.py [decision.json]")
    if len(sys.argv) == 2:
        return json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    return json.load(sys.stdin)


def number(value, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a number")
    return float(value)


def main() -> None:
    payload = load_payload()
    options = payload.get("options")
    if not isinstance(options, list) or len(options) < 2:
        raise ValueError("options must contain at least two entries")

    values = payload.get("values_of_time", [])
    if not isinstance(values, list):
        raise ValueError("values_of_time must be a list")
    values = [number(v, "values_of_time") for v in values]

    normalized = []
    names = set()
    for index, raw in enumerate(options):
        if not isinstance(raw, dict):
            raise ValueError(f"options[{index}] must be an object")
        name = str(raw.get("name", "")).strip()
        if not name or name in names:
            raise ValueError("every option needs a unique non-empty name")
        names.add(name)
        probability = raw.get("risk_probability")
        consequence = raw.get("risk_consequence_hours")
        if (probability is None) != (consequence is None):
            raise ValueError(f"{name}: provide both risk_probability and risk_consequence_hours")
        risk_hours = 0.0
        if probability is not None:
            probability = number(probability, f"{name}.risk_probability")
            consequence = number(consequence, f"{name}.risk_consequence_hours")
            if not 0 <= probability <= 1:
                raise ValueError(f"{name}.risk_probability must be between 0 and 1")
            risk_hours = probability * consequence
        normalized.append(
            {
                "name": name,
                "money": number(raw.get("money"), f"{name}.money"),
                "time_hours": number(raw.get("time_hours"), f"{name}.time_hours"),
                "friction_money": number(raw.get("friction_money", 0), f"{name}.friction_money"),
                "expected_risk_hours": risk_hours,
            }
        )

    baseline_name = payload.get("baseline") or normalized[0]["name"]
    baseline = next((o for o in normalized if o["name"] == baseline_name), None)
    if baseline is None:
        raise ValueError("baseline must match an option name")

    scenarios = []
    for vot in values:
        rows = []
        for option in normalized:
            effective = (
                option["money"]
                + option["friction_money"]
                + (option["time_hours"] + option["expected_risk_hours"]) * vot
            )
            rows.append({"name": option["name"], "effective_cost": round(effective, 2)})
        scenarios.append({"value_of_time": vot, "options": rows})

    break_even = []
    for option in normalized:
        if option is baseline:
            continue
        premium = option["money"] + option["friction_money"] - baseline["money"] - baseline["friction_money"]
        time_saved = (
            baseline["time_hours"]
            + baseline["expected_risk_hours"]
            - option["time_hours"]
            - option["expected_risk_hours"]
        )
        value = premium / time_saved if premium > 0 and time_saved > 0 else None
        break_even.append(
            {
                "option": option["name"],
                "versus": baseline["name"],
                "premium": round(premium, 2),
                "time_saved_hours": round(time_saved, 4),
                "value_of_time": round(value, 2) if value is not None else None,
            }
        )

    print(json.dumps({"baseline": baseline["name"], "break_even": break_even, "scenarios": scenarios}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

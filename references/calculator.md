# Deterministic calculator

Use `scripts/compare_options.py` when the decision has numeric option data and arithmetic should be reproducible.

The script reads JSON from a file or standard input:

```json
{
  "baseline": "Hybrid",
  "values_of_time": [200, 400, 600, 1000],
  "options": [
    {"name": "Direct", "money": 13000, "time_hours": 0},
    {"name": "Hybrid", "money": 9000, "time_hours": 4}
  ]
}
```

`time_hours` means time consumed relative to the fastest option. Use usable time when that better reflects the decision. Optional fields:

- `friction_money`: only when the user explicitly supplies a monetary estimate;
- `risk_probability` and `risk_consequence_hours`: include both or neither.

Run:

```bash
python3 scripts/compare_options.py decision.json
```

The output includes effective cost at each supplied value of time and pairwise break-even values against the baseline. A negative or missing break-even means the comparison does not represent paying more to save time; explain the trade-off directly instead.


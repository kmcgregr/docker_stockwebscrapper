from pathlib import Path
from typing import Iterable, Optional, Union

import pandas as pd


def _is_missing(value) -> bool:
    try:
        return bool(pd.isna(value))
    except (TypeError, ValueError):
        return False


def _as_float(value) -> Optional[float]:
    try:
        return float(str(value).replace(",", "").strip())
    except (TypeError, ValueError):
        return None


def _format_value(
    value,
    column: str,
    float_columns: frozenset,
    date_columns: frozenset,
) -> str:
    if _is_missing(value):
        return ""

    if pd.api.types.is_datetime64_any_dtype(type(value)) or isinstance(value, pd.Timestamp):
        return pd.Timestamp(value).strftime("%Y-%m-%d")

    if isinstance(value, pd.Period):
        return value.to_timestamp().strftime("%Y-%m-%d")

    if isinstance(value, pd.Timedelta):
        return str(value)

    if column in float_columns:
        number = _as_float(value)
        return "" if number is None else f"{number:.2f}"

    return str(value)


def to_markdown(
    df: pd.DataFrame,
    float_columns: Optional[Iterable[str]] = None,
    date_columns: Optional[Iterable[str]] = None,
) -> str:
    columns = [str(column) for column in df.columns]
    float_columns = frozenset(str(column) for column in (float_columns or ()))
    date_columns = frozenset(str(column) for column in (date_columns or ()))

    for column in date_columns:
        if column in columns:
            df[column] = pd.to_datetime(df[column], errors="coerce")

    lines = [
        "| " + " | ".join(columns) + " |",
        "|" + "|".join("---" for _ in columns) + "|",
    ]

    for record in df.itertuples(index=False, name=None):
        cells = [
            _format_value(value, column, float_columns, date_columns)
            for value, column in zip(record, columns)
        ]
        lines.append("| " + " | ".join(cells) + " |")

    return "\n".join(lines) + "\n"


def export_to_markdown(
    df: pd.DataFrame,
    path: Union[str, Path],
    float_columns: Optional[Iterable[str]] = None,
    date_columns: Optional[Iterable[str]] = None,
) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        to_markdown(df, float_columns=float_columns, date_columns=date_columns),
        encoding="utf-8",
    )
    return target

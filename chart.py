"""Zero-dependency SVG trend chart builder."""

from typing import List


def render_svg_line(values: List[float], width: int = 420, height: int = 160) -> str:
    if not values:
        return "<svg></svg>"
    peak = max(values) or 1.0
    step_x = width / max(1, len(values) - 1)
    points = []
    for idx, val in enumerate(values):
        x = round(idx * step_x, 1)
        y = round(height - (val / peak) * (height - 20) - 10, 1)
        points.append(f"{x},{y}")
    poly = " ".join(points)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">'
        f'<polyline fill="none" stroke="#e63946" stroke-width="2.5" points="{poly}" />'
        "</svg>"
    )

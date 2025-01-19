from typing import Iterable

from plotly.subplots import make_subplots
import plotly.graph_objects as go
from plotly.graph_objects import Figure


def traditional_plot(positions: Iterable, values: Iterable) -> Figure:
    fig = make_subplots(
        rows=2, cols=3, subplot_titles=["N", "Vy", "Vz", "Tx", "My", "Mz"]
    )

    fig.add_trace(go.Scatter(x=positions, y=values[:, 0]), row=1, col=1)

    fig.add_trace(go.Scatter(x=positions, y=values[:, 1]), row=1, col=2)

    fig.add_trace(go.Scatter(x=positions, y=values[:, 2]), row=1, col=3)

    fig.add_trace(go.Scatter(x=positions, y=values[:, 3]), row=2, col=1)

    fig.add_trace(go.Scatter(x=positions, y=values[:, 4]), row=2, col=2)

    fig.add_trace(go.Scatter(x=positions, y=values[:, 5]), row=2, col=3)

    fig.update_layout(title_text="Traditional plot", showlegend=False)

    return fig


def parallel_plot(positions: Iterable, values: Iterable) -> Figure:
    fig = go.Figure(
        data=go.Parcoords(
            dimensions=list(
                [
                    dict(
                        label="N",
                        values=values[:, 0],
                    ),
                    dict(
                        label="Vy",
                        values=values[:, 1],
                    ),
                    dict(
                        label="Vz",
                        values=values[:, 2],
                    ),
                    dict(
                        label="Tx",
                        values=values[:, 3],
                    ),
                    dict(
                        label="My",
                        values=values[:, 4],
                    ),
                    dict(
                        label="Mz",
                        values=values[:, 5],
                    ),
                ]
            ),
        )
    )
    return fig



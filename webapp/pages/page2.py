import dash
from dash import html, dcc, Output, Input, callback
from flask_login import current_user

from webapp import redis_client
from webapp.login_handler import require_login


dash.register_page(__name__)
require_login(__name__)


def layout():
    if not current_user.is_authenticated:
        return html.Div(["Please ", dcc.Link("login", href="/login"), " to continue"])

    return html.Div(
        [
            html.H1("Page 2"),
            dcc.RadioItems(
                id="page-2-radios",
                options=[{"label": i, "value": i} for i in ["Orange", "Blue", "Red"]],
                value="Orange",
            ),
            html.Div(id="page-2-content"),
            html.Br(),
            dcc.Link("Go to Page 1", href="/page1"),
            html.Br(),
            dcc.Link("Go back to home", href="/"),
            html.Br(),
            html.Button(id="button-counter", n_clicks=0),
            html.Div(id="div-counter", children=[]),
        ]
    )


@callback(Output("page-2-content", "children"), Input("page-2-radios", "value"))
def page_2_radios(value):
    return f'You have selected "{value}"'


@callback(Output("div-counter", "children"), Input("button-counter", "n_clicks"))
def on_button_counter(n_clicks):
    redis_client.get_redis_client().incr('hits')
    return f"Number of hits {redis_client.get_redis_client().get('hits')}"

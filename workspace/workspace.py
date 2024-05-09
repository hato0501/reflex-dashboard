"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from workspace.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from workspace.pages.tools import tools
from workspace.pages.team import team
from workspace.pages.index import index

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(tools, route="/tools")
app.add_page(team, route="/team")

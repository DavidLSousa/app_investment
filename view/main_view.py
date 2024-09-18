from dataclasses import dataclass
from flask import render_template

@dataclass
class MainView:

    @classmethod
    def render_main_page(cls):
        return render_template('main_page.html')
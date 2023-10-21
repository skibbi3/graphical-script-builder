from dash import Dash, dcc, html, callback, Output, Input, State, dash_table
import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    brand="Script Formatter"
)

forms = dbc.Container(
    children=[
        dbc.FormFloating(
            [
                dbc.Input(placeholder="Title of program", id='program-title'),
                dbc.Label("Title of program"),
            ]
        ),
        html.Br(),
        dbc.FormFloating(
            [
                dbc.Input(placeholder="Program code", id='program-code'),
                dbc.Label("Program code"),
            ]
        ),
        html.Br(),
        dbc.FormFloating(
            [
                dbc.Input(placeholder="Duration", id='duration'),
                dbc.Label("Duration"),
            ]
        ),
        html.Br(),
        dbc.FormFloating(
            [
                dbc.Input(placeholder="Date", id='date'),
                dbc.Label("Date of this draft"),
            ]
        ),
        html.Br(),
        dbc.FormFloating(
            [
                dbc.Input(placeholder="Version", id='version'),
                dbc.Label("Version"),
            ]
        ),
        html.Br(),
        dbc.FormFloating(
            [
                dbc.Input(placeholder="Script Written By", id='writtenby'),
                dbc.Label("Script Written By"),
            ]
        ),
        html.Br(),
        dbc.FormFloating(
            [
                dbc.Input(placeholder="Script Edited By", id='editedby'),
                dbc.Label("Script Edited By"),
            ]
        )
    ] 
)

table = dash_table.DataTable(
    id="script-table",
    editable=True,
    row_deletable=True,
    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
    },
    style_cell={'textAlign': 'left'},
    style_cell_conditional=[
        {
            'if': {'column_id':'scene'},
            'width':'10%'
        },
        {
            'if': {'column_id':'duration'},
            'width':'10%'
        },
        {
            'if': {'column_id':'video'},
            'width':'40%'
        },
        {
            'if': {'column_id':'audio'},
            'width':'40%'
        }
    ],
    columns=(
        [
            {'id':'scene', 'name':'Scene'},
            {'id':'duration', 'name':'Duration'},
            {'id':'video', 'name':'Video'},
            {'id':'audio', 'name':'Audio'}
        ]
    ),
    data=(
        [
            {'scene':'000', 'duration':'', 'video':'', 'audio':''}
        ]
    )
)
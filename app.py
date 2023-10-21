from dash import Dash, dcc, html, callback, Output, Input, State, dash_table
import dash_bootstrap_components as dbc

# Components stored externally
import layouts.layout as layout
import callbacks.callbacks as callbacks

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    children=[
        layout.navbar,
        dcc.Download(id="save-work-download"),
        dcc.Download(id="export-work-download"),
        
        dbc.Container(
            children=[
                layout.forms,                
                dbc.Button(
                    "Add row",
                    color="primary",
                    class_name="me-1",
                    id="add-row"
                ),
                dbc.Button(
                    "Save",
                    color="primary",
                    class_name="me-1",
                    id="save-work-button"
                ),
                dbc.Button(
                    "Export",
                    color="primary",
                    class_name="me-1",
                    id="export-work-button"
                ),
                dcc.Upload(
                    id="previous-work-upload",
                    children=[
                        dbc.Button(
                            "Upload",
                            color="primary",
                            id="upload-button"
                        )
                    ]
                ),
                layout.table,
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
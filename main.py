import flet as ft

class Player:
    def __init__(self, name, score_field):
        self.name = name
        self.score_field = score_field

def safe_float(value):
    """Converts a string to a float, returns 0.0 if conversion fails."""
    try:
        return float(value) if value.strip() else 0.0
    except ValueError:
        return 0.0

def update_leaderboard(page, players):
    # Sort players based on their scores
    sorted_players = sorted(players, key=lambda p: safe_float(p.score_field.value), reverse=True)

    # Update the DataTable rows
    leaderboard.rows = [
        ft.DataRow(cells=[
            ft.DataCell(ft.Text(player.name)),
            ft.DataCell(ft.Text(f"{safe_float(player.score_field.value):.2f}")),
        ]) for player in sorted_players
    ]
    
    # Re-render the page to update the changes
    page.update()

def on_button_click(e, page, players):
    # Calculate the scores
    whistA = safe_float(txtab.value) - safe_float(txtba.value) + safe_float(txtac.value) - safe_float(txtca.value) + safe_float(txtad.value) - safe_float(txtda.value)
    whistB = safe_float(txtba.value) - safe_float(txtab.value) + safe_float(txtbc.value) - safe_float(txtcb.value) + safe_float(txtbd.value) - safe_float(txtdb.value)
    whistC = safe_float(txtca.value) - safe_float(txtac.value) + safe_float(txtcb.value) - safe_float(txtbc.value) + safe_float(txtcd.value) - safe_float(txtdc.value)
    whistD = safe_float(txtda.value) - safe_float(txtad.value) + safe_float(txtdb.value) - safe_float(txtbd.value) + safe_float(txtdc.value) - safe_float(txtcd.value)
    
    mount_list = [safe_float(mounta.value), safe_float(mountb.value), safe_float(mountc.value), safe_float(mountd.value)]

    finScoreA = whistA + 10 / 4 * (sum(mount_list) - 4 * min(mount_list)) - 10 * (safe_float(mounta.value) - min(mount_list))
    finScoreB = whistB + 10 / 4 * (sum(mount_list) - 4 * min(mount_list)) - 10 * (safe_float(mountb.value) - min(mount_list))
    finScoreC = whistC + 10 / 4 * (sum(mount_list) - 4 * min(mount_list)) - 10 * (safe_float(mountc.value) - min(mount_list))
    finScoreD = whistD + 10 / 4 * (sum(mount_list) - 4 * min(mount_list)) - 10 * (safe_float(mountd.value) - min(mount_list))

    # Update player scores
    players[0].score_field.value = f"{finScoreA:.2f}"
    players[1].score_field.value = f"{finScoreB:.2f}"
    players[2].score_field.value = f"{finScoreC:.2f}"
    players[3].score_field.value = f"{finScoreD:.2f}"

    update_leaderboard(page, players)

def main(page: ft.Page):
    # META
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Controllers
    global txtab, mounta, txtac, txtad, txtba, mountb, txtbc, txtbd, txtca, mountc, txtcb, txtcd, txtda, mountd, txtdb, txtdc
    txtab = ft.TextField(label="A-B", width=100)
    mounta = ft.TextField(label="Mount A", width=100, value="0")
    txtac = ft.TextField(label="A-C", width=100)
    txtad = ft.TextField(label="A-D", width=100)

    txtba = ft.TextField(label="B-A", width=100)
    mountb = ft.TextField(label="Mount B", width=100, value="0")
    txtbc = ft.TextField(label="B-C", width=100)
    txtbd = ft.TextField(label="B-D", width=100)

    txtca = ft.TextField(label="C-A", width=100)
    mountc = ft.TextField(label="Mount C", width=100, value="0")
    txtcb = ft.TextField(label="C-B", width=100)
    txtcd = ft.TextField(label="C-D", width=100)

    txtda = ft.TextField(label="D-A", width=100)
    mountd = ft.TextField(label="Mount D", width=100, value="0")
    txtdb = ft.TextField(label="D-B", width=100)
    txtdc = ft.TextField(label="D-C", width=100)

    # Initialize players with their respective score fields
    players = [
        Player(name="Player A", score_field=mounta),
        Player(name="Player B", score_field=mountb),
        Player(name="Player C", score_field=mountc),
        Player(name="Player D", score_field=mountd),
    ]

    # Initialize leaderboard with empty values
    global leaderboard
    leaderboard = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Name")),
            ft.DataColumn(label=ft.Text("Score")),
        ],
        rows=[
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(player.name)),
                ft.DataCell(ft.Text("0")),
            ]) for player in players
        ]
    )

    # Button to update leaderboard
    update_button = ft.ElevatedButton(
        text="Update Leaderboard",
        on_click=lambda e: on_button_click(e, page, players)
    )

    short_divider = ft.Container(
        content=ft.Divider(),
        width=200,  # Set the desired width of the divider
        alignment=ft.alignment.center
    )

    # Page Builder
    input_column = ft.Column([
        ft.Row([txtab, mounta]),
        ft.Row([txtac, txtad]),
        short_divider,

        ft.Row([txtba, mountb]),
        ft.Row([txtbc, txtbd]),
        short_divider,

        ft.Row([txtca, mountc]),
        ft.Row([txtcb, txtcd]),
        short_divider,

        ft.Row([txtda, mountd]),
        ft.Row([txtdb, txtdc]),
    ])

    # Add the button and leaderboard to the page
    main_row = ft.Row([
        input_column,
        ft.Container(width=20),  # Add some spacing between the columns if needed
        ft.Column([
            update_button,
            leaderboard
        ]),
    ])

    # Page Builder
    page.add(main_row)

ft.app(main)
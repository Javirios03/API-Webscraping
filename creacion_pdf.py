from fpdf import FPDF
import pandas as pd
import api_basketball as api
import dataframe_image as dfi


def stats_to_png(df: pd.DataFrame, name: str):
    dfi.export(df, name+".png")


def write_to_pdf(png1: str, png2: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('Arial', '', 12)

    pdf.image(png1,x=50, y=30, w=110, h= 60)
    pdf.ln(5)
    pdf.set_xy(50, 110)
    pdf.cell(110, 10, "Statistics of the games played by the team in percentages")

    pdf.set_xy(50, 140)
    pdf.image(png2, w=110, h=60)
    pdf.ln(5)
    pdf.set_xy(45,210)
    pdf.cell(260, 10, "Statistics of the points scored during games, both for and against")

    pdf.output("reporte_nba.pdf")


if __name__ == "__main__":
    print("Bienvenido al analizador de equipos de baloncesto de la NBA")
    print("A continuación, se mostrará una lista de los equipos disponibles para obtener datos")
    ids = api.equipos()
    equipo = input("Elija por favor uno de los equipos listados previamente (introduzca el nombre tal y como aparece en la consola): ")
    try:
        team_id = ids[equipo]
    except Exception:
        print("Ha introducido un nombre incorrecto, se cerrará el programa")
        exit()
    df_games, df_points = api.get_stats(team_id)
    stats_to_png(df_games, "Games played")
    stats_to_png(df_points, "Points scored")
    write_to_pdf("Games played.png", "Points scored.png")

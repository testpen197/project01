import pandas


def prepare_data(explorator_df):

	adjacent_table = {row["noeud_amont"] : row["noeud_aval"] for _, row in explorator_df.iterrows()}
	
	starting_nodes = explorator_df[explorator_df["type_aretes"] == "depart"]["noeud_amont"].values
	
	ending_nodes = set(explorator_df[explorator_df["type_aretes"] == "arrivee"]["noeud_aval"].values)

	return adjacent_table, starting_nodes, ending_nodes

explorator_df = pandas.read_csv("./parcours_explorateurs.csv")
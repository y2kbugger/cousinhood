import matplotlib.pyplot as plt
import logging
logging.getLogger('matplotlib.font_manager').disabled = True

taboo_vs_cousinhood = [
    (0.1, 10, "Sibling"), # fudge for plotting
    (1, 5, "First Cousin"),
    (2, 2, "Second Cousin"),
    (6, 0, "6th Cousin"),
    (100, 0, "100th Cousin"),

    (2500, 0.8, "Migration from Africa"), # 55_000 year, 22yr_gen
    (7000, 1.9, "mitochondrial Eve"), # 155_000 year, 22yr_gen
    (12500, 2.2, "Y-chromosomal Adam"), # 275_000 year, 22yr_gen

    (24_000, 3.1, "Neanderthal"), # 588_000 years ago, 20yr_gen
    (145_000, 8, "A. afarensis"),
    (284_000, 13, "Chimpanzee"),
    (359_000, 14, "Mountain Gorilla"),
    (709_000, 17, "Orangutan"),
    (1_000_000, 17.3, "Gibbon"),
    (1_700_000, 16.4, "De Brazza's Monkey"),
    (3_200_000, 16, "Squirrel Monkey"),
    (6_700_000, 15, "Tarsier"),
    (16_000_000, 13, "House Mouse"),
    (21_000_000, 12, "Domesticated Cat"),
    (86_000_000, 11.5, "Red necked wallaby"),
    (124_000_000, 8, "Canadian Goose"),
    (223_000_000, 5, "Sea Lamprey"),
    (327_000_000, 4, "Red Wiggler Worm"),
    (497_000_000, 2.5, "Comb Jelly"),
    (697_000_000, 1.1, "Morel Mushroom"),
    (897_000_000, .8, "Amoeba"),
    (2_900_000_000, .5, "Pine Cone"),
    (6_900_000_000, .3, "S. hantzschii (Diatom)"),
    (357_900_000_000, .2, "H. walsbyi (Archaea)"),
    (706_000_000_000, .1, "E. coli"),
    # https://www.evogeneao.com/en/explore/cousin-table lots of help
]
yaxis_label = "Degree of Taboo in Sexual Relationships"
xaxis_label = "Cousinhood"

# xkcd style chart
with plt.xkcd():
    fig, ax = plt.subplots(figsize=(25, 5))
    x, y, labels = zip(*taboo_vs_cousinhood)
    ax.plot(x, y, marker=None)
    ax.set_xscale("log")
    ax.set_xlabel(xaxis_label)
    ax.set_ylabel(yaxis_label)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=55, ha="right", fontsize=10)
    # set x min to zero
    ax.set_xlim(left=0.07, right=1_000_000_000_000)
    ax.grid(True)
    ax.set_title("Sexual Taboo vs Cousinhood")
    # hide y axis number
    ax.set_yticklabels([])
    plt.show()

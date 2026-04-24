import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

def gen_paper_base():
    paper_corners = np.array([[0,0],[1,0],[0,1],[1,1]])
    creases = [
        [0,0,1,1,1],
        [1,0,0,1,1],
        [0,0.5,1,0.5,-1]
    ]

    df = pd.DataFrame(creases, columns=['x1','y1','x2','y2','type'])
    return df

def plot_creases_pattern(df):
    plt.figure(figsize=(5,5))

    for _, row in df.iterrows():
        color = 'red' if row['type'] == 1 else 'blue'
        style = '-' if row['type'] == 1 else '--'
        plt.plot([row['x1'], row['x2']], [row['y1'], row['y2']],
        color = color, linestyle = style, lw=2)

        plt.xlim(-0.1, 1.1)
        plt.ylim(-0.1, 1.1)
        plt.title('generated paper with pattern')
        plt.grid(True)
        plt.show()

pattern_df = gen_paper_base()
print(pattern_df)
plot_creases_pattern(pattern_df)

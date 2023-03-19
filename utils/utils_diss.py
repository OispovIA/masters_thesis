###############################
#                             
#      PRINT FACTOR LEVELS
#                             
###############################

import matplotlib.pyplot as plt

def residual_plot(target, prediction, score=None, marks=10):
    fig, ax = plt.subplots()
    plt.rcParams["figure.figsize"] = (8, 8)

    if score:
        ax.set_title(f'Residual_plot (R2 ={score.round(3)})')

    ax.plot(target, prediction, "o", markevery=marks)
    ax.plot([0, 0.5], [0, 0.5], 'k--', lw=3)
    ax.set_xlabel('Measured')
    ax.set_ylabel('Predicted')
    ax.set_ylim(bottom=0, top=0.5)
    ax.set_xlim(left=0, right=0.5)

    plt.show()
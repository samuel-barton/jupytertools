import matplotlib.pyplot as plt

def darkPlot(x,y,style,color='white'):
    '''
        This function sets up and does a plot 
        on a dark themed notebook. It removes
        the background color of the plot and
        sets all the outline and text colors 
        to white.
    '''
    fig = plt.figure()
    fig.patch.set_alpha(0.0)
    ax = fig.add_subplot(111)
    ax.plot(x, y,style)
    ax.patch.set_alpha(0.0)
    ax.tick_params(axis='x', colors=color)
    ax.tick_params(axis='y', colors=color)
    ax.yaxis.label.set_color(color)
    ax.xaxis.label.set_color(color)
    ax.title.set_color(color)
    ax.spines['bottom'].set_color(color)
    ax.spines['top'].set_color(color)
    ax.spines['left'].set_color(color)
    ax.spines['right'].set_color(color)
    plt.show()
    return

def darkFigure(fig, color="white"):
    '''
        Make a matplotlib.pyplot figure be formatted correctly for Dark themed
        Jupyter Notebooks.
    '''
    fig.patch.set_alpha(0.0)
    fig.patch.set_alpha(0.0)
    fig.tick_params(axis='x', colors=color)
    fig.tick_params(axis='y', colors=color)
    fig.yaxis.label.set_color(color)
    fig.xaxis.label.set_color(color)
    fig.title.set_color(color)
    fig.spines['bottom'].set_color(color)
    fig.spines['top'].set_color(color)
    fig.spines['left'].set_color(color)
    fig.spines['right'].set_color(color)
    return

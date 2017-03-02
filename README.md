# Useful Python Functions for Scientific Programming in Jupyter Notebooks


## Make plots visible on dark themed notebooks

The function is `darkPlot(x,y,style,color)`. This function is used to make plotting with 
matplotlib on dark themes, see https://github.com/dunovank/jupyter-themes, usable by changing the
color of the frame, text, labels, and ticks of the plot. 

    The arguments to darkPlot(...) mean the following.
        x       the array of values to be plotted along the x-axis of the plot
        y       the array of values to be plotted along the y-axis of the plot
        style   the style string passed to matplotlib.pyplot.plot(...)
        color   the color of the plot's trimmings, defaults to white.

### Dependencies

This package depends on the following Python packages in order to operate

    matplotlib



### Deployment

Use `pip` to install this package with the following command.

    pip install git+https://github.com/samuel-barton/jupytertools

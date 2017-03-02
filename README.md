# Useful Python Functions for Scientific Programming in Jupyter Notebooks


## Make plots visible on dark themed notebooks

The function is `darkPlot(x,y,style,color)`. This function is used to make plotting with 
matplotlib on dark themes, see https://github.com/dunovank/jupyter-themes, usable by changing the
color of the frame, text, labels, and ticks of the plot. Beyond this, any time you wish to have 
custom colored plot frames with transparent backgrounds this function will do the trick. 

    The arguments to darkPlot(...) mean the following.
        x       the array of values to be plotted along the x-axis of the plot
        y       the array of values to be plotted along the y-axis of the plot
        style   the style string passed to matplotlib.pyplot.plot(...) see [here](http://matplotlib.org/api/markers_api.html) 
        color   the color of the plot's trimmings, defaults to white.

This function acts as a replacement for both `matplotlib.pyplot.plot(...)` and 
`matplotlib.plot.show()`. When you wish to do a plot using `darkPlot(...)` just type 

```python
# assuming x and y are arrays ready to plot
import jupytertools
style = 'o' # choose your styling options from the pyplot format string options.
color = 'red' # Optional color argument, if left out color is white
jupytertools.darkPlot(x,y,style,color)
```

### Dependencies

This package depends on the following Python packages in order to operate

    matplotlib



### Deployment

Use `pip` to install this package with the following command.

    pip install git+https://github.com/samuel-barton/jupytertools

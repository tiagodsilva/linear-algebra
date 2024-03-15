import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np 
matplotlib.rcParams.update({
    'font.family' : 'serif',
    'font.size' : 14.0,
    'lines.linewidth' : 2,
    'lines.antialiased' : True,
    'axes.facecolor': 'fdfdfd',
    'axes.edgecolor': '777777',
    'axes.linewidth' : 1,
    'axes.titlesize' : 'medium',
    'axes.labelsize' : 'medium',
    'axes.axisbelow' : True,
    # 'xtick.major.size'     : 0,      # major tick size in points
    # 'xtick.minor.size'     : 0,      # minor tick size in points
    # 'xtick.major.pad'      : 6,      # distance to major tick label in points
    # 'xtick.minor.pad'      : 6,      # distance to the minor tick label in points
    'xtick.color'          : '333333', # color of the tick labels
    'xtick.labelsize'      : 'medium', # fontsize of the tick labels
    'xtick.direction'      : 'in',     # direction: in or out
    'ytick.major.size'     : 0,      # major tick size in points
    'ytick.minor.size'     : 0,      # minor tick size in points
    'ytick.major.pad'      : 6,      # distance to major tick label in points
    'ytick.minor.pad'      : 6,      # distance to the minor tick label in points
    'ytick.color'          : '333333', # color of the tick labels
    'ytick.labelsize'      : 'medium', # fontsize of the tick labels
    'ytick.direction'      : 'in',     # direction: in or out
    'axes.grid' : True,
    'grid.alpha' : 0.3,
    'grid.linewidth' : 1,
    'legend.fancybox' : True,
    'legend.fontsize' : 'Small',
    'figure.figsize' : (2.5, 2.5),
    'figure.facecolor' : '1.0',
    'figure.edgecolor' : '0.5',
    'hatch.linewidth' : 0.1,
    'text.usetex' : True 
    })
plt.rcParams['text.latex.preamble'] = r'\usepackage{times, amsmath, amssymb}'
from matplotlib.ticker import FuncFormatter
def my_formatter(x, pos):
    """Format 1 as 1, 0 as 0, and all values whose absolute values is between
    0 and 1 without the leading "0." (e.g., 0.7 is formatted as .7 and -0.4 is
    formatted as -.4)."""
    val_str = '{:g}'.format(x)
    if np.abs(x) > 0 and np.abs(x) < 1:
        return val_str.replace("0", "", 1)
    else:
        return val_str
def evenly_spaced_ticks(ax, axis='x', n=5): 
    if axis == 'x': 
        max_v = max(ax.get_xlim()) 
    elif axis == 'y': 
        max_v = max(ax.get_ylim())
    else: 
        raise ValueError(axis) 
    tick_positions = [i / (n + 1) * max_v for i in range(1, n + 1)] 
    primitive = ax.xaxis if axis == 'x' else ax.yaxis 
    primitive.set_major_locator(FixedLocator(tick_positions))

major_formatter = FuncFormatter(my_formatter)
from matplotlib.ticker import NullFormatter
from matplotlib.ticker import ScalarFormatter, StrMethodFormatter, MaxNLocator, FixedLocator 

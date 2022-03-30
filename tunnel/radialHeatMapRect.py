import numpy as np
#from matplotlib.path import Path

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

from  mpl_toolkits.axisartist.grid_helper_curvelinear import GridHelperCurveLinear
from mpl_toolkits.axisartist import Subplot

from mpl_toolkits.axisartist import SubplotHost, \
     ParasiteAxesAuxTrans

import  mpl_toolkits.axisartist.angle_helper as angle_helper
from matplotlib.projections import PolarAxes
from matplotlib.transforms import Affine2D

def createTunnel(radius=1,centerSize=0,nbOfLines=400,function=None,symetry=8,t=0):
    n = nbOfLines
    m = 100
    rad = np.linspace(centerSize, radius, m)
    a = np.linspace(0, 360, n)
    r, th = np.meshgrid(rad, a)
    z=np.zeros((n,m))
    symAngleSize=int(n/symetry)
    for i in range(m):
        currentRad=rad[i]
        for j in range(symAngleSize):
            theta=a[j]
            for k in range(symetry):
                if k%2:
                    z[k*symAngleSize+j][i]=np.cos(2*currentRad)*np.tan(2*np.pi*theta/360)
                else:
                    z[(k+1)*symAngleSize-j-1][i]=np.cos(2*currentRad)*np.tan(2*np.pi*theta/360)
    return(r,th,z)

def PolarasRect(fig):
    from  mpl_toolkits.axisartist.grid_helper_curvelinear import GridHelperCurveLinear
    from mpl_toolkits.axisartist import Subplot

    from mpl_toolkits.axisartist import SubplotHost, \
     ParasiteAxesAuxTrans

    import  mpl_toolkits.axisartist.angle_helper as angle_helper
    from matplotlib.projections import PolarAxes
    from matplotlib.transforms import Affine2D
    """
    polar projection, but in a rectangular box.
    """

    # PolarAxes.PolarTransform takes radian. However, we want our coordinate
    # system in degree
    tr = Affine2D().translate(-135,0) + Affine2D().scale(np.pi/180., 1.) + PolarAxes.PolarTransform()

    # polar projection, which involves cycle, and also has limits in
    # its coordinates, needs a special method to find the extremes
    # (min, max of the coordinate within the view).

    # 20, 20 : number of sampling points along x, y direction
    extreme_finder = angle_helper.ExtremeFinderCycle(20, 20,
                                                     lon_cycle = 360,
                                                     lat_cycle = None,
                                                     lon_minmax = None,
                                                     lat_minmax = (0, np.inf),
                                                     )

    grid_locator1 = angle_helper.LocatorDMS(12)
    # Find a grid values appropriate for the coordinate (degree,
    # minute, second).

    tick_formatter1 = angle_helper.FormatterDMS()
    # And also uses an appropriate formatter.  Note that,the
    # acceptable Locator and Formatter class is a bit different than
    # that of mpl's, and you cannot directly use mpl's Locator and
    # Formatter here (but may be possible in the future).

    grid_helper = GridHelperCurveLinear(tr,
                                        extreme_finder=extreme_finder,
                                        grid_locator1=grid_locator1,
                                        tick_formatter1=tick_formatter1
                                        )


    ax1 = SubplotHost(fig, 1, 1, 1, grid_helper=grid_helper)

    # make ticklabels of right and top axis visible.
    ax1.axis["right"].major_ticklabels.set_visible(False)
    ax1.axis["top"].major_ticklabels.set_visible(False)
    ax1.tick_params(left=False,bottom=False,labelleft=False,labelbottom=False)

    # let right axis shows ticklabels for 1st coordinate (angle)
    ax1.axis["right"].get_helper().nth_coord_ticks=0
    # let bottom axis shows ticklabels for 2nd coordinate (radius)
    ax1.axis["bottom"].get_helper().nth_coord_ticks=1

    fig.add_subplot(ax1)


    # A parasite axes with given transform
    ax2 = ParasiteAxesAuxTrans(ax1, tr, "equal")
    # note that ax2.transData == tr + ax1.transData
    # Anthing you draw in ax2 will match the ticks and grids of ax1.
    ax1.parasites.append(ax2)

    ax1.set_aspect(1)
    ax1.set_xlim(-1, 1)
    ax1.set_ylim(-1, 1)


    ax1.grid(True)
    return ax1, ax2

if 1:
    fig = plt.figure()
    fig.clf()

    ax, aux_ax = PolarasRect(fig)
    z,ra = np.random.rand(200000), 360*np.random.rand(200000)
    #z = [0.11693845,0.09111419,0.09107255,0.09114332,0.09113075,0.09117671,0.09107338,0.10745689,0.09192869,0.08961995]
    #ra = [2.34269333,2.26779991,2.26750563,2.26784652,2.26796822,2.26747208, 2.26755943,2.2657325, 2.26631627,2.34835654]
    (r,th,z)=createTunnel()
    aux_ax.pcolormesh(th, r, z, cmap = 'Blues',shading='auto')
    plt.show()
    '''from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
    axins = zoomed_inset_axes(ax, 2.5, loc=2) # zoom-factor: 2.5, location: upper-left
    axins.scatter(ra,z,c='r',s=10.0,linewidths=0.0)
    plt.show()'''
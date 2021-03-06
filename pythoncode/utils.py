import numpy as np

from network_loader import SeizureData
from relabeling_functions import relabel, reorder

def normalise(series):
    #return series
    a = np.min(series, axis=1)
    b = np.max(series, axis=1)
    return np.divide((series - a[:, None]), (b-a)[:,None])


mc = {'b' :(77, 117, 179),
      'r' :(210, 88, 88),
      'k' :(38,35,35),
      'white':(255,255,255),
     'grey':(197,198,199)}

for key in mc.keys():
    mc[key] = [x / 255.0 for x in mc[key]]
    #print key, mc[key]

def raw_validation_load():
    dirpath1 = '/Users/Jonathan/PhD/Seizure_related/batchSept_UC_20'
    testdataobj20 = SeizureData(dirpath1,amount_to_downsample = 40)
    testdataobj20.load_data()
    datasettest20 = testdataobj20.data_array

    dirpath2 = '/Users/Jonathan/PhD/Seizure_related/batchSept_UC_40'
    testdataobj40 = SeizureData(dirpath2,amount_to_downsample = 40)
    testdataobj40.load_data()
    datasettest40 = testdataobj40.data_array
    print datasettest40.shape,'is correct data shape'

    datasettest = np.vstack([datasettest20,datasettest40])
    return datasettest

def raw_training_load():
    ################# 'NEW data' ###################
    dirpath = '/Users/Jonathan/PhD/Seizure_related/20150616'
    _20150616dataobj = SeizureData(dirpath, amount_to_downsample = 40)
    _20150616dataobj.load_data()
    _20150616data = _20150616dataobj.data_array
    _20150616labels = _20150616dataobj.label_colarray
    _20150616data_norm = normalise(_20150616data)

    print _20150616dataobj.filename_list.shape
    _20150616dataobj.filenames_list = [_20150616dataobj.filename_list[i] for i in range(_20150616dataobj.filename_list.shape[0])]
    for name in _20150616dataobj.filenames_list[0:20]:
        print name[-34:]

    # select out the stuff we want
    #inds = np.loadtxt('0901_400newdata.csv', delimiter=',')
    notebook_dir = '/Users/jonathan/PhD/Seizure_related/2015_08_PyRanalysis/'
    inds = np.loadtxt(notebook_dir +'0616correctedintervals.csv', delimiter=',')
    data0616_unnorm = _20150616data[list(inds[:,0])]
    data0616 = _20150616data_norm[list(inds[:,0])]
    labels0616 = _20150616labels[list(inds[:,0])]
    for i in range(data0616.shape[0]):
        labels0616[i] = inds[i,1]

    ################## Original Data ####################
    dirpath = '/Users/Jonathan/PhD/Seizure_related/Classified'
    dataobj = SeizureData(dirpath,amount_to_downsample = 20)
    dataobj.load_data()
    dataobj = relabel(dataobj)
    dataobj = reorder(dataobj)
    dataset301 = dataobj.data_array
    labels301 = dataobj.label_colarray
    new_labels = np.loadtxt(notebook_dir+'new_event_labels_28082015.csv',delimiter= ',')
    for x in new_labels:
        labels301[x[0]] = x[1]

    selection = np.loadtxt(notebook_dir+'perfect_event_labels_28082015.csv',delimiter= ',')
    indexes =  list(selection[:,0])
    dataset129_unnorm = dataset301[indexes,:]
    dataset129_norm = normalise(dataset129_unnorm)
    dataset301_norm = normalise(dataset301)
    labels129 = labels301[indexes]
    return np.vstack((data0616_unnorm,dataset301))

def plot_scalebars(ax, div=3.0, labels=True,
                    xunits="", yunits="", nox=False,
                    sb_xoff=0, sb_yoff=0, rotate_yslabel=False,
                    linestyle="-k", linewidth=4.0,
                    textcolor='k', textweight='normal', labelfontsize = 13):
    '''
    Stolen from C. Schmit Hieber (sp)
    Args:
        ax:
        div:
        labels:
        xunits:
        yunits:
        nox:
        sb_xoff:
        sb_yoff:
        rotate_yslabel:
        linestyle:
        linewidth:
        textcolor:
        textweight:
        labelfontsize:

    Returns:

    '''

    scale_dist_x = 0.02
    scale_dist_y = 0.02
    graph_width = 6.0
    graph_height = 4.0
    key_dist = 0.01
    # print dir(ax.dataLim)
    xmin = ax.dataLim.xmin
    xmax = ax.dataLim.xmax
    ymin = ax.dataLim.ymin
    ymax = ax.dataLim.ymax
    xscale = xmax-xmin
    yscale = ymax-ymin

    xoff = (scale_dist_x + sb_xoff) * xscale
    yoff = (scale_dist_y - sb_yoff) * yscale

    # plot scale bars:
    xlength = prettyNumber((xmax-xmin)/div)
    xend_x, xend_y = xmax, ymin
    if not nox:
        xstart_x, xstart_y = xmax-xlength, ymin
        scalebarsx = [xstart_x+xoff, xend_x+xoff]
        scalebarsy = [xstart_y-yoff, xend_y-yoff]
    else:
        scalebarsx=[xend_x+xoff,]
        scalebarsy=[xend_y-yoff]

    ylength = prettyNumber((ymax-ymin)/div)
    yend_x, yend_y = xmax, ymin+ylength
    scalebarsx.append(yend_x+xoff)
    scalebarsy.append(yend_y-yoff)

    ax.plot(scalebarsx, scalebarsy, linestyle, linewidth=linewidth, solid_joinstyle='miter')

    if labels:
        # if textcolor is not None:
        #     color = "\color{%s}" % textcolor
        # else:
        #     color = ""
        if not nox:
            # xlabel
            if xlength >=1:
                xlabel = r"%d$\,$%s" % (xlength, xunits)
            else:
                xlabel = r"%g$\,$%s" % (xlength, xunits)
            xlabel_x, xlabel_y = xmax-xlength/2.0, ymin
            xlabel_y -= key_dist*yscale
            ax.text(xlabel_x+xoff, xlabel_y-yoff, xlabel, ha='center', va='top',
                    weight=textweight, color=textcolor, fontsize = labelfontsize) #, [pyx.text.halign.center,pyx.text.valign.top])
        # ylabel
        if ylength >=1:
            ylabel = r"%d$\,$%s" % (ylength,yunits)
        else:
            ylabel = r"%g$\,$%s" % (ylength,yunits)
        if not rotate_yslabel:
            ylabel_x, ylabel_y = xmax, ymin + ylength/2.0
            ylabel_x += key_dist*xscale
            ax.text(ylabel_x+xoff, ylabel_y-yoff, ylabel, ha='left', va='center',
                    weight=textweight, color=textcolor,fontsize = labelfontsize)
        else:
            ylabel_x, ylabel_y = xmax, ymin + ylength/2.0
            ylabel_x += key_dist*xscale
            ax.text(ylabel_x+xoff, ylabel_y-yoff, ylabel, ha='center', va='top', rotation=90,
                    weight=textweight, color=textcolor, fontsize = labelfontsize)

def prettyNumber(f):
    fScaled = f
    if fScaled < 1:
        correct = 10.0
    else:
        correct = 1.0

    # set stepsize
    nZeros = int(np.log10(fScaled))
    prev10e = 10.0**nZeros / correct
    next10e = prev10e * 10

    if fScaled / prev10e  > 7.5:
        return next10e
    elif fScaled / prev10e  > 5.0:
        return 5 * prev10e
    else:
        return round(fScaled/prev10e) * prev10e
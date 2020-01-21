import numpy as np
import matplotlib
matplotlib.use('Agg')
from chainconsumer import ChainConsumer


def plot_chainwalk(chains, params_name, params_truth=None, convolve = 50, figname=None, blind=None):
    c = ChainConsumer()

    chains_copy = [ ch.copy() for ch in chains ]

    if blind:

        print 'chain will be blinded'


        for i in range(len(params_name)):

            if params_name[i] == '$As$' : r = np.random.random() * 10e-08
            else : r = np.random.random()

            for ch in chains_copy:
                #print r, params_name[i]
                ch[:,i] += r

    for ch in chains_copy:
        c.add_chain(ch, parameters=params_name)

    if blind : params_truth = None

    fig = c.plotter.plot_walks(convolve=convolve, truth=params_truth, filename=figname)
    fig.set_size_inches(4.5 + fig.get_size_inches())

    chains_copy = None



def plot_contours(chains, params_names, params_fid, figname,
    keep=None, extents = None, chain_names=None, plot_hists=True,
    blind= None, shade_alpha = None, figsize=(7,7), summary=None,
    shade = None, colors = None, linestyles = None, linewidths=None,
    kde = None, legend_location=None, flip=False, sigmas=[0,1,2], multinest=None ):
    """
    keep : list. choose in the second chain
    params_fid : fiducial value of chain2

    """

    if chain_names is None : chain_names = ['chain'+str(i) for i in len(chains)]

    if keep is None :
        pn = params_names[0]
        pf = params_fid
    else :
        pn = [params_names[0][i] for i in keep]
        pf = [params_fid[i] for i in keep]
        #extents = [extents[i] for i in keep]

    if blind: pf = None

    c = ChainConsumer()

    if multinest is None :
        multinest = [ False for i in range(len(chains)) ]
    for i in range(len(chains)):
        if multinest[i]:
            weights = chains[i][:,-1]
            chain_i = chains[i][:,:-1]
        else :
            weights = None
            chain_i = chains[i]

        c.add_chain(chain_i, parameters = params_names[i], name=chain_names[i],weights=weights)
        #print c.analysis.get_covariance(chain=i)[1]
    statistics = ['max' for i in range(len(chains))]  #["max","max","max","max","max", "max"]
    if kde is None :kde=[ False for i in range(len(chains))] #False,False,False,False,False,False][:len(chains)]
    c.configure(statistics=statistics,#[:len(chains)],
                linestyles=linestyles,#[:len(chains)],
                label_font_size=20, tick_font_size =20,
                summary=summary, #[: len(chains)],
                sigmas=sigmas,
                shade=shade, #[: len(chains)], \
                colors=colors, #[: len(chains)], \
                shade_alpha = shade_alpha, #[: len(chains)],
                linewidths=linewidths, #[:len(chains)],
                kde = kde,
                plot_hists=plot_hists,
                flip=flip,
                legend_location=legend_location,
                legend_kwargs = {'loc':'best'})

    fig = c.plotter.plot(filename=figname, figsize=figsize, truth = pf, parameters =pn, extents=extents, blind=blind)
    print "plot save to ", figname
    return c, fig


def main():

    # Set output figurename 
    figname = 'contour.png'

    # Calling DES chains
    chainfile_name = 'example_chain.txt'
    multinest_des_col_p = (0,4,3,2,1,6,18,-1)
    cosmosis_example_chain = np.genfromtxt(chainfile_name, usecols=multinest_des_col_p)

    # your chain 
    your_chainfile_name = 'output/output_baseline/multinest/gc_ggl_shear_chain.txt' 
    cosmosis_your_chain = np.genfromtxt(your_chainfile_name, usecols=multinest_des_col_p)

    # Set parameters' names and values
    params_names = ['$\Omega_m$', '$A_s$', '$n_s$', '$\Omega_b$', '$h_0$', '$b$', '$\sigma_8$']
    params_values = [ 3.057076e-01, 2.195731e-09, 9.683760e-01, 4.845864e-02,6.785960e-01, 2, 0.8152491E+00]

    # calling function
    plot_contours([ cosmosis_example_chain, cosmosis_your_chain], \
                [params_names , params_names],\
                params_values, figname,\
                linewidths = [1.5,1.5,1.5,1.5, 1.5, 1.5, 1.5],
                shade = [0.05, 0.05, 0.05, 0, 0,0,0],
                kde = [1, 1, 1, 1, 1],          
                chain_names=['example', 'your chain'],\
                multinest=[True, True],
                keep=[0,1,2,3,4,5,6],
                #blind=True
                )

#############
main()


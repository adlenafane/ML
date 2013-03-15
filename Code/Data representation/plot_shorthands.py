# Useful functions for plotting & exporting the graph

import matplotlib.pyplot as pyplot # to plot

#==============================================================================
# Set the fontsize for a legend
def set_legend_fontsize(legend_handle, fontsize):
    '''
    INPUT
         legend_handle  - handle to the legend
         fontsize       - fontsize: numeric or 'xx-small'->'medium'->'xx-large' 
    '''
    for t in legend_handle.get_texts():
        t.set_fontsize(fontsize)
#----------------------------------------------------------------------------- 
# to make a niiiiiiice & customizable output figures
def print_to_file(handle_fig, fig_name, dpi, paper_width, paper_height,
                  left, bottom, right, top, wspace= None, hspace= None):
    '''
    handle_fig : handle of the figure to plot
    
    fig_name : name of the file to save to WITH extension (.pdf ...)
    
    paper_width, paper_height : dimension of the figure, *in cm*
    
    left, bottom, right, top : margins *in cm* (from the plot zone, NOT
                            including x/y labels !)
    
    whspace, hspace : space between subplots, in cm (width / height)
    '''
    
    # --- We might get strange results otherwise
    paper_width = float(paper_width)
    paper_height = float(paper_height)
    
    
    # --- Expressing the dimension in % of the paper size
    left = left / paper_width
    right = (paper_width - right) / paper_width
    bottom = bottom / paper_height
    top = (paper_height - top) / paper_height
    
    wspace = wspace / paper_width
    hspace = hspace / paper_height
    
    
    # --- Converting paper size in inches ! :(
    # 1 inch = 2.54 cm
    paper_width = paper_width / 2.54
    paper_height = paper_height / 2.54
    
    handle_fig.set_size_inches(paper_width, paper_height)
    
    
    
    # left / right / top / bottom : margins, in % of w/h paper
    # wspace, hspace = blank space between subplot, in % of w/h paper
    pyplot.subplots_adjust(left= left, bottom= bottom, right= right, top= top,
                        wspace= wspace, hspace= hspace)
    
    pyplot.savefig(fig_name, dpi= dpi)
# 
#==============================================================================
# END OF FILE
#
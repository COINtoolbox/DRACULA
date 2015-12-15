def create_name(Method,params,prefix,end='.dat'):
    fname = prefix +Method+ end
    return fname
def plot_name(Method_red,Method_cl,params_red,params_cl,ext='.png'):
    fname = 'plots/plot_' + Method_red + '_' + Method_cl +ext
    return fname

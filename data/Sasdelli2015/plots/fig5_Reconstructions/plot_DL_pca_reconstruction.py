from numpy import loadtxt, genfromtxt, shape, mean, sort, savetxt, size, array, copy
from pylab import figure
from matplotlib.pyplot import plot, savefig, xlabel, ylabel, scatter, axis, xlim, fill_between, legend, text, show
from sklearn.decomposition.pca import PCA
import pylab as plt
import numpy as np

# define data directory
data_dir= '../../data/'

# read data
der = loadtxt(data_dir+'derivatives_all_epochs.dat')
flux = 0.8*loadtxt(data_dir+'fluxes_not_res.dat.gz')
labels = loadtxt(data_dir+'mask.dat')
spectra_data = genfromtxt(data_dir+'spectra_data_id.dat',dtype=None)

# make pca reduction
pca = PCA(n_components=4)
pca.fit(der)
X = pca.transform(der)
pred_PCA = (pca.inverse_transform(X))
pca = PCA(n_components=15)
pca.fit(der)
X = pca.transform(der)
pred_PCA_15PC = (pca.inverse_transform(X))

# load deep learning results
pred_DL = loadtxt('../../data/DL_4features_predictions.dat' )

# define wavelength range
wavelenght_array = array(range(3200,9000,2))
wavelenght_array = wavelenght_array[range(370,1850,1)]
wavelenght_array_flux = copy(wavelenght_array)
wavelenght_array = wavelenght_array[::5]

wavelenght_array_int = wavelenght_array[:]-5.

# plot
n_plot1 = 0

range_to_plot =[
 2240,
2920,
47,
175,
 3174,
17,
 108,
 1401,
 26,
 1794,
 ]


n_plot = size(range_to_plot)

axs = [[] for i in xrange(2)]
names = ['measured', 'reconst. 4PCs', 'reconst. 15PCs', 'reconst. DL \n 4 features']

fig = plt.figure(figsize=(20,14))
plt.subplot(1,2,1)
plt.plot(wavelenght_array_flux, flux[range_to_plot[0]], color='black', lw=1.0)
plt.plot(wavelenght_array_flux, flux[range_to_plot[1]] + 1.5, color='black', lw=1.0)
plt.plot(wavelenght_array_flux, flux[range_to_plot[2]] + 3.0, color='black', lw=1.0)
plt.plot(wavelenght_array_flux, flux[range_to_plot[3]] + 4.5, color='black', lw=1.0)
plt.plot(wavelenght_array_flux, flux[range_to_plot[4]] + 6.0, color='black', lw=1.0)
plt.plot(wavelenght_array_flux, flux[range_to_plot[5]] + 7.5, color='black', lw=1.0)

plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[range_to_plot[0]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[0]][0], color='red', ls=':', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[range_to_plot[1]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[1]][0] + 1.5, color='red', ls=':', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[range_to_plot[2]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[2]][0] + 3.0, color='red', ls=':', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[range_to_plot[3]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[3]][0] + 4.5, color='red', ls=':', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[range_to_plot[4]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[4]][0] + 6.0, color='red', ls=':', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[range_to_plot[5]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[5]][0] + 7.5, color='red', ls=':', lw=2.0)

plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[range_to_plot[0]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[0]][0], color='green', ls='-.', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[range_to_plot[1]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[1]][0] + 1.5, color='green', ls='-.', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[range_to_plot[2]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[2]][0] + 3.0, color='green', ls='-.', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[range_to_plot[3]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[3]][0] + 4.5, color='green', ls='-.', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[range_to_plot[4]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[4]][0] + 6.0, color='green', ls='-.', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[range_to_plot[5]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[5]][0] + 7.5, color='green', ls='-.', lw=2.0)

plt.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[range_to_plot[0]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[0]][0], color='blue', lw=1.5)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[range_to_plot[1]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[1]][0] + 1.5, color='blue', lw=1.5)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[range_to_plot[2]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[2]][0] + 3.0, color='blue', lw=1.5)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[range_to_plot[3]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[3]][0] + 4.5, color='blue', lw=1.5)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[range_to_plot[4]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[4]][0] + 6.0, color='blue', lw=1.5)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[range_to_plot[5]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[5]][0] + 7.5, color='blue', lw=1.5)

plt.text(3600, 1.15, 'SN%s \n %.1fd' % (spectra_data['f0'][range_to_plot[0]][2:],spectra_data['f3'][range_to_plot[0]]))
plt.text(3600, 1.15 + 1.5, 'SN%s \n %.1fd' % (spectra_data['f0'][range_to_plot[1]][2:],spectra_data['f3'][range_to_plot[1]]))
plt.text(3600, 1.15 + 2.75, 'SN%s \n %.1fd' % (spectra_data['f0'][range_to_plot[2]][2:],spectra_data['f3'][range_to_plot[2]]))
plt.text(3600, 1.15 + 4.0, 'SN%s \n %.1fd' % (spectra_data['f0'][range_to_plot[3]][2:],spectra_data['f3'][range_to_plot[3]]))
plt.text(3600, 1.15 + 5.5, 'SN%s \n %.1fd' % (spectra_data['f0'][range_to_plot[4]][2:],spectra_data['f3'][range_to_plot[4]]))
plt.text(3600, 1.15 + 7.0, 'SN%s \n %.1fd' % (spectra_data['f0'][range_to_plot[5]][2:],spectra_data['f3'][range_to_plot[5]]))

plt.xlabel('wavelength ($\AA$)', fontsize=18)
plt.ylabel('$\log_{10}$ flux (arbitrary units)', fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

axs = plt.subplot(1,2,2)
line,  = axs.plot(wavelenght_array_flux, flux[range_to_plot[6]] + 0.5, color='black', label=names[0], lw=1.0)
plt.plot(wavelenght_array_flux, flux[range_to_plot[7]] + 1.5, color='black', lw=1.0)
plt.plot(wavelenght_array_flux, flux[range_to_plot[8]] + 2.5, color='black', lw=1.0)
plt.plot(wavelenght_array_flux, flux[range_to_plot[9]] + 3.25, color='black', lw=1.0)

line,  = axs.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[range_to_plot[6]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[6]][0] + 0.5, color='red', ls=':', lw=2.0, label=names[1])
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[range_to_plot[7]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[7]][0] + 1.5, color='red', ls=':', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[range_to_plot[8]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[8]][0] + 2.5, color='red', ls=':', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA[range_to_plot[9]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[9]][0] + 3.25, color='red', ls=':', lw=2.0)

line,  = axs.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[range_to_plot[6]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[6]][0] + 0.5, color='green', ls='-.', lw=2.0, label=names[2])
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[range_to_plot[7]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[7]][0] + 1.5, color='green', ls='-.', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[range_to_plot[8]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[8]][0] + 2.5, color='green', ls='-.', lw=2.0)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_PCA_15PC[range_to_plot[9]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[9]][0] + 3.25, color='green', ls='-.', lw=2.0)

line,  = axs.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[range_to_plot[6]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[6]][0] + 0.5, color='blue', lw=1.5, label=names[3])
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[range_to_plot[7]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[7]][0] + 1.5, color='blue', lw=1.5)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[range_to_plot[8]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[8]][0] + 2.5, color='blue', lw=1.5)
plt.plot(wavelenght_array_int, -4*np.array([sum(pred_DL[range_to_plot[9]][:i]) for i in range(size(der[0]))]) + flux[range_to_plot[9]][0] + 3.25, color='blue', lw=1.5)

plt.text(3600, 1.15, 'SN%s \n %.1fd' % (spectra_data['f0'][range_to_plot[6]][2:],spectra_data['f3'][range_to_plot[6]]))
plt.text(3600, 1.15 + 1.0, 'SN%s \n %.1fd' % (spectra_data['f0'][range_to_plot[7]][2:],spectra_data['f3'][range_to_plot[7]]))
plt.text(3600, 1.15 + 2.0, 'SN%s \n %.1fd' % (spectra_data['f0'][range_to_plot[8]][2:],spectra_data['f3'][range_to_plot[8]]))
plt.text(3600, 1.15 + 3.0, 'SN%s \n %.1fd' % (spectra_data['f0'][range_to_plot[9]][2:],spectra_data['f3'][range_to_plot[9]]))

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('wavelength ($\AA$)', fontsize=18)
plt.ylabel('$\log_{10}$ flux (arbitrary units)', fontsize=18)
plt.ylim(0,4.6)

plt.tight_layout()
axs.legend(bbox_to_anchor=(1.010, 1.007), ncol=1, fontsize=14)
plt.savefig('reconstructions.pdf', format='pdf', dpi=1000)

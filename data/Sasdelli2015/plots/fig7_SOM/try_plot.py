import numpy as np
import pylab as plt
import pandas as pd
import os
from scipy import stats

path = "../../data/"

p = {'data_file': 'DL_4features_all_epochs.dat',
 'folder_out': '.',
 'path_data': '../../data/',
 'path_out': '.'}


nx = 10
ny = 10

labels_class ={'(0,0)': '91bg',
 '(0,1)': '91bg',
 '(0,2)': 'pec',
 '(0,3)': 'N',
 '(0,5)': 'N',
 '(0,6)': 'pec',
 '(0,7)': 'N',
 '(0,8)': 'N',
 '(0,9)': 'pec',
 '(1,0)': '91bg',
 '(1,3)': 'N',
 '(1,6)': 'N',
 '(1,7)': 'N',
 '(1,9)': 'N',
 '(2,0)': '91bg',
 '(2,1)': 'N',
 '(2,3)': 'N',
 '(2,4)': 'N',
 '(2,5)': 'N',
 '(2,6)': 'N',
 '(2,7)': 'N',
 '(2,9)': 'N',
 '(3,0)': '91bg',
 '(3,2)': 'N',
 '(3,4)': 'N',
 '(3,5)': 'N',
 '(3,6)': 'N',
 '(3,7)': 'N',
 '(3,9)': '91T',
 '(4,0)': '91bg',
 '(4,2)': 'N',
 '(4,3)': 'N',
 '(4,4)': 'N',
 '(4,5)': 'N',
 '(4,6)': 'N',
 '(4,7)': 'N',
 '(4,9)': '91T',
 '(5,0)': 'N',
 '(5,3)': 'N',
 '(5,4)': 'N',
 '(5,5)': 'N',
 '(5,6)': 'N',
 '(5,7)': 'N',
 '(5,8)': 'N',
 '(5,9)': 'N',
 '(6,0)': 'N',
 '(6,1)': 'N',
 '(6,3)': 'N',
 '(6,4)': 'N',
 '(6,5)': 'N',
 '(6,6)': 'N',
 '(6,7)': 'N',
 '(6,8)': 'N',
 '(6,9)': 'N',
 '(7,0)': '91T',
 '(7,1)': 'N',
 '(7,3)': 'N',
 '(7,4)': 'N',
 '(7,5)': 'N',
 '(7,7)': 'N',
 '(7,9)': 'N',
 '(8,0)': 'N',
 '(8,1)': 'N',
 '(8,2)': 'N',
 '(8,4)': 'N',
 '(8,5)': 'N',
 '(8,6)': 'N',
 '(8,9)': '91T',
 '(9,0)': 'HV',
 '(9,1)': 'HV',
 '(9,2)': 'N',
 '(9,3)': 'HV',
 '(9,4)': 'N',
 '(9,5)': 'N',
 '(9,6)': 'N',
 '(9,7)': 'N',
 '(9,8)': 'N',
 '(9,9)': 'N'}




w = tuple(map(tuple, np.loadtxt('../../data/w.dat')))

indx_unique = tuple(map(tuple, np.loadtxt('../../data/indx_unique.dat')))
indx_counts = tuple(map(tuple, np.loadtxt('../../data/indx_counts.dat')))

fluxes = np.loadtxt(os.path.join("../../data/fluxes_all_epochs.dat"))        
spectra_data = pd.read_csv(os.path.join("../../data/spectra_data_id.dat"),sep=" ")
labels = np.loadtxt(os.path.join("../../data/mask.dat"))
data_all = np.loadtxt(os.path.join(p["path_data"],p["data_file"]))

        
data = data_all[labels==1]
            
ndim = data.shape[0]
        
fluxes = fluxes[labels==1]
            
spectra_data = spectra_data[spectra_data["at_max_flag"] == 1]
         
spectra_data.columns = ["SN","zhelio","MJD","epoch","at_max_flag"]
            
spectra_data.index=range(ndim)

colors = []

for i in range(len(indx_unique)):
    colors.append((np.random.uniform(0,1),np.random.uniform(0,1),np.random.uniform(0,1)))
    colors.sort()

fig,ax = plt.subplots(nx,ny)
fig.subplots_adjust(left=0, bottom=0, right=1, top=1,wspace=0.0,hspace=0.0)

FILE = open(os.path.join("stats.dat"),"w")
FILE_group_members = open(os.path.join("group_member_stats.dat"),"w")
FILE.write("Pair\t Nspec\t mean epoch\t epoch std\n")


for i in xrange(nx):
    for j in xrange(ny):
        indices = [ k for k in xrange(len(w)) if w[k] == (i,j)]
        if len(indices) == 0:
            ax[i,j].set_xticks([])
            ax[i,j].set_yticks([])
            pass
        elif len(indices) == 1:
            #print indices
            f = fluxes[indices,:][0]
            n2 = f.shape[0]
            
            NORM = f[200:301].sum()
            f/=NORM
            epoch = spectra_data["epoch"].values[indices]
            
            epoch_mean = stats.nanmedian(epoch)
            epoch_std = stats.nanstd(epoch)
          
            
            ax[i,j].plot(f,'k-' )
            if labels_class['(' +  str(i) +',' + str(j) + ')'] in ['91bg', 'pec']:
                xt = -4
            elif labels_class['(' +  str(i) +',' + str(j) + ')'] in ['91T', 'N']:
                xt = -3
            elif labels_class['(' +  str(i) +',' + str(j) + ')'] in ['HV']:
                xt = -2

            if '(' +  str(i) +',' + str(j) + ')' == '(8,5)':
                ax[i,j].text(ax[i,j].get_xticks()[-6], 0.35*ax[i,j].get_ylim()[1], '1-' + labels_class['(' +  str(i) +',' + str(j) + ')'], 
                         fontsize=7)
            else:
                ax[i,j].text(ax[i,j].get_xticks()[xt], 0.8*ax[i,j].get_ylim()[1], '1-' + labels_class['(' +  str(i) +',' + str(j) + ')'], 
                         fontsize=7)
            ax[i,j].set_xticks([])
            ax[i,j].set_yticks([])

            FILE.write("(%d,%d)\t %d\t\t\t %.2f\t\t\t %.2f\n"%(i,j,len(indices),epoch_mean,epoch_std) )
                    
            #if len(indices) !=0:
                    
            FILE_group_members.write("Pair =(%d,%d)\t Nspec=%d\t\t\t mean epoch=%.2f\t\t\t epoch std=%.2f\n"%(i,j,len(indices),epoch_mean,epoch_std) )
                       
            FILE_group_members.write("SNIa\t zhelio\t MJD\t epoch\n")
                        
            #print "SNIa\t zhelio\t MJD\t epoch\n"
                        
            for SNIa in spectra_data.values[indices]:
                            
                FILE_group_members.write("%s\t %.5f\t %.2f\t %.3f\n"%(SNIa[0],SNIa[1],SNIa[2],SNIa[3]))
                            
                #print "%s\t %.5f\t %.2f\t %.3f"%(SNIa[0],SNIa[1],SNIa[2],SNIa[3])
                        
            FILE_group_members.write("-----------------------------------------------------------------\n")
            
        
        else:
            
            f = fluxes[indices]
            epoch = spectra_data["epoch"].values[indices]
            
            n1,n2 = f.shape
    
            epoch_mean = stats.nanmedian(epoch)
            #epoch_mean = stats.nanmean(epoch)
            epoch_std = stats.nanstd(epoch)
            
            for k in xrange(n1):
                NORM = f[k,200:301].sum()
                for kk in xrange(n2):
                    f[k,kk]/=NORM
            
            ff=np.median(f,axis=0)
    
            CL68 = np.array( [ [ stats.scoreatpercentile(f[:,k],16), stats.scoreatpercentile(f[:,k],16+68)] for k in xrange(n2)] )
            CL95 = np.array( [ [ stats.scoreatpercentile(f[:,k],2.5), stats.scoreatpercentile(f[:,k],97.5)] for k in xrange(n2) ] )
    
    
            ax[i,j].plot(range(n2),ff,'k-' )
        
            ax[i,j].fill_between( range(n2) ,CL68[:,0], CL68[:,1],interpolate=True,facecolor = "red",alpha = 0.4)
            ax[i,j].fill_between( range(n2) , CL95[:,0], CL95[:,1],interpolate= True,facecolor = "blue",alpha = 0.3)
                

            if '(' +  str(i) +',' + str(j) + ')' == '(0,0)':
                ax[i,j].text(0.45*ax[i,j].get_xlim()[1], 0.8*ax[i,j].get_ylim()[1], str(len(indices)) + '-' + labels_class['(' +  str(i) +',' + str(j) + ')'], fontsize=7)
            elif '(' +  str(i) +',' + str(j) + ')' == '(0,1)':
                ax[i,j].text(0.5*ax[i,j].get_xlim()[1], 0.8*ax[i,j].get_ylim()[1], str(len(indices)) + '-' + labels_class['(' +  str(i) +',' + str(j) + ')'], fontsize=7)
            elif '(' +  str(i) +',' + str(j) + ')' in ['(4,9)', '(9,2)']:
                ax[i,j].text(0.6*ax[i,j].get_xlim()[1], 0.8*ax[i,j].get_ylim()[1], str(len(indices)) + '-' + labels_class['(' +  str(i) +',' + str(j) + ')'], fontsize=7)
            elif '(' +  str(i) +',' + str(j) + ')' in ['(4,6)', '(4,7)', '(9,4)', '(9,6)', '(9,7)', '(5,0)','(7,9)', '(6,9)', '(5,9)']:
                ax[i,j].text(0.6*ax[i,j].get_xlim()[1], 0.8*ax[i,j].get_ylim()[1], str(len(indices)) + '-' + labels_class['(' +  str(i) +',' + str(j) + ')'], fontsize=7)
            elif '(' +  str(i) +',' + str(j) + ')' in ['(1,0)', '(9,0)','(9,1)', '(9,3)',  '(8,9)', '(0,9)']:
                ax[i,j].text(0.5*ax[i,j].get_xlim()[1], 0.8*ax[i,j].get_ylim()[1], str(len(indices)) + '-' + labels_class['(' +  str(i) +',' + str(j) + ')'], fontsize=7)
            elif '(' +  str(i) +',' + str(j) + ')' == '(2,0)':
                ax[i,j].text(0.5*ax[i,j].get_xlim()[1], 0.8*ax[i,j].get_ylim()[1], str(len(indices)) + '-' + labels_class['(' +  str(i) +',' + str(j) + ')'], fontsize=7)
            elif '(' +  str(i) +',' + str(j) + ')' == '(3,9)':
                ax[i,j].text(0.6*ax[i,j].get_xlim()[1], 0.8*ax[i,j].get_ylim()[1], str(len(indices)) + '-' + labels_class['(' +  str(i) +',' + str(j) + ')'], fontsize=7)
            elif '(' +  str(i) +',' + str(j) + ')' == '(9,9)':
                ax[i,j].text(0.6*ax[i,j].get_xlim()[1], 0.8*ax[i,j].get_ylim()[1], str(len(indices)) + '-' + labels_class['(' +  str(i) +',' + str(j) + ')'], fontsize=7)
            elif '(' +  str(i) +',' + str(j) + ')' == '(0,6)':
                ax[i,j].text(0.5*ax[i,j].get_xlim()[1], 0.8*ax[i,j].get_ylim()[1], '2-N/pec', fontsize=7)
            elif '(' +  str(i) +',' + str(j) + ')' == '(1,7)':
                ax[i,j].text(0.7*ax[i,j].get_xlim()[1], 0.8*ax[i,j].get_ylim()[1], '1-N', fontsize=7)
            elif '(' +  str(i) +',' + str(j) + ')' == '(4,0)':
                ax[i,j].text(0.4*ax[i,j].get_xlim()[1], 0.8*ax[i,j].get_ylim()[1], '2-N/91bg', fontsize=7)
            elif '(' +  str(i) +',' + str(j) + ')' == '(8,0)':
                ax[i,j].text(0.5*ax[i,j].get_xlim()[1], 0.8*ax[i,j].get_ylim()[1], str(len(indices)) + '-N/HV', fontsize=7)
            elif '(' +  str(i) +',' + str(j) + ')' == '(7,0)':
                ax[i,j].text(0.5*ax[i,j].get_xlim()[1], 0.8*ax[i,j].get_ylim()[1], str(len(indices)) + '-N/91T', fontsize=7)
            elif labels_class['(' +  str(i) +',' + str(j) + ')'] != 0:
                ax[i,j].text(0.7*ax[i,j].get_xlim()[1], 0.8*ax[i,j].get_ylim()[1], str(len(indices)) + '-' + labels_class['(' +  str(i) +',' + str(j) + ')'], fontsize=7)
            ax[i,j].set_xticks([])
            ax[i,j].set_yticks([])
        
            

            #print "Pair = (%d,%d)\t Nspec=%d\t mean epoch=%.2f\t epoch std=%.2f"%(i,j,len(indices),epoch_mean,epoch_std)
            FILE.write("(%d,%d)\t %d\t\t\t %.2f\t\t\t %.2f\n"%(i,j,len(indices),epoch_mean,epoch_std) )
                    
            #if len(indices) !=0:
                    
            FILE_group_members.write("Pair =(%d,%d)\t Nspec=%d\t\t\t mean epoch=%.2f\t\t\t epoch std=%.2f\n"%(i,j,len(indices),epoch_mean,epoch_std) )
                       
            FILE_group_members.write("SNIa\t zhelio\t MJD\t epoch\n")
                        
            #print "SNIa\t zhelio\t MJD\t epoch\n"
                        
            for SNIa in spectra_data.values[indices]:
                            
                FILE_group_members.write("%s\t %.5f\t %.2f\t %.3f\n"%(SNIa[0],SNIa[1],SNIa[2],SNIa[3]))
                            
                #print "%s\t %.5f\t %.2f\t %.3f"%(SNIa[0],SNIa[1],SNIa[2],SNIa[3])
                        
            FILE_group_members.write("-----------------------------------------------------------------\n")
            #print "-----------------------------------------------------------------"
                        
                            
                            
                        

FILE.close()
FILE_group_members.close()

fig.savefig(os.path.join("SOM_grid_10x10.pdf"),format = "pdf",dpi = 4000)
    


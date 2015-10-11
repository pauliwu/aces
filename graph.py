# encoding : utf8
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as pl	
def twinx(x,y1,y2,filename):
	fig,ax1=pl.subplots()
	a=ax1.plot(x[0],y1[0])
	ax1.set_xlabel(x[1])
	ax1.set_ylabel(y1[1])
	ax2=ax1.twinx()
	ax2.set_ylabel(y2[1])
	b=ax2.plot(x[0],y2[0],'r')
	ax1.set_frame_on(False)
	ax1.legend(a+b,[y1[1],y2[1]],loc='best').get_frame().set_alpha(0.0)
	pl.savefig(filename,bbox_inches='tight',transparent=True)
	pl.close()
def plot(x,y,filename,grid=False,linewidth=1,scatter=False,xmax=None,logx=False,logy=False):
	series(x[1],y[1],[(x[0],y[0],y[1])],filename,legend=False,grid=grid,linewidth=linewidth,scatter=scatter,xmax=xmax,logx=logx,logy=logy)
	
def series(xlabel,ylabel,datas,filename,linewidth=1,legend=True,grid=False,xmax=None,scatter=False,logx=False,logy=False):
	pl.figure()
	pl.xlabel(xlabel)
	pl.ylabel(ylabel)
	plot=pl.plot
	if logx:
		plot=pl.semilogx
	if logy:
		plot=pl.semilogy
	if logx and logy:
		plot=pl.loglog
	if scatter:
		marker='.'
		linestyle='.'
	else: 
		marker=None
		linestyle='-'
	if len(datas)==1:
		serie=datas[0]
		plot(serie[0],serie[1],label=serie[2],linewidth=linewidth,color='r',marker=marker,linestyle=linestyle)
		if xmax is None:xmax=serie[0].max()
		pl.xlim([serie[0].min(),xmax])
	else:
		min0=100000;max0=-100000
		for serie in datas:
			plot(serie[0],serie[1],label=serie[2],linewidth=linewidth,marker=marker,linestyle=linestyle)
			min0=min(serie[0].min(),min0)
			max0=max(serie[0].max(),max0)
		if xmax is None:xmax=max0
		pl.xlim([min0,xmax])
	if legend:
		pl.legend(loc='best').get_frame().set_alpha(0.0)
	if grid:
		pl.grid(True)
	
	pl.savefig(filename,bbox_inches='tight',transparent=True) 
	pl.close()

def surf(X, Y, Z,filename):
	from mpl_toolkits.mplot3d import Axes3D
	fig = pl.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.plot_surface(X, Y, Z)
	pl.savefig(filename,bbox_inches='tight',transparent=True) 
	pl.close()
def imshow(c,filename,extent=[0,1,0,1]):
	pl.figure()
	pl.imshow(np.array(c).astype('float'),extent=extent,origin='lower')
	pl.savefig(filename,bbox_inches='tight',transparent=True) 
	pl.close()
def scatter(x,y,c,xlabel,ylabel,filename,marker_size=2.0,marker='s'):
	pl.figure()
	pl.xlabel(xlabel)
	pl.ylabel(ylabel)
	pl.scatter(x,y,edgecolors='none',s=marker_size,c=c,marker=marker)
	pl.savefig(filename,bbox_inches='tight',transparent=True) 
	pl.close()
def scatter3d(x,y,z,filename):
	from mpl_toolkits.mplot3d import Axes3D,proj3d
	fig = pl.figure()
	ax = fig.add_subplot(111, projection='3d')
	#ax.view_init(0, 0)
	import numpy
	def orthogonal_proj(zfront, zback):
	    a = (zfront+zback)/(zfront-zback)
	    b = -2*(zfront*zback)/(zfront-zback)
	    return numpy.array([[1,0,0,0],
	                        [0,1,0,0],
	                        [0,0,a,b],
	                        [0,0,0,zback]])
	proj3d.persp_transformation = orthogonal_proj
	ax.scatter(x,y,z)
	pl.savefig(filename,bbox_inches='tight',transparent=True) 
	pl.close()
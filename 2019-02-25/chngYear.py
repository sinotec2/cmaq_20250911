import netCDF4
addOn={i:5000 for i in 'AB'}
addOn.update({i:5001 for i in 'CD'})
for c in 'ABCD':
    nc = netCDF4.Dataset('ptse'+c+'.nc', 'r+')
    nc.SDATE+=addOn[c]
    nc['TFLAG'][:,:,0]+=addOn[c]
    nc.close()



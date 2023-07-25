# Gaussian Bump in Channel

## Data organization
Groups should submit convergence data (DOFs, enthalpy error, x location of shock attachment, other pertinent information) in separate files following the file location and name convention:
```
<GroupOrCodeName>/Conv-p<OrderIndex>.csv
```
In this convention, `p0` corresponds to first-order accurate discretizations, `p1` corresponds to second-order accurate discretizations, etc.

An example data file location and name would be
```
ND/Conv-p2.csv
```

Other files/images submitted for specific simulations should follow a similar format with `Conv` replaced by an appropriate description (e.g., `InletMachProfile`) and the grid index should be indicated:
```
<GroupOrCodeName>/<Description>-h<GridIndex>-p<OrderIndex>.<ext>
```
In this convention, h1 should correspond to the coarsest spatial discretization submitted in the corresponding convergence file (`<GroupOrCodeName>/Conv-p<OrderIndex>.csv`), h2 to the next finest, etc.

For example, inlet Mach number profile submitted for the third level of refinement with `p = 2` elements would be
```
ND/InletMachProfile-h3-p2.png
```

## Data format
For each contribution, we are requesting convergence information. Each contributed data-file should be submitted in comma-separated-value format that consists of an arbitrary number of comments, followed by a single-line header, and all convergence information on subsequent lines. Data should be provided with at least 8-digits of precision. If a requested output is not able to be provided the entry should be filled with value NaN.

The data-header should be the following:
```
Ndofs, Herror, Xattach, <Additional1>, <Additional2>, ...
```

An example of data file contents for a submission that does not provide 'Xattach' would be:
```
Ndofs,Herror,Xattach,Solution dofs,Mesh dofs
3792,0.00145,NaN,2844,948
15166,0.000356,NaN,11376,3790
60662,9.43e-05,NaN,45504,15158
```

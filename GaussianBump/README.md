# Gaussian Bump in Channel

## Data organization
Groups should submit convergence data (DOFs, enthalpy error, x location of shock attachment, other pertinent information) in separate files following the file location and name convention:
```
<GroupName>/<Code>-p<OrderIndex>.csv
```
In this convention, `p0` corresponds to first-order accurate discretizations, `p1` corresponds to second-order accurate discretizations, etc.

An example data file location and name would be
```
ND/HOIST-p2.txt
```

## Data format
For each contribution, we are requesting convergence information. Each contributed data-file should be submitted in comma-separated-value format that consists of an arbitrary number of comments, followed by a single-line header, and all convergence information on subsequent lines. Data should be provided with at least 8-digits of precision. If a requested output is not able to be provided the entry should be filled with value NaN.

The data-header should be the following:
```
Ndofs, Herror, Shock attachment (x), <Additional 1>, ...
```

An example of data file contents for a submission that does not provide 'Shock attachment (x)' would be:
```
Ndofs,Herror,Shock attachment (x),Solution dofs,Mesh dofs
3792,0.00145,0.10279225135,2844,948
15166,0.000356,0.10301295362,11376,3790
60662,9.43e-05,0.10285594945,45504,15158
```

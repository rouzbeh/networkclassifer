# networkclassifer
Program for classifying network state in a given window before light pulses.

Currently taking 10 seconds before a light pulse and extracting 22 features from this window.

## Todo:

1. Refactor network_loader - bug fix on the window and downsampling
2. Features are currently linearly dependent. 
3. Implement feature selection
4. Sort out the code from early days vs ipython notebook copies etc
5. 

## Exclusions:
1 . EX110215T12



## Possible features
* Stationarity testing
Potential features:
vector strength of cross freq coulping 
Wavelet coefficients
stationarity of prev to light - diff to when dive into blocks?
coastline
PCs of AR coefs, over time many small stationary bins
PCs in general - will not work?!
The low freq components? - including the weird change ups m hines did, per sec?
Or sum of wavelets
Eigenvalues

Asses by having counter for x and just plotting? per one. For AR "fingerprint" can use subplots.

# genproductions
Generator fragments for MC production

The package includes the datacards used for various generators inclusing POWHEG, MG5_aMC@NLO, Sherpa, Phantom, Pythia...

Further details are reported in the twiki: https://twiki.cern.ch/twiki/bin/view/CMS/GeneratorMain#How_to_produce_gridpacks

Instructions on how to use the fragments are here https://twiki.cern.ch/twiki/bin/view/CMS/GitRepositoryForGenProduction

## Setup on UMN cluster

Run the following commands from within /data/cmszfs1/user/<username>/ directory to setup scripts

1. python -m pip install htcondor --user
2. git clone https://github.com/Michael-Krohn/genproductions.git
  
Then generate the gridpacks. And then produce the LHE file.

### Generating gridpacks
  
Run the following:
  
1. cd genproductions/bin/MadGraph5_aMCatNLO/
2. ./submit_condor_gridpack_generation.sh DYJets_m200 DYJets_m200_InputCards/   #make modifications to the files within DYJets_m200_InputCards before running if you do not want to produce sample with nominal settings
  
### LHE creation

Run the following:
  
1. cd DYJets_m200/DYJets_m200_gridpack/work/gridpack/
2. ./runcmsgrid.sh <nEvents> <randomSeed> <nCPUs>   #100k events takes about 24hrs to be produced.
  
This will produce the file cmsgrid_final.lhe. Move this to your directory within /hdfs/cms/user/

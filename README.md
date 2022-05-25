# genproductions
Generator fragments for MC production

The package includes the datacards used for various generators inclusing POWHEG, MG5_aMC@NLO, Sherpa, Phantom, Pythia...

Further details are reported in the twiki: https://twiki.cern.ch/twiki/bin/view/CMS/GeneratorMain#How_to_produce_gridpacks

Instructions on how to use the fragments are here https://twiki.cern.ch/twiki/bin/view/CMS/GitRepositoryForGenProduction

## Setup on UMN cluster

Run the following commands from within /data/cmszfs1/user/<username>/ directory to setup scripts

1. python -m pip install htcondor --user
2. git clone https://github.com/Michael-Krohn/genproductions.git

### Generating gridpacks
  
Run the following:
  
1. cd genproductions/bin/MadGraph5_aMCatNLO/
2. ./submit_condor_gridpack_generation.sh DYJets_m50to150 DYJets_m50to150_InputCards/

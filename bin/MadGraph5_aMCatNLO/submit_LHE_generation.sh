executable           = /data/cmszfs1/user/jack1851/WR/DY_PRODUCTION/genproductions/bin/MadGraph5_aMCatNLO/LHE_generation.sh 
universe             = vanilla
error                = error/LHE_$(ClusterId)_$(Process).err
output               = output/LHE_$(ClusterId)_$(Process).out
log                  = log/LHE_$(ClusterId)_$(Process).log

InitialDir           = /data/cmszfs1/user/jack1851/WR/DY_PRODUCTION/genproductions/bin/MadGraph5_aMCatNLO/samples/m200/DYJets_m200_qqll/DYJets_m200_qqll_gridpack/work/gridpack

should_transfer_files = YES

transfer_input_files = DYJets_m200_qqll_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz
transfer_output_files = cmsgrid_final_$(ClusterId)$(Process).lhe

Arguments            = DYJets_m200_qqll $(Process) 200000 $(ClusterId)$(Process) 1  

notification = always
notify_user = jack1851@umn.edu

Queue 10

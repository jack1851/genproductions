#!/bin/bash

echo "Currently in scractch directory: $(pwd)"
echo 
echo "The contents of this directory is: "
echo
ls -lrt
echo
#echo "Making a new directory to move the tarball to...directory made"
#mkdir $1_$2
#echo
#ls -lrt
#echo
#mv $1_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz $1_$2\

#echo "Moving the tarball. It should be gone now."

#ls -lrt

#echo "Changing Directories. The contents of the new directory is:"

#cd $1_$2

#ls -lrt

#echo

#echo "And its path is: $(pwd)"

echo "Unzipping tarball: $1_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz"
tar -xf $1_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz
#tar -xf $1-incl_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz
echo "Tarball unzipped."

echo "Submitting LHE file"

./runcmsgrid.sh $3 $4 $5

echo "The contents of the directory is now:"

ls -lrt

mv cmsgrid_final.lhe cmsgrid_final_$4.lhe

echo "Renaming the LHE file:"

ls -lrt

echo "Removing unused files..."

rm $1_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz
#rm $1-incl_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz
rm merge.pl
rm gridpack_generation.log

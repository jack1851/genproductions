COM_ENERGY = 13000.0 # GeV
CROSS_SECTION = 1 # pb
PROCESS = 'HiggsBSM:gg2H2 = on'
SLHA_TABLE = """BLOCK SPINFO
     1   FeynHiggs
     2   2.12.0
     2   built on ott 13, 2016
BLOCK MODSEL
         1                  0   # Model
         2                  1   # GridPts
         3                  0   # Content
         4                  0   # RPV
         5                  0   # CPV
         6                  0   # FV
BLOCK SMINPUTS
         1     1.28952828E+02   # invAlfaMZ
         2     1.16637000E-05   # GF
         3     1.19000000E-01   # AlfasMZ
         4     9.11876000E+01   # MZ
         5     4.16000000E+00   # Mb
         6     1.73200000E+02   # Mt
         7     1.77703000E+00   # Mtau
        11     5.10998902E-04   # Me
        13     1.05658357E-01   # Mmu
        21     6.00000000E-03   # Md
        22     3.00000000E-03   # Mu
        23     9.50000000E-02   # Ms
        24     1.28600000E+00   # Mc
BLOCK MINPAR
         3     1.50000000E+01   # TB
BLOCK EXTPAR
         0     0.00000000E+00   # Q
         1     9.54716519E+01   # M1
         2     2.00000000E+02   # M2
         3     1.50000000E+03   # M3
        11     1.51333333E+03   # At
        12     1.51333333E+03   # Ab
        13     1.51333333E+03   # Atau
        23     2.00000000E+02   # MUE
        25     1.50000000E+01   # TB
        26     4.00000000E+02   # MA0
        27     4.07999802E+02   # MHp
        31     5.00000000E+02   # MSL(1)
        32     5.00000000E+02   # MSL(2)
        33     1.00000000E+03   # MSL(3)
        34     5.00000000E+02   # MSE(1)
        35     5.00000000E+02   # MSE(2)
        36     1.00000000E+03   # MSE(3)
        41     1.50000000E+03   # MSQ(1)
        42     1.50000000E+03   # MSQ(2)
        43     1.00000000E+03   # MSQ(3)
        44     1.50000000E+03   # MSU(1)
        45     1.50000000E+03   # MSU(2)
        46     1.00000000E+03   # MSU(3)
        47     1.50000000E+03   # MSD(1)
        48     1.50000000E+03   # MSD(2)
        49     1.00000000E+03   # MSD(3)
BLOCK MASS
   1000012     4.95862081E+02   # MSf(1,1,1)
   1000011     5.02280644E+02   # MSf(1,2,1)
   2000011     5.01831596E+02   # MSf(2,2,1)
   1000002     1.49903386E+03   # MSf(1,3,1)
   2000002     1.49959218E+03   # MSf(2,3,1)
   1000001     1.50116930E+03   # MSf(1,4,1)
   2000001     1.50020383E+03   # MSf(2,4,1)
   1000014     4.95862081E+02   # MSf(1,1,2)
   1000013     5.02443408E+02   # MSf(1,2,2)
   2000013     5.01668656E+02   # MSf(2,2,2)
   1000004     1.49903435E+03   # MSf(1,3,2)
   2000004     1.49959279E+03   # MSf(2,3,2)
   1000003     1.50117823E+03   # MSf(1,4,2)
   2000003     1.50019489E+03   # MSf(2,4,2)
   1000016     9.97937475E+02   # MSf(1,1,3)
   1000015     9.99706008E+02   # MSf(1,2,3)
   2000015     1.00235473E+03   # MSf(2,2,3)
   1000006     8.76433964E+02   # MSf(1,3,3)
   2000006     1.13478597E+03   # MSf(2,3,3)
   1000005     9.97997226E+02   # MSf(1,4,3)
   2000005     1.00406865E+03   # MSf(2,4,3)
        25     1.24474536E+02   # Mh0
        35     4.00073220E+02   # MHH
        36     4.00000000E+02   # MA0
        37     4.08156581E+02   # MHp
   1000022     8.73151787E+01   # MNeu(1)
   1000023     1.50691484E+02   # MNeu(2)
   1000025    -2.09765112E+02   # MNeu(3)
   1000035     2.67230101E+02   # MNeu(4)
   1000024     1.46382964E+02   # MCha(1)
   1000037     2.67394287E+02   # MCha(2)
   1000021     1.50000000E+03   # MGl
BLOCK DMASS
         0     1.73200000E+02   # Q
        25     7.18376481E-01   # Delta Mh0
        35     4.63288770E-03   # Delta MHH
        36     0.00000000E+00   # Delta MA0
        37     3.53382503E-02   # Delta MHp
BLOCK NMIX
     1   1     9.27221638E-01   # ZNeu(1,1)
     1   2    -1.25407267E-01   # ZNeu(1,2)
     1   3     3.17017881E-01   # ZNeu(1,3)
     1   4    -1.55024882E-01   # ZNeu(1,4)
     2   1    -3.31751353E-01   # ZNeu(2,1)
     2   2    -6.94205426E-01   # ZNeu(2,2)
     2   3     5.03447544E-01   # ZNeu(2,3)
     2   4    -3.93141752E-01   # ZNeu(2,4)
     3   1     9.44178182E-02   # ZNeu(3,1)
     3   2    -1.31418945E-01   # ZNeu(3,2)
     3   3    -6.78531191E-01   # ZNeu(3,3)
     3   4    -7.16526175E-01   # ZNeu(3,4)
     4   1    -1.45898421E-01   # ZNeu(4,1)
     4   2     6.96477498E-01   # ZNeu(4,2)
     4   3     4.30854565E-01   # ZNeu(4,3)
     4   4    -5.54974855E-01   # ZNeu(4,4)
BLOCK UMIX
     1   1    -6.09959700E-01   # UCha(1,1)
     1   2     7.92432435E-01   # UCha(1,2)
     2   1     7.92432435E-01   # UCha(2,1)
     2   2     6.09959700E-01   # UCha(2,2)
BLOCK VMIX
     1   1    -7.92432435E-01   # VCha(1,1)
     1   2     6.09959700E-01   # VCha(1,2)
     2   1     6.09959700E-01   # VCha(2,1)
     2   2     7.92432435E-01   # VCha(2,2)
BLOCK STAUMIX
     1   1     6.76377949E-01   # USf(1,1)
     1   2     7.36554729E-01   # USf(1,2)
     2   1     7.36554729E-01   # USf(2,1)
     2   2    -6.76377949E-01   # USf(2,2)
BLOCK STOPMIX
     1   1     7.08245033E-01   # USf(1,1)
     1   2    -7.05966694E-01   # USf(1,2)
     2   1     7.05966694E-01   # USf(2,1)
     2   2     7.08245033E-01   # USf(2,2)
BLOCK SBOTMIX
     1   1     6.17101759E-01   # USf(1,1)
     1   2     7.86883358E-01   # USf(1,2)
     2   1     7.86883358E-01   # USf(2,1)
     2   2    -6.17101759E-01   # USf(2,2)
BLOCK ALPHA
              -7.84593728E-02   # Alpha
BLOCK DALPHA
               2.46174542E-04   # Delta Alpha
BLOCK HMIX Q= -0.99900000E+03
         1     2.00000000E+02   # MUE
         2     1.50000000E+01   # TB
BLOCK MSOFT Q=  0.00000000E+00
         1     9.54716519E+01   # M1
         2     2.00000000E+02   # M2
         3     1.50000000E+03   # M3
        31     5.00000000E+02   # MSL(1)
        32     5.00000000E+02   # MSL(2)
        33     1.00000000E+03   # MSL(3)
        34     5.00000000E+02   # MSE(1)
        35     5.00000000E+02   # MSE(2)
        36     1.00000000E+03   # MSE(3)
        41     1.50000000E+03   # MSQ(1)
        42     1.50000000E+03   # MSQ(2)
        43     1.00000000E+03   # MSQ(3)
        44     1.50000000E+03   # MSU(1)
        45     1.50000000E+03   # MSU(2)
        46     1.00000000E+03   # MSU(3)
        47     1.50000000E+03   # MSD(1)
        48     1.50000000E+03   # MSD(2)
        49     1.00000000E+03   # MSD(3)
BLOCK AE Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.51333333E+03   # Af(3,3)
BLOCK AU Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.51333333E+03   # Af(3,3)
BLOCK AD Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.51333333E+03   # Af(3,3)
BLOCK YE Q=  0.00000000E+00
     1   1     4.41229818E-05   # Yf(1,1)
     2   2     9.12323244E-03   # Yf(2,2)
     3   3     1.53440373E-01   # Yf(3,3)
BLOCK YU Q=  0.00000000E+00
     1   1     1.72693059E-05   # Yf(1,1)
     2   2     7.40277579E-03   # Yf(2,2)
     3   3     9.97014594E-01   # Yf(3,3)
BLOCK YD Q=  0.00000000E+00
     1   1     5.10250933E-04   # Yf(1,1)
     2   2     8.07871351E-03   # Yf(2,2)
     3   3     3.42821112E-01   # Yf(3,3)
BLOCK VCKMIN
         1     2.25300000E-01   # lambda
         2     8.08000000E-01   # A
         3     1.32000000E-01   # rhobar
         4     3.41000000E-01   # etabar
BLOCK MSL2 Q=  0.00000000E+00
     1   1     2.50000000E+05   # MSL2(1,1)
     2   2     2.50000000E+05   # MSL2(2,2)
     3   3     1.00000000E+06   # MSL2(3,3)
BLOCK MSE2 Q=  0.00000000E+00
     1   1     2.50000000E+05   # MSE2(1,1)
     2   2     2.50000000E+05   # MSE2(2,2)
     3   3     1.00000000E+06   # MSE2(3,3)
BLOCK MSQ2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSQ2(1,1)
     2   2     2.25000000E+06   # MSQ2(2,2)
     3   3     1.00000000E+06   # MSQ2(3,3)
BLOCK MSU2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSU2(1,1)
     2   2     2.25000000E+06   # MSU2(2,2)
     3   3     1.00000000E+06   # MSU2(3,3)
BLOCK MSD2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSD2(1,1)
     2   2     2.25000000E+06   # MSD2(2,2)
     3   3     1.00000000E+06   # MSD2(3,3)
BLOCK TE Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     2.32206432E+02   # Tf(3,3)
BLOCK TU Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     1.50881542E+03   # Tf(3,3)
BLOCK TD Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     5.18802616E+02   # Tf(3,3)
BLOCK SELMIX
     1   1     9.99994220E-01   # UASf(1,1)
     1   4    -3.39992530E-03   # UASf(1,4)
     2   2     8.88703374E-01   # UASf(2,2)
     2   5    -4.58482621E-01   # UASf(2,5)
     3   3     6.76377949E-01   # UASf(3,3)
     3   6     7.36554729E-01   # UASf(3,6)
     4   1     3.39992530E-03   # UASf(4,1)
     4   4     9.99994220E-01   # UASf(4,4)
     5   2     4.58482621E-01   # UASf(5,2)
     5   5     8.88703374E-01   # UASf(5,5)
     6   3     7.36554729E-01   # UASf(6,3)
     6   6    -6.76377949E-01   # UASf(6,6)
BLOCK USQMIX
     1   1     1.00000000E+00   # UASf(1,1)
     1   4     2.38921826E-05   # UASf(1,4)
     2   2     9.99947568E-01   # UASf(2,2)
     2   5     1.02401713E-02   # UASf(2,5)
     3   3     7.08245033E-01   # UASf(3,3)
     3   6    -7.05966694E-01   # UASf(3,6)
     4   1    -2.38921826E-05   # UASf(4,1)
     4   4     1.00000000E+00   # UASf(4,4)
     5   2    -1.02401713E-02   # UASf(5,2)
     5   5     9.99947568E-01   # UASf(5,5)
     6   3     7.05966694E-01   # UASf(6,3)
     6   6     7.08245033E-01   # UASf(6,6)
BLOCK DSQMIX
     1   1     9.99981285E-01   # UASf(1,1)
     1   4    -6.11805721E-03   # UASf(1,4)
     2   2     9.95425579E-01   # UASf(2,2)
     2   5    -9.55401352E-02   # UASf(2,5)
     3   3     6.17101759E-01   # UASf(3,3)
     3   6     7.86883358E-01   # UASf(3,6)
     4   1     6.11805721E-03   # UASf(4,1)
     4   4     9.99981285E-01   # UASf(4,4)
     5   2     9.55401352E-02   # UASf(5,2)
     5   5     9.95425579E-01   # UASf(5,5)
     6   3     7.86883358E-01   # UASf(6,3)
     6   6    -6.17101759E-01   # UASf(6,6)
BLOCK CVHMIX
     1   1     9.99988987E-01   # UH(1,1)
     1   2     4.69316213E-03   # UH(1,2)
     1   3     0.00000000E+00   # UH(1,3)
     2   1    -4.69316213E-03   # UH(2,1)
     2   2     9.99988987E-01   # UH(2,2)
     2   3     0.00000000E+00   # UH(2,3)
     3   1     0.00000000E+00   # UH(3,1)
     3   2     0.00000000E+00   # UH(3,2)
     3   3     1.00000000E+00   # UH(3,3)
DECAY        25     4.65276693E-03   # Gamma(h0)
     1.96724963E-03   2        22        22   # BR(h0 -> photon photon)
     1.21737978E-03   2        22        23   # BR(h0 -> photon Z)
     2.15844839E-02   2        23        23   # BR(h0 -> Z Z)
     1.80179278E-01   2       -24        24   # BR(h0 -> W W)
     5.91355526E-02   2        21        21   # BR(h0 -> gluon gluon)
     5.89789674E-09   2       -11        11   # BR(h0 -> Electron electron)
     2.62348611E-04   2       -13        13   # BR(h0 -> Muon muon)
     7.53683135E-02   2       -15        15   # BR(h0 -> Tau tau)
     1.72380829E-07   2        -2         2   # BR(h0 -> Up up)
     2.38762943E-02   2        -4         4   # BR(h0 -> Charm charm)
     9.62799653E-07   2        -1         1   # BR(h0 -> Down down)
     2.41791409E-04   2        -3         3   # BR(h0 -> Strange strange)
     6.36166167E-01   2        -5         5   # BR(h0 -> Bottom bottom)
DECAY        35     2.25086318E+00   # Gamma(HH)
    -4.08257740E-06   2        22        22   # BR(HH -> photon photon)
    -8.48563911E-06   2        22        23   # BR(HH -> photon Z)
    -4.88125035E-04   2        23        23   # BR(HH -> Z Z)
    -1.06154917E-03   2       -24        24   # BR(HH -> W W)
    -2.49961313E-04   2        21        21   # BR(HH -> gluon gluon)
    -6.28467171E-09   2       -11        11   # BR(HH -> Electron electron)
     2.79651172E-04   2       -13        13   # BR(HH -> Muon muon)
    -7.93478114E-02   2       -15        15   # BR(HH -> Tau tau)
    -4.89058931E-12   2        -2         2   # BR(HH -> Up up)
    -6.76746446E-07   2        -4         4   # BR(HH -> Charm charm)
    -8.23354627E-03   2        -6         6   # BR(HH -> Top top)
    -8.07831627E-07   2        -1         1   # BR(HH -> Down down)
    -2.02873198E-04   2        -3         3   # BR(HH -> Strange strange)
    -5.08425815E-01   2        -5         5   # BR(HH -> Bottom bottom)
    -1.64246048E-01   2  -1000024   1000024   # BR(HH -> Chargino1 chargino1)
    -3.78523772E-02   2   1000022   1000022   # BR(HH -> neutralino1 neutralino1)
    -7.55623257E-02   2   1000022   1000023   # BR(HH -> neutralino1 neutralino2)
    -6.73726394E-02   2   1000022   1000025   # BR(HH -> neutralino1 neutralino3)
    -1.36161727E-06   2   1000022   1000035   # BR(HH -> neutralino1 neutralino4)
    -2.45404168E-02   2   1000023   1000023   # BR(HH -> neutralino2 neutralino2)
    -2.62042176E-02   2   1000023   1000025   # BR(HH -> neutralino2 neutralino3)
    -5.91722191E-03   2        25        25   # BR(HH -> h0 h0)
DECAY        36     2.98489556E+00   # Gamma(A0)
     7.81394817E-06   2        22        22   # BR(A0 -> photon photon)
     1.75210699E-05   2        22        23   # BR(A0 -> photon Z)
     1.76890625E-04   2        21        21   # BR(A0 -> gluon gluon)
     4.74775799E-09   2       -11        11   # BR(A0 -> Electron electron)
     2.11262656E-04   2       -13        13   # BR(A0 -> Muon muon)
     5.99706586E-02   2       -15        15   # BR(A0 -> Tau tau)
     2.61279044E-12   2        -2         2   # BR(A0 -> Up up)
     3.62383666E-07   2        -4         4   # BR(A0 -> Charm charm)
     1.77137970E-02   2        -6         6   # BR(A0 -> Top top)
     6.10587596E-07   2        -1         1   # BR(A0 -> Down down)
     1.53338701E-04   2        -3         3   # BR(A0 -> Strange strange)
     3.84334584E-01   2        -5         5   # BR(A0 -> Bottom bottom)
     3.17389469E-01   2  -1000024   1000024   # BR(A0 -> Chargino1 chargino1)
     4.07269148E-02   2   1000022   1000022   # BR(A0 -> neutralino1 neutralino1)
     1.05034520E-01   2   1000022   1000023   # BR(A0 -> neutralino1 neutralino2)
     1.72777060E-02   2   1000022   1000025   # BR(A0 -> neutralino1 neutralino3)
     2.50574755E-04   2   1000022   1000035   # BR(A0 -> neutralino1 neutralino4)
     5.38254466E-02   2   1000023   1000023   # BR(A0 -> neutralino2 neutralino2)
     2.32036857E-03   2   1000023   1000025   # BR(A0 -> neutralino2 neutralino3)
     5.88155799E-04   2        23        25   # BR(A0 -> Z h0)
     6.14087099E-35   2        25        25   # BR(A0 -> h0 h0)
DECAY        37     1.68806399E+00   # Gamma(Hp)
     9.00389912E-09   2       -11        12   # BR(Hp -> Electron nu_e)
     3.84944691E-04   2       -13        14   # BR(Hp -> Muon nu_mu)
     1.08883918E-01   2       -15        16   # BR(Hp -> Tau nu_tau)
     1.03786491E-06   2        -1         2   # BR(Hp -> Down up)
     1.18283266E-05   2        -3         2   # BR(Hp -> Strange up)
     7.07997573E-06   2        -5         2   # BR(Hp -> Bottom up)
     7.97911900E-08   2        -1         4   # BR(Hp -> Down charm)
     2.60441150E-04   2        -3         4   # BR(Hp -> Strange charm)
     9.91431528E-04   2        -5         4   # BR(Hp -> Bottom charm)
     2.41628735E-06   2        -1         6   # BR(Hp -> Down top)
     5.29340653E-05   2        -3         6   # BR(Hp -> Strange top)
     5.00585719E-01   2        -5         6   # BR(Hp -> Bottom top)
     2.16770205E-01   2   1000022   1000024   # BR(Hp -> neutralino1 chargino1)
     3.51866617E-03   2   1000022   1000037   # BR(Hp -> neutralino1 chargino2)
     3.32873893E-02   2   1000023   1000024   # BR(Hp -> neutralino2 chargino1)
     1.34053727E-01   2   1000024   1000025   # BR(Hp -> chargino1 neutralino3)
     1.18811690E-03   2        24        25   # BR(Hp -> W h0)
     2.71651248E-08   2        24        35   # BR(Hp -> W HH)
     2.84172162E-08   2        24        36   # BR(Hp -> W A0)
DECAY         6     1.37127534E+00   # Gamma(top)
     1.00000000E+00   2         5        24   # BR(top -> bottom W)
"""

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(1),                        
                         filterEfficiency = cms.untracked.double(1),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         SLHATableForPythia8 = cms.string('%s' % SLHA_TABLE),
                         comEnergy = cms.double(COM_ENERGY),
                         crossSection = cms.untracked.double(CROSS_SECTION),                         
                         maxEventsToPrint = cms.untracked.int32(1),
                         PythiaParameters = cms.PSet(
                             pythia8CommonSettingsBlock,
                             pythia8CUEP8M1SettingsBlock,
                             processParameters = cms.vstring(
                                 'Higgs:useBSM = on', 
                                 PROCESS, 
                                 'SLHA:allowUserOverride = off', 
                                 'SLHA:minMassSM = 100.', 
                                 'PhaseSpace:mHatMin = 56.0'
                             ),
                             parameterSets = cms.vstring(
                                 'pythia8CommonSettings',
                                 'pythia8CUEP8M1Settings',
                                 'processParameters'
                                 )
                             )
                         )

ProductionFilterSequence = cms.Sequence(generator)

import uproot3
import numpy as np
import pandas as pd
import random

path1 = '/data2/Users/undergraduate/bharadwaj/csvfiles/Groundhog_files/temp/sig/'

path2 = '/data2/Users/undergraduate/bharadwaj/csvfiles/Groundhog_files/temp/bkg/bkg/'

path3 = '/data2/Users/undergraduate/bharadwaj/csvfiles/G12/data/'

sig = pd.read_csv(path1+'sig1.csv',names=["entry","subentry","nPho", "phoE", "phoSigmaE", "phoESEnP1", "phoESEnP2", "phoE2x2Full5x5", "phoE5x5Full5x5", "phoMaxEnergyXtal", "phoE2ndFull5x5", "phoE1x3Full5x5", "phoE1x5Full5x5", "phoE2x5Full5x5", "phoR9Full5x5","phoPFClusEcalIso", "phoPFClusHcalIso", "nPhoTrkSolidConeDR03", "nPhoTrkHollowConeDR03", "phoTrkSumPtSolidConeDR03", "phoTrkSumPtHollowConeDR03","nPhoTrkHollowConeDR04", "nPhoTrkSolidConeDR04", "phoTrkSumPtSolidConeDR04", "phoTrkSumPtHollowConeDR04", "phoECALIso", "phoHCALIso", "phoSeedBCE", "phoSeedBCEta", "phoSeedBCPhi", "phoMIPChi2", "phoMIPTotEnergy", "phoMIPSlope", "phoMIPIntercept","phoMIPNhitCone", "phoEt", "phoEta", "phoPhi", "phoUnCalibE", "phoUnCalibESigma", "phoCalibE", "phoCalibESigma", "phoCalibEt", "phoEnergyScale", "phoEnergySigma","phoSCE", "phoSCRawE", "phoSCindex", "phoSCEta", "phoSCPhi", "phoSCEtaWidth", "phoSCPhiWidth", "phohasPixelSeed", "phoEleVeto", "phoHoverE", "phoSigmaIEtaIEtaFull5x5", "phoSigmaIEtaIPhiFull5x5", "phoSigmaIPhiIPhiFull5x5", "phoPFChIso", "phoPFChWorstIso", "phoPFPhoIso", "phoPFNeuIso", "phoIDMVA", "phoIDbit", "phoSeedTime", "phoSeedEnergy", "phoFiredSingleTrgs", "phoFiredDoubleTrgs", "phoFiredTripleTrgs", "phoFiredL1Trgs", "phoScale_up", "phoScale_dn", "phoScale_stat_up", "phoScale_stat_dn", "phoScale_syst_up", "phoScale_syst_dn", "phoScale_gain_up", "phoScale_gain_dn", "phoResol_up", "phoResol_dn", "phoResol_rho_up", "phoResol_rho_dn", "phoResol_phi_up", "phoResol_phi_dn", "pho_gen_index", "necalSC","phoDirectEcalSCindex"])
sig = sig[(sig.subentry == 0) & (sig.phoEta >= -1.4442) & (sig.phoEta <= 1.4442) & (sig.phoCalibEt >= 200)]
sig['Weights'] = 0.00807;
print(sig.shape)
print("completed reading sig")

sig['phoEoverphoraw'] = sig['phoE']/sig['phoSCRawE'] #4

sig['phoE2ndoverphoraw'] = sig['phoE2ndFull5x5']/sig['phoSCRawE'] #5

sig['phoE2x2overphoraw'] = sig['phoE2x2Full5x5']/sig['phoSCRawE'] #6

sig['phoE1x3overphoraw'] = sig['phoE1x3Full5x5']/sig['phoSCRawE'] #7

sig['phoE2x5overphoraw'] = sig['phoE2x5Full5x5']/sig['phoSCRawE'] #8

sig['phoE5x5overphoraw'] = sig['phoE5x5Full5x5']/sig['phoSCRawE'] #9

sig['photrkisooverphoEt'] = sig['phoTrkSumPtHollowConeDR03']/sig['phoEt']

sig['phoEcaloverphoEt'] = sig['phoPFClusEcalIso']/sig['phoEt']

sig['phoHcaloverphoEt'] = sig['phoPFClusHcalIso']/sig['phoEt']

sig['isSignal'] = 1;

list = ['phoHoverE','phoTrkSumPtHollowConeDR03','phoPFClusEcalIso','phoPFClusHcalIso','phoEoverphoraw',
'phoE2ndoverphoraw','phoE2x2overphoraw','phoE1x3overphoraw','phoE2x5overphoraw','phoE5x5overphoraw',
'phoSigmaIEtaIEtaFull5x5','phoSigmaIPhiIPhiFull5x5','phoSigmaIEtaIPhiFull5x5','Weights','isSignal'] 

sig.to_csv(path3+'sig.csv', columns = list )

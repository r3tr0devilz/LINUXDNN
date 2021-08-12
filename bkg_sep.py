import numpy as np
import random
import matplotlib
import pandas as pd

path1 = "/data2/User/undergraduate/bharadwaj/csvfiles/Groundhog_files/temp/sig/" 

path = "/data2/Users/undergraduate/bharadwaj/csvfiles/Groundhog_files/temp/bkg/bkg/"

path3 = "/data2/Users/undergraduate/bharadwaj/csvfiles/G12/data/"


bkg1 = pd.read_csv(path+"bkg1(170to300).csv",names=["entry","subentry","nPho", "phoE", "phoSigmaE", "phoESEnP1", "phoESEnP2", "phoE2x2Full5x5", "phoE5x5Full5x5", "phoMaxEnergyXtal", "phoE2ndFull5x5", "phoE1x3Full5x5", "phoE1x5Full5x5", "phoE2x5Full5x5", "phoR9Full5x5","phoPFClusEcalIso", "phoPFClusHcalIso", "nPhoTrkSolidConeDR03", "nPhoTrkHollowConeDR03", "phoTrkSumPtSolidConeDR03", "phoTrkSumPtHollowConeDR03","nPhoTrkHollowConeDR04", "nPhoTrkSolidConeDR04", "phoTrkSumPtSolidConeDR04", "phoTrkSumPtHollowConeDR04", "phoECALIso", "phoHCALIso", "phoSeedBCE", "phoSeedBCEta", "phoSeedBCPhi", "phoMIPChi2", "phoMIPTotEnergy", "phoMIPSlope", "phoMIPIntercept","phoMIPNhitCone", "phoEt", "phoEta", "phoPhi", "phoUnCalibE", "phoUnCalibESigma", "phoCalibE", "phoCalibESigma", "phoCalibEt", "phoEnergyScale", "phoEnergySigma","phoSCE", "phoSCRawE", "phoSCindex", "phoSCEta", "phoSCPhi", "phoSCEtaWidth", "phoSCPhiWidth", "phohasPixelSeed", "phoEleVeto", "phoHoverE", "phoSigmaIEtaIEtaFull5x5", "phoSigmaIEtaIPhiFull5x5", "phoSigmaIPhiIPhiFull5x5", "phoPFChIso", "phoPFChWorstIso", "phoPFPhoIso", "phoPFNeuIso", "phoIDMVA", "phoIDbit", "phoSeedTime", "phoSeedEnergy", "phoFiredSingleTrgs", "phoFiredDoubleTrgs", "phoFiredTripleTrgs", "phoFiredL1Trgs", "phoScale_up", "phoScale_dn", "phoScale_stat_up", "phoScale_stat_dn", "phoScale_syst_up", "phoScale_syst_dn", "phoScale_gain_up", "phoScale_gain_dn", "phoResol_up", "phoResol_dn", "phoResol_rho_up", "phoResol_rho_dn", "phoResol_phi_up", "phoResol_phi_dn", "pho_gen_index", "necalSC","phoDirectEcalSCindex"])
bkg1 = bkg1[(bkg1.subentry == 0) & (bkg1.phoEta >= -1.4442) & (bkg1.phoEta <= 1.4442) & (bkg1.phoCalibEt >= 200)]
bkg1['Weights'] = 2835;
bkg1 = bkg1.iloc[:200000,:]
print(bkg1.shape)
print("Completed reading bkg1")


bkg2 = pd.read_csv(path+'bkg2(300to470).csv',names=["entry","subentry","nPho", "phoE", "phoSigmaE", "phoESEnP1", "phoESEnP2", "phoE2x2Full5x5", "phoE5x5Full5x5", "phoMaxEnergyXtal", "phoE2ndFull5x5", "phoE1x3Full5x5", "phoE1x5Full5x5", "phoE2x5Full5x5", "phoR9Full5x5","phoPFClusEcalIso", "phoPFClusHcalIso", "nPhoTrkSolidConeDR03", "nPhoTrkHollowConeDR03", "phoTrkSumPtSolidConeDR03", "phoTrkSumPtHollowConeDR03","nPhoTrkHollowConeDR04", "nPhoTrkSolidConeDR04", "phoTrkSumPtSolidConeDR04", "phoTrkSumPtHollowConeDR04", "phoECALIso", "phoHCALIso", "phoSeedBCE", "phoSeedBCEta", "phoSeedBCPhi", "phoMIPChi2", "phoMIPTotEnergy", "phoMIPSlope", "phoMIPIntercept","phoMIPNhitCone", "phoEt", "phoEta", "phoPhi", "phoUnCalibE", "phoUnCalibESigma", "phoCalibE", "phoCalibESigma", "phoCalibEt", "phoEnergyScale", "phoEnergySigma","phoSCE", "phoSCRawE", "phoSCindex", "phoSCEta", "phoSCPhi", "phoSCEtaWidth", "phoSCPhiWidth", "phohasPixelSeed", "phoEleVeto", "phoHoverE", "phoSigmaIEtaIEtaFull5x5", "phoSigmaIEtaIPhiFull5x5", "phoSigmaIPhiIPhiFull5x5", "phoPFChIso", "phoPFChWorstIso", "phoPFPhoIso", "phoPFNeuIso", "phoIDMVA", "phoIDbit", "phoSeedTime", "phoSeedEnergy", "phoFiredSingleTrgs", "phoFiredDoubleTrgs", "phoFiredTripleTrgs", "phoFiredL1Trgs", "phoScale_up", "phoScale_dn", "phoScale_stat_up", "phoScale_stat_dn", "phoScale_syst_up", "phoScale_syst_dn", "phoScale_gain_up", "phoScale_gain_dn", "phoResol_up", "phoResol_dn", "phoResol_rho_up", "phoResol_rho_dn", "phoResol_phi_up", "phoResol_phi_dn", "pho_gen_index", "necalSC","phoDirectEcalSCindex"])
bkg2 = bkg2[(bkg2.subentry == 0) & (bkg2.phoEta >= -1.4442) & (bkg2.phoEta <= 1.4442) & (bkg2.phoCalibEt >= 200)]
bkg2['Weights'] = 143.43;
bkg2 = bkg2.iloc[:200000,:]
print(bkg2.shape)
print("Completed reading bkg2")

bkg3 = pd.read_csv(path+'bkg3(470to600).csv',names=["entry","subentry","nPho", "phoE", "phoSigmaE", "phoESEnP1", "phoESEnP2", "phoE2x2Full5x5", "phoE5x5Full5x5", "phoMaxEnergyXtal", "phoE2ndFull5x5", "phoE1x3Full5x5", "phoE1x5Full5x5", "phoE2x5Full5x5", "phoR9Full5x5","phoPFClusEcalIso", "phoPFClusHcalIso", "nPhoTrkSolidConeDR03", "nPhoTrkHollowConeDR03", "phoTrkSumPtSolidConeDR03", "phoTrkSumPtHollowConeDR03","nPhoTrkHollowConeDR04", "nPhoTrkSolidConeDR04", "phoTrkSumPtSolidConeDR04", "phoTrkSumPtHollowConeDR04", "phoECALIso", "phoHCALIso", "phoSeedBCE", "phoSeedBCEta", "phoSeedBCPhi", "phoMIPChi2", "phoMIPTotEnergy", "phoMIPSlope", "phoMIPIntercept","phoMIPNhitCone", "phoEt", "phoEta", "phoPhi", "phoUnCalibE", "phoUnCalibESigma", "phoCalibE", "phoCalibESigma", "phoCalibEt", "phoEnergyScale", "phoEnergySigma","phoSCE", "phoSCRawE", "phoSCindex", "phoSCEta", "phoSCPhi", "phoSCEtaWidth", "phoSCPhiWidth", "phohasPixelSeed", "phoEleVeto", "phoHoverE", "phoSigmaIEtaIEtaFull5x5", "phoSigmaIEtaIPhiFull5x5", "phoSigmaIPhiIPhiFull5x5", "phoPFChIso", "phoPFChWorstIso", "phoPFPhoIso", "phoPFNeuIso", "phoIDMVA", "phoIDbit", "phoSeedTime", "phoSeedEnergy", "phoFiredSingleTrgs", "phoFiredDoubleTrgs", "phoFiredTripleTrgs", "phoFiredL1Trgs", "phoScale_up", "phoScale_dn", "phoScale_stat_up", "phoScale_stat_dn", "phoScale_syst_up", "phoScale_syst_dn", "phoScale_gain_up", "phoScale_gain_dn", "phoResol_up", "phoResol_dn", "phoResol_rho_up", "phoResol_rho_dn", "phoResol_phi_up", "phoResol_phi_dn", "pho_gen_index", "necalSC","phoDirectEcalSCindex"])
bkg3 = bkg3[(bkg3.subentry == 0) & (bkg3.phoEta >= -1.4442) & (bkg3.phoEta <= 1.4442) & (bkg3.phoCalibEt >= 200)]
bkg3['Weights'] = 115.92;
bkg3 = bkg3.iloc[:200000,:]
print(bkg3.shape)
print("Completed reading bkg3")

bkg4 = pd.read_csv(path+'bkg4(600to800).csv',names=["entry","subentry","nPho", "phoE", "phoSigmaE", "phoESEnP1", "phoESEnP2", "phoE2x2Full5x5", "phoE5x5Full5x5", "phoMaxEnergyXtal", "phoE2ndFull5x5", "phoE1x3Full5x5", "phoE1x5Full5x5", "phoE2x5Full5x5", "phoR9Full5x5","phoPFClusEcalIso", "phoPFClusHcalIso", "nPhoTrkSolidConeDR03", "nPhoTrkHollowConeDR03", "phoTrkSumPtSolidConeDR03", "phoTrkSumPtHollowConeDR03","nPhoTrkHollowConeDR04", "nPhoTrkSolidConeDR04", "phoTrkSumPtSolidConeDR04", "phoTrkSumPtHollowConeDR04", "phoECALIso", "phoHCALIso", "phoSeedBCE", "phoSeedBCEta", "phoSeedBCPhi", "phoMIPChi2", "phoMIPTotEnergy", "phoMIPSlope", "phoMIPIntercept","phoMIPNhitCone", "phoEt", "phoEta", "phoPhi", "phoUnCalibE", "phoUnCalibESigma", "phoCalibE", "phoCalibESigma", "phoCalibEt", "phoEnergyScale", "phoEnergySigma","phoSCE", "phoSCRawE", "phoSCindex", "phoSCEta", "phoSCPhi", "phoSCEtaWidth", "phoSCPhiWidth", "phohasPixelSeed", "phoEleVeto", "phoHoverE", "phoSigmaIEtaIEtaFull5x5", "phoSigmaIEtaIPhiFull5x5", "phoSigmaIPhiIPhiFull5x5", "phoPFChIso", "phoPFChWorstIso", "phoPFPhoIso", "phoPFNeuIso", "phoIDMVA", "phoIDbit", "phoSeedTime", "phoSeedEnergy", "phoFiredSingleTrgs", "phoFiredDoubleTrgs", "phoFiredTripleTrgs", "phoFiredL1Trgs", "phoScale_up", "phoScale_dn", "phoScale_stat_up", "phoScale_stat_dn", "phoScale_syst_up", "phoScale_syst_dn", "phoScale_gain_up", "phoScale_gain_dn", "phoResol_up", "phoResol_dn", "phoResol_rho_up", "phoResol_rho_dn", "phoResol_phi_up", "phoResol_phi_dn", "pho_gen_index", "necalSC","phoDirectEcalSCindex"])
bkg4 = bkg4[(bkg4.subentry == 0) & (bkg4.phoEta >= -1.4442) & (bkg4.phoEta <= 1.4442) & (bkg4.phoCalibEt >= 200)]
bkg4['Weights'] = 32.76;
bkg4 = bkg4.iloc[:200000,:]
print(bkg4.shape)
print("Completed reading bkg4")


bkg5 = pd.read_csv(path+'bkg5(800to1000).csv',names=["entry","subentry","nPho", "phoE", "phoSigmaE", "phoESEnP1", "phoESEnP2", "phoE2x2Full5x5", "phoE5x5Full5x5", "phoMaxEnergyXtal", "phoE2ndFull5x5", "phoE1x3Full5x5", "phoE1x5Full5x5", "phoE2x5Full5x5", "phoR9Full5x5","phoPFClusEcalIso", "phoPFClusHcalIso", "nPhoTrkSolidConeDR03", "nPhoTrkHollowConeDR03", "phoTrkSumPtSolidConeDR03", "phoTrkSumPtHollowConeDR03","nPhoTrkHollowConeDR04", "nPhoTrkSolidConeDR04", "phoTrkSumPtSolidConeDR04", "phoTrkSumPtHollowConeDR04", "phoECALIso", "phoHCALIso", "phoSeedBCE", "phoSeedBCEta", "phoSeedBCPhi", "phoMIPChi2", "phoMIPTotEnergy", "phoMIPSlope", "phoMIPIntercept","phoMIPNhitCone", "phoEt", "phoEta", "phoPhi", "phoUnCalibE", "phoUnCalibESigma", "phoCalibE", "phoCalibESigma", "phoCalibEt", "phoEnergyScale", "phoEnergySigma","phoSCE", "phoSCRawE", "phoSCindex", "phoSCEta", "phoSCPhi", "phoSCEtaWidth", "phoSCPhiWidth", "phohasPixelSeed", "phoEleVeto", "phoHoverE", "phoSigmaIEtaIEtaFull5x5", "phoSigmaIEtaIPhiFull5x5", "phoSigmaIPhiIPhiFull5x5", "phoPFChIso", "phoPFChWorstIso", "phoPFPhoIso", "phoPFNeuIso", "phoIDMVA", "phoIDbit", "phoSeedTime", "phoSeedEnergy", "phoFiredSingleTrgs", "phoFiredDoubleTrgs", "phoFiredTripleTrgs", "phoFiredL1Trgs", "phoScale_up", "phoScale_dn", "phoScale_stat_up", "phoScale_stat_dn", "phoScale_syst_up", "phoScale_syst_dn", "phoScale_gain_up", "phoScale_gain_dn", "phoResol_up", "phoResol_dn", "phoResol_rho_up", "phoResol_rho_dn", "phoResol_phi_up", "phoResol_phi_dn", "pho_gen_index", "necalSC","phoDirectEcalSCindex"])
bkg5 = bkg5[(bkg5.subentry == 0) & (bkg5.phoEta >= -1.4442) & (bkg5.phoEta <= 1.4442) & (bkg5.phoCalibEt >= 200)]
bkg5['Weights'] = 5.46;
bkg5 = bkg5.iloc[:200000,:]
print(bkg5.shape)
print("Completed reading bkg5")

bkg6 = pd.read_csv(path+'bkg6(1000to1400).csv',names=["entry","subentry","nPho", "phoE", "phoSigmaE", "phoESEnP1", "phoESEnP2", "phoE2x2Full5x5", "phoE5x5Full5x5", "phoMaxEnergyXtal", "phoE2ndFull5x5", "phoE1x3Full5x5", "phoE1x5Full5x5", "phoE2x5Full5x5", "phoR9Full5x5","phoPFClusEcalIso", "phoPFClusHcalIso", "nPhoTrkSolidConeDR03", "nPhoTrkHollowConeDR03", "phoTrkSumPtSolidConeDR03", "phoTrkSumPtHollowConeDR03","nPhoTrkHollowConeDR04", "nPhoTrkSolidConeDR04", "phoTrkSumPtSolidConeDR04", "phoTrkSumPtHollowConeDR04", "phoECALIso", "phoHCALIso", "phoSeedBCE", "phoSeedBCEta", "phoSeedBCPhi", "phoMIPChi2", "phoMIPTotEnergy", "phoMIPSlope", "phoMIPIntercept","phoMIPNhitCone", "phoEt", "phoEta", "phoPhi", "phoUnCalibE", "phoUnCalibESigma", "phoCalibE", "phoCalibESigma", "phoCalibEt", "phoEnergyScale", "phoEnergySigma","phoSCE", "phoSCRawE", "phoSCindex", "phoSCEta", "phoSCPhi", "phoSCEtaWidth", "phoSCPhiWidth", "phohasPixelSeed", "phoEleVeto", "phoHoverE", "phoSigmaIEtaIEtaFull5x5", "phoSigmaIEtaIPhiFull5x5", "phoSigmaIPhiIPhiFull5x5", "phoPFChIso", "phoPFChWorstIso", "phoPFPhoIso", "phoPFNeuIso", "phoIDMVA", "phoIDbit", "phoSeedTime", "phoSeedEnergy", "phoFiredSingleTrgs", "phoFiredDoubleTrgs", "phoFiredTripleTrgs", "phoFiredL1Trgs", "phoScale_up", "phoScale_dn", "phoScale_stat_up", "phoScale_stat_dn", "phoScale_syst_up", "phoScale_syst_dn", "phoScale_gain_up", "phoScale_gain_dn", "phoResol_up", "phoResol_dn", "phoResol_rho_up", "phoResol_rho_dn", "phoResol_phi_up", "phoResol_phi_dn", "pho_gen_index", "necalSC","phoDirectEcalSCindex"])
bkg6 = bkg6[(bkg6.subentry == 0) & (bkg6.phoEta >= -1.4442) & (bkg6.phoEta <= 1.4442) & (bkg6.phoCalibEt >= 200)]
bkg6['Weights']= 1.575;
bkg6 = bkg6.iloc[:200000,:]
print(bkg6.shape)
print("Completed reading bkg6")

bkg7 = pd.read_csv(path+'bkg7(1400to1800).csv',names=["entry","subentry","nPho", "phoE", "phoSigmaE", "phoESEnP1", "phoESEnP2", "phoE2x2Full5x5", "phoE5x5Full5x5", "phoMaxEnergyXtal", "phoE2ndFull5x5", "phoE1x3Full5x5", "phoE1x5Full5x5", "phoE2x5Full5x5", "phoR9Full5x5","phoPFClusEcalIso", "phoPFClusHcalIso", "nPhoTrkSolidConeDR03", "nPhoTrkHollowConeDR03", "phoTrkSumPtSolidConeDR03", "phoTrkSumPtHollowConeDR03","nPhoTrkHollowConeDR04", "nPhoTrkSolidConeDR04", "phoTrkSumPtSolidConeDR04", "phoTrkSumPtHollowConeDR04", "phoECALIso", "phoHCALIso", "phoSeedBCE", "phoSeedBCEta", "phoSeedBCPhi", "phoMIPChi2", "phoMIPTotEnergy", "phoMIPSlope", "phoMIPIntercept","phoMIPNhitCone", "phoEt", "phoEta", "phoPhi", "phoUnCalibE", "phoUnCalibESigma", "phoCalibE", "phoCalibESigma", "phoCalibEt", "phoEnergyScale", "phoEnergySigma","phoSCE", "phoSCRawE", "phoSCindex", "phoSCEta", "phoSCPhi", "phoSCEtaWidth", "phoSCPhiWidth", "phohasPixelSeed", "phoEleVeto", "phoHoverE", "phoSigmaIEtaIEtaFull5x5", "phoSigmaIEtaIPhiFull5x5", "phoSigmaIPhiIPhiFull5x5", "phoPFChIso", "phoPFChWorstIso", "phoPFPhoIso", "phoPFNeuIso", "phoIDMVA", "phoIDbit", "phoSeedTime", "phoSeedEnergy", "phoFiredSingleTrgs", "phoFiredDoubleTrgs", "phoFiredTripleTrgs", "phoFiredL1Trgs", "phoScale_up", "phoScale_dn", "phoScale_stat_up", "phoScale_stat_dn", "phoScale_syst_up", "phoScale_syst_dn", "phoScale_gain_up", "phoScale_gain_dn", "phoResol_up", "phoResol_dn", "phoResol_rho_up", "phoResol_rho_dn", "phoResol_phi_up", "phoResol_phi_dn", "pho_gen_index", "necalSC","phoDirectEcalSCindex"])
bkg7 = bkg7[(bkg7.subentry == 0) & (bkg7.phoEta >= -1.4442) & (bkg7.phoEta <= 1.4442) & (bkg7.phoCalibEt >= 200)]
bkg7['Weights'] = 0.136;
bkg7 = bkg7.iloc[:200000,:]
print(bkg7.shape)
print("Completed reading bkg7")

bkg8 = pd.read_csv(path+'bkg8(1800to2400).csv',names=["entry","subentry","nPho", "phoE", "phoSigmaE", "phoESEnP1", "phoESEnP2", "phoE2x2Full5x5", "phoE5x5Full5x5", "phoMaxEnergyXtal", "phoE2ndFull5x5", "phoE1x3Full5x5", "phoE1x5Full5x5", "phoE2x5Full5x5", "phoR9Full5x5","phoPFClusEcalIso", "phoPFClusHcalIso", "nPhoTrkSolidConeDR03", "nPhoTrkHollowConeDR03", "phoTrkSumPtSolidConeDR03", "phoTrkSumPtHollowConeDR03","nPhoTrkHollowConeDR04", "nPhoTrkSolidConeDR04", "phoTrkSumPtSolidConeDR04", "phoTrkSumPtHollowConeDR04", "phoECALIso", "phoHCALIso", "phoSeedBCE", "phoSeedBCEta", "phoSeedBCPhi", "phoMIPChi2", "phoMIPTotEnergy", "phoMIPSlope", "phoMIPIntercept","phoMIPNhitCone", "phoEt", "phoEta", "phoPhi", "phoUnCalibE", "phoUnCalibESigma", "phoCalibE", "phoCalibESigma", "phoCalibEt", "phoEnergyScale", "phoEnergySigma","phoSCE", "phoSCRawE", "phoSCindex", "phoSCEta", "phoSCPhi", "phoSCEtaWidth", "phoSCPhiWidth", "phohasPixelSeed", "phoEleVeto", "phoHoverE", "phoSigmaIEtaIEtaFull5x5", "phoSigmaIEtaIPhiFull5x5", "phoSigmaIPhiIPhiFull5x5", "phoPFChIso", "phoPFChWorstIso", "phoPFPhoIso", "phoPFNeuIso", "phoIDMVA", "phoIDbit", "phoSeedTime", "phoSeedEnergy", "phoFiredSingleTrgs", "phoFiredDoubleTrgs", "phoFiredTripleTrgs", "phoFiredL1Trgs", "phoScale_up", "phoScale_dn", "phoScale_stat_up", "phoScale_stat_dn", "phoScale_syst_up", "phoScale_syst_dn", "phoScale_gain_up", "phoScale_gain_dn", "phoResol_up", "phoResol_dn", "phoResol_rho_up", "phoResol_rho_dn", "phoResol_phi_up", "phoResol_phi_dn", "pho_gen_index", "necalSC","phoDirectEcalSCindex"])
bkg8 = bkg8[(bkg8.subentry == 0) & (bkg8.phoEta >= -1.4442) & (bkg8.phoEta <= 1.4442) & (bkg8.phoCalibEt >= 200)]
bkg8['Weights'] = 0.0182;
bkg8 = bkg8.iloc[:200000,:]
print(bkg8.shape)
print("Completed reading bkg8")

bkg9 = pd.read_csv(path+'bkg9(2400to3200).csv',names=["entry","subentry","nPho", "phoE", "phoSigmaE", "phoESEnP1", "phoESEnP2", "phoE2x2Full5x5", "phoE5x5Full5x5", "phoMaxEnergyXtal", "phoE2ndFull5x5", "phoE1x3Full5x5", "phoE1x5Full5x5", "phoE2x5Full5x5", "phoR9Full5x5","phoPFClusEcalIso", "phoPFClusHcalIso", "nPhoTrkSolidConeDR03", "nPhoTrkHollowConeDR03", "phoTrkSumPtSolidConeDR03", "phoTrkSumPtHollowConeDR03","nPhoTrkHollowConeDR04", "nPhoTrkSolidConeDR04", "phoTrkSumPtSolidConeDR04", "phoTrkSumPtHollowConeDR04", "phoECALIso", "phoHCALIso", "phoSeedBCE", "phoSeedBCEta", "phoSeedBCPhi", "phoMIPChi2", "phoMIPTotEnergy", "phoMIPSlope", "phoMIPIntercept","phoMIPNhitCone", "phoEt", "phoEta", "phoPhi", "phoUnCalibE", "phoUnCalibESigma", "phoCalibE", "phoCalibESigma", "phoCalibEt", "phoEnergyScale", "phoEnergySigma","phoSCE", "phoSCRawE", "phoSCindex", "phoSCEta", "phoSCPhi", "phoSCEtaWidth", "phoSCPhiWidth", "phohasPixelSeed", "phoEleVeto", "phoHoverE", "phoSigmaIEtaIEtaFull5x5", "phoSigmaIEtaIPhiFull5x5", "phoSigmaIPhiIPhiFull5x5", "phoPFChIso", "phoPFChWorstIso", "phoPFPhoIso", "phoPFNeuIso", "phoIDMVA", "phoIDbit", "phoSeedTime", "phoSeedEnergy", "phoFiredSingleTrgs", "phoFiredDoubleTrgs", "phoFiredTripleTrgs", "phoFiredL1Trgs", "phoScale_up", "phoScale_dn", "phoScale_stat_up", "phoScale_stat_dn", "phoScale_syst_up", "phoScale_syst_dn", "phoScale_gain_up", "phoScale_gain_dn", "phoResol_up", "phoResol_dn", "phoResol_rho_up", "phoResol_rho_dn", "phoResol_phi_up", "phoResol_phi_dn", "pho_gen_index", "necalSC","phoDirectEcalSCindex"])
bkg9 = bkg9[(bkg9.subentry == 0) & (bkg9.phoEta >= -1.4442) & (bkg9.phoEta <= 1.4442) & (bkg9.phoCalibEt >= 200)]
bkg9['Weights'] = 0.0010;
bkg9 = bkg9.iloc[:200000,:]
print(bkg9.shape)
print("Completed reading bkg9")

bkg10 = pd.read_csv(path+'bkg10(3200toinf).csv',names=["entry","subentry","nPho", "phoE", "phoSigmaE", "phoESEnP1", "phoESEnP2", "phoE2x2Full5x5", "phoE5x5Full5x5", "phoMaxEnergyXtal", "phoE2ndFull5x5", "phoE1x3Full5x5", "phoE1x5Full5x5", "phoE2x5Full5x5", "phoR9Full5x5","phoPFClusEcalIso", "phoPFClusHcalIso", "nPhoTrkSolidConeDR03", "nPhoTrkHollowConeDR03", "phoTrkSumPtSolidConeDR03", "phoTrkSumPtHollowConeDR03","nPhoTrkHollowConeDR04", "nPhoTrkSolidConeDR04", "phoTrkSumPtSolidConeDR04", "phoTrkSumPtHollowConeDR04", "phoECALIso", "phoHCALIso", "phoSeedBCE", "phoSeedBCEta", "phoSeedBCPhi", "phoMIPChi2", "phoMIPTotEnergy", "phoMIPSlope", "phoMIPIntercept","phoMIPNhitCone", "phoEt", "phoEta", "phoPhi", "phoUnCalibE", "phoUnCalibESigma", "phoCalibE", "phoCalibESigma", "phoCalibEt", "phoEnergyScale", "phoEnergySigma","phoSCE", "phoSCRawE", "phoSCindex", "phoSCEta", "phoSCPhi", "phoSCEtaWidth", "phoSCPhiWidth", "phohasPixelSeed", "phoEleVeto", "phoHoverE", "phoSigmaIEtaIEtaFull5x5", "phoSigmaIEtaIPhiFull5x5", "phoSigmaIPhiIPhiFull5x5", "phoPFChIso", "phoPFChWorstIso", "phoPFPhoIso", "phoPFNeuIso", "phoIDMVA", "phoIDbit", "phoSeedTime", "phoSeedEnergy", "phoFiredSingleTrgs", "phoFiredDoubleTrgs", "phoFiredTripleTrgs", "phoFiredL1Trgs", "phoScale_up", "phoScale_dn", "phoScale_stat_up", "phoScale_stat_dn", "phoScale_syst_up", "phoScale_syst_dn", "phoScale_gain_up", "phoScale_gain_dn", "phoResol_up", "phoResol_dn", "phoResol_rho_up", "phoResol_rho_dn", "phoResol_phi_up", "phoResol_phi_dn", "pho_gen_index", "necalSC","phoDirectEcalSCindex"])
bkg10 = bkg10[(bkg10.subentry == 0) & (bkg10.phoEta >= -1.4442) & (bkg10.phoEta <= 1.4442) & (bkg10.phoCalibEt >= 200)]
bkg10['Weights'] = 0.000039;
bkg10 = bkg10.iloc[:200000,:]
print(bkg10.shape)
print("Completed reading bkg10")


bkg = pd.concat([bkg1,bkg2,bkg3,bkg4,bkg5,bkg6,bkg7,bkg8,bkg9,bkg10],ignore_index = True)

bkg['phoEoverphoraw'] = bkg['phoE']/bkg['phoSCRawE'] #4

bkg['phoE2ndoverphoraw'] = bkg['phoE2ndFull5x5']/bkg['phoSCRawE'] #5

bkg['phoE2x2overphoraw'] = bkg['phoE2x2Full5x5']/bkg['phoSCRawE'] #6

bkg['phoE1x3overphoraw'] = bkg['phoE1x3Full5x5']/bkg['phoSCRawE'] #7

bkg['phoE2x5overphoraw'] = bkg['phoE2x5Full5x5']/bkg['phoSCRawE'] #8

bkg['phoE5x5overphoraw'] = bkg['phoE5x5Full5x5']/bkg['phoSCRawE'] #9

bkg['isSignal'] = 0;

print("Completed Division and bkg generation")

header = ['phoHoverE','phoTrkSumPtHollowConeDR03','phoPFClusEcalIso','phoPFClusHcalIso','phoEoverphoraw','phoE2ndoverphoraw','phoE2x2overphoraw','phoE1x3overphoraw','phoE2x5overphoraw','phoE5x5overphoraw','phoSigmaIEtaIEtaFull5x5','phoSigmaIPhiIPhiFull5x5','phoSigmaIEtaIPhiFull5x5','Weights','isSignal']

bkg.to_csv(path3 + "bkg.csv",columns = header)





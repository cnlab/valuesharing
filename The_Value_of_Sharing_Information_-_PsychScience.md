# The Value of Sharing Information: A Neural Account of Information Transmission
Elisa Baek  
April 21, 2016  

The Value of Sharing Information: A Neural Account of Information Transmission

First, we will pull ROI datasheets where we ran the contrasts of interest (SELECT TO READ > CONTENT, SHARE > CONTENT, SHARE > SELECT TO READ) in SPM8.


```r
#Subjective Valuation (SV)
sv_combined<-read.csv('Main Effects/sv_combined.csv')
sv_vmpfc<-read.csv('Main Effects/sv_vmpfc.csv')
sv_vs<-read.csv('Main Effects/sv_vs.csv')

#Self-Relevance
self_combined<-read.csv('Main Effects/self_combined.csv')
self_mpfc<-read.csv('Main Effects/self_mpfc.csv')
self_pcc<-read.csv('Main Effects/self_pcc.csv')
  
#Social Cognition (SC)
sc_combined<-read.csv('Main Effects/sc_combined.csv')
sc_vmpfc<-read.csv('Main Effects/sc_vmpfc.csv')
sc_mmpfc<-read.csv('Main Effects/sc_mmpfc.csv')
sc_dmpfc<-read.csv('Main Effects/sc_dmpfc.csv')
sc_rtpj<-read.csv('Main Effects/sc_rtpj.csv')
sc_ltpj<-read.csv('Main Effects/sc_ltpj.csv')
sc_rsts<-read.csv('Main Effects/sc_rsts.csv')
sc_pc<-read.csv('Main Effects/sc_pc.csv')
```

Now that the datasheets have been read, we will conduct a series of t-tests for statistical significance.

Select > Content

```r
#Subjective Valuation
t.test(sv_combined$READvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sv_combined$READvsCONTENT_reading
## t = 7.2238, df = 40, p-value = 9.168e-09
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.08512276 0.15125691
## sample estimates:
## mean of x 
## 0.1181898
```

```r
t.test(sv_vs$READvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sv_vs$READvsCONTENT_reading
## t = 3.9667, df = 40, p-value = 0.0002939
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.01949318 0.05999123
## sample estimates:
## mean of x 
## 0.0397422
```

```r
t.test(sv_vmpfc$READvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sv_vmpfc$READvsCONTENT_reading
## t = 7.8751, df = 40, p-value = 1.168e-09
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.1344722 0.2273242
## sample estimates:
## mean of x 
## 0.1808982
```

```r
#Self-Relevance
t.test(self_combined$READvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  self_combined$READvsCONTENT_reading
## t = 7.2645, df = 40, p-value = 8.053e-09
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.1033179 0.1829660
## sample estimates:
## mean of x 
## 0.1431419
```

```r
t.test(self_mpfc$READvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  self_mpfc$READvsCONTENT_reading
## t = 7.9126, df = 40, p-value = 1.039e-09
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.1140162 0.1922426
## sample estimates:
## mean of x 
## 0.1531294
```

```r
t.test(self_pcc$READvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  self_pcc$READvsCONTENT_reading
## t = 4.9233, df = 40, p-value = 1.511e-05
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.07634634 0.18268060
## sample estimates:
## mean of x 
## 0.1295135
```

```r
#Social Cognition
t.test(sc_combined$READvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_combined$READvsCONTENT_reading
## t = 4.9916, df = 40, p-value = 1.216e-05
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.04011502 0.09470116
## sample estimates:
##  mean of x 
## 0.06740809
```

```r
t.test(sc_vmpfc$READvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_vmpfc$READvsCONTENT_reading
## t = 8.0266, df = 40, p-value = 7.274e-10
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.1175090 0.1966004
## sample estimates:
## mean of x 
## 0.1570547
```

```r
t.test(sc_mmpfc$READvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_mmpfc$READvsCONTENT_reading
## t = 7.1838, df = 40, p-value = 1.042e-08
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.09137601 0.16291892
## sample estimates:
## mean of x 
## 0.1271475
```

```r
t.test(sc_dmpfc$READvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_dmpfc$READvsCONTENT_reading
## t = 5.2303, df = 40, p-value = 5.669e-06
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.04903765 0.11080295
## sample estimates:
## mean of x 
## 0.0799203
```

```r
t.test(sc_rtpj$READvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_rtpj$READvsCONTENT_reading
## t = 2.7312, df = 40, p-value = 0.009344
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.007379179 0.049384987
## sample estimates:
##  mean of x 
## 0.02838208
```

```r
t.test(sc_ltpj$READvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_ltpj$READvsCONTENT_reading
## t = 4.255, df = 40, p-value = 0.0001224
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.03068068 0.08619621
## sample estimates:
##  mean of x 
## 0.05843844
```

```r
t.test(sc_rsts$READvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_rsts$READvsCONTENT_reading
## t = 3.3429, df = 40, p-value = 0.001808
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.01465979 0.05948991
## sample estimates:
##  mean of x 
## 0.03707485
```

```r
t.test(sc_pc$READvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_pc$READvsCONTENT_reading
## t = 2.6128, df = 40, p-value = 0.01259
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.01202793 0.09419211
## sample estimates:
##  mean of x 
## 0.05311002
```

Share > Content

```r
#Subjective Valuation
t.test(sv_combined$SHAREvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sv_combined$SHAREvsCONTENT_reading
## t = 12.688, df = 40, p-value = 1.324e-15
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.1330943 0.1835298
## sample estimates:
## mean of x 
##  0.158312
```

```r
t.test(sv_vs$SHAREvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sv_vs$SHAREvsCONTENT_reading
## t = 5.5381, df = 40, p-value = 2.105e-06
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.02990585 0.06427735
## sample estimates:
## mean of x 
## 0.0470916
```

```r
t.test(sv_vmpfc$SHAREvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sv_vmpfc$SHAREvsCONTENT_reading
## t = 13.986, df = 40, p-value < 2.2e-16
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.2120068 0.2836286
## sample estimates:
## mean of x 
## 0.2478177
```

```r
#Self-Relevance
t.test(self_combined$SHAREvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  self_combined$SHAREvsCONTENT_reading
## t = 15.25, df = 40, p-value < 2.2e-16
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.1953341 0.2550199
## sample estimates:
## mean of x 
##  0.225177
```

```r
t.test(self_mpfc$SHAREvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  self_mpfc$SHAREvsCONTENT_reading
## t = 16.037, df = 40, p-value < 2.2e-16
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.2012041 0.2592328
## sample estimates:
## mean of x 
## 0.2302184
```

```r
t.test(self_pcc$SHAREvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  self_pcc$SHAREvsCONTENT_reading
## t = 9.6109, df = 40, p-value = 5.99e-12
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.1758923 0.2695681
## sample estimates:
## mean of x 
## 0.2227302
```

```r
#Social Cognition
t.test(sc_combined$SHAREvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_combined$SHAREvsCONTENT_reading
## t = 9.4134, df = 40, p-value = 1.072e-11
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.08178651 0.12650742
## sample estimates:
## mean of x 
##  0.104147
```

```r
t.test(sc_vmpfc$SHAREvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_vmpfc$SHAREvsCONTENT_reading
## t = 12.93, df = 40, p-value = 7.184e-16
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.1879701 0.2576198
## sample estimates:
## mean of x 
##  0.222795
```

```r
t.test(sc_mmpfc$SHAREvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_mmpfc$SHAREvsCONTENT_reading
## t = 14.448, df = 40, p-value < 2.2e-16
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.1699766 0.2252634
## sample estimates:
## mean of x 
##   0.19762
```

```r
t.test(sc_dmpfc$SHAREvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_dmpfc$SHAREvsCONTENT_reading
## t = 8.9903, df = 40, p-value = 3.789e-11
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.09686981 0.15305430
## sample estimates:
## mean of x 
## 0.1249621
```

```r
t.test(sc_rtpj$SHAREvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_rtpj$SHAREvsCONTENT_reading
## t = 4.483, df = 40, p-value = 6.047e-05
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.02329175 0.06153381
## sample estimates:
##  mean of x 
## 0.04241278
```

```r
t.test(sc_ltpj$SHAREvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_ltpj$SHAREvsCONTENT_reading
## t = 5.7348, df = 40, p-value = 1.115e-06
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.04167536 0.08703595
## sample estimates:
##  mean of x 
## 0.06435566
```

```r
t.test(sc_rsts$SHAREvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_rsts$SHAREvsCONTENT_reading
## t = 3.9668, df = 40, p-value = 0.0002938
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.01857001 0.05714750
## sample estimates:
##  mean of x 
## 0.03785876
```

```r
t.test(sc_pc$SHAREvsCONTENT_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_pc$SHAREvsCONTENT_reading
## t = 7.2125, df = 40, p-value = 9.504e-09
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.09186375 0.16339011
## sample estimates:
## mean of x 
## 0.1276269
```

Share > Select

```r
#Subjective Valuation
t.test(sv_combined$SHAREvsREAD_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sv_combined$SHAREvsREAD_reading
## t = 3.091, df = 40, p-value = 0.003625
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.01388805 0.06635813
## sample estimates:
##  mean of x 
## 0.04012309
```

```r
t.test(sv_vs$SHAREvsREAD_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sv_vs$SHAREvsREAD_reading
## t = 0.75366, df = 40, p-value = 0.4555
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  -0.01235920  0.02705767
## sample estimates:
##   mean of x 
## 0.007349237
```

```r
t.test(sv_vmpfc$SHAREvsREAD_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sv_vmpfc$SHAREvsREAD_reading
## t = 3.9184, df = 40, p-value = 0.0003397
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.03240334 0.10143585
## sample estimates:
## mean of x 
## 0.0669196
```

```r
#Self-Relevance
t.test(self_combined$SHAREvsREAD_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  self_combined$SHAREvsREAD_reading
## t = 5.0215, df = 40, p-value = 1.105e-05
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.04901774 0.11505348
## sample estimates:
##  mean of x 
## 0.08203561
```

```r
t.test(self_mpfc$SHAREvsREAD_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  self_mpfc$SHAREvsREAD_reading
## t = 4.4285, df = 40, p-value = 7.163e-05
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.04190753 0.11227095
## sample estimates:
##  mean of x 
## 0.07708924
```

```r
t.test(self_pcc$SHAREvsREAD_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  self_pcc$SHAREvsREAD_reading
## t = 4.9184, df = 40, p-value = 1.535e-05
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.05491164 0.13152106
## sample estimates:
##  mean of x 
## 0.09321635
```

```r
#Social Cognition
t.test(sc_combined$SHAREvsREAD_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_combined$SHAREvsREAD_reading
## t = 3.1196, df = 40, p-value = 0.003353
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.01293747 0.06054069
## sample estimates:
##  mean of x 
## 0.03673908
```

```r
t.test(sc_vmpfc$SHAREvsREAD_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_vmpfc$SHAREvsREAD_reading
## t = 4.19, df = 40, p-value = 0.0001494
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.03402960 0.09744964
## sample estimates:
##  mean of x 
## 0.06573962
```

```r
t.test(sc_mmpfc$SHAREvsREAD_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_mmpfc$SHAREvsREAD_reading
## t = 4.457, df = 40, p-value = 6.556e-05
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.03851651 0.10243091
## sample estimates:
##  mean of x 
## 0.07047371
```

```r
t.test(sc_dmpfc$SHAREvsREAD_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_dmpfc$SHAREvsREAD_reading
## t = 3.2224, df = 40, p-value = 0.00253
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.01679144 0.07329170
## sample estimates:
##  mean of x 
## 0.04504157
```

```r
t.test(sc_rtpj$SHAREvsREAD_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_rtpj$SHAREvsREAD_reading
## t = 1.43, df = 40, p-value = 0.1605
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  -0.005799261  0.033861012
## sample estimates:
##  mean of x 
## 0.01403088
```

```r
t.test(sc_ltpj$SHAREvsREAD_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_ltpj$SHAREvsREAD_reading
## t = 0.52538, df = 40, p-value = 0.6022
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  -0.01684696  0.02868228
## sample estimates:
##   mean of x 
## 0.005917656
```

```r
t.test(sc_rsts$SHAREvsREAD_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_rsts$SHAREvsREAD_reading
## t = 0.069227, df = 40, p-value = 0.9452
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  -0.02209584  0.02366320
## sample estimates:
##   mean of x 
## 0.000783678
```

```r
t.test(sc_pc$SHAREvsREAD_reading)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_pc$SHAREvsREAD_reading
## t = 5.0139, df = 40, p-value = 1.133e-05
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.04448013 0.10455533
## sample estimates:
##  mean of x 
## 0.07451773
```

Next, we will try to answer the question - does activity in these ROIs scale with preference for selection and sharing?

First, we will pull ROIs of the results of the parametric modulator model we ran in SPM8.


```r
#Subjective Valuation (SV)
sv_combined_rating<-read.csv('Parametric Modulation/sv_combined.csv')
sv_vmpfc_rating<-read.csv('Parametric Modulation/sv_vmpfc.csv')
sv_vs_rating<-read.csv('Parametric Modulation/sv_vs.csv')

#Self-Relevance
self_combined_rating<-read.csv('Parametric Modulation/self_combined.csv')
self_mpfc_rating<-read.csv('Parametric Modulation/self_mpfc.csv')
self_pcc_rating<-read.csv('Parametric Modulation/self_pcc.csv')
  
#Social Cognition (SC)
sc_combined_rating<-read.csv('Parametric Modulation/sc_combined.csv')
sc_vmpfc_rating<-read.csv('Parametric Modulation/sc_vmpfc.csv')
sc_mmpfc_rating<-read.csv('Parametric Modulation/sc_mmpfc.csv')
sc_dmpfc_rating<-read.csv('Parametric Modulation/sc_dmpfc.csv')
sc_rtpj_rating<-read.csv('Parametric Modulation/sc_rtpj.csv')
sc_ltpj_rating<-read.csv('Parametric Modulation/sc_ltpj.csv')
sc_rsts_rating<-read.csv('Parametric Modulation/sc_rsts.csv')
sc_pc_rating<-read.csv('Parametric Modulation/sc_pc.csv')
```

Next, we will conduct a series of t-tests to test for significance.


```r
# Select x Rating
# Neural activity modulated by preference to select articles

#Subjective Valuation
t.test(sv_combined_rating$readxrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sv_combined_rating$readxrating
## t = 6.0093, df = 40, p-value = 4.587e-07
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.03043223 0.06127614
## sample estimates:
##  mean of x 
## 0.04585419
```

```r
t.test(sv_vs_rating$readxrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sv_vs_rating$readxrating
## t = 3.9699, df = 40, p-value = 0.0002911
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.01174911 0.03611838
## sample estimates:
##  mean of x 
## 0.02393374
```

```r
t.test(sv_vmpfc_rating$readxrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sv_vmpfc_rating$readxrating
## t = 6.0419, df = 40, p-value = 4.127e-07
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.04269756 0.08562168
## sample estimates:
##  mean of x 
## 0.06415962
```

```r
#Self-Relevance
t.test(self_combined_rating$readxrating)
```

```
## 
## 	One Sample t-test
## 
## data:  self_combined_rating$readxrating
## t = 5.2755, df = 40, p-value = 4.903e-06
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.03251588 0.07290224
## sample estimates:
##  mean of x 
## 0.05270906
```

```r
t.test(self_mpfc_rating$readxrating)
```

```
## 
## 	One Sample t-test
## 
## data:  self_mpfc_rating$readxrating
## t = 5.382, df = 40, p-value = 3.482e-06
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.03586534 0.07900019
## sample estimates:
##  mean of x 
## 0.05743277
```

```r
t.test(self_pcc_rating$readxrating)
```

```
## 
## 	One Sample t-test
## 
## data:  self_pcc_rating$readxrating
## t = 3.2914, df = 40, p-value = 0.002088
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.01658514 0.06935676
## sample estimates:
##  mean of x 
## 0.04297095
```

```r
#Social Cognition
t.test(sc_combined_rating$readxrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_combined_rating$readxrating
## t = 3.47, df = 40, p-value = 0.001261
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.01122841 0.04255225
## sample estimates:
##  mean of x 
## 0.02689033
```

```r
t.test(sc_vmpfc_rating$readxrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_vmpfc_rating$readxrating
## t = 5.2544, df = 40, p-value = 5.248e-06
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.03219899 0.07245317
## sample estimates:
##  mean of x 
## 0.05232608
```

```r
t.test(sc_mmpfc_rating$readxrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_mmpfc_rating$readxrating
## t = 5.3767, df = 40, p-value = 3.541e-06
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.03228509 0.07117531
## sample estimates:
## mean of x 
## 0.0517302
```

```r
t.test(sc_dmpfc_rating$readxrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_dmpfc_rating$readxrating
## t = 4.6178, df = 40, p-value = 3.967e-05
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.02411730 0.06165883
## sample estimates:
##  mean of x 
## 0.04288807
```

```r
t.test(sc_rtpj_rating$readxrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_rtpj_rating$readxrating
## t = 0.59151, df = 40, p-value = 0.5575
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  -0.01214525  0.02219583
## sample estimates:
##   mean of x 
## 0.005025288
```

```r
t.test(sc_ltpj_rating$readxrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_ltpj_rating$readxrating
## t = 3.0925, df = 40, p-value = 0.003609
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.007540359 0.035986784
## sample estimates:
##  mean of x 
## 0.02176357
```

```r
t.test(sc_rsts_rating$readxrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_rsts_rating$readxrating
## t = 3.0571, df = 40, p-value = 0.003972
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.008667432 0.042483260
## sample estimates:
##  mean of x 
## 0.02557535
```

```r
t.test(sc_pc_rating$readxrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_pc_rating$readxrating
## t = 0.98715, df = 40, p-value = 0.3295
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  -0.01183948  0.03444731
## sample estimates:
##  mean of x 
## 0.01130392
```

```r
# Share x Rating
# Neural activity modulated by preference to share articles

#Subjective Valuation
t.test(sv_combined_rating$sharexrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sv_combined_rating$sharexrating
## t = 3.6562, df = 40, p-value = 0.000737
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.01744046 0.06055367
## sample estimates:
##  mean of x 
## 0.03899707
```

```r
t.test(sv_vs_rating$sharexrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sv_vs_rating$sharexrating
## t = 3.502, df = 40, p-value = 0.001151
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.01188464 0.04432375
## sample estimates:
## mean of x 
## 0.0281042
```

```r
t.test(sv_vmpfc_rating$sharexrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sv_vmpfc_rating$sharexrating
## t = 3.4569, df = 40, p-value = 0.001309
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.01992702 0.07602493
## sample estimates:
##  mean of x 
## 0.04797598
```

```r
#Self-Relevance
t.test(self_combined_rating$sharexrating)
```

```
## 
## 	One Sample t-test
## 
## data:  self_combined_rating$sharexrating
## t = 3.3555, df = 40, p-value = 0.001745
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.02315992 0.09331657
## sample estimates:
##  mean of x 
## 0.05823824
```

```r
t.test(self_mpfc_rating$sharexrating)
```

```
## 
## 	One Sample t-test
## 
## data:  self_mpfc_rating$sharexrating
## t = 3.5581, df = 40, p-value = 0.0009798
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.02404079 0.08726613
## sample estimates:
##  mean of x 
## 0.05565346
```

```r
t.test(self_pcc_rating$sharexrating)
```

```
## 
## 	One Sample t-test
## 
## data:  self_pcc_rating$sharexrating
## t = 2.7228, df = 40, p-value = 0.009545
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.01577061 0.10661476
## sample estimates:
##  mean of x 
## 0.06119269
```

```r
#Social Cognition
t.test(sc_combined_rating$sharexrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_combined_rating$sharexrating
## t = 3.2022, df = 40, p-value = 0.002675
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.01339565 0.05924111
## sample estimates:
##  mean of x 
## 0.03631838
```

```r
t.test(sc_vmpfc_rating$sharexrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_vmpfc_rating$sharexrating
## t = 3.51, df = 40, p-value = 0.001125
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.01948322 0.07237821
## sample estimates:
##  mean of x 
## 0.04593071
```

```r
t.test(sc_mmpfc_rating$sharexrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_mmpfc_rating$sharexrating
## t = 3.8234, df = 40, p-value = 0.0004508
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.02624357 0.08510032
## sample estimates:
##  mean of x 
## 0.05567194
```

```r
t.test(sc_dmpfc_rating$sharexrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_dmpfc_rating$sharexrating
## t = 4.2301, df = 40, p-value = 0.0001321
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.02865771 0.08109723
## sample estimates:
##  mean of x 
## 0.05487747
```

```r
t.test(sc_rtpj_rating$sharexrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_rtpj_rating$sharexrating
## t = 1.0517, df = 40, p-value = 0.2993
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  -0.009445545  0.029939886
## sample estimates:
##  mean of x 
## 0.01024717
```

```r
t.test(sc_ltpj_rating$sharexrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_ltpj_rating$sharexrating
## t = 4.4184, df = 40, p-value = 7.391e-05
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.02043369 0.05488675
## sample estimates:
##  mean of x 
## 0.03766022
```

```r
t.test(sc_rsts_rating$sharexrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_rsts_rating$sharexrating
## t = 2.0016, df = 40, p-value = 0.05214
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  -0.0002086719  0.0431893075
## sample estimates:
##  mean of x 
## 0.02149032
```

```r
t.test(sc_pc_rating$sharexrating)
```

```
## 
## 	One Sample t-test
## 
## data:  sc_pc_rating$sharexrating
## t = 2.1112, df = 40, p-value = 0.04105
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  0.001577752 0.072314050
## sample estimates:
## mean of x 
## 0.0369459
```


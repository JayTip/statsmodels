import statsmodels.regression.linear_model as lm_
import statsmodels.discrete.discrete_model as dm_
import statsmodels.regression.mixed_linear_model as mlm_
import statsmodels.genmod.generalized_linear_model as glm_
import statsmodels.robust.robust_linear_model as roblm_
import statsmodels.regression.quantile_regression as qr_
import statsmodels.duration.hazard_regression as hr_
import statsmodels.genmod.generalized_estimating_equations as gee_

gls = lm_.GLS.from_formula
wls = lm_.WLS.from_formula
ols = lm_.OLS.from_formula
glsar = lm_.GLSAR.from_formula
mixedlm = mlm_.MixedLM.from_formula
glm = glm_.GLM.from_formula
rlm = roblm_.RLM.from_formula
mnlogit = dm_.MNLogit.from_formula
logit = dm_.Logit.from_formula
probit = dm_.Probit.from_formula
poisson = dm_.Poisson.from_formula
negativebinomial = dm_.NegativeBinomial.from_formula
quantreg = qr_.QuantReg.from_formula
phreg = hr_.PHReg.from_formula
ordinal_gee = gee_.OrdinalGEE.from_formula
nominal_gee = gee_.NominalGEE.from_formula
gee = gee_.GEE.from_formula

del lm_, dm_, mlm_, glm_, roblm_, qr_, hr_, gee_

import smartpy as sp

tstorage = sp.record(myParameter1 = sp.intOrNat, myParameter2 = sp.intOrNat).layout(("myParameter1", "myParameter2"))
tparameter = sp.variant(myEntryPoint = sp.intOrNat).layout("myEntryPoint")
tprivates = { }
tviews = { }

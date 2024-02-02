def test_1():
	from numpy import sqrt
	from mysqrt import sqrt2
	small=1.0e-14
	
	xvalues=[2,100,10000,0.0001,0,1e8]
	for x in xvalues:
		s=sqrt2(x)
		s_numpy=sqrt(x)
		print(f"for x={x}, s={s} and s_numpy={s_numpy}")
		assert (s-s_numpy)<small, f"square root disagrees with numpy square root for x={x}"
	
def test_2():
	from numpy import sqrt
	from mysqrt import sqrt2
	small=1.0e-14
	
	xvalues=[3,6,"10"]
	for x in xvalues:
		s=sqrt2(x)
		s_numpy=sqrt(x)
		print(f"for x={x}, s={s} and s_numpy={s_numpy}")
		assert (s-s_numpy)<small, f"square root disagrees with numpy square root for x={x}"
	

data = """[l[dj%i;fNMd.a)mg74Cep_bbW%+$&4<M_dZemi4DJ4'&$&14M_d,*14n,*=47ffb[M[XA_j%+)-$),4<A>JCB"4b_a[4=[Yae=49^hec[%-/$&$)/*+$''-4IW\Wh_%+)-$),4'+-/'/(&,.(*,"""



def unhash(string):
	result = ''
	for i in string:
		if ord(i) + 10 <= 43:
			result += chr(ord(i)-20)
		else:
			result += chr(ord(i)+10)
	return result


print(unhash(data).replace(">", " "))
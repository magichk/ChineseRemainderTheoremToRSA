import binascii
import struct

# return (g, x, y) a*x + b*y = gcd(x, y)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def decryptRSA(p,q,e,ct):
	# compute n
	n = p * q
	phi = (p - 1) * (q - 1)	
	gcd, a, b = egcd(e, phi)
	d = a
	print "d: " + str(d)
	pt = pow(ct, d, n)
	return pt

def encryptRSA(p,q,e,pt):
	# compute n
	n = p * q
	phi = (p - 1) * (q - 1)
	gcd, a, b = egcd(e, phi)
	d = a
	print "d: " + str(d)
	ct = pow(pt, e, n)
	return ct


def convert(int_value):
   encoded = format(int_value, 'x')
   length = len(encoded)
   encoded = encoded.zfill(length+length%2)
   return encoded.decode('hex')

# x = mulinv(b) mod n, (x * b) % n == 1
def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

def main():
	# By implementing Chinese remainder algorithm
	# 1) p and q are the primes
	# 2) dp = d mod (p - 1)
	# 3) dq = d mod (q - 1)
	# 4) Qinv = 1/q mod p *This is not integer devision but multiplicative inverse
	# 5) m1 = pow(c, dp, p)
	# 6) m2 = pow(c, dq, q)
	# 7-1) h = Qinv(m1 - m2) mod p  ; if m1 < m2
	# 7-2) h = Qinv * (m1 + q/p) 
	# 8) m = m2 + hq

	# m = 65
	# p = 61
	# q = 53
	# dp = 53
	# dq = 49
	# c = 2790

	p = <p>
	q = <q>
	dp = <dp>
	dq = <dq>
	c = <c>

	Qinv = mulinv(q,p)
	print "Qinv: " + str(Qinv)

	m1 = pow(c, dp, p)
	print "m1: " + str(m1)

	m2 = pow(c, dq, q)
	print "m2: " + str(m2)

	h = (Qinv * (m1 - m2)) % p
	print "h: " + str(h)

	m = m2 + (h*q)
	print "m: " + str(int(m))

	hexadecimals = str(hex(m))[2:-1]
	print "solved: " + str(binascii.unhexlify(hexadecimals))
	# solved: Theres_more_than_one_way_to_RSA

if __name__ == "__main__":
	main()

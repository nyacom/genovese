int alpha(unsigned char a1, unsigned char a2) {
	return (a1 + a2) >> 1;
}

int main() {

	unsigned char r1[64];
	unsigned char g1[64];
	unsigned char b1[64];

	unsigned char r2[32];
	unsigned char g2[32];
	unsigned char b2[32];

	int i;

	for (i = 0; i < 32; i++) {
		r1[i+32] = alpha(r1[i], r2[i]);
		g1[i+32] = alpha(g1[i], g2[i]);
		b1[i+32] = alpha(b1[i], b2[i]);
	}

	return 0;
}


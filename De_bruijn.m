seq = [0 0 0 1];
for i = 4:18
    seq = [seq FSR2(seq(i-3:i))];
end
seq
length(seq)


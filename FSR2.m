function x = FSR2(A)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
if length(A) ~= 4
    sprintf("Kass!!!")
end
term1 = xor(A(1), A(4));
term2 = (xor(A(2), 1)) && (xor(A(3),1)) && (xor(A(4),1));

x = xor(term1, term2);

end


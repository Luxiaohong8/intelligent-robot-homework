function [ randVal ] = sample( variance )
    maxVal = variance;
    minVal = -maxVal;
    randVal = ((1/2)*sum(minVal + (maxVal-minVal).*rand(12,1)));
end


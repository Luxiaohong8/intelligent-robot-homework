%% true probability distribution
true_func = @(x) betapdf(x,1+1,1+10);

%% Do importance sampling
N = 10^6;
% uniform proposal distribution
x_samples = rand(N,1);
proposal = 1/N;
% evaluate for each sample
target = true_func(x_samples);
% calculate importance weight
w = target ./ proposal;
w = w ./ sum(w);
% resample, with replacement, according to importance weight
samples = randsample(x_samples,N,true,w);

%% plot
subplot(1,2,1)
x = linspace(0,1,1000);
plot(x, true_func(x) )
axis square

subplot(1,2,2)
hist(samples,1000)
title('importance sampling')
axis square
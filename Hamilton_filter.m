function [ filteredxi , predictedxi ] = Hamilton_filter(p11,p22,mu,sigma, y, initialise)

% Extract length of data
T = size(y,2);

% Build transition matrix from p11 and p22
P   = [ p11 , 1-p22 ; 1-p11 , p22];

if (initialise == 1)
% Initialise by being in state 1
predictedxi(:,1) = [ 1 ; 0 ];
elseif initialise == 2
% Initialise by being in state 2
predictedxi(:,1) = P*[ 0 ; 1 ];
elseif initialise == 3
% Initialise by being in Long Term Mean - again how do we know if p11/p22
% are correct?
predictedxi(:,1) = [ (1-p22) / (2-p11-p22) ; (1-p11)/(2-p11-p22) ];
end

% Run the Hamilton filter
for i=1:T
   likelihood(:,i)   = [ normpdf(y(1,i),mu(1),sigma(1)) ; normpdf(y(1,i),mu(2),sigma(2)) ];
   % Update Step
   filteredxi(:,i)   = predictedxi(:,i) .* likelihood(:,i) / ([1,1]*(predictedxi(:,i).*likelihood(:,i)) );
   % Prediction Step
   predictedxi(:,i+1)= P * filteredxi(:,i) ;
end

% Delete the last prediction, because we want filteredxi and
% predictedxi to have the same length
predictedxi = predictedxi(:,1:T);

% Close the function
end


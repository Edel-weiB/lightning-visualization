data = readmatrix('ALL20130801_G2a.csv');

close

%% Info
% 1 - year
% 2 - month
% 3 - day
% 4 - hour
% 5 - minute
% 6 - second
% 7 - lattitude
% 8 - longitude
% 9 - height (m)
% 10 - sigma
% 11 - flash number

min_lat = min(data(:,7));
max_lat = max(data(:,7));
min_long = min(data(:,8));
max_long = max(data(:,8));
min_h = min(data(:,9));
max_h = max(data(:,9));


current_lighting = 1;

for i = 1:length(data(:,1))
    if data(i,11) > current_lighting
        clf
        current_lighting = data(i,11);
    end
    scatter3(data(i,7), data(i,8), data(i,9), '.', 'b');
    xlim([min_lat max_lat])
    ylim([min_long max_long])
    zlim([min_h max_h])
    hold on
    
    delay = data(i+1,6)-data(i,6);
    if delay > 2
        delay = 1;
    end
    pause(delay)
%     pause(0.05);
end
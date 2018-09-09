xs=zeros(500,1);
ys=zeros(500,1);
thetas = zeros(500,1);
xT_array = [0,0,0;5,0,0;10,0,0;15,0,0;
            15,5,pi/2;15,10,pi/2;15,15,pi/2;
            10,15,pi;5,15,pi;0,15,pi];
aT = [.0004;.0002;.0004;.0004];


for j=1:size(xT_array,1)-1
    aT=aT*2;
    for i=1:500
        [xs(i),ys(i),thetas(i)]=sample_motion_model(xT_array(j,:),xT_array(j+1,:),aT);
    end
    plot(xs,ys,'r.');
    hold on;
end

plot([0;15],[0;0],'k','LineWidth',2)
plot([15;15],[0;15],'k','LineWidth',2)
plot([15;0],[15;15],'k','LineWidth',2)

hold off;


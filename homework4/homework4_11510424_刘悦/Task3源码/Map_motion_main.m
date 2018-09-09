xs=zeros(500,1);
ys=zeros(500,1);
thetas = zeros(500,1);
xT = [0,0,0];
aT = [.04;.006;.006;.4;0.4;.2];
v=1;
w=0.5;%v=w*r
t=0.6*pi;%8.7
for i=1:500
    [xs(i),ys(i),thetas(i)]=Map_Consistent_Motion_Model(xT,v,w,aT,t);
end
plot(xs,ys,'r.');
axis([0 2.5 0 2.5])
hold on;

plot([0;0],[0;v/w],'k','LineWidth',1)
plot([0;mean(xs)],[v/w;mean(ys)],'k','LineWidth',1)
plot([0;mean(xs)],[0;mean(ys)],'k','LineWidth',1)
%plot([0;mean(xs)],[0;mean(ys)],'k','LineWidth',1)
rectangle('Position',[1.34,0.74,0.42,0.12],'FaceColor','b','EdgeColor','b','LineWidth',2,'LineStyle','-');

%line(xT_array(1,1:3),xT_array(4,1:3))

hold off;
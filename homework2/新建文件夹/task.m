
b1=1:3;
a1=1+b1-b1;
a2=1:3;
b2=3-a2+a2;


plot(a1,b1);
hold on
plot(a2,b2);
hold on
xlim([0 5])
ylim([0 5])

robot=[3,0.5];
plot(robot(1),robot(2),'r.','markersize',50);
hold on

for i=0:360
    deltat = i*pi/180;
    x1 = robot(1) + 1*cos(deltat);    y1 = robot(2) +1* sin(deltat);
    syms x y;
    y=tan(deltat)*x+y1-tan(deltat)*x1;
    
    
    plot(x1,y1,'g.','markersize',5);
    pause(0.2);
    hold on
end


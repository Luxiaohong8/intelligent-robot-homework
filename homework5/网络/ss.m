landmark=[10,10];
landmark2=[30,34];
landmark3=[4,20];

a=[21.1,14];
r=landmark(0);
%r=landmark(0)-a(0)+landmark(1)-a(1);
x=[];
y=[];
for i=1:500
    deltat = i*pi/180;
    x1 = landmark(0) + r*cos(deltat)-1+2*rand;
    y1 = landmark(1) + r*sin(deltat)-1+2*rand;
    x.append(x1);
    y.append(y1);
end

plt.plot(x,y, 'y*')


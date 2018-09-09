function p=sample_point(landmark,a)
    p=zeros(900,2);
    r=sqrt((landmark(1)-a(1)).^2+(landmark(2)-a(2)).^2);
    for i=1:900
       deltat = i*pi/180;
       x1 = landmark(1) + r*cos(deltat)-1.5+3*rand;
       y1 = landmark(2) + r*sin(deltat)-1.5+3*rand;
       p(i,1)=x1;
       p(i,2)=y1;
    end
    rectangle('Position',[landmark(1)-r,landmark(2)-r,2*r,2*r],'Curvature',[1,1],'edgecolor','b');
    hold on
end
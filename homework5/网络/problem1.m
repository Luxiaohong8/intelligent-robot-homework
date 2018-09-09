landmark1=[10,10];
landmark2=[30,34];
landmark3=[4,20];
position=[21.1,14];

p1=[sample_point(landmark1,position);sample_point(landmark2,position);sample_point(landmark3,position)];

for ii =1: size(p1,1)
    if norm(p1(ii,:)-position)<3 
    end
    hold on
end

plot(landmark1(1),landmark1(2), 'g*');hold on
plot(landmark2(1),landmark2(2), 'g*');hold on
plot(landmark3(1),landmark3(2), 'g*');hold on
plot(position(1),position(2), 'g+');hold on
axis([4 40 4 36]);
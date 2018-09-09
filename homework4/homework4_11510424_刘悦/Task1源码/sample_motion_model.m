function [ newX,newY,newTheta]  = sample_motion_model( xT,x2T,aT )
%Simple odometry-based motion model. 
%Argumentts are xT=(x,y,theta),
    O_trans=sqrt((x2T(1)-xT(1)).^2+(x2T(2)-xT(2)).^2);
    O_rot1=atan2(x2T(2)-xT(2),x2T(1)-xT(1))-xT(3);
    O_rot2=x2T(3)-xT(3)-O_rot1

    varianceVal = aT(1)*abs(O_rot1)+aT(2)*O_trans;
    newRot1 =O_rot1+sample(varianceVal);

    varianceVal = aT(3)*O_trans + aT(4)*(abs(O_rot1)+abs(O_rot2));
    newRot_trans = O_trans + sample(varianceVal);

    varianceVal = (aT(1)*abs(O_rot2)+aT(2)*O_trans);
    newRot2 = O_rot2+sample(varianceVal);

    newX = xT(1)+newRot_trans*cos(xT(3)+newRot1);
    newY = xT(2)+newRot_trans*sin(xT(3)+newRot1);
    newTheta = xT(3)+newRot1+newRot2;
end
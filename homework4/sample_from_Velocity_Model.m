function [ newX,newY,newTheta] = sample_from_Velocity_Model( X,v,w,aT,t )
    new_v=v+sample(aT(1)*abs(v)+aT(2)*abs(w));
    new_w=w+sample(aT(3)*abs(v)+aT(4)*abs(w));
    new_yj=sample(aT(5)*abs(v)+aT(6)*abs(w));
    
    newX=X(1)-(new_v/new_w)*sin(X(3))+(new_v/new_w)*sin(X(3)+new_w*t);
    newY=X(2)+(new_v/new_w)*cos(X(3))-(new_v/new_w)*cos(X(3)+new_w*t);
    newTheta=X(3)+new_w*t+new_yj*t;
end


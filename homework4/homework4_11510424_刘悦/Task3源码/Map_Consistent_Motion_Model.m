function[ newX,newY,newTheta] = Map_Consistent_Motion_Model( X,v,w,aT,t )
    [ newX,newY,newTheta] =sample_from_Velocity_Model(X,v,w,aT,t);
    while (newX>=1.3&&newX<=1.8)&&(newY>=0.7&&newY<=0.9)
        [ newX,newY,newTheta] =sample_from_Velocity_Model(X,v,w,aT,t);
    end
end


function main
%MAIN �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
    [x,y,z]= Differential_drive([0,0,0],2,1,500);
    a=[x.' y.'];
    for i=1:size(a,1)
        plot(a(i,1),a(i,2),'.');
        hold on;
        pause(0.1);
    end
end


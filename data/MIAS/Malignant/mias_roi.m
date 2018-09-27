clear all;
close all;

[num, txt, raw] = xlsread('mias_db.xlsx');

%num

%txt

%raw

[rn, cn] = size(num);
[rt, ct] = size(txt);
[rr, cr] = size(raw);
%rn
%cn
%rt
%ct
%rr
%cr

for i = 1:322
    fil = raw{i,1};
    fname = strcat(num2str(fil),'.pgm');
    img = imread(fname);
    if size(img,3) == 3
        img_gr = rgb2gray(img);
    else
        img_gr = img;
    end
    [r, c] = size(img_gr);
    x = raw{i,5};
    y = raw{i,6};
    l = raw{i,7};
    xmin = x - l; ymin = y - l;
    d = 2*l - 1;
    rect  = [xmin ymin d d];
    imcr = imcrop(img_gr, rect);
    imcr = imresize(imcr, [256 256]);
    str = strcat('roi', num2str(i));
    %str
    oname = strcat(num2str(str),'.jpg');
    imwrite(imcr,oname);
end
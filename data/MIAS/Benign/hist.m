clear all;
for i = 1:64
im = imread(strcat('E:\medical imaging\Mam\roi_mias\roi_classes\roi_classes\Benign\roi',num2str(i),'B.jpg'));
j = histeq(im);
% figure(1);imshow(i);title('original');
% figure(2);imshow(j);title('equalized');
fname1 = strcat('E:\medical imaging\Mam\roi_mias\roi_classes\roi_classes\Benign\equalized\roi',num2str(i),'B.jpg');
imwrite(j,fname1);
disp(strcat('Wrote ',num2str(i),'.jpg image'));
end
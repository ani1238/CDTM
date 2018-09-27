clear all;
clc;
close all;

%% PARAETER INITIALIZATION BLOCK
% TN_IMG = TOTAL NUMBER OF IMAGE
% TN_RL = TOTAL NUMBER OF RESOLUTION LEVEL(l)
% RL = RESOLUTION LEVEL(j)
% DM = DETAIL COEEFICIENT MATRIX
% TN_DIR_DM = TOTAL NO. OF DIRECTION FOR DM(r)
% TN_DIR_NGLCM = TOTAL NO. OF DIRECTION FOR NGLCM(p)
% DIR_NGLCM = DIRECTION FOR NGLCM(thetha)
% D_GLCM = DISTANCE FOR COMPUTING GLCM(D)
% FD = FEATURE DESCRIPTOR
% FDM = FEATURE DESCRIPTOR MATRIX
% TN_FD = TOTAL NO OF FEATURE DESCRIPTOR(s)
% TN_F = TOTAL NO OF FEATURES(M)
% FM = OUTPUT FEATURE MATRIX
TN_IMG = 64;
TN_RL = 2; TN_DIR_DM = 3; TN_DIR_NGLCM = 4; TN_FD = 5; 
TN_F = TN_RL * TN_DIR_DM * TN_DIR_NGLCM * TN_FD; 
pixel_dist = 3; 
FM = zeros(TN_IMG,TN_RL,TN_DIR_DM, 4,5);
%% 
for i = 1 : TN_IMG
    img = imread(strcat('roi',num2str(i),'B.jpg'));
%     if size(img,3) == 3
%         img_gr = rgb2gray(img);
%     else
%         img_gr = img;
%     end
%     [r c] = size(img_gr);
%     figure, imshow(img);
%     h = imfreehand(gca);
%     pos = getPosition(h);
%     close(figure);
%     minr = min(pos(:,2));
%     maxr = max(pos(:,2));
%     minc = min(pos(:,1));
%     maxc = max(pos(:,1));
%     minf=[minr minc];
%     maxf=[maxr maxc];
%     if (minf(1,1)-pixel_dist) > r | (maxf(1,1)+pixel_dist) > r | (minf(1,2)-pixel_dist) > c | (maxf(1,2)+pixel_dist) > c
%     else
%         window_generate = [(minf(1,1)-pixel_dist) (maxf(1,1)+pixel_dist) (minf(1,2)-pixel_dist) (maxf(1,2)+pixel_dist)];
%     end
%     img_selected_cancer_region = img(window_generate(1,1):window_generate(1,2),window_generate(1,3):window_generate(1,4));
%     figure; imshow(img_selected_cancer_region,[]);    
    %% 2D-DWT, GLCM, AND NGLCM COMPUTATION BLOCK
        %% REQUIRED PARAMETER INITIALIZATION
%         H = zeros(TN_RL,size(img_selected_cancer_region,1),size(img_selected_cancer_region,2));
%         V = zeros(TN_RL,size(img_selected_cancer_region,1),size(img_selected_cancer_region,2));
%         D = zeros(TN_RL,size(img_selected_cancer_region,1),size(img_selected_cancer_region,2));
%         DM = zeros(TN_RL,TN_DIR_DM);
        GLCM_MAT = zeros(TN_RL,TN_DIR_DM, 4,8,8);
        NGLCM_MAT = zeros(TN_RL,TN_DIR_DM, 4,8,8);
        FDM = zeros(TN_RL,TN_DIR_DM, 4,5);
        D_GLCM = 1;
        for j = 1 : TN_RL           
            %% DWT BLOCK
            [c,s]=wavedec2(img,j,'haar');
            [H1,V1,D1] = detcoef2('all',c,s,j);
%             H(j,1:size(H1,1),1:size(H1,2)) = H1;
%             V(j,1:size(H1,1),1:size(H1,2)) = V1;
%             D(j,1:size(H1,1),1:size(H1,2)) = D1;
            %% GLCM AND NGLCM BLOCK
            for d = 1 : 3
                for k = 1 : TN_DIR_NGLCM
                    if k == 1       % FOR 0 DEGREE   
                        DIR_NGLCM = [0 D_GLCM];
                    elseif k == 2   % FOR 45 DEGREE
                        DIR_NGLCM = [(-D_GLCM) D_GLCM];
                    elseif k == 3   % FOR 90 DEGREE
                        DIR_NGLCM = [(-D_GLCM) 0];
                    elseif k == 4   % FOR 135 DEGREE
                        DIR_NGLCM = [(-D_GLCM) (-D_GLCM)];
                    end
                    if d == 1       % H COMPUTATION
                        [glcms, SI] = graycomatrix(H1,'Offset',DIR_NGLCM);
                        GLCM_MAT(j,d,k,:,:) = glcms;
                        NGLCM_MAT(j,d,k,:,:) = glcms./sum(glcms(:));
                        NGLCM = glcms./sum(glcms(:));
                    elseif d == 2   % V COMPUTATION
                        [glcms, SI] = graycomatrix(V1,'Offset',DIR_NGLCM);
                        GLCM_MAT(j,d,k,:,:) = glcms;
                        NGLCM_MAT(j,d,k,:,:) = glcms./sum(glcms(:));
                        NGLCM = glcms./sum(glcms(:));
                    elseif d == 3   % D COMPUTATION
                        [glcms, SI] = graycomatrix(D1,'Offset',DIR_NGLCM);
                        GLCM_MAT(j,d,k,:,:) = glcms;
                        NGLCM_MAT(j,d,k,:,:) = glcms./sum(glcms(:));
                        NGLCM = glcms./sum(glcms(:));
                    end
                    %% FEATURE DESCRIPTOR BLOCK
                     [out] = GLCMFeatures(NGLCM);
                     FDM(j,d,k,1) = out.energy;
                     FDM(j,d,k,2) = out.entropy;
                     FDM(j,d,k,3) = out.correlation;
                     FDM(j,d,k,4) = out.sumVariance;
                     FDM(j,d,k,5) = out.sumAverage;
                end               
            end   
             D_GLCM =  D_GLCM + 1;
        end   
        %% FINAL FEATURE MATRIX FOR ALL IMAGES
        FM(i,:,:,:,:) = FDM;
        
        %% CONVERTING FM MATRIX INTO 2-D MATRIX
        COUNT = 1;
        for p = 1 : TN_RL
            for q = 1 : TN_DIR_DM
                for r = 1 : TN_DIR_NGLCM
                    for s = 1 : TN_FD
                        FM_1(COUNT,i) = FM(i,p,q,r,s);
                        COUNT = COUNT + 1;
                    end
                end
            end
        end
end